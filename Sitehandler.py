from selenium import webdriver
import datetime as dt


class eqx(object):
	def __init__(self):
		super(eqx, self).__init__()
		self.br = None #browser
		self.songs = {} #songs to be accessed for the spotify playlist
		
	def openeqx(self):
		self.br = webdriver.Chrome()
		self.br.get('http://www.weqx.com/song-history/')

	def getsongs(self, curtime):
		time = self.br.find_element_by_name('playlisttime')
		time.clear()
		time.send_keys(curtime)
		submit = self.br.find_element_by_name('submitbtn')
		submit.click()
		content = self.br.find_elements_by_class_name('songhistoryitem')
		for song in content:
			title = (song.get_property('title'))
			if title in self.songs: #i miss maps man
				self.songs[title]+=1
			else:
				self.songs[title]=1

	def songdriver(self,d,m,y):
		day = dt.date(y,m,d)
		daydif = dt.timedelta(days=1)
		endday = day - dt.timedelta(days=1)
  		am = ["am", "pm"]
  		thirty = ["00", "30"] 
  		while day != endday:
  			#change the date of song log
			date = self.br.find_element_by_name('playlistdate')
			date.clear()
			daystring = str(day.month)+"/"+str(day.day)+"/"+str(day.year)
			date.send_keys(daystring)
			submit = self.br.find_element_by_name('submitbtn')
			submit.click()
			for tOfD in am: #time of day am/pm
				for hour in range(1,13):
					for minute in thirty:
						curtime = str(hour)+":"+minute+tOfD
						self.getsongs(curtime)
			day = day - daydif
  		return self.songs