from pydub import AudioSegment
from pydub.playback import play
'''
1. Loudness
from pydub import AudioSegment
sound1 = AudioSegment.from_file("sound1.wav")

# make sound1 louder by 3.5 dB
louder_via_method = sound1.apply_gain(+3.5)
louder_via_operator = sound1 + 3.5

# make sound1 quieter by 5.7 dB
quieter_via_method = sound1.apply_gain(-5.7)
quieter_via_operator = sound1 - 5.7
'''
class Mixer:
    def mergeFiles(self):
        clap = AudioSegment.from_wav("sounds/clap.wav")
        # play(song)

        fill = AudioSegment.from_wav("sounds/fill.wav")

        impact = AudioSegment.from_wav("sounds/impact.wav")

        # with_style = fill.append(clap, crossfade=100)
        #
        # three_concat = with_style.append(impact, crossfade=2000)

        #play(clap + fill + impact)
        awesome = clap + fill + impact
        file_path = "./mashup.mp3"
        awesome.export(file_path, format="mp3", bitrate="192k")

        return file_path
        # play(three_concat)

    def mixFileSounds(self, files, instrumental):
        clap = AudioSegment.from_wav("./sounds/clap.wav")
        # # play(song)
        #
        fill = AudioSegment.from_wav("./sounds/impact.wav")

        overlay = clap.overlay(clap, position=100)
        file_path = "./output.mp3"
        file_handle = overlay.export(file_path, format="mp3")

        return file_path




