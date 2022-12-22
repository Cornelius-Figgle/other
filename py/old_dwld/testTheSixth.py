import os
from datetime import datetime

from eyed3 import load
from eyed3.id3.frames import ImageFrame
from mutagen.easyid3 import EasyID3
from requests import get
from spotipy import Spotify as Spotipy_
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = Spotipy_(client_credentials_manager = client_credentials_manager)

#________________________________________________________________________________________________________________________________

searchQuery = 'drivers liscense' + ' ' + 'olivia rodrigo'
searchResults = sp.search(q=searchQuery)
song = 'T:\py\projects\Spotify_Downloader\dwld\song.mp3'
pathDwld = 'T:\py\projects\Spotify_Downloader\dwld'

audio = EasyID3(song)

audio['title'] = searchResults['tracks']['items'][0]['name']
audio['artist'] = searchResults['tracks']['items'][0]['artists'][0]['name']
audio['album'] = searchResults['tracks']['items'][0]['album']['name']
audio['albumartist'] = searchResults['tracks']['items'][0]['album']['artists'][0]['name']
audio['originaldate'] = searchResults['tracks']['items'][0]['album']['release_date']
audio['date'] = datetime.utcnow().strftime('%Y-%m-%d')
audio['author'] = 'Spotify_Downloader.py'

audio.save()

img_data = get(searchResults['tracks']['items'][0]['album']['images'][0]['url']).content
os.makedirs(f'{pathDwld}\.tempCovers', exist_ok=True)
with open(f'{pathDwld}\.tempCovers\_cover.jpg', 'wb') as handler: handler.write(img_data)


audiofile = load(song)
if (audiofile.tag == None): audiofile.initTag()

audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(f'{pathDwld}\.tempCovers\_cover.jpg','rb').read(), 'image/jpeg')
audiofile.tag.save()

os.remove(f'{pathDwld}\.tempCovers\_cover.jpg')

input('end')



print(EasyID3.valid_keys.keys())

#dict_keys(['album', 'bpm', 'compilation', 'composer', 'copyright', 'encodedby', 'lyricist', 'length', 'media', 'mood', 'title', 'version', 'artist', 'albumartist', 'conductor', 'arranger', 'discnumber', 'organization', 'tracknumber', 'author', 'albumartistsort', 'albumsort', 'composersort', 'artistsort', 'titlesort', 'isrc', 'discsubtitle', 'language', 'genre', 'date', 'originaldate', 'performer:*', 'musicbrainz_trackid', 'website', 'replaygain_*_gain', 'replaygain_*_peak', 'musicbrainz_artistid', 'musicbrainz_albumid', 'musicbrainz_albumartistid', 'musicbrainz_trmid', 'musicip_puid', 'musicip_fingerprint', 'musicbrainz_albumstatus', 'musicbrainz_albumtype', 'releasecountry', 'musicbrainz_discid', 'asin', 'performer', 'barcode', 'catalognumber', 'musicbrainz_releasetrackid', 'musicbrainz_releasegroupid', 'musicbrainz_workid', 'acoustid_fingerprint', 'acoustid_id'])    
#dict_keys(['album', 'title', 'artist', 'albumartist', 'discnumber', 'tracknumber', 'author', 'date', 'originaldate'])    

input()

searchQuery = 'drivers liscense' + ' ' + 'olivia rodrigo'
searchResults = sp.search(q=searchQuery)
#print(searchResults)

print(searchResults['tracks']['items'][0]['album']['images'][0]['url']) #album art
print(searchResults['tracks']['items'][0]['album']['name']) #album name 
print(searchResults['tracks']['items'][0]['album']['artists'][0]['name']) #album artist
print(searchResults['tracks']['items'][0]['album']['release_date']) #album release date


print(searchResults['tracks']['items'][0]['name']) #track name
print(searchResults['tracks']['items'][0]['artists'][0]['name']) #artist name
print(searchResults['tracks']['items'][0]['track_number']) #tracknum
print(searchResults['tracks']['items'][0]['disc_number']) #discnum

