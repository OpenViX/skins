# Enigma2 skins → 2560×1440 (WQHD)

A GitHub Action that takes skins from [OpenViX/skins](https://github.com/OpenViX/skins) and rescales them to 2560×1440 for EGL/GLES OpenViX builds that support a 1440p canvas (e.g. VU+ Uno 4K / Duo 4K / Zero 4K, GigaBlue Quad 4K / UE 4K).

The conversion step:
- scales every position, size, font size, item height, padding, parameter and list template by 4/3 (1080 skins) or 2 (720 skins). Layout expressions such as `e-85`, `c+15`, `e//42*42` and `17*45` are scaled too.
- resizes all PNG/JPG graphics to match.
- renames the skin so it installs alongside the original. For example `Simple_Ten_Eighty` → `Simple_Fourteen_Forty`, `YouViX-Blue` → `YouViX-Blue-1440`, `MetrixFHD` → `MetrixWQHD`.
- converts and renames any shared folder the skin uses, such as `YouViX-Common` → `YouViX-Common-1440`.

## Running it

1. Push this repository to your own GitHub account. Actions must be enabled for it.
2. Go to **Actions → Convert skins to 2560x1440 → Run workflow**.
3. Enter the skin folder names from `src/skins/1080`, separated by commas, e.g. `Simple_Ten_Eighty, YouViX-Blue`, or enter `all`. You can also give 720 skins from `src/skins/720`.
4. When the run finishes, download each skin from the run's **Artifacts** section. If you ticked *release*, they are also attached to a new Release.
5. With *add_to_repo* ticked (the default), the run also commits the converted skins to `src/skins/1440/` in this repo. See below.

Each download unzips to `usr/share/enigma2/...`. Copy that onto the box, or unzip it at `/` on the box, then restart the GUI and pick the skin in the skin selector.

Each skin's job summary shows its conversion report. The report is also saved as `CONVERSION-REPORT.txt` inside the skin folder. It lists:
- **Numeric attributes NOT scaled**: attributes whose meaning the converter couldn't tell. Check the screens that use them.
- **Referenced files not found**: images the skin points at that aren't in the repo. These usually come from the image's `skin_default`, so they stay at their original size.

## The `src/skins/1440` folder

Each run with *add_to_repo* ticked copies the converted skins into `src/skins/1440/`. This uses the same layout as `src/skins/1080/` and `src/skins/720/` in OpenViX/skins:

```
src/skins/1440/
  Makefile.am                    SUBDIRS = every skin and shared folder here
  configure.ac-makefiles.txt     Makefile lines for configure.ac (see below)
  Simple_Fourteen_Forty/
    Makefile.am                  installdir = $(datadir)/enigma2/Simple_Fourteen_Forty
    buttons/Makefile.am ...      one per subfolder
    CONVERSION-REPORT.txt
  YouViX-Blue-1440/
    meta/skin_YouViX-Blue-1440.xml   package info, installed to $(datadir)/meta
  YouViX-Common-1440/            shared folders get their own entry
```

When you re-run a skin, its folder is replaced. If the source hasn't changed, the output is identical and no commit is made. The workflow needs **Settings → Actions → General → Workflow permissions** set to *Read and write* so it can push.

### Building it into an OpenViX/skins checkout

To build these into a checkout of OpenViX/skins with its autotools setup, copy `src/skins/1440` across, then:

1. In `src/skins/Makefile.am` add:
   ```
   if HAVE_SKINS1440
   SUBDIRS += 1440
   endif
   ```
2. In `configure.ac`, before `AC_OUTPUT([`, add:
   ```
   AC_ARG_WITH(skins1440,
   	AC_HELP_STRING([--with-skins1440], [machine support 1440p skins yes no]),
   	[[withskins1440=$withval]],
   	[[withskins1440=no]]
   )
   if test x"$withskins1440" != xno ; then
   	AC_DEFINE(HAVE_SKINS1440, 1,[Define if machine support 1440p skins.])
   fi
   AM_CONDITIONAL(HAVE_SKINS1440, test x"$withskins1440" != xno)
   ```
3. Inside `AC_OUTPUT([ ... ])`, paste the contents of `src/skins/1440/configure.ac-makefiles.txt`.
4. Build with `./configure --with-skins1440`. The image recipe must pass that option. OpenViX's EGL builds set a `skins1440` machine feature on boxes that support it, but the skins recipe has to be updated to use it.

## Running locally

```sh
pip install pillow
git clone --depth 1 https://github.com/OpenViX/skins.git openvix-skins
python3 wqhd_convert.py --skins-root openvix-skins/src/skins --skins "Simple_Ten_Eighty" --out dist
```

Use `--rename OLD=NEW` to choose your own output folder name. To lay the result out as `src/skins/1440`:

```sh
python3 add_to_repo.py --repo-dir src/skins/1440 dist/*/
```

## Limits

- `Default1080` can't be converted. It only wraps the image's built-in `skin_default.xml`.
- Graphics are upscaled from the 1080 artwork, so icons are a little softer than text, which renders at full resolution.
- Images supplied by plugins or by the image itself (outside the skin folder) are not scaled.
- Python "applet" code inside skins is scaled with a rule: every integer is scaled except list indexes, divisors and text-length checks. Check message boxes after converting a new skin.
