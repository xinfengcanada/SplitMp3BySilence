# -*- coding: utf-8 -*-
"""
@author:Simphen（3043292995@qq.com)
@description:
@created time: 2023.1.26 09:06
@last edited time: 2023.1.26 17:54
"""
from pathlib import Path
import os

from pydub import AudioSegment
from pydub.silence import split_on_silence


def splitaudio():
    # Split track where the silence is 1 seconds or more and get chunks using
    # the imported function.
    chunks = split_on_silence(
        # Use the loaded audio.
        song,
        # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
        min_silence_len=2 * 1000,
        # Consider a chunk silent if it's quieter than -50 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh=-50)

    for i, chunk in enumerate(chunks):
        # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
        silence_chunk = AudioSegment.silent(duration=500)
        # Add the padding chunk to beginning and end of the entire chunk.
        audio_chunk = silence_chunk + chunk + silence_chunk
        out_file = Path("{0}/chunk{1}.mp3".format(chunk_path, i))
        print("Exporting file", out_file)
        # Export the audio chunk
        chunk.export(out_file, format=extension)


path = "./"
files = os.listdir(path)
for file in files:
    file_path = Path(path + "/" + file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)
        # delete the .
        extension = extension.lstrip(".")
        if extension == 'mp3':
            chunk_path = Path(path + "/out/" + filename)
            if not os.path.isdir(chunk_path):
                os.makedirs(chunk_path)
            # Load your audio.
            song = AudioSegment.from_mp3(file)
            splitaudio()
