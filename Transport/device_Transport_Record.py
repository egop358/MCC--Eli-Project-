# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi


# SET VARIABLES
Transport_RECORD = 22


def OnMidiMsg(event):
	
	event.handled = False

	if event.midiId == midi.MIDI_CONTROLCHANGE:
		if event.data2 > 0:

			# RECORD BUTTON
			if event.data1 == Transport_RECORD:
				if transport.isRecording() == 0:
					print('Recording ENABLED')
				elif transport.isRecording() == 1:
					print('Recording DISABLED')
				transport.record()
				event.handled = True



			