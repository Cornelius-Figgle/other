# pyinstaller --noconfirm --log-level=WARN --clean --distpath ".\bin\bin" --workpath ".\bin\build" --name spotify_downloader --onefile --paths ".\spotify-env\Lib\site-packages" .\main.py
# pyinstaller --noconfirm --log-level=WARN --clean --distpath "./bin/bin" --workpath "./bin/build" --name spotify_downloader --onefile --paths "./spotify-env/Lib/site-packages" ./main.py
# -*- coding: UTF-8 -*-

# https://github.com/Cornelius-Figgle/spotify-downloader/

'''
THIS FILE IS PART OF THE `spotify-downloader` REPO, MAINTAINED AND 
PRODUCED BY MAX HARRISON, AS OF 2022

It may work separately and independently of the main repo, it may not

 - Code (c) Max Harrison 2022

'''

# note: view associated GitHub info as well
__version__ = 'Pre-release'  
__author__ = 'Cornelius-Figgle'
__email__ = 'max@fullimage.net'
__maintainer__ = 'Cornelius-Figgle'
__copyright__ = 'Copyright (c) 2022 Max Harrison'
__license__ = 'MIT'
__status__ = 'Development'
__credits__ = ['Max Harrison']

import os
import subprocess
import sys
from contextlib import contextmanager
from io import BytesIO
from msvcrt import getwche
from re import findall
from urllib import parse
from urllib.request import Request, urlopen

from moviepy.editor import VideoFileClip
from pytube import YouTube
from spotipy import Spotify as Spotipy_
from spotipy.oauth2 import SpotifyClientCredentials


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
# NOTE: copied this from here, thanks
# NOTE: https://www.delftstack.com/howto/python/python-clear-console

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials()
sp = Spotipy_(client_credentials_manager = client_credentials_manager)

@contextmanager
def nostdout() -> None:
    save_stdout = sys.stdout
    sys.stdout = BytesIO()
    yield
    sys.stdout = save_stdout

illegalChars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '¦']


def getTracksFromSpotifyPlaylist(playlist_link):
    playlist_URI = playlist_link.split('/')[-1].split('?')[0]

    songsToDownload = []
    print('\n\tListing songs...\n')
    
    UP = "\x1B[3A"
    CLR = "\x1B[0K"
    print('\n\n')

    for track in sp.playlist_tracks(playlist_URI)['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']

        songsLeftToFindUrls = len(sp.playlist_tracks(playlist_URI)['items']) - len(songsToDownload) - 1
        prog = '#'*len(songsToDownload)
        prog += '-'*songsLeftToFindUrls
        print(f'{UP}\t{prog}{CLR}\n\t{track_name} by {artist_name}{CLR}\n')

        track_name_spl = track_name.split()
        artist_name_spl = artist_name.split()

        song = '+'.join(track_name_spl) + '+by+' + '+'.join(artist_name_spl)
        songsToDownload.append(song)

    return songsToDownload

def getUrlsFromYT(songsToDownload):
    urlsToDownload = []

    print('\n\tListing URLs...\n')
    UP = "\x1B[3A"
    CLR = "\x1B[0K"
    print('\n\n')
    for track in songsToDownload:
        songsLeftToFindUrls = len(songsToDownload) - len(urlsToDownload) - 1
        prog = '#'*len(urlsToDownload)
        prog += '-'*songsLeftToFindUrls
        trackd = track.replace('+', ' ')
        print(f'{UP}\t{prog}{CLR}\n\t{trackd}{CLR}\n')

        songParse = parse.quote(str(track), safe='')
        url = Request('https://www.youtube.com/results?search_query=' + songParse, headers={'User-Agent': 'Mozilla/5.0'})

        html = urlopen(url)
        video_ids = findall(r'watch\?v=(\S{11})', html.read().decode())
        vidUrl = 'https://www.youtube.com/watch?v='+ video_ids[0]
        urlsToDownload.append(vidUrl)

    return urlsToDownload

