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
src/plugins/Makefile

src/plugins/Metrix/Makefile
src/plugins/Novum/Makefile

src/skins/Makefile
src/skins/720/Makefile

src/skins/720/Blue-HD/Makefile
src/skins/720/Blue-HD/buttons/Makefile
src/skins/720/Blue-HD/countries/Makefile
src/skins/720/Blue-HD/epg/Makefile
src/skins/720/Blue-HD/extensions/Makefile
src/skins/720/Blue-HD/fonts/Makefile
src/skins/720/Blue-HD/icons/Makefile
src/skins/720/Blue-HD/infobar/Makefile
src/skins/720/Blue-HD/meta/Makefile
src/skins/720/Blue-HD/ondemand/Makefile
src/skins/720/Blue-HD/piconbg/Makefile
src/skins/720/Blue-HD/screens/Makefile
src/skins/720/Blue-HD/spinner/Makefile

src/skins/720/Magic-HD-Night/Makefile
src/skins/720/Magic-HD-Night/buttons/Makefile
src/skins/720/Magic-HD-Night/crossepg/Makefile
src/skins/720/Magic-HD-Night/epg/Makefile
src/skins/720/Magic-HD-Night/meta/Makefile

src/skins/720/Magic-HD-Noire/Makefile
src/skins/720/Magic-HD-Noire/buttons/Makefile
src/skins/720/Magic-HD-Noire/crossepg/Makefile
src/skins/720/Magic-HD-Noire/epg/Makefile
src/skins/720/Magic-HD-Noire/meta/Makefile

src/skins/720/MetrixHD/Makefile
src/skins/720/MetrixHD/buttons/Makefile
src/skins/720/MetrixHD/buttonsHD/Makefile
src/skins/720/MetrixHD/colors/Makefile
src/skins/720/MetrixHD/Default/Makefile
src/skins/720/MetrixHD/Default/SkinDesign/Makefile
src/skins/720/MetrixHD/epg/Makefile
src/skins/720/MetrixHD/extensions/Makefile
src/skins/720/MetrixHD/fonts/Makefile
src/skins/720/MetrixHD/icons/Makefile
src/skins/720/MetrixHD/icons/message/Makefile
src/skins/720/MetrixHD/icons/picons/Makefile
src/skins/720/MetrixHD/iconsHD/Makefile
src/skins/720/MetrixHD/iconsHD/message/Makefile
src/skins/720/MetrixHD/iconsHD/picons/Makefile
src/skins/720/MetrixHD/menu/Makefile
src/skins/720/MetrixHD/meta/Makefile
src/skins/720/MetrixHD/mmp/Makefile
src/skins/720/MetrixHD/skin_default/Makefile
src/skins/720/MetrixHD/skin_default/buttons/Makefile
src/skins/720/MetrixHD/skin_default/icons/Makefile
src/skins/720/MetrixHD/SkinDesign/Makefile

src/skins/720/MHD-Common/Makefile
src/skins/720/MHD-Common/border/Makefile
src/skins/720/MHD-Common/buttons/Makefile
src/skins/720/MHD-Common/dvr/Makefile
src/skins/720/MHD-Common/fonts/Makefile
src/skins/720/MHD-Common/infobar/Makefile
src/skins/720/MHD-Common/logos/Makefile
src/skins/720/MHD-Common/window/Makefile

src/skins/720/PLi-HD-Night/Makefile
src/skins/720/PLi-HD-Night/border/Makefile
src/skins/720/PLi-HD-Night/buttons/Makefile
src/skins/720/PLi-HD-Night/dvr/Makefile
src/skins/720/PLi-HD-Night/epg/Makefile
src/skins/720/PLi-HD-Night/icons/Makefile
src/skins/720/PLi-HD-Night/infobar/Makefile
src/skins/720/PLi-HD-Night/logos/Makefile
src/skins/720/PLi-HD-Night/meta/Makefile
src/skins/720/PLi-HD-Night/window/Makefile

