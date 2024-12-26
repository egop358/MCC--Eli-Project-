# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi


# SET VARIABLES
Transport_START = 20


def OnMidiMsg(event):
	
	event.handled = False

	if event.midiId == midi.MIDI_CONTROLCHANGE:
		if event.data2 > 0:

			# Play / Pause (If playing, Pause.. else Play)
			if event.data1 == Transport_START:
				if transport.isPlaying() == 0: print('Play')
				elif transport.isPlaying() == 1: print('Pause')
				transport.start()
				event.handled = True