def downloadVidsFrom_ThenConvert(urlsToDownload, songsToDownload, pathDwld):
    print(f'\n\n\tDownloading videos to \'{pathDwld}\' and converting to MP3...\n')
    UP = "\x1B[3A"
    CLR = "\x1B[0K"
    print('\n\n')
    startPathSize = sum(len(files) for _, _, files in os.walk(pathDwld))

    for trackURL in urlsToDownload:
        trackName = songsToDownload[urlsToDownload.index(trackURL)]
        trackName = trackName.replace('+', ' ')
        
        pathSize = sum(len(files) for _, _, files in os.walk(pathDwld))
        pathSize -= startPathSize

        vidsLeftToDownload = len(urlsToDownload) - pathSize -1 
        prog = '#'*pathSize
        prog += '-'*vidsLeftToDownload
        if urlsToDownload.index(trackURL) == 0: print(f'{UP}\t{prog}{CLR}\n\t{trackName}{CLR}\n') #no, like, moviepy bar ¯\(ツ)/¯
        else: print(f'\x1B[2A{UP}\t{prog}{CLR}\n\t{trackName}{CLR}\n{CLR}\n{CLR}\n{CLR}\x1B[2A') #I'm lazy and ``nostdout()`` doesn't work for moviepy ¯\(ツ)/¯ 


        try:
            process = subprocess.run(
                [
                    'yt-dlp',
                    '-P',
                    pathDwld,
                    '--no-playlist',
                    trackURL
                ], 
                shell=True, check=True, text=True,
                stderr=subprocess.PIPE, stdout=subprocess.PIPE
            )

            print(process)
        except subprocess.CalledProcessError as e:
            print(e.returncode, e.stderr, e.output)

        with nostdout():
            yt = YouTube(trackURL)
            video_title = yt.title
            video_id = str(yt)[-12:-1]

            for char in video_title:
                if char in illegalChars:
                    video_title = video_title.replace(char, '_')
            video_title_path = os.path.join(pathDwld, video_title + ' [' + video_id + '].mp4')

            for char in trackName:
                if char in illegalChars:
                    trackName = trackName.replace(char, '_')
            trackName_path = os.path.join(pathDwld, trackName + '.mp3')
            
        videoclip = VideoFileClip(video_title_path)
        
        audioclip = videoclip.audio
        audioclip.write_audiofile(trackName_path)
            
        audioclip.close()
        videoclip.close()

        os.remove(video_title_path)

def removeDuplicates(list):
    countDupes = {}
    for i in list:
        if not i in countDupes:
            countDupes[i] = 1
        else:
            countDupes[i] +=1

    numOfDupes = 0
    for i in countDupes:
        if countDupes[i] > 1: 
            numOfDupes += 1

    if numOfDupes <= 0: return list
    print(f'\n\t{numOfDupes} duplicates were found')
    print('', end='\tDo you want to remove them? y/n\n\t\t')
    choice = getwche()
    if choice == 'y' or choice == 'Y': 
        for i in list:
            if countDupes[i] > 1: list.remove(i)
        return list
    elif choice == 'n' or choice == 'N': return list
    else: pass

#________________________________________________________________________________________________________________________________

def main():
    print('\n\tUse Spotify Playlist? y/n\n\t\t')
    choice = getwche()
    if choice == 'y' or choice == 'Y':
        linkToPlaylist = input('\n\tPlease provide a link:\n\t\t')
        while linkToPlaylist is None: linkToPlaylist = input('\n\tPlease provide a link:\n\t\t')

        songsToDownload = getTracksFromSpotifyPlaylist(linkToPlaylist)
        songsToDownload = removeDuplicates(songsToDownload)
        urlsToDownload = getUrlsFromYT(songsToDownload)

        pathDwld = input('\tPlease provide a path:\n\t\t')
        while pathDwld is None: pathDwld = input('\tPlease provide a path:\n\t\t') #c:\users\max.harrison\source\py\Spotify_Downloader\dwld
        pathDwld = pathDwld.rstrip()

        downloadVidsFrom_ThenConvert(urlsToDownload, songsToDownload, pathDwld)

        print(f'\n\n\tDone! Find your songs in \'{pathDwld}\'\n\n')

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': 
    main()
    getwche()

#________________________________________________________________________________________________________________________________
