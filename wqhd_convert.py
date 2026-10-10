#!/usr/bin/env python3
"""
Convert Enigma2 skins (1920x1080 or 1280x720) to WQHD 2560x1440.

Scales every position, size, font size, list/item height, parameter and
list-template value in the skin XML, plus all PNG/JPG graphics, and renames
the skin folder (and any shared "Common" folders it uses) so the result
installs alongside the original.

Usage:
  python3 wqhd_convert.py --skins-root path/to/OpenViX-skins/src/skins \
      --skins "Simple_Ten_Eighty,YouViX-Blue" --out dist

Each selected skin produces  dist/<NewName>.zip  (unpacks to
usr/share/enigma2/...) and  dist/<NewName>-report.txt.
"""
import argparse
import collections
import fnmatch
import os
import re
import shutil
import sys
import zipfile
from fractions import Fraction

from PIL import Image

TARGET_W, TARGET_H = 2560, 1440
SKIP_FILES = ("Makefile.am", "Makefile", "Thumbs.db", "*.db")

# ---------------------------------------------------------------------------
# What counts as a pixel value
# ---------------------------------------------------------------------------
# Geometry attributes that may hold layout expressions (e, c, center, *, %, top, fill ...)
EXPR_ATTRS = {"position", "size"}
# Integer (or integer list) attributes measured in pixels.
PIXEL_ATTRS = {
    "borderWidth", "widgetBorderWidth", "scrollbarWidth", "scrollbarSliderBorderWidth",
    "ProgressbarBorderWidth", "progressbarBorderWidth", "progressbarHeight", "progressBarWidth",
    "progressPercentWidth", "EventBorderWidth", "ServiceBorderWidth", "EventBorderVerWidth",
    "ServiceBorderVerWidth", "EventNamePadding", "ServiceNamePadding", "IconXPadding",
    "IconYPadding", "RecIconSize", "itemHeight", "itemHeightTwoLine", "itemWidth", "itemmHeight",
    "itemmheight", "itemSpacing", "itemsDistances", "iconMargin", "iconsWidth", "offset",
    "textOffset", "shadowOffset", "fieldMargins", "nonplayableMargins", "dateWidth",
    "durationWidth", "partIconeShift", "partIconeShiftCompact", "partIconeShiftMinimal",
    "partIconeShiftOriginal", "pbarHeight", "pbarLargeWidth", "piconMargin", "rowHeight",
    "rowSplit", "rowSplit1", "rowSplit2", "satPosLeft", "separatorLineThickness",
    "serviceItemHeight", "spaceIconeText", "spaceLeft", "spaceRight", "spacing", "padding",
    "bubbletextPadding", "treeDescription", "columns", "columnsCompactDescription",
    "columnsOriginal", "compactColumn", "column", "fontSizesCompact", "fontSizesMinimal",
    "setColGap", "setColWidths", "setIconDistance", "setPboxDistance", "setPiconDistance",
    "setPiconSize", "setPict", "setTemp", "setTempUnits", "setTime", "setTimeWidth", "setWind",
    "setWindPict", "setWindUnits", "text1Pos", "text2Pos", "text3Pos", "text4Pos", "textPos",
    "height", "width", "xres", "yres",
}
# Attributes that hold numbers which are NOT pixels.
NON_PIXEL_ATTRS = {
    "zPosition", "zposition", "NumberOfRows", "NumberOfItems", "NoAnimationAfter", "rowsincolumn",
    "colposition", "maxPages", "Wrap", "wrap", "nostrip", "scale", "split", "selectionDisabled",
    "index", "id", "bpp", "version", "replacement", "alphaBlend", "hidePointerOnZeroLength",
    "noLabel", "allVisible", "setPictScale", "setWindPictScale", "enableWrapAround", "noWrap",
    "transparent", "paddingFactor", "selectionZoom", "steptime", "options", "objectTypes",
    "conditional", "text", "title", "name", "source", "render", "type", "flags", "filename",
    "pixmap", "pixmaps", "selectionPixmap", "backgroundPixmap", "path", "encoding",
    "standalone", "connection", "elements", "addon", "pos", "layout", "orientation",
}
# Name patterns for plugin-specific geometry attributes (e.g. CoolTVGuide "CoolBarPos").
PIXEL_NAME = re.compile(r"(^spacing|Pos$|Size$|SizeSa$|Width$|Height$|High$|Padding$|Margins?$|Distances?$|"
                        r"Gap$|Offset$|Shift$|Thickness$|Spacing$|Pico$)")
