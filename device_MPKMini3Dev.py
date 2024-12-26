# name=MPK Mini 3

# supportedDevices=MPK Mini 3

# WELCOME MESSAGE
def OnInit():
	print('')
	print('-----------------------------------------')
	print('')
	print('AKAI MPK MINI MK3 MIDI Script by Eli Mercado')
	print('')
	print('V1')
	print('')
	print('IF YOU PAID FOR THIS YOU GOT RIPPED OFF')
	print('')
	print('-----------------------------------------')
	print('')

# IMPORT LIBRARIES
import transport
import ui
import midi
import plugins
import channels

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



			# STOP BUTTON (If playing, Stop. If Stopped, RESET)
			elif event.data1 == Transport_STOP:
				if transport.isPlaying() == 0: print('Stop: RESET')
				elif transport.isPlaying() == 1: print('Stop')
				transport.stop()
				event.handled = True



			# RECORD BUTTON
			elif event.data1 == Transport_RECORD:
				if transport.isRecording() == 0: print('Recording ENABLED')
				elif transport.isRecording() == 1: print('Recording DISABLED')
				transport.record()
				event.handled = True



			# LOOP BUTTON (Song / Pattern Mode)
			elif event.data1 == Transport_Loop:
				if transport.getLoopMode() == 0: print('SONG MODE')
				elif transport.getLoopMode() == 1: print('PATTERN MODE')
				transport.setLoopMode()
				event.handled = True	



			# BACK 1 BAR [<<]
			elif event.data1 == Transport_BACK:
				print('1 BAR LEFT')
				transport.globalTransport(midi.FPT_Jog, -1, 2, 8)
				event.handled = True



			# FORWARD 1 BAR [>>]
			elif event.data1 == Transport_FORWARD:
				print('1 BAR RIGHT')
				transport.globalTransport(midi.FPT_Jog, 1, 2, 8)
				event.handled = True


			# Select channel (1)
			elif event.data1 == Channels_setchannel:
				print('Channel set')
				channels