#
#  EVENTS INFO Converter
#
#  Based on Converter NextEvents
#  by m0rphU & LN
#
#  Modified by tomele:
#  Added support for current event
#  Added descriptions as output
#
#  This code is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported
#  License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan
#  Abbott Way, Stanford, California 94305, USA.
#

from Components.Converter.Converter import Converter
from Components.Element import cached
from Components.VariableText import VariableText
from enigma import eLabel, eEPGCache, eServiceReference
from time import localtime, strftime, mktime, time
from datetime import datetime
from Components.config import config


class NovumEventsInfo(Converter, object):

	Event1 = 0
	Event2 = 1
	Event3 = 2
	PrimeTime = 3
	Event0 = 4

	noDuration = 10
	onlyDuration = 11
	withDuration = 12
	showDuration = 12
	shortDescription = 13
	longDescription = 14

	def __init__(self, type):
		Converter.__init__(self, type)
		self.epgcache = eEPGCache.getInstance()

		args = type.split(',')
		if len(args) != 2:
			raise ElementError("type must contain exactly 2 arguments")

		type = args.pop(0)
		showDuration = args.pop(0)

		if type == "Event1":
			self.type = self.Event1
		elif type == "Event2":
			self.type = self.Event2
		elif type == "Event3":
			self.type = self.Event3
		elif type == "PrimeTime":
			self.type = self.PrimeTime
		else:
			self.type = self.Event0

		if showDuration == "noDuration":
			self.showDuration = self.noDuration
		elif showDuration == "onlyDuration":
			self.showDuration = self.onlyDuration
		elif showDuration == "showDuration":
			self.showDuration = self.withDuration
		elif showDuration == "shortDescription":
			self.showDuration = self.shortDescription
		else:
			self.showDuration = self.longDescription

	@cached
	def getText(self):
		ref = self.source.service
		info = ref and self.source.info
		if info is None:
			return ""
		textvalue = ""
		if self.type < self.PrimeTime:
			curEvent = self.source.getCurrentEvent()
			if curEvent:
				self.epgcache.startTimeQuery(eServiceReference(ref.toString()), curEvent.getBeginTime() + curEvent.getDuration())
				nextEvents = []
				for i in range(self.type): # Hole x-1 Eintraege aus dem EPG
					self.epgcache.getNextTimeEntry()
				#nextEvent.getEventId(), sRef, nextEvent.getBeginTime(), nextEvent.getDuration(), nextEvent.getEventName(), nextEvent.getShortDescription(), nextEvent.getExtendedDescription()
				next = self.epgcache.getNextTimeEntry()
				if next:
					textvalue = self.formatEvent(next)

		elif self.type == self.PrimeTime:
			curEvent = self.source.getCurrentEvent()
			if curEvent:
				now = localtime(time())
				try:
	                           dt = datetime(now.tm_year, now.tm_mon, now.tm_mday, int(config.plugins.Novum.Primetime.value[0]), int(config.plugins.Novum.Primetime.value[1]))
                                except:
                                   dt = datetime(now.tm_year, now.tm_mon, now.tm_mday, 20, 15)
				primeTime = int(mktime(dt.timetuple()))
				self.epgcache.startTimeQuery(eServiceReference(ref.toString()), primeTime)
				next = self.epgcache.getNextTimeEntry()
				if next and (next.getBeginTime() <= int(mktime(dt.timetuple()))):
					textvalue = self.formatEvent(next)
		else:
			event = self.source.event
			if event:
				textvalue = self.formatEvent(event)

		return textvalue

	text = property(getText)

	def formatEvent(self, event):
		begin = strftime("%H:%M", localtime(event.getBeginTime()))
		end = strftime("%H:%M", localtime(event.getBeginTime() + event.getDuration()))
		title = event.getEventName()#[:self.titleWidth]
		duration = "%d min" % (event.getDuration() / 60)
		sdescr = event.getShortDescription()
		ldescr = event.getExtendedDescription()
		if self.showDuration == self.withDuration:
			f = "{begin} - {end:10}{title:<} -  {duration}"
			return f.format(begin=begin, end=end, title=title, duration=duration)
		elif self.showDuration == self.onlyDuration:
			return duration
		elif self.showDuration == self.noDuration:
			f = "{begin} {title:<}"
			return f.format(begin=begin, end=end, title=title)
		elif self.showDuration == self.shortDescription:
			return sdescr
		elif self.showDuration == self.longDescription:
			return ldescr
		else:
			return ""
