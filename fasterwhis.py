from faster_whisper import WhisperModel
from chatgpt4 import *
import os


def text_generation(sound_path):
    '''

    :param sound_path: 声音文件路径
    :return: 经由chatgpt修改的字幕字符串
    '''
    model_size = "large_v2"
    condition_on_previous_text = False
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    segments, info = model.transcribe(sound_path, beam_size=5)
    updated_segments = OpenAiResponse_text(segments)
    return updated_segments
