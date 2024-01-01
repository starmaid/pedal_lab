# pedal_lab

Set of tools for quantifying guitar pedal characteristics. Can be used for generic audio stuff too.

The frequency response library `freqbench` is included from [kuramohler's repository kurtamohler@gmail.com](https://github.com/kurtamohler/freqbench). I don't want to use conda so I'm using it venv style. I also might want to modify it so thats why I have my own copy.

## Reference

https://realpython.com/python-scipy-fft/

https://librosa.org/doc/latest/core.html#spectral-representations

https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft

https://github.com/kurtamohler/freqbench

https://matplotlib.org/stable/users/explain/animations/animations.html


## Goals

For a pedal/setting, I want to generate:

- Frequency response plot
- Animated fourier plot response to a set of pure input signals
- Animated fourier plot response to a set of guitar input signals

## Setup

```
py -m venv <name>

.\venv\Scripts\Activate.*

pip install -r requirements.txt

deactivate
```