src/skins/720/Red-HD/Makefile
src/skins/720/Red-HD/buttons/Makefile
src/skins/720/Red-HD/countries/Makefile
src/skins/720/Red-HD/crossepg/Makefile
src/skins/720/Red-HD/epg/Makefile
src/skins/720/Red-HD/extensions/Makefile
src/skins/720/Red-HD/fonts/Makefile
src/skins/720/Red-HD/icons/Makefile
src/skins/720/Red-HD/infobar/Makefile
src/skins/720/Red-HD/meta/Makefile
src/skins/720/Red-HD/ondemand/Makefile
src/skins/720/Red-HD/screens/Makefile
src/skins/720/Red-HD/selectionbars/Makefile
src/skins/720/Red-HD/spinner/Makefile

src/skins/720/ViXBMC_HD-Common/Makefile
src/skins/720/ViXBMC_HD-Common/busy/Makefile
src/skins/720/ViXBMC_HD-Common/buttons/Makefile
src/skins/720/ViXBMC_HD-Common/common_icons/Makefile
src/skins/720/ViXBMC_HD-Common/fonts/Makefile
src/skins/720/ViXBMC_HD-Common/icons/Makefile
src/skins/720/ViXBMC_HD-Common/images/Makefile
src/skins/720/ViXBMC_HD-Common/menu/Makefile

src/skins/720/ViXBMC_HD-Night/Makefile
src/skins/720/ViXBMC_HD-Night/meta/Makefile

src/skins/720/ViXBMC_HD-Slim/Makefile
src/skins/720/ViXBMC_HD-Slim/meta/Makefile

src/skins/720/ViXBMC_Metropolis/Makefile
src/skins/720/ViXBMC_Metropolis/border/Makefile
src/skins/720/ViXBMC_Metropolis/busy/Makefile
src/skins/720/ViXBMC_Metropolis/buttons/Makefile
src/skins/720/ViXBMC_Metropolis/buttons_old/Makefile
src/skins/720/ViXBMC_Metropolis/dvr/Makefile
src/skins/720/ViXBMC_Metropolis/epg/Makefile
src/skins/720/ViXBMC_Metropolis/fonts/Makefile
src/skins/720/ViXBMC_Metropolis/icons/Makefile
src/skins/720/ViXBMC_Metropolis/infobar/Makefile
src/skins/720/ViXBMC_Metropolis/logos/Makefile
src/skins/720/ViXBMC_Metropolis/markus625/Makefile
src/skins/720/ViXBMC_Metropolis/meta/Makefile
src/skins/720/ViXBMC_Metropolis/osd/Makefile
src/skins/720/ViXBMC_Metropolis/VU/Makefile
src/skins/720/ViXBMC_Metropolis/window/Makefile

src/skins/720/ViX-Common/Makefile
src/skins/720/ViX-Common/buttons/Makefile
src/skins/720/ViX-Common/menu/Makefile

src/skins/720/ViX-Day-HD/Makefile
src/skins/720/ViX-Day-HD/crossepg/Makefile
src/skins/720/ViX-Day-HD/epg/Makefile
src/skins/720/ViX-Day-HD/icons/Makefile
src/skins/720/ViX-Day-HD/buttons/Makefile
src/skins/720/ViX-Day-HD/infobar/Makefile
src/skins/720/ViX-Day-HD/menu/Makefile
src/skins/720/ViX-Day-HD/meta/Makefile
src/skins/720/ViX-Day-HD/screens/Makefile

src/skins/720/ViX-Night-HD/Makefile
src/skins/720/ViX-Night-HD/crossepg/Makefile
src/skins/720/ViX-Night-HD/epg/Makefile
src/skins/720/ViX-Night-HD/icons/Makefile
src/skins/720/ViX-Night-HD/buttons/Makefile
src/skins/720/ViX-Night-HD/menu/Makefile
src/skins/720/ViX-Night-HD/meta/Makefile