PARAM_NOT_PIXEL = {"AllowUserDatesAndTimes", "AboutHddSplit", "SecondInfoBarSimple"}
FONT_VALUE = re.compile(r"^\s*[^;,\"]+;\s*\d+\s*(,\s*[^;,\"]+;\s*\d+\s*)*$")
INT = re.compile(r"^(\s*)([+-]?\d+)(\s*)$")


class Converter:
    def __init__(self, factor, renames):
        self.f = Fraction(factor)
        self.renames = renames  # {old_folder: new_folder}
        self.log = collections.Counter()
        self.unknown = collections.Counter()
        self.left_expr = collections.Counter()

    # -- number scaling ------------------------------------------------------
    def sc(self, v):
        v = int(v)
        x = abs(v) * self.f
        r = int(x + Fraction(1, 2))  # round half up
        return -r if v < 0 else r

    def scale_int_token(self, tok):
        m = INT.match(tok)
        return f"{m.group(1)}{self.sc(m.group(2))}{m.group(3)}" if m else tok

    def scale_list(self, val):
        return ",".join(self.scale_int_token(t) for t in val.split(","))

    def scale_expr_token(self, tok):
        if INT.match(tok):
            return self.scale_int_token(tok)
        s = tok.strip()
        if s in ("center", "fill", "top", "bottom", "left", "right", "e", "c", "*", ""):
            return tok
        if re.search(r"[fwh]", s):  # skin-factor / font-metric formulas rescale themselves
            self.left_expr[s] += 1
            return tok
        m = re.fullmatch(r"(\d+)\*(\d+)", s)
        if m:  # rows * itemHeight -> only the pixel part scales
            new = f"{m.group(1)}*{self.sc(m.group(2))}"
        else:
            new = re.sub(r"(?<![\d.])\d+(?![\d%.])", lambda d: str(self.sc(d.group(0))), s)
        self.log[f"expr {s} -> {new}"] += 1
        return tok.replace(s, new)

    def scale_expr(self, val):
        return ",".join(self.scale_expr_token(t) for t in val.split(","))

    def scale_font(self, val):
        if re.search(r";\s*[^\d\s,]", val):  # e.g. "Regular;20*f" - self scaling
            return val
        return re.sub(r";(\s*)(\d+)", lambda m: f";{m.group(1)}{self.sc(m.group(2))}", val)

    # -- XML -----------------------------------------------------------------
    ATTR = re.compile(r'(?<![\w:.-])([A-Za-z_][\w:.-]*)(\s*=\s*)"([^"]*)"')
    TAG = re.compile(r"<([A-Za-z_][\w:.-]*)((?:\s+[\w:.-]+\s*=\s*\"[^\"]*\")*\s*/?)>")

    def scale_tag(self, m):
        tag, body = m.group(1), m.group(2)
        pname = None
        if tag == "parameter":
            pm = re.search(r'\bname\s*=\s*"([^"]*)"', body)
            pname = pm.group(1) if pm else None

        def attr(a):
            name, eq, val = a.groups()
            new = val
            if tag == "font" or not re.search(r"\d", val) or val.lstrip().startswith("#"):
                return a.group(0)
            if tag == "parameter" and name == "value":
                if pname in PARAM_NOT_PIXEL:
                    pass
                elif val.startswith("*"):
                    if pname and pname.lower().endswith("font"):  # "*Regular,33"
                        new = re.sub(r",(\s*)(\d+)$", lambda d: f",{d.group(1)}{self.sc(d.group(2))}", val)
                elif FONT_VALUE.match(val):
                    new = self.scale_font(val)
                else:
                    new = self.scale_list(val)
            elif name in EXPR_ATTRS:
                new = self.scale_expr(val)
            elif name in ("pointer", "seek_pointer"):
                f, _, xy = val.rpartition(":")
                new = f"{f}:{self.scale_list(xy)}" if f else val
            elif name == "cornerRadius" or "CornerRadius" in name:
                new = re.sub(r"^\s*\d+", lambda d: str(self.sc(d.group(0))), val)
            elif FONT_VALUE.match(val) and name not in NON_PIXEL_ATTRS:
                new = self.scale_font(val)
            elif name in PIXEL_ATTRS or (name not in NON_PIXEL_ATTRS and PIXEL_NAME.search(name)):
                new = self.scale_list(val)
                if name not in PIXEL_ATTRS:
                    self.log[f"pixel by name: {name}"] += 1
            elif name not in NON_PIXEL_ATTRS and not re.search(r"Colou?r", name):
                if re.fullmatch(r"[\d\s,+-]+", val):
                    self.unknown[f"<{tag} {name}=\"{val}\">"] += 1
            return f'{name}{eq}"{new}"'

        return f"<{tag}{self.ATTR.sub(attr, body)}>"

    def scale_code_block(self, text):
        """TemplatedMultiContent bodies."""
        sc = self.sc
        pair = lambda m: f"{m.group(1)}{sc(m.group(2))}{m.group(3)}{sc(m.group(4))}{m.group(5)}"
        one = lambda m: f"{m.group(1)}{sc(m.group(2))}"
        text = re.sub(r"(\b(?:pos|size)\s*=\s*\(\s*)(-?\d+)(\s*,\s*)(-?\d+)(\s*\))", pair, text)
        text = re.sub(r'(gFont\(\s*"[^"]*"\s*,\s*)(\d+)', one, text)
        text = re.sub(r'("item(?:Height|Width)"\s*:\s*)(\d+)', one, text)
        text = re.sub(r'("[\w -]+"\s*:\s*\(\s*)(\d+)(?=\s*,\s*\[)', one, text)
        text = re.sub(r"(\b(?:border_width|borderWidth|cornerRadius|corner_radius)\s*=\s*)(\d+)", one, text)
        return text

    def scale_applet(self, code):
        """Python applets: scale integer literals, except indexes, divisors and text-length checks."""
        out = []
        for line in code.split("\n"):
            if line.lstrip().startswith("#"):
                out.append(line)
                continue
            has_len = "len(" in line

            def num(m):
                s, pre = m.group(0), line[:m.start()].rstrip()
                if pre.endswith(("[", "/", "getDesktop(")):
                    return s
                if has_len and re.search(r"(&lt;|&gt;|<|>|==|!=)=?$", pre):
                    return s
                return str(self.sc(s))
            new = re.sub(r"(?<![\w.])\d+(?![\w.])", num, line)
            if new != line:
                self.log["applet lines scaled"] += 1
            out.append(new)
        return "\n".join(out)

    def rename_refs(self, text):
        for old, new in self.renames.items():
            text = text.replace(f"/usr/share/enigma2/{old}/", f"/usr/share/enigma2/{new}/")
            text = re.sub(rf"(?<=[\"'>,:]){re.escape(old)}/", f"{new}/", text)
        return text

    def convert_xml(self, text):
        text = self.TAG.sub(self.scale_tag, text)
        text = re.sub(r'(<convert\s+type="TemplatedMultiContent"\s*>)(.*?)(</convert>)',
                      lambda m: m.group(1) + self.scale_code_block(m.group(2)) + m.group(3), text, flags=re.S)
        text = re.sub(r"(<applet\b[^>]*>)(.*?)(</applet>)",
                      lambda m: m.group(1) + self.scale_applet(m.group(2)) + m.group(3), text, flags=re.S)
        return self.rename_refs(text)

    # -- images --------------------------------------------------------------
    def convert_image(self, src, dst):
        im = Image.open(src)
        w, h = im.size
        nw, nh = max(1, self.sc(w)), max(1, self.sc(h))
        if src.lower().endswith((".jpg", ".jpeg")):
            im.convert("RGB").resize((nw, nh), Image.LANCZOS).save(dst, quality=92, subsampling=0)
            return
        has_alpha = im.mode in ("RGBA", "LA", "PA") or "transparency" in im.info
        if has_alpha:
            # resample with premultiplied alpha so transparent edges don't get dark fringes
            out = im.convert("RGBA").convert("RGBa").resize((nw, nh), Image.LANCZOS).convert("RGBA")
            if out.getextrema()[3][0] == 255:
                out = out.convert("RGB")
        else:
            out = im.convert("RGB").resize((nw, nh), Image.LANCZOS)
        out.save(dst, optimize=True)


