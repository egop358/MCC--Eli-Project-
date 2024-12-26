# name=MPK Mini 3


# supportedDevices=MPK Mini 3


# IMPORT LIBRARIES
import transport
import midi


# SET VARIABLES
Transport_STOP = 21


def OnMidiMsg(event):
    
    event.handled = False

    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data2 > 0:

         # STOP BUTTON (If playing, Stop. If Stopped, RESET)
            if event.data1 == Transport_STOP:
                if transport.isPlaying() == 0: 
                    print('Stop: RESET')
                elif transport.isPlaying() == 1: 
                    print('Stop')
                transport.stop()
                event.handled = True