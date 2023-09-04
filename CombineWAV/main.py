import glob
from os.path import join, basename, dirname, split
import librosa
import numpy as np
import soundfile as sf


data_dir = './data/sample'
outfile = 'result.wav'

wav_files = glob.glob(join(data_dir, '*.wav'))
audio_dst = np.zeros(1)
# print(wav_files)
wav_files.sort()
for file in wav_files:
    print(file)
    a, sample_rate = librosa.load(file)
    audio_dst = np.hstack((audio_dst, a))

sf.write(outfile, audio_dst, sample_rate)


