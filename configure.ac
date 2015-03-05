AC_INIT([enigma2-skinspack],1.0.0,[andrew.blackburn644@btinternet.com])
AM_INIT_AUTOMAKE([foreign])

m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AM_PATH_PYTHON

AC_ARG_WITH(skins1080,
	AC_HELP_STRING([--with-skins1080], [machine support 1080p skins yes no]),
	[[withskins1080=$withval]],
	[[withskins1080=no]]
)
if test x"$withskins1080" != xno ; then
	AC_DEFINE(HAVE_SKINS1080, 1,[Define if machine support 1080p skins.])
fi
AM_CONDITIONAL(HAVE_SKINS1080, test x"$withskins1080" != xno)

A
AC_OUTPUT([
Makefile
src/Makefile
skins/src/converters/Makefile
skins/src/renderers/Makefile
skins/src/plugins/Makefile
skins/src/plugins/metrixplugin/Makefile
skins/src/plugins/metrixplugin/data/Makefile
skins/src/plugins/metrixplugin/email/Makefile
skins/src/plugins/metrixplugin/images/Makefile
skins/src/plugins/metrixplugin/locale/Makefile
skins/src/plugins/metrixplugin/locale/de/Makefile
skins/src/plugins/metrixplugin/locale/de/LC_MESSAGES/Makefile
skins/src/plugins/metrixplugin/skinparts/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/active/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_105/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_108/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_109/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_118/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_121/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_122/Makefile
skins/src/plugins/metrixplugin/skinparts/screens/inactive/screen_172/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/active/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_14/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_16/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_20/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_23/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_24/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_27/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_28/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_29/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_39/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_103/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_119/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_120/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_139/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_141/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_155/Makefile
skins/src/plugins/metrixplugin/skinparts/widgets/inactive/widget_169/Makefile
skins/src/plugins/metrixplugin/skintemplates/Makefile

skins/src/skins/Makefile
skins/src/skins/720/Makefile
skins/src/skins/720/MetrixHD/Makefile
skins/src/skins/720/MetrixHD/buttons/Makefile
skins/src/skins/720/MetrixHD/buttonsHD/Makefile
skins/src/skins/720/MetrixHD/colors/Makefile
skins/src/skins/720/MetrixHD/Default/Makefile
skins/src/skins/720/MetrixHD/Default/SkinDesign
skins/src/skins/720/MetrixHD/epg/Makefile
skins/src/skins/720/MetrixHD/extensions/Makefile
skins/src/skins/720/MetrixHD/fonts/Makefile
skins/src/skins/720/MetrixHD/icons/Makefile
skins/src/skins/720/MetrixHD/icons/message/Makefile
skins/src/skins/720/MetrixHD/icons/picons/Makefile
skins/src/skins/720/MetrixHD/iconsHD/Makefile
skins/src/skins/720/MetrixHD/iconsHD/message/Makefile
skins/src/skins/720/MetrixHD/iconsHD/picons/Makefile
skins/src/skins/720/MetrixHD/menu/Makefile
skins/src/skins/720/MetrixHD/mmp/Makefile
skins/src/skins/720/MetrixHD/skin_default/Makefile
skins/src/skins/720/MetrixHD/skin_default/buttons/Makefile
skins/src/skins/720/MetrixHD/skin_default/icons/Makefile
skins/src/skins/720/MetrixHD/SkinDesign/Makefile

skins/src/skins/1080
])
