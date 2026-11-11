# Install the OpenViX skins.
#
#   make install DESTDIR=<root> [datadir=/usr/share] [SKINS1080=0] [PYTHON=python3]
#
# Every folder under src/skins/720/ (and src/skins/1080/ unless SKINS1080=0)
# is a skin. Its files are installed to $(datadir)/enigma2/<folder>/, its
# meta/*.xml to $(datadir)/meta/, and genmetaindex.py builds the skins index
# from the meta files of the installed skins. Adding a skin only needs its folder.

DESTDIR ?=
datadir ?= /usr/share
PYTHON ?= python3
SKINS1080 ?= 1

# file types installed from the skin folders
EXTS := png xml ttf otf jpg txt

SKINDIRS := $(wildcard src/skins/720/*/)
ifneq ($(SKINS1080),0)
SKINDIRS += $(wildcard src/skins/1080/*/)
endif
SKINDIRS := $(patsubst %/,%,$(SKINDIRS))
METAXML := $(sort $(wildcard $(addsuffix /meta/skin_*.xml,$(SKINDIRS))))

FIND_EXTS := $(patsubst %,-o -name '*.%',$(EXTS))
FIND_EXTS := $(wordlist 2,$(words $(FIND_EXTS)),$(FIND_EXTS))

.PHONY: all clean install
all:

clean:

install:
	@set -e; \
	for skin in $(SKINDIRS); do \
		name=$${skin##*/}; \
		( cd "$$skin" && find . -type f ! -path './meta/*' \( $(FIND_EXTS) \) ) | \
		while read -r f; do \
			install -D -m 0644 "$$skin/$$f" "$(DESTDIR)$(datadir)/enigma2/$$name/$${f#./}"; \
		done; \
		if [ -d "$$skin/meta" ]; then \
			install -d "$(DESTDIR)$(datadir)/meta"; \
			install -m 0644 "$$skin"/meta/*.xml "$(DESTDIR)$(datadir)/meta/"; \
		fi; \
	done
	install -d "$(DESTDIR)$(datadir)/meta"
	$(PYTHON) genmetaindex.py $(METAXML) > "$(DESTDIR)$(datadir)/meta/index-enigma2-skinspack.xml"