src/skins/1080/Makefile

src/skins/1080/Default1080/Makefile
src/skins/1080/Halo/Makefile
src/skins/1080/Halo/buttons/Makefile
src/skins/1080/Halo/common/Makefile
src/skins/1080/Halo/countries/Makefile
src/skins/1080/Halo/crossepg/Makefile
src/skins/1080/Halo/epg/Makefile
src/skins/1080/Halo/extensions/Makefile
src/skins/1080/Halo/fonts/Makefile
src/skins/1080/Halo/Halo_fonts/Makefile
src/skins/1080/Halo/icons/Makefile
src/skins/1080/Halo/imdb/Makefile
src/skins/1080/Halo/infobar/Makefile
src/skins/1080/Halo/menuicons/Makefile
src/skins/1080/Halo/networkbrowser/Makefile
src/skins/1080/Halo/osd/Makefile
src/skins/1080/Halo/pvr/Makefile
src/skins/1080/Halo/pvr/pvr1/Makefile
src/skins/1080/Halo/pvr/pvr2/Makefile
src/skins/1080/Halo/pvr/pvrstate/Makefile
src/skins/1080/Halo/screens/Makefile
src/skins/1080/Halo/settings/Makefile
src/skins/1080/Halo/spinner/Makefile
src/skins/1080/Halo/views/Makefile
src/skins/1080/Halo/vixcore/Makefile

src/skins/1080/iSkin-Light/Makefile
src/skins/1080/iSkin-Light/buttons/Makefile
src/skins/1080/iSkin-Light/crossepg/Makefile
src/skins/1080/iSkin-Light/epg/Makefile
src/skins/1080/iSkin-Light/extensions/Makefile
src/skins/1080/iSkin-Light/icons/Makefile
src/skins/1080/iSkin-Light/meta/Makefile
src/skins/1080/iSkin-Light/networkbrowser/Makefile
src/skins/1080/iSkin-Light/screens/Makefile
src/skins/1080/iSkin-Light/skin_default/Makefile
src/skins/1080/iSkin-Light/skin_default/icons/Makefile
src/skins/1080/iSkin-Light/spinner/Makefile
src/skins/1080/iSkin-Light/vixcore/Makefile

src/skins/1080/iSkin-Dark/Makefile
src/skins/1080/iSkin-Dark/buttons/Makefile
src/skins/1080/iSkin-Dark/crossepg/Makefile
src/skins/1080/iSkin-Dark/epg/Makefile
src/skins/1080/iSkin-Dark/extensions/Makefile
src/skins/1080/iSkin-Dark/icons/Makefile
src/skins/1080/iSkin-Dark/meta/Makefile
src/skins/1080/iSkin-Dark/networkbrowser/Makefile
src/skins/1080/iSkin-Dark/screens/Makefile
src/skins/1080/iSkin-Dark/skin_default/Makefile
src/skins/1080/iSkin-Dark/skin_default/icons/Makefile
src/skins/1080/iSkin-Dark/spinner/Makefile
src/skins/1080/iSkin-Dark/vixcore/Makefile

src/skins/1080/iSkin-Common/Makefile
src/skins/1080/iSkin-Common/buttons/Makefile
src/skins/1080/iSkin-Common/fonts/Makefile
src/skins/1080/iSkin-Common/icons/Makefile
src/skins/1080/iSkin-Common/screens/Makefile

src/skins/1080/Magic-FHD/Makefile
src/skins/1080/Magic-FHD/border/Makefile
src/skins/1080/Magic-FHD/crossepg/Makefile
src/skins/1080/Magic-FHD/buttons/Makefile
src/skins/1080/Magic-FHD/countries/Makefile
src/skins/1080/Magic-FHD/dvr/Makefile
src/skins/1080/Magic-FHD/epg/Makefile
src/skins/1080/Magic-FHD/extensions/Makefile
src/skins/1080/Magic-FHD/fonts/Makefile
src/skins/1080/Magic-FHD/icons/Makefile
src/skins/1080/Magic-FHD/infobar/Makefile
src/skins/1080/Magic-FHD/meta/Makefile
src/skins/1080/Magic-FHD/networkbrowser/Makefile
src/skins/1080/Magic-FHD/plugins/Makefile
src/skins/1080/Magic-FHD/spinner/Makefile
src/skins/1080/Magic-FHD/window/Makefile