"""
{'tracks': {'href': 'https://api.spotify.com/v1/search?query=drivers+liscense+olivia+rodrigo&type=track&offset=0&limit=10', 'items': [{'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 
'https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG'}, 'href': 'https://api.spotify.com/v1/artists/1McMsnEElThX1knmY4oliG', 'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo', 'type': 'artist', 'uri': 'spotify:artist:1McMsnEElThX1knmY4oliG'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 
'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 
'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 
'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 
'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 
'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'external_urls': {'spotify': 'https://open.spotify.com/album/6s84u2TUpR3wdUv4NgKA2j'}, 'href': 
'https://api.spotify.com/v1/albums/6s84u2TUpR3wdUv4NgKA2j', 'id': '6s84u2TUpR3wdUv4NgKA2j', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a91c10fe9472d9bd89802e5a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a91c10fe9472d9bd89802e5a', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a91c10fe9472d9bd89802e5a', 'width': 64}], 
'name': 'SOUR', 'release_date': '2021-05-21', 'release_date_precision': 'day', 'total_tracks': 11, 'type': 'album', 'uri': 'spotify:album:6s84u2TUpR3wdUv4NgKA2j'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG'}, 'href': 'https://api.spotify.com/v1/artists/1McMsnEElThX1knmY4oliG', 'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo', 'type': 'artist', 'uri': 'spotify:artist:1McMsnEElThX1knmY4oliG'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'disc_number': 1, 'duration_ms': 242013, 'explicit': True, 'external_ids': {'isrc': 'USUG12004749'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/5wANPM4fQCJwkGd4rN57mH'}, 'href': 'https://api.spotify.com/v1/tracks/5wANPM4fQCJwkGd4rN57mH', 'id': '5wANPM4fQCJwkGd4rN57mH', 'is_local': False, 'name': 'drivers license', 'popularity': 89, 'preview_url': None, 'track_number': 3, 'type': 'track', 'uri': 'spotify:track:5wANPM4fQCJwkGd4rN57mH'}, {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG'}, 'href': 'https://api.spotify.com/v1/artists/1McMsnEElThX1knmY4oliG', 'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo', 'type': 'artist', 'uri': 'spotify:artist:1McMsnEElThX1knmY4oliG'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'external_urls': {'spotify': 'https://open.spotify.com/album/7bYichzvtYHdjF8HF69dyA'}, 'href': 'https://api.spotify.com/v1/albums/7bYichzvtYHdjF8HF69dyA', 'id': '7bYichzvtYHdjF8HF69dyA', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273bdf5ed83a765fd10a97f08f1', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02bdf5ed83a765fd10a97f08f1', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851bdf5ed83a765fd10a97f08f1', 'width': 64}], 'name': 'SOUR', 'release_date': '2021-05-21', 'release_date_precision': 'day', 'total_tracks': 11, 'type': 'album', 'uri': 'spotify:album:7bYichzvtYHdjF8HF69dyA'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG'}, 'href': 'https://api.spotify.com/v1/artists/1McMsnEElThX1knmY4oliG', 'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo', 'type': 'artist', 'uri': 'spotify:artist:1McMsnEElThX1knmY4oliG'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'disc_number': 1, 'duration_ms': 242013, 'explicit': False, 'external_ids': {'isrc': 
'USUG12004750'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/4ml4WlnHDEpOK8HRVYTCWf'}, 'href': 'https://api.spotify.com/v1/tracks/4ml4WlnHDEpOK8HRVYTCWf', 'id': '4ml4WlnHDEpOK8HRVYTCWf', 'is_local': False, 'name': 'drivers license', 'popularity': 67, 'preview_url': None, 'track_number': 3, 'type': 'track', 'uri': 'spotify:track:4ml4WlnHDEpOK8HRVYTCWf'}, {'album': {'album_type': 'compilation', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': ['AE', 'AL', 'AR', 'AT', 'AU', 'BA', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 
'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW']
"""
