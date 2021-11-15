# Project Progress Report
## Project Description
For my project, I will be doing something similar to MIT's missing semester for the ML in Wireless Networking class. Specifically, I will be creating a set of Wireless Networking tutorials to help students learn and engage more with the material to build and strengthen understanding. The project will use a combination of Python, Software Defined Radios (SDR), and various packages.

## Hardware Radios
Traditionally, a lot of the different parts that go into a radio were implemented in the hardware. However, with increased knowledge in the field and development of software toolkits, the SDR has come to be the dominant tool used to prototype and hack with RF signals. 

A traditional radio (like a car radio) has a Mixer, Local Oscillator, and a Filter in order correctly filter out noise and only receive your targeted frequency.
- Mixer - Accepts 2 frequencies. Outputs the addition and subtraction of these 2 frequencies.
- Local Oscillator - Creates a frequency at a specified Hz
- Filter - Only accepts frequencies within a specified range around a point. Theoretically sets dB to 0 all other frequencies outside of the range.

Once we have filtered our given frequencies, we pass it through an FM Demodulator to get sound waves, pass it through an amplifier, and then out to a loud speaker so you can hear your music. 

## Software Defined Radios (SDR)
Currently, SDRs are more popular due to the programmable nature of the technology, making it highly adaptable for a range of uses. A SDR uses a Analog-to-Digital Converter (ADC) in order to convert the radio signals to a digital signal for the computer to process. Whereas hardware do all filterin while the signal is still in analog, computers need to conver to a digital signal in order to do any work. 

Unfortunately due to the converstion time for ADC, there is a maximum allowable bits per second depending on the ADC, with price being exponential with respect to higher bits per second.

In order to decrease the frequency needed for the ADC, what we can do is insert a secondary frequency as close as possible to the first frequency to the mixer in order to get a difference of near 0 Hz. Take a look at the Quadrature Demodulator digram in order to get a feel for how it filters the RF signal to conver it to a digital component. Note that we use the imaginary plane here in order to get the negative side of the signals when it is passed through the Mixer. 

## Project Contents
For my project, I am planning on using SRPs in order to develop tutorials for the following:
1. Listen in on conversations between SRPs at a given frequency. 
   - Think transmitting a message from a known frequency and receiving it at the other end and decoding it. We will send out a packet from SRP 1 at 2.4GHz, something like "I love CS 498 ML in Networking!" on repeat with a known preamble and modulation. Then we will receive the raw packet at SRP 2 and save that as a complex-valued numpy array. A Jupyter Notebook will then be created to show how to use the Complex-valued numpy array to obtain CSI information and decode the message.
2. Obtaining CSI information by listening in
   - The second thing I want to do is use SRP to obtain channels for different frequencies. We can have devices broadcasting, say a computer and a phone (on cellular), and see the packets they are sending and obtain channel information relative to the SRP as the preamble is known. I will focus first on WiFi as it is more ubiquitous and easier to test indoors. We will save the complex-valued raw data into a variety of Numpy arrays in order to use it later. Furthermore, if there is time, I may look into a live-version that allows it to stream the data and decode using a script of some sort.
3. (optional) Research Projects:
   - Drone Localization: If there is additional time, I want to work on a proof of concept for my gradient-based AoA localization and drone swarm tracking to see if there is any possible benefit. This will use ESP32/ESP8266 and a SRP for debugging in order to figure out how heavily the broadcast transmissions are affected by multipath as well. A prototype will start with around 6-8 ESPs broadcasting on a known frequency and 1-2 ESPs some distance away that will try and chart a vector (AoA) corresponding to the "average" of the swarm. One possible research question to look into would be a formula corresponding to how far away a single drone must be from (the middle of) the swarm in order to be able to average out the signal to a single pont (think vanishing point). 
     - A secondary research question looks to utilize the closeness of the drones in the swarm in order for them not to crash with each other. This should be somewhat iterative based where it looks at AoA and is able to discern if it is too close or not.
     - A tertiary research questions is in regards to the potentialy for mesh communication during the broadcast, or for the broadcast to be somewhat meaningful and not just random noise.
   - Satellite Tracking: See if I can help set up and come up with ideas for passive satellite tracking

## References:
- [How does Software Defined Radio (SDR) work under teh Hood? SDR Tutorial](https://www.youtube.com/watch?v=xQVm-YTKR9s&t=1072s&ab_channel=AndreasSpiess) - by Andreas Spiess

## Additional Notes:

Taken from Youtube: 


Just some information that may be helpful for beginners:

0.) Programs like GNU Radio allow the use of sound-cards to learn the basics of software defined radio. Build simple digital transmitters and receivers that use the microphone and speakers instead of a SDR.