src/skins/1080/MetrixFHD/Makefile
src/skins/1080/MetrixFHD/buttons/Makefile
src/skins/1080/MetrixFHD/buttonsHD/Makefile
src/skins/1080/MetrixFHD/colors/Makefile
src/skins/1080/MetrixFHD/Default/Makefile
src/skins/1080/MetrixFHD/Default/SkinDesign/Makefile
src/skins/1080/MetrixFHD/epg/Makefile
src/skins/1080/MetrixFHD/extensions/Makefile
src/skins/1080/MetrixFHD/fonts/Makefile
src/skins/1080/MetrixFHD/icons/Makefile
src/skins/1080/MetrixFHD/icons/message/Makefile
src/skins/1080/MetrixFHD/icons/picons/Makefile
src/skins/1080/MetrixFHD/iconsHD/Makefile
src/skins/1080/MetrixFHD/iconsHD/message/Makefile
src/skins/1080/MetrixFHD/iconsHD/picons/Makefile
src/skins/1080/MetrixFHD/menu/Makefile
src/skins/1080/MetrixFHD/meta/Makefile
src/skins/1080/MetrixFHD/mmp/Makefile
src/skins/1080/MetrixFHD/skin_default/Makefile
src/skins/1080/MetrixFHD/skin_default/buttons/Makefile
src/skins/1080/MetrixFHD/skin_default/icons/Makefile
src/skins/1080/MetrixFHD/SkinDesign/Makefile

src/skins/1080/myNOVUM_FHD2/Makefile
src/skins/1080/myNOVUM_FHD2/buttons/Makefile
src/skins/1080/myNOVUM_FHD2/countries/Makefile
src/skins/1080/myNOVUM_FHD2/epg/Makefile
src/skins/1080/myNOVUM_FHD2/extensions/Makefile
src/skins/1080/myNOVUM_FHD2/fonts/Makefile
src/skins/1080/myNOVUM_FHD2/icons/Makefile
src/skins/1080/myNOVUM_FHD2/images/Makefile
src/skins/1080/myNOVUM_FHD2/images/pvrstate/Makefile
src/skins/1080/myNOVUM_FHD2/images/slider/Makefile
src/skins/1080/myNOVUM_FHD2/menu/Makefile
src/skins/1080/myNOVUM_FHD2/meta/Makefile
src/skins/1080/myNOVUM_FHD2/mmp/Makefile
src/skins/1080/myNOVUM_FHD2/SkinDesign/Makefile
src/skins/1080/myNOVUM_FHD2/spinner/Makefile
src/skins/1080/myNOVUM_FHD2/WeatherIcons/Makefile

src/skins/1080/myNOVUM_FHD2_Black/Makefile
src/skins/1080/myNOVUM_FHD2_Black/buttons/Makefile
src/skins/1080/myNOVUM_FHD2_Black/countries/Makefile
src/skins/1080/myNOVUM_FHD2_Black/epg/Makefile
src/skins/1080/myNOVUM_FHD2_Black/extensions/Makefile
src/skins/1080/myNOVUM_FHD2_Black/fonts/Makefile
src/skins/1080/myNOVUM_FHD2_Black/icons/Makefile
src/skins/1080/myNOVUM_FHD2_Black/images/Makefile
src/skins/1080/myNOVUM_FHD2_Black/images/pvrstate/Makefile
src/skins/1080/myNOVUM_FHD2_Black/images/slider/Makefile
src/skins/1080/myNOVUM_FHD2_Black/menu/Makefile
src/skins/1080/myNOVUM_FHD2_Black/meta/Makefile
src/skins/1080/myNOVUM_FHD2_Black/mmp/Makefile
src/skins/1080/myNOVUM_FHD2_Black/SkinDesign/Makefile
src/skins/1080/myNOVUM_FHD2_Black/spinner/Makefile
src/skins/1080/myNOVUM_FHD2_Black/WeatherIcons/Makefile

