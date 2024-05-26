from fasterwhis import *
from videosegment import *

if __name__=='__main__':
    video_path='video\\2. 深度学习立体匹配初接触.mp4'
    sound_path='sound\\2.深度学习立体匹配初接触.mp3'
    #extract_audio_from_video(video_path,sound_path)
    print(text_generation(sound_path))