1.) There is not much difference between the blue/plastic and the silver/metal rtl-sdr. The bandwidth and the software is the same, both are useful up to 2.2 MSps but can be pushed up to 3 MSps (no difference here). The difference is, that the metal one has a much better connector, SMA instead of MCX. The blue plastic one also has a really cheap crystal oscillator, it wanders around whenever the temperature changes. The silver/metal version has a temperature compensated oscillator, it measures the temperature and uses this to correct its drift, so it is much more stable. The drift normally is a few parts per million (it it is 10ppm, this would be 10 Hz at 1 MHz, but already 1000 Hz if you receive something on 100 MHz or 10 kHz if you are interested in 1000 MHz signals).The TCXO has only 0.5 ppm drift and the cheap crystal up to 20ppm.

2.) The most important things are antennas and short good coaxial cables. They decide about the signal quality. The cheapest RTL-SDR with a good antenna (and band-filters, see #3) is better than a 10000€ SDR with a crappy antenna. Beginners should go for the cheapest SDR and use the saved money for the antenna. With RTL-SDRs it is cheaper to use a long USB cable and get the SDR close to the antenna and away from the PC (which may create interfering emissions) than a good coax.

An old satellite dish with LNB, a bias-t (basically a box with two coaxial connectors, a coil and a capacitor) and a power supply that can deliver 14V (a bunch of batteries) are enough to receive that satellite shown in the video. More information and WebSDR: https://eshail.batc.org.uk/nb/ https://amsat-dl.org/p4-a-nb-transponder-bandplan-and-operating-guidelines/

3.) Almost all SDR have wide open inputs. All signals received together (in case of the HackRF everything between 1 and 6000 MHz) must not exceed the maximum allowable signal strength. It's a common source of problems for beginners. They get interested in weak signals from far away and enable the AGC (automatic gain control) to get a nice strong signal but the signal strength (including the noise floor) jumps up and down because the AGC constantly increases and decreases the gain. Then they switch the AGC off and manually set the gain to some value, but then some mystery signals appear, signals that aren't there. That is what happens if the sum of the received signals exceed the maximum allowable signal strength, which turns amplifiers and ADCs into mixers that mix different received signals and produce these mystery signals.

Fortunately there is a solution to this: Filters. If the offending signals are local FM broadcast stations, there are band-stop filters for 88-108 MHz that eliminate this problem (but Airplanes, DAB, DVB-T and cellphones may still interfere and would require separate band stop filters). If your frequency of interest is clearly defined, use a band-filter that discards everything except the interesting band. And even better is a pre-selector, that is a device full of band-filters and some switches to select them depending on your needs. And the luxury variant is something like this: https://www.crowdsupply.com/lime-micro/limerfe It is a pre-selector that is controllable by software. ;-)

Do it yourself band-stop filters however can be extremely cheap. The cheapest is the quarter wave stub. If you have only one interfering FM station at 100 MHz, which is a wavelength of 3 meters, add a 75cm (1/4 of 3 meters) piece of coax to the antenna cable. The waves will travel to the open end, get reflected and come back 180° out of phase. They will destructively interfere with the offending signal and thereby stopping it from reaching the SDR. The waves travel only 2/3 the speed of light in coax, so the 75cm will be way too long (the final length will be around 50cm). To tune such a stub, you can connect a noise source instead of the antenna and look at the dip in the noise. If the frequency of the dip will be too low, cut a bit of coax off and see how that dip rises in frequency. If it gets too high you have cut off too much (just push some copper wire into the open end of the coax).

4.) Almost all SDR have wide open outputs! The produced signal may contain spurious emissions and harmonics. If a signal is produced, say at 145 MHz, you need at least a low-pass filter above your frequency but below twice that frequency (i.e. 200 MHz) to get rid of all harmonics. Then look at the signal with a spectrum analyzer (i.e. another SDR)! If you have tuned your SDR to 145 MHz (center frequency), modulated some NFM (narrow frequency modulation) signal at +500 kHz and send it to the SDR  and expect it to only transmit at 145.5 MHz, you might also see a copy of it at 144.5 MHz. This happens due to I/Q imbalance and this error can be corrected. Then you might produce a good signal and send through an amplifier, which again might add harmonics that must be filtered with another low-pass filter.