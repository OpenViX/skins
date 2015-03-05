SUBDIRS = src

metadir = $(datadir)/meta
meta_DATA = index-enigma2-skinspack.xml
CLEANFILES = index-enigma2-skinspack.xml

index-enigma2-skinspack.xml: $(top_srcdir)/genmetaindex.py $(top_srcdir)/src/skins/*/*/meta/skin_*.xml
	$(AM_V_GEN)$(PYTHON) $^ > $@
