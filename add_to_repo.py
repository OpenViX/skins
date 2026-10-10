#!/usr/bin/env python3
"""
Copy converted skins into the repo as  src/skins/1440/<Skin>/  in the same layout
OpenViX/skins uses for 1080/ and 720/, with a Makefile.am in every folder.

Usage:
  python3 add_to_repo.py --repo-dir src/skins/1440  CONVERTED [CONVERTED ...]

Each CONVERTED is a folder holding the box layout written by wqhd_convert.py
(usr/share/enigma2/<Skin>/..., usr/share/meta/skin_<Skin>.xml).

Afterwards the script rewrites:
  <repo-dir>/Makefile.am                 SUBDIRS = every skin folder in <repo-dir>
  <repo-dir>/configure.ac-makefiles.txt  the Makefile lines to add to AC_OUTPUT in
                                         OpenViX/skins' configure.ac
"""
import argparse
import os
import re
import shutil

NOT_INSTALLED = {".am", ".txt", ".in"}  # not part of dist_install_DATA


def partial_folders(skin_dir):
    """Folders the converter only borrowed a few files into (read from its report)."""
    report = os.path.join(skin_dir, "CONVERSION-REPORT.txt")
    if not os.path.isfile(report):
        return set()
    text = open(report, encoding="utf-8").read()
    return set(re.findall(r"^  \S+ -> (\S+)  \(only the files it uses\)", text, flags=re.M))


def write_makefiles(folder, installdir):
    """Write Makefile.am for folder and every subfolder, OpenViX style."""
    for root, dirs, files in os.walk(folder):
        dirs.sort(key=str.lower)
        rel = os.path.relpath(root, folder)
        inst = installdir if rel == "." else f"{installdir}/{rel.replace(os.sep, '/')}"
        lines = [f"installdir = {inst}", ""]
        if dirs:
            lines += [f"SUBDIRS = {' '.join(dirs)}", ""]
        exts = sorted({os.path.splitext(f)[1].lower() for f in files} - NOT_INSTALLED - {""})
        if exts:
            lines.append("dist_install_DATA = " + " ".join(f"*{e}" for e in exts))
        open(os.path.join(root, "Makefile.am"), "w").write("\n".join(lines).rstrip() + "\n")


def add(converted, repo_dir):
    share = os.path.join(converted, "usr", "share")
    e2 = os.path.join(share, "enigma2")
    if not os.path.isdir(e2):
        raise SystemExit(f"{converted}: no usr/share/enigma2 inside - is this a converted skin?")
    folders = sorted(os.listdir(e2))
    skins = [f for f in folders if os.path.isfile(os.path.join(e2, f, "skin.xml"))]
    partial = set()
    for s in skins:
        partial |= partial_folders(os.path.join(e2, s))
    for f in folders:
        src, dst = os.path.join(e2, f), os.path.join(repo_dir, f)
        if f in partial:
            shutil.copytree(src, dst, dirs_exist_ok=True)  # merge: never wipe a full copy of that folder
        else:
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        write_makefiles(dst, f"$(datadir)/enigma2/{f}")
        print(f"  {f}{'  (merged, partial)' if f in partial else ''}")
    # package metadata -> <skin>/meta/
    meta = os.path.join(share, "meta")
    if os.path.isdir(meta):
        for m in sorted(os.listdir(meta)):
            skin = re.fullmatch(r"skin_(.+)\.xml", m)
            if not skin or not os.path.isdir(os.path.join(repo_dir, skin.group(1))):
                continue
            mdir = os.path.join(repo_dir, skin.group(1), "meta")
            os.makedirs(mdir, exist_ok=True)
            shutil.copy2(os.path.join(meta, m), mdir)
            open(os.path.join(mdir, "Makefile.am"), "w").write(f"installdir = $(datadir)/meta/\ndist_install_DATA = {m}\n")
            top = os.path.join(repo_dir, skin.group(1), "Makefile.am")  # add meta to the skin's SUBDIRS
            write_makefiles_top_with_meta(top)


def write_makefiles_top_with_meta(top_makefile):
    text = open(top_makefile).read()
    if re.search(r"^SUBDIRS = .*\bmeta\b", text, flags=re.M):
        return
    if "SUBDIRS = " in text:
        text = re.sub(r"^(SUBDIRS = .*)$", r"\1 meta", text, count=1, flags=re.M)
    else:
        text = text.replace("\n\n", "\n\nSUBDIRS = meta\n\n", 1)
    open(top_makefile, "w").write(text)


def refresh_index(repo_dir):
    names = sorted((d for d in os.listdir(repo_dir) if os.path.isdir(os.path.join(repo_dir, d))), key=str.lower)
    open(os.path.join(repo_dir, "Makefile.am"), "w").write(f"SUBDIRS = {' '.join(names)}\n")
    prefix = os.path.normpath(repo_dir).replace(os.sep, "/")
    if "/src/skins/" in f"/{prefix}":  # paths in configure.ac are relative to the repo root
        prefix = "src/skins/" + f"/{prefix}".split("/src/skins/", 1)[1]
    out = []
    for n in names:
        for root, dirs, files in os.walk(os.path.join(repo_dir, n)):
            dirs.sort(key=str.lower)
            if "Makefile.am" in files:
                rel = os.path.relpath(root, repo_dir).replace(os.sep, "/")
                out.append(f"{prefix}/{rel}/Makefile")
        out.append("")
    open(os.path.join(repo_dir, "configure.ac-makefiles.txt"), "w").write(
        f"{prefix}/Makefile\n\n" + "\n".join(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo-dir", default="src/skins/1440")
    ap.add_argument("converted", nargs="+")
    a = ap.parse_args()
    os.makedirs(a.repo_dir, exist_ok=True)
    for c in a.converted:
        print(f"{c}:")
        add(c, a.repo_dir)
    refresh_index(a.repo_dir)


if __name__ == "__main__":
    main()
