from subprocess import run
from moviepy.editor import VideoFileClip
import os

pathDwld = 'c:/users/max.harrison/source/py/Spotify_Downloader/dwld'
urlsToDownload = ['https://www.youtube.com/watch?v=mAwQX9mwNuw', 'https://www.youtube.com/watch?v=qVwckL8Q3_Y']
songsToDownload = ['Nice To Meet Me (feat. Au/Ra) by Rxseboy', 'Alleyways by The Neighbourhood']
#Rxseboy - Nice To Meet Me (Lyric Video) ft. Au_Ra [mAwQX9mwNuw].mp4
#Nice To Meet Me (feat. Au/Ra) by Rxseboy.mp3

illegalChars = ['/', '/', ':', '*', '?', '"', '<', '>', '|', '¦']

for trackURL in urlsToDownload:
    trackName = songsToDownload[urlsToDownload.index(trackURL)]
    run(['yt-dlp', '-P', 'dwld', '--no-playlist', trackURL])
    from yt_dlp import YoutubeDL
    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(trackURL, download=False)
        video_id = info_dict.get('id', None)
        video_title = info_dict.get('title', None)
        
    for char in video_title:
        if char in illegalChars:
            video_title.replace(char, '_')
    video_title_path = os.path.join(pathDwld, video_title + ' [' + video_id + '].mp4')
    video = VideoFileClip(video_title_path)

    for char in trackName:
        if char in illegalChars:
            trackName.replace(char, '_')
    trackName = trackName + '.mp3'
    completeName = os.path.join(pathDwld, trackName)
    file = open(completeName, "wb")
    file.close()

    video.audio.write_audiofile(completeName)