# NeoPixel library dna example
# Authors: Neil and Rick
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

import argparse
import signal
import sys
def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)
                signal.signal(signal.SIGTERM, signal_handler)

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50   # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=5):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.setPixelColor(i-1,Color(0,0,0))
		strip.show()
		time.sleep(wait_ms/1000.0)

def dna(strip, dna_string, palette, wait_ms=200):
	"""DNA representation."""
	for i in range(0, len(dna_string)):		
		for j in range(0, strip.numPixels()):
			strip.setPixelColor(j, palette[dna_string[(i + j) % len(dna_string)]])
		strip.show()
		time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
	opt_parse()
        
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	
	dna_palette = {
		"G": Color(14, 180, 104),
		"A": Color(87, 29, 177),
		"T": Color(255, 230, 20),
		"C": Color(255, 83, 20)
	}
	dna_string = "TGACGTGGAGGTGCATGTTTTTTTTTTTCTAGCTAGCGGCGATAGCGCGATCGATCGATCGCGCTATTTTTTTGCGTATCGGAGCTAGCGATCGAGCTAGCGGATCTTTTTTTGAGCTAGCGATCGAGATCTAGCGATCGAGCGCGCGCTAGCGTTTTTTTATCGACGTGTGATCGATCGAGTTCGAGCTAGCTAGCTAGCTGTTTTTTTCTAGGATCTGACGTGGAGGTGCATGCTAGCTATTTTTTTGCGGCGATAGCGCGATCGATCGATCGCGCTAGCGTATCGGAGCTAGCGATCGAGCTAGCGGATCGAGCTAGCGATCGAGATCTAGCGATCGAGCGCGCGCTAGCGATCGACGTGTGATCGATCGAGTTCGAGCTAGCTAGCTAGCTGCTAG"

	print ('Press Ctrl-C to quit.')
	while True:
		print ('DNA animation.')
		dna(strip, dna_string, dna_palette, 50)