# ---------------------------------------------------------------------------
# Folder discovery / naming
# ---------------------------------------------------------------------------
def default_new_name(name):
    if name == "Simple_Ten_Eighty":
        return "Simple_Fourteen_Forty"
    for a, b in (("1080", "1440"), ("FHD", "WQHD"), ("720", "1440")):
        if a in name:
            return name.replace(a, b)
    return f"{name}-1440"


def index_folders(skins_root):
    """{folder_name: path} for every top-level folder under 1080/ and 720/ (1080 wins)."""
    found = {}
    for res in ("720", "1080"):
        base = os.path.join(skins_root, res)
        if os.path.isdir(base):
            for d in sorted(os.listdir(base)):
                if os.path.isdir(os.path.join(base, d)):
                    found[d] = os.path.join(base, d)
    return found


def xml_files(folder):
    for root, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(".xml"):
                yield os.path.join(root, f)


def find_refs(folder, known):
    """Folder names referenced from this folder's XML, plus the exact relative paths used."""
    own_subdirs = {d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))}
    names = "|".join(re.escape(n) for n in sorted(known, key=len, reverse=True))
    pat = re.compile(rf"(?:/usr/share/enigma2/|(?<=[\"'>,:]))({names})/([^\"'<>,:\s]*)")
    refs = collections.defaultdict(set)
    for f in xml_files(folder):
        text = re.sub(r"<!--.*?-->", "", open(f, encoding="utf-8", errors="replace").read(), flags=re.S)
        for m in pat.finditer(text):
            name = m.group(1)
            absolute = text[max(0, m.start() - 19):m.start()] == "/usr/share/enigma2/"
            if name in own_subdirs and not absolute:
                continue  # resolves inside the skin's own folder first
            refs[name].add(m.group(2))
    return refs


