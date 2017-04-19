import requests 
from requests_oauthlib import OAuth1

r = requests.get('https://api.spotify.com/v1/search?q={}&type=track'.format('Swalla'))
track_id = r.json()['tracks']['items'][0]['id']
track_features = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(track_id), auth = ('BQD-mlnSvNB8U_GvRjtO2QU__TAQtf4RKN37y61u9lParKiXYqYHC96QgUMv2f7GlcPC2N-ZcTEhVbEg8ilAKSUSQ0DUoeCsmJt9KOPDVCSaK25FtrQOdd5q5NggRiGTeflxZJlzmJ4'))
print(track_features)