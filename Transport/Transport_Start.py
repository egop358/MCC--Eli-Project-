# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi
import plugins


# SET VARIABLES
Transport_START = 20
Transport_STOP = 21
Transport_RECORD = 22
Transport_Loop = 16
Transport_BACK = 17
Transport_FORWARD = 18
Channels_setchannel = 28


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