src/skins/1080/NOVUM_FHD_Slim/Makefile
src/skins/1080/NOVUM_FHD_Slim/buttons/Makefile
src/skins/1080/NOVUM_FHD_Slim/countries/Makefile
src/skins/1080/NOVUM_FHD_Slim/epg/Makefile
src/skins/1080/NOVUM_FHD_Slim/extensions/Makefile
src/skins/1080/NOVUM_FHD_Slim/fonts/Makefile
src/skins/1080/NOVUM_FHD_Slim/icons/Makefile
src/skins/1080/NOVUM_FHD_Slim/images/Makefile
src/skins/1080/NOVUM_FHD_Slim/images/pvrstate/Makefile
src/skins/1080/NOVUM_FHD_Slim/images/slider/Makefile
src/skins/1080/NOVUM_FHD_Slim/menu/Makefile
src/skins/1080/NOVUM_FHD_Slim/meta/Makefile
src/skins/1080/NOVUM_FHD_Slim/mmp/Makefile
src/skins/1080/NOVUM_FHD_Slim/SkinDesign/Makefile
src/skins/1080/NOVUM_FHD_Slim/spinner/Makefile
src/skins/1080/NOVUM_FHD_Slim/WeatherIcons/Makefile

src/skins/1080/Simple_Ten_Eighty/Makefile
src/skins/1080/Simple_Ten_Eighty/border/Makefile
src/skins/1080/Simple_Ten_Eighty/buttons/Makefile
src/skins/1080/Simple_Ten_Eighty/dvr/Makefile
src/skins/1080/Simple_Ten_Eighty/epg/Makefile
src/skins/1080/Simple_Ten_Eighty/extensions/Makefile
src/skins/1080/Simple_Ten_Eighty/fonts/Makefile
src/skins/1080/Simple_Ten_Eighty/icons/Makefile
src/skins/1080/Simple_Ten_Eighty/infobar/Makefile
src/skins/1080/Simple_Ten_Eighty/window/Makefile

src/skins/1080/ViX-1080-Common/Makefile
src/skins/1080/ViX-1080-Common/buttons/Makefile
src/skins/1080/ViX-1080-Common/menu/Makefile

src/skins/1080/ViX-Day-1080/Makefile
src/skins/1080/ViX-Day-1080/crossepg/Makefile
src/skins/1080/ViX-Day-1080/epg/Makefile
src/skins/1080/ViX-Day-1080/icons/Makefile
src/skins/1080/ViX-Day-1080/infobar/Makefile
src/skins/1080/ViX-Day-1080/menu/Makefile
src/skins/1080/ViX-Day-1080/meta/Makefile
src/skins/1080/ViX-Day-1080/screens/Makefile

src/skins/1080/ViX-Night-1080/Makefile
src/skins/1080/ViX-Night-1080/crossepg/Makefile
src/skins/1080/ViX-Night-1080/epg/Makefile
src/skins/1080/ViX-Night-1080/icons/Makefile
src/skins/1080/ViX-Night-1080/menu/Makefile
src/skins/1080/ViX-Night-1080/meta/Makefile

