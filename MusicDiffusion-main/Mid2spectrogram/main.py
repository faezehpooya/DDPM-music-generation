from midi2audio import FluidSynth
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
# see this page: https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html to get "FluidR3_GM.sf2"
fs = FluidSynth('FluidR3_GM.sf2')
fs.midi_to_audio('input.mid', 'output1.wav')



Fs, aud = wavfile.read('output1.wav')
# select left channel only
aud = aud[:,0]
first = aud

powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
plt.show()

