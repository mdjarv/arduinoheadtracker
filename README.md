# Arduino Headtracker

By using an Arduino and an appropriate IMU you can for very little money build yourself an excellent headtracker similar to products such as TrackIR.

You can see a short demo video of my own build here: https://www.youtube.com/watch?v=QpO1Wty3F3I

This repo contains both the Arduino code and the FreePIE script to get your headtracker working.

## Hardware

Below is the hardware I used, you can substitute with your own parts as you see fit.

* Arduino Nano
* GY-85 9DOF IMU

I prefer the Arduino Nano due to the combination of formfactor and the USB port but any Arduino should work. I have ordered a couple of cheaper MPU-6050 IMUs to try if they work well, as that would cut the hardware cost in half, but they have not arrived so I can not yet vouch for them.

Wire up the IMU to the Nano over the I2C bus, try to orient the IMU in a way that makes sense. Preferrably the X axis should point towards your screen once the headtracker has been mounted.

When you've verified that the software works you can mount it on top of a headset or something similar.

## On the Arduino

Before you load the provided sketch you need to install the FreeIMU library for Arduino, found here: https://github.com/Fabio-Varesano-Association/freeimu

For this to work with the GY-85 IMU I had to open the `arduino\libraries\FreeIMU\FreeIMU.h` file, comment out the original version (I think it was `#define FREEIMU_v04`) and uncommend the following line:

```c++
#define FREEIMU_v03
```

The `FreeIMU_yaw_pitch_roll` sketch provided in this repo is very close to the original example from the FreeIMU library with the output changed to comma-separated values. Upload it to your Arduino and verify the output through the serial monitor. You should see a lot of values rolling by similar to this:

```
145.49,31.35,0.91
```

## On the PC

Download and install FreePIE from here: http://andersmalmgren.github.io/FreePIE/

Configure the FreeIMU plugin to the COM port of your connected Arduino headtracker, and load up the `FreeIMU Headtracking.py` script. Configure it to your liking and run it by pressing F5. If you have `DEBUG` set to true you can see both the input and output values under the Watch tab at the bottom

## Games

The games listed below have been tested with this setup and should hopefully work well.

### Assetto Corsa

I found the following settings to behave very well in this game:

```python
OUTPUT_TRACKIR = True
TRACKIR_MULTIPLIER = 10 
```

You might want a different multiplier but this felt natural for my setup with regards to size and distance to the monitor.

### ARMA 2

For some reason I have not been able to get ARMA 2 to work with TrackIR, however the following worked for me:

```python
OUTPUT_FREETRACK = True
FREETRACK_MULTIPLIER = 0.001
```

This worked nicely when flying helicopters or driving cars.