src/skins/1080/ViXBMC_1080/Makefile
src/skins/1080/ViXBMC_1080/buttons/Makefile
src/skins/1080/ViXBMC_1080/countries/Makefile
src/skins/1080/ViXBMC_1080/crossepg/Makefile
src/skins/1080/ViXBMC_1080/epg/Makefile
src/skins/1080/ViXBMC_1080/extensions/Makefile
src/skins/1080/ViXBMC_1080/fonts/Makefile
src/skins/1080/ViXBMC_1080/icons/Makefile
src/skins/1080/ViXBMC_1080/imdb/Makefile
src/skins/1080/ViXBMC_1080/infobar/Makefile
src/skins/1080/ViXBMC_1080/menuicons/Makefile
src/skins/1080/ViXBMC_1080/meta/Makefile
src/skins/1080/ViXBMC_1080/networkbrowser/Makefile
src/skins/1080/ViXBMC_1080/pvr/Makefile
src/skins/1080/ViXBMC_1080/screens/Makefile
src/skins/1080/ViXBMC_1080/spinner/Makefile
src/skins/1080/ViXBMC_1080/vixcore/Makefile

src/skins/1080/ViXBMC_1080_Bello/Makefile
src/skins/1080/ViXBMC_1080_Bello/buttons/Makefile
src/skins/1080/ViXBMC_1080_Bello/countries/Makefile
src/skins/1080/ViXBMC_1080_Bello/crossepg/Makefile
src/skins/1080/ViXBMC_1080_Bello/epg/Makefile
src/skins/1080/ViXBMC_1080_Bello/extensions/Makefile
src/skins/1080/ViXBMC_1080_Bello/icons/Makefile
src/skins/1080/ViXBMC_1080_Bello/imdb/Makefile
src/skins/1080/ViXBMC_1080_Bello/infobar/Makefile
src/skins/1080/ViXBMC_1080_Bello/meta/Makefile
src/skins/1080/ViXBMC_1080_Bello/networkbrowser/Makefile
src/skins/1080/ViXBMC_1080_Bello/pvr/Makefile
src/skins/1080/ViXBMC_1080_Bello/screens/Makefile
src/skins/1080/ViXBMC_1080_Bello/spinner/Makefile
src/skins/1080/ViXBMC_1080_Bello/vixcore/Makefile

src/skins/1080/ViXBMC_1080_Common/Makefile
src/skins/1080/ViXBMC_1080_Common/fonts/Makefile
src/skins/1080/ViXBMC_1080_Common/icons/Makefile
src/skins/1080/ViXBMC_1080_Common/infobar/Makefile
src/skins/1080/ViXBMC_1080_Common/yahoo/Makefile

src/skins/1080/ViXBMC_1080_Confluence/Makefile
src/skins/1080/ViXBMC_1080_Confluence/buttons/Makefile
src/skins/1080/ViXBMC_1080_Confluence/countries/Makefile
src/skins/1080/ViXBMC_1080_Confluence/crossepg/Makefile
src/skins/1080/ViXBMC_1080_Confluence/epg/Makefile
src/skins/1080/ViXBMC_1080_Confluence/extensions/Makefile
src/skins/1080/ViXBMC_1080_Confluence/icons/Makefile
src/skins/1080/ViXBMC_1080_Confluence/imdb/Makefile
src/skins/1080/ViXBMC_1080_Confluence/infobar/Makefile
src/skins/1080/ViXBMC_1080_Confluence/meta/Makefile
src/skins/1080/ViXBMC_1080_Confluence/networkbrowser/Makefile
src/skins/1080/ViXBMC_1080_Confluence/pvr/Makefile
src/skins/1080/ViXBMC_1080_Confluence/screens/Makefile
src/skins/1080/ViXBMC_1080_Confluence/spinner/Makefile
src/skins/1080/ViXBMC_1080_Confluence/vixcore/Makefile

