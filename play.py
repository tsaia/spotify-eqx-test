from Sitehandler import eqx
from spothandler import playmaker
import sys

#earliest date = 2/11/2014 apparently
#command line: python play.py (y) (m) (d)

def main(argv):
	print argv
	
	sitenav = eqx()
	sitenav.openeqx()
	y = int(argv[0])
	m = int(argv[1])
	d = int(argv[2])
	songs = sitenav.songdriver(d,m,y) #dict {title:playcount}
	songs = sorted(songs.items(), key=lambda x: x[1]) #sort by play count
	i = len(songs)-1
	lim = i-40
	if lim < 0:
		lim = 0
	playgen = []
	while i >= lim:
		print songs[i]
		playgen.append(songs[i][0])
		i-=1
	print playgen[0]
	sitenav.br.close()
	#set these fields
	user = ""
	cid=""
	secret = ""
	uri = ""
	scope = ""
	cache = ""
	name = "EQX Top 40 of " + str(y) + "/" + str(m) + "/" + str(d)
	playlistmaker = playmaker(user)
	playlistmaker.authorize(cid, secret, uri, scope, cache)
	playlistmaker.makePlay(playgen, name)
	


if __name__ == "__main__":
	if len(sys.argv) < 4: print "Usage: (year) (month) (day)"
	else: main(sys.argv[1:])