def skin_resolution(folder):
    p = os.path.join(folder, "skin.xml")
    if os.path.exists(p):
        m = re.search(r'xres="(\d+)"', open(p, encoding="utf-8", errors="replace").read())
        if m:
            return int(m.group(1))
    return None


# ---------------------------------------------------------------------------
def convert_skin(name, folders, out_dir, rename_overrides):
    if name not in folders:
        raise SystemExit(f"Skin '{name}' not found. Available: {', '.join(sorted(folders))}")
    src = folders[name]
    xres = skin_resolution(src)
    if not xres:
        raise SystemExit(f"'{name}' has no skin.xml with a resolution - is it a shared/common folder?")
    if xres == TARGET_W:
        raise SystemExit(f"'{name}' is already {TARGET_W} wide")
    factor = Fraction(TARGET_W, xres)

    # dependency closure
    deps, partial, queue = {}, collections.defaultdict(set), [name]
    while queue:
        cur = queue.pop()
        if cur in deps:
            continue
        deps[cur] = folders[cur]
        for ref, paths in find_refs(folders[cur], folders).items():
            if ref == cur:
                continue
            other_skin = os.path.exists(os.path.join(folders[ref], "skin.xml"))
            other_res = os.path.dirname(folders[ref]) != os.path.dirname(src)
            if ref != name and (other_skin or other_res):
                partial[ref] |= paths  # another skin's folder: only borrow the files actually used
                deps.setdefault(ref, folders[ref])
            else:
                queue.append(ref)
    renames = {d: rename_overrides.get(d, default_new_name(d)) for d in deps}
    for d, n in renames.items():
        if n in folders:
            raise SystemExit(f"New name '{n}' for '{d}' clashes with an existing skin folder; use --rename {d}=OtherName")

    conv = Converter(factor, renames)
    new_name = renames[name]
    stage = os.path.join(out_dir, new_name)
    if os.path.exists(stage):
        shutil.rmtree(stage)
    root_out = os.path.join(stage, "usr", "share", "enigma2")
    counts = collections.Counter()
    missing = []

    for dep, dep_src in deps.items():
        dst_root = os.path.join(root_out, renames[dep])
        if dep in partial:
            files = sorted(p for p in partial[dep] if p and not p.endswith("/"))
        else:
            files = []
            for r, _, fs in os.walk(dep_src):
                for f in fs:
                    files.append(os.path.relpath(os.path.join(r, f), dep_src))
        for rel in files:
            s, d = os.path.join(dep_src, rel), os.path.join(dst_root, rel)
            base = os.path.basename(rel)
            if any(fnmatch.fnmatch(base, p) for p in SKIP_FILES):
                continue
            if rel.split(os.sep)[0] == "meta":  # package metadata installs to /usr/share/meta, handled below
                continue
            if not os.path.isfile(s):
                missing.append(f"{dep}/{rel}")
                continue
            os.makedirs(os.path.dirname(d), exist_ok=True)
            low = rel.lower()
            if low.endswith(".xml"):
                text = open(s, "rb").read().decode("utf-8")
                open(d, "wb").write(conv.convert_xml(text).encode("utf-8"))
                counts["xml"] += 1
            elif low.endswith((".png", ".jpg", ".jpeg")):
                conv.convert_image(s, d)
                counts["images"] += 1
            else:
                shutil.copy2(s, d)
                counts["copied"] += 1

    # package metadata (src/skins/<res>/<skin>/meta/skin_<skin>.xml installs to /usr/share/meta)
    meta_src = os.path.join(src, "meta", f"skin_{name}.xml")
    if os.path.isfile(meta_src):
        m = open(meta_src, encoding="utf-8").read()
        m = m.replace(f"<name>{name}</name>", f"<name>{new_name}</name>")
        def pkg(x):
            old = x.group(2)
            new = old.replace("1080", "1440").replace("fhd", "wqhd")
            return x.group(1) + (new if new != old else old + "-wqhd")
        m = re.sub(r"(<(?:packagename>|file type=\"package\" name=\"))([^<\"]+)", pkg, m)
        m = re.sub(r"\b(1080|720|FHD|HD) Skin\b", "1440 Skin", m)
        meta_dst = os.path.join(stage, "usr", "share", "meta", f"skin_{new_name}.xml")
        os.makedirs(os.path.dirname(meta_dst), exist_ok=True)
        open(meta_dst, "w", encoding="utf-8").write(m)

    # note the conversion in skin.xml
    skin_xml = os.path.join(root_out, new_name, "skin.xml")
    t = open(skin_xml, encoding="utf-8").read()
    t = re.sub(r"(<skin[^>]*>)", r"\1\n\t<!-- WQHD (2560x1440) conversion of " + name +
               f" by wqhd_convert.py: geometry, fonts and graphics scaled x{factor} -->", t, count=1)
    open(skin_xml, "w", encoding="utf-8").write(t)

    # report
    lines = [f"{name} -> {new_name}  (source {xres} wide, scale x{factor} = {float(factor):.4f})", ""]
    lines.append("Folders written to /usr/share/enigma2:")
    for dep in deps:
        how = "only the files it uses" if dep in partial else "full folder"
        lines.append(f"  {dep} -> {renames[dep]}  ({how})")
    lines += ["", f"Files: {dict(counts)}", ""]
    if missing:
        lines.append("Referenced files not found in the repo (left out):")
        lines += [f"  {m}" for m in missing] + [""]
    if conv.unknown:
        lines.append("Numeric attributes NOT scaled (unknown meaning - check these screens):")
        lines += [f"  {k}  x{v}" for k, v in sorted(conv.unknown.items())] + [""]
    if conv.left_expr:
        lines.append("Expressions left as-is (they use f/w/h and rescale themselves):")
        lines += [f"  {k}  x{v}" for k, v in sorted(conv.left_expr.items())] + [""]
    lines.append("Notes:")
    lines += [f"  {k}  x{v}" for k, v in sorted(conv.log.items()) if not k.startswith("expr ")]
    lines.append("  Layout expressions converted:")
    lines += [f"    {k[5:]}  x{v}" for k, v in sorted(conv.log.items()) if k.startswith("expr ")]
    report = "\n".join(lines) + "\n"
    open(os.path.join(out_dir, f"{new_name}-report.txt"), "w", encoding="utf-8").write(report)
    open(os.path.join(root_out, new_name, "CONVERSION-REPORT.txt"), "w", encoding="utf-8").write(report)
    # zip
    zpath = os.path.join(out_dir, f"{new_name}.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(stage):
            for f in sorted(fs):
                p = os.path.join(r, f)
                z.write(p, os.path.relpath(p, stage))

    print(f"{name} -> {zpath}  {dict(counts)}  unknown={sum(conv.unknown.values())}")
    return zpath


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skins-root", required=True, help="the repo's src/skins folder (contains 1080/ and 720/)")
    ap.add_argument("--skins", required=True, help="comma separated skin folder names, or 'all'")
    ap.add_argument("--out", default="dist")
    ap.add_argument("--rename", action="append", default=[], metavar="OLD=NEW",
                    help="override an output folder name (repeatable)")
    ap.add_argument("--list", action="store_true",
                    help="only check the names and print them as a JSON list (used by the workflow)")
    a = ap.parse_args(argv)
    folders = index_folders(a.skins_root)
    overrides = dict(r.split("=", 1) for r in a.rename)
    convertible = [n for n, p in folders.items() if skin_resolution(p) and n != "Default1080"]
    if a.skins.strip().lower() == "all":
        names = [n for n in convertible if os.path.basename(os.path.dirname(folders[n])) == "1080"]
    else:
        names = list(dict.fromkeys(s.strip().strip("/") for s in re.split(r"[,\s]+", a.skins) if s.strip()))
    bad = [n for n in names if n not in convertible]
    if bad:
        hint = {"Default1080": "it only wraps the image's built-in skin_default.xml"}
        for n in bad:
            why = hint.get(n) or ("it is a shared folder used by other skins, not a skin" if n in folders
                                  else "no such folder in 1080/ or 720/")
            print(f"ERROR: can't convert '{n}': {why}", file=sys.stderr)
        print("Convertible skins: " + ", ".join(sorted(convertible, key=str.lower)), file=sys.stderr)
        sys.exit(2)
    if a.list:
        import json
        print(json.dumps(names))
        return
    os.makedirs(a.out, exist_ok=True)
    failed = []
    for n in names:
        try:
            zpath = convert_skin(n, folders, a.out, overrides)
        except SystemExit as e:
            print(f"ERROR {n}: {e}", file=sys.stderr)
            failed.append(n)
            continue
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a") as gh:
                gh.write(f"new_name={os.path.basename(zpath)[:-4]}\n")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