src/skins/1080/YouViX-Blue/Makefile
src/skins/1080/YouViX-Blue/buttons/Makefile
src/skins/1080/YouViX-Blue/countries/Makefile
src/skins/1080/YouViX-Blue/crossepg/Makefile
src/skins/1080/YouViX-Blue/epg/Makefile
src/skins/1080/YouViX-Blue/extensions/Makefile
src/skins/1080/YouViX-Blue/icons/Makefile
src/skins/1080/YouViX-Blue/infobar/Makefile
src/skins/1080/YouViX-Blue/meta/Makefile
src/skins/1080/YouViX-Blue/networkbrowser/Makefile
src/skins/1080/YouViX-Blue/screens/Makefile
src/skins/1080/YouViX-Blue/selectionbars/Makefile
src/skins/1080/YouViX-Blue/spinner/Makefile
src/skins/1080/YouViX-Blue/vixcore/Makefile

src/skins/1080/YouViX-Common/Makefile
src/skins/1080/YouViX-Common/fonts/Makefile
src/skins/1080/YouViX-Common/icons/Makefile
src/skins/1080/YouViX-Common/imdb/Makefile
src/skins/1080/YouViX-Common/infobar/Makefile
src/skins/1080/YouViX-Common/logos/Makefile
src/skins/1080/YouViX-Common/menuicons/Makefile
src/skins/1080/YouViX-Common/ondemand/Makefile
src/skins/1080/YouViX-Common/pvr/Makefile
src/skins/1080/YouViX-Common/screens/Makefile
src/skins/1080/YouViX-Common/spinner/Makefile

src/skins/1080/YouViX-Green/Makefile
src/skins/1080/YouViX-Green/buttons/Makefile
src/skins/1080/YouViX-Green/countries/Makefile
src/skins/1080/YouViX-Green/crossepg/Makefile
src/skins/1080/YouViX-Green/epg/Makefile
src/skins/1080/YouViX-Green/extensions/Makefile
src/skins/1080/YouViX-Green/icons/Makefile
src/skins/1080/YouViX-Green/infobar/Makefile
src/skins/1080/YouViX-Green/meta/Makefile
src/skins/1080/YouViX-Green/networkbrowser/Makefile
src/skins/1080/YouViX-Green/screens/Makefile
src/skins/1080/YouViX-Green/selectionbars/Makefile
src/skins/1080/YouViX-Green/spinner/Makefile
src/skins/1080/YouViX-Green/vixcore/Makefile

src/skins/1080/YouViX-Purple/Makefile
src/skins/1080/YouViX-Purple/buttons/Makefile
src/skins/1080/YouViX-Purple/countries/Makefile
src/skins/1080/YouViX-Purple/crossepg/Makefile
src/skins/1080/YouViX-Purple/epg/Makefile
src/skins/1080/YouViX-Purple/extensions/Makefile
src/skins/1080/YouViX-Purple/icons/Makefile
src/skins/1080/YouViX-Purple/infobar/Makefile
src/skins/1080/YouViX-Purple/meta/Makefile
src/skins/1080/YouViX-Purple/networkbrowser/Makefile
src/skins/1080/YouViX-Purple/screens/Makefile
src/skins/1080/YouViX-Purple/selectionbars/Makefile
src/skins/1080/YouViX-Purple/spinner/Makefile
src/skins/1080/YouViX-Purple/vixcore/Makefile

src/skins/1080/YouViX-Red/Makefile
src/skins/1080/YouViX-Red/buttons/Makefile
src/skins/1080/YouViX-Red/countries/Makefile
src/skins/1080/YouViX-Red/crossepg/Makefile
src/skins/1080/YouViX-Red/epg/Makefile
src/skins/1080/YouViX-Red/extensions/Makefile
src/skins/1080/YouViX-Red/icons/Makefile
src/skins/1080/YouViX-Red/infobar/Makefile
src/skins/1080/YouViX-Red/meta/Makefile
src/skins/1080/YouViX-Red/networkbrowser/Makefile
src/skins/1080/YouViX-Red/screens/Makefile
src/skins/1080/YouViX-Red/selectionbars/Makefile
src/skins/1080/YouViX-Red/spinner/Makefile
src/skins/1080/YouViX-Red/vixcore/Makefile

])
