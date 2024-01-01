import freqbench
import matplotlib.pyplot as plt
import matplotlib
import argparse

import argparse

# ---------- Parse Arguments ------------
parser = argparse.ArgumentParser(description='Perform signal analysis for pedals.')
parser.add_argument('--list-devices', action='store_true',
                    help='list audio devices to get the integers for the next few')
parser.add_argument('--in', type=int, nargs='?',
                    help='Input device integer.')
parser.add_argument('--out', type=int, nargs='?',
                    help='Output device integer.')
parser.add_argument('--name', type=str, nargs='?',
                    help='Name to put in graph title and filenames')

parser.add_argument('--freqresp', action='store_true',
                    help='Perform freq response for on/off of this pedal')

args = parser.parse_args()

devinput = vars(args)['in']
devoutput = vars(args)['out']
pedalname = vars(args)['name']

if pedalname is None:
    pedalname = "Unknown"

if vars(args)['list_devices']:
    print(freqbench.get_devices())

if vars(args)['freqresp']:
    freq0 = 0
    freq1 = 10_000
    time = 10
    frame_rate = 44_100
    test_signal = 0.1 * freqbench.signal.sweep(freq0, freq1, time, frame_rate)

    print("Make sure pedal is connected and in bypass mode.")
    input("Press ENTER to continue...")

    base_signal = freqbench.run(test_signal, frame_rate, devinput, devoutput)

    print("Power on the pedal.")
    input("Press ENTER to continue...")

    dut_signal = freqbench.run(test_signal, frame_rate, devinput, devoutput)

    freqs, response = freqbench.analysis.freqresp(
    base_signal, dut_signal, frame_rate)

    plt.figure(figsize=(10, 4))
    plt.tight_layout()
    plt.grid()
    plt.xscale('log')
    plt.xlim([20, freq1])
    plt.ylim([-50, 50])
    plt.ylabel('Response, dB')
    plt.xlabel('Frequency, Hz')
    plt.title(f"{pedalname} Frequency Response")
    plt.plot(freqs, response)
    plt.savefig(f"{pedalname}_freqresp.png")
    plt.show()
    



'''

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
'''