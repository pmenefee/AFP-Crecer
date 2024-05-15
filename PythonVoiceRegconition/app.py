from pyAudioAnalysis import audioSegmentation
import os

def speaker_diarization(audio_file):
    # Perform speaker diarization
    _, speaker_labels = audioSegmentation.speaker_diarization(audio_file, 2)

    # Print the speaker labels
    for label in speaker_labels:
        print("Speaker {}: {}s - {}s".format(label[0], label[1], label[2]))

if __name__ == "__main__":
    # Path to your audio file
    audio_file = "paul01.wav"    

    if not os.path.exists(audio_file):
        cwd = os.getcwd
        #dir_list = os.listdir(str(cwd))
        print("Audio file not found.")
        print()
    else:
        speaker_diarization(audio_file)