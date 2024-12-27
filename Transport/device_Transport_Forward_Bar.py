# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi


# SET VARIABLES
Transport_FORWARD = 18


def OnMidiMsg(event):
	
	event.handled = False

	if event.midiId == midi.MIDI_CONTROLCHANGE:
		if event.data2 > 0:

			# FORWARD 1 BAR [>>]
			if event.data1 == Transport_FORWARD:
				print('1 BAR RIGHT')
				transport.globalTransport(midi.FPT_Jog, 1, 2, 8)
				event.handled = True