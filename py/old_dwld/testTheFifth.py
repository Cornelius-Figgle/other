from moviepy.editor import *


mp4_file = [r'D:\__temp__\slime.mp4', r'D:\__temp__\slimeTwo.mp4', r'D:\__temp__\slimeThree.mp4']
mp3_file = [r'D:\__temp__\slime.mp3', r'D:\__temp__\slimeTwo.mp3', r'D:\__temp__\slimeThree.mp3']
 
for file in mp4_file:
    videoclip = VideoFileClip(file)
    
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file[mp4_file.index(file)])
    
    audioclip.close()
    videoclip.close()