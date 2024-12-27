# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi


# SET VARIABLES
Transport_BACK = 17


def OnMidiMsg(event):
	
	event.handled = False

	if event.midiId == midi.MIDI_CONTROLCHANGE:
		if event.data2 > 0:

			# BACK 1 BAR [<<]
			if event.data1 == Transport_BACK:
				print('1 BAR LEFT')
				transport.globalTransport(midi.FPT_Jog, -1, 2, 8)
				event.handled = True