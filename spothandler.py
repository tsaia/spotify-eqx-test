import spotipy 
import spotipy.util as util
import spotipy.oauth2 as oa
from bottle import route, run, request

class playmaker(object):
	"""docstring for thing"""
	sp = spotipy.Spotify()

	user = ""
	def __init__(self, userarg):
		#super(thing, self).__init__()
		sp = spotipy.Spotify()
		user = userarg


	def makePlay(self, songs, name):
		playmake = self.sp.user_playlist_create(self.user,name, public=True)
		play = playmake['id']
		toadd = []
		for song in songs:
			if "Explicit" in song: #explicit in title throws off spotify search
				song = song[:song.index("Explicit")-1]
			result = self.sp.search(q=song, type='track', limit=1)
			if result['tracks']['items']:
				#print result['tracks']['items'][0]['name'], result['tracks']['items'][0]['uri']
				#print result['tracks']['items'][0]['uri'][14:]
				addsong = result['tracks']['items'][0]['uri']
				#print addsong
				toadd.append(addsong)
				#self.sp.user_playlist_add_tracks(self.user, play, addsong)
			else:
				print 'Not found:', song
		self.sp.user_playlist_add_tracks(self.user, play, toadd)

	def authorize(self, cid, secret, uri, scopea, cache):
		#modified from https://github.com/plamere/spotipy/blob/master/spotipy/util.py
		auth = oa.SpotifyOAuth(cid, secret, uri, scope=scopea, cache_path = cache)
		token_info = auth.get_cached_token()
		access_token = ""
		if token_info:
			access_token = token_info['access_token']
			self.sp = spotipy.Spotify(access_token)
			print "already have token"
		else: 
			url = request.url
			code = auth.parse_response_code(url)
			if code:
				print "token acquired"
				token_info = sp_oauth.get_access_token(code)
				access_token = token_info['access_token']
			else:
				print "could not get token"
		if access_token:
			print "have token"
			self.sp = spotipy.Spotify(access_token)
		else:
			print "no token"