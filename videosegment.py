from pydub import AudioSegment


def extract_audio_from_video(input_video_path, output_audio_path):
    # 读取视频文件
    video = AudioSegment.from_file(input_video_path, "mp4")
    # 导出音频为mp3格式
    video.export(output_audio_path, format="mp3")

