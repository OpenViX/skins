##
## Picon renderer by Gruffy .. some speedups by Ghost
## XPicon mod by iMaxxx
##
from Renderer import Renderer
from enigma import ePixmap, eServiceReference
from Tools.Directories import fileExists, SCOPE_SKIN_IMAGE, SCOPE_CURRENT_SKIN, resolveFilename

class XPiconChannel(Renderer):
	searchPaths = ('/media/hdd/XPicons/%s/','/media/usb/XPicons/%s/','/usr/share/enigma2/XPicons/%s/','/usr/share/enigma2/%s/Picon2/', '/media/sde1/%s/Picon2/', '/media/cf/%s/Picon2/', '/media/sdd1/%s/Picon2/', '/media/usb/%s/Picon2/', '/media/ba/%s/Picon2/', '/mnt/ba/%s/Picon2/', '/media/sda/%s/Picon2/', '/etc/%s/Picon2/', '/usr/share/enigma2/%s/', '/media/sde1/%s/', '/media/cf/%s/', '/media/sdd1/%s/', '/media/usb/%s/', '/media/ba/%s/', '/mnt/ba/%s/', '/media/sda/%s/', '/etc/%s/')
	

	def __init__(self):
		Renderer.__init__(self)
		self.path = "picon"
		self.nameCache = { }
		self.pngname = ""

	def applySkin(self, desktop, parent):
		attribs = [ ]
		for (attrib, value) in self.skinAttributes:
			if attrib == "path":
				self.path = value
			else:
				attribs.append((attrib,value))
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, parent)

	GUI_WIDGET = ePixmap

	def changed(self, what):
		if self.instance:
			pngname = ""
			if what[0] != self.CHANGED_CLEAR:
				service = self.source.service
				marker = (service.flags & eServiceReference.isMarker == eServiceReference.isMarker)
				bouquet = (service.flags & eServiceReference.flagDirectory == eServiceReference.flagDirectory)
				print marker
				print bouquet
				if marker:
					pngname = self.nameCache.get("marker", "")
					if pngname == "": # no default yet in cache..
						tmp = resolveFilename(SCOPE_CURRENT_SKIN, "marker.png")
						if fileExists(tmp):
							pngname = tmp
						else:
							pngname = resolveFilename(SCOPE_SKIN_IMAGE, "skin_default/marker.png")

						self.nameCache["marker"] = pngname
				elif bouquet:
					pngname = self.nameCache.get("bouquet", "")
					if pngname == "": # no default yet in cache..
						tmp = resolveFilename(SCOPE_CURRENT_SKIN, "bouquet.png")
						if fileExists(tmp):
							pngname = tmp
						else:
							pngname = resolveFilename(SCOPE_SKIN_IMAGE, "skin_default/bouquet.png")

						self.nameCache["bouquet"] = pngname
				else:
					sname = service.toString()
					# strip all after last :
					pos = sname.rfind(':')
					if pos != -1:
						sname = sname[:pos].rstrip(':').replace(':','_')
					pngname = self.nameCache.get(sname, "")
					if pngname == "":
						pngname = self.findPicon(sname)
						if pngname != "":
							self.nameCache[sname] = pngname
			
			if pngname == "": # no picon for service found
				pngname = self.nameCache.get("default", "")
				if pngname == "": # no default yet in cache..
					pngname = self.findPicon("picon_default")
					if pngname == "":
						tmp = resolveFilename(SCOPE_CURRENT_SKIN, "picon_default.png")
						if fileExists(tmp):
							pngname = tmp
						else:
							pngname = resolveFilename(SCOPE_SKIN_IMAGE, "skin_default/picon_default.png")
					self.nameCache["default"] = pngname

			if self.pngname != pngname:
				self.instance.setPixmapFromFile(pngname)
				self.pngname = pngname

	def findPicon(self, serviceName):
		print "ActiveXPicon: " + serviceName
		for path in self.searchPaths:
			pngname = (path % self.path) + serviceName + ".png"
			if fileExists(pngname):
				return pngname
		return ""
