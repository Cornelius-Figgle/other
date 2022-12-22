import os
import sys
from contextlib import contextmanager
from io import BytesIO
from subprocess import DEVNULL, run

from moviepy.editor import VideoFileClip
from pytube import YouTube

os.system('')

urlsToDownload = ['https://www.youtube.com/watch?v=mAwQX9mwNuw', 'https://www.youtube.com/watch?v=qVwckL8Q3_Y']
songsToDownload = ['Nice To Meet Me (feat. Au/Ra) by Rxseboy', 'Alleyways by The Neighbourhood']
#Rxseboy - Nice To Meet Me (Lyric Video) ft. Au_Ra [mAwQX9mwNuw].mp4
#Nice To Meet Me (feat. Au_Ra) by Rxseboy.mp3

illegalChars = ['/', '/', ':', '*', '?', '"', '<', '>', '|', '¦']

@contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = BytesIO()
    yield
    sys.stdout = save_stdout

def downloadVidsFrom_(urlsToDownload, songsToDownload):
    pathDwld = input("\tPlease provide a path (can be relative to launched location):\n\t\t")
    while pathDwld is None: pathDwld = input("\tPlease provide a path (can be relative to launched location):\n\t\t") #\source\py\Spotify_Downloader\dwld 
    pathDwld = pathDwld.rstrip()

    print(f"\n\n\tDownloading videos to '{pathDwld}'...\n")
    UP = "\x1B[3A"
    CLR = "\x1B[0K"
    print("\n\n")
    startPathSize = sum(len(files) for _, _, files in os.walk(pathDwld))

    for trackURL in urlsToDownload:
        trackName = songsToDownload[urlsToDownload.index(trackURL)]
        trackName = trackName.replace("+", " ")
        
        pathSize = sum(len(files) for _, _, files in os.walk(pathDwld))
        pathSize -= startPathSize

        vidsLeftToDownload = len(urlsToDownload) - pathSize
        prog = "#"*pathSize
        prog += "-"*vidsLeftToDownload
        print(f"{UP}\t{prog}{CLR}\n\t{trackName}{CLR}\n")

        run(['yt-dlp', '-P', 'dwld', '--no-playlist', trackURL], stdout=DEVNULL, stderr=DEVNULL)

        with nostdout():
            yt = YouTube(trackURL)
            video_title = yt.title
            video_id = str(yt)[-12:-1]

            for char in video_title:
                if char in illegalChars:
                    video_title = video_title.replace(char, '_')
            video_title_path = os.path.join(pathDwld, video_title + ' [' + video_id + '].mp4')
            video = VideoFileClip(video_title_path)

            for char in trackName:
                if char in illegalChars:
                    trackName = trackName.replace(char, '_')
            trackName = trackName + '.mp3'
            completeName = os.path.join(pathDwld, trackName)
            file = open(completeName, "wb")
            file.close()

            video.audio.write_audiofile(completeName)
    pathSize = sum(len(files) for _, _, files in os.walk(pathDwld))
    prog = "#"*pathSize
    print(f"{UP}\t{prog}{CLR}\n\t{trackName}{CLR}\n")
    #sleep(1000)
    return pathDwld

downloadVidsFrom_(urlsToDownload, songsToDownload)