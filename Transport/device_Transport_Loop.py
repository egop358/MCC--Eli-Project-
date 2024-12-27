# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi


# SET VARIABLES
Transport_Loop = 16


def OnMidiMsg(event):
	
	event.handled = False

	if event.midiId == midi.MIDI_CONTROLCHANGE:
		if event.data2 > 0:

			# LOOP BUTTON (Song / Pattern Mode)
			if event.data1 == Transport_Loop:
				if transport.getLoopMode() == 0: print('SONG MODE')
				elif transport.getLoopMode() == 1: print('PATTERN MODE')
				transport.setLoopMode()
				event.handled = True	