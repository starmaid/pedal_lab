import freqbench
import matplotlib.pyplot as plt
import matplotlib


freqbench.get_devices()

freq0 = 0
freq1 = 8_000
time = 10
frame_rate = 44_100
input_signal = 0.1 * freqbench.signal.sweep(freq0, freq1, time, frame_rate)

#freqbench.play_signal(input_signal, 12, 44_100)

test_signal = input_signal

input_device = 5
output_device = 8

base_signal = freqbench.run(test_signal, frame_rate, input_device, output_device)

dut_signal = freqbench.run(test_signal, frame_rate, input_device, output_device)

freqbench.save(base_signal, frame_rate, 'base_signal.wav')
freqbench.save(dut_signal, frame_rate, 'dut_signal.wav')

# input: 6
# output: 11

base_signal, fr0 = freqbench.load('base_signal.wav')
dut_signal, fr1 = freqbench.load('dut_signal.wav')
assert fr0 == fr1
frame_rate = fr0



freqs, response = freqbench.analysis.freqresp(
    base_signal, dut_signal, frame_rate)

plt.figure(figsize=(10, 4))
plt.xscale('log')
plt.xlim([20, 20_000])
plt.ylim([-50, 50])
plt.ylabel('Response, dB')
plt.xlabel('Frequency, Hz')
plt.plot(freqs, response)
plt.show()