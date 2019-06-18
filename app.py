import sys
import datetime
import json
import threading
import time
# import winsound
from subprocess import Popen

from src import constants as enums
from src.services.dataService import DataService
from src.services.instrument import Instrument
# from src.utilities.RepeatedTimer import RepeatedTimer

from gui import main_form as Gui

watch_list = json.load(open('watch_list.json'))
watch_list = watch_list['items']




ds: DataService = DataService()

kill_threads = False



def run(speed: int, sound: bool = False):
    print('Running...')
    while True:
        time.sleep(speed)
        global kill_threads
        if kill_threads:
            print('function was terminated')
            break
        # if sound:
            # beep()
        try:
            for item in watch_list:
                inst: Instrument = Instrument(
                    enums.Providers[item['provider']],
                    enums.ForexPairs[item['symbol']],
                    enums.Intervals[item['interval']]
                )
                last_request_done = ds.update_instrument(inst)
            # if sound:
                # beep(250)
        except:
            print("Unexpected error:", sys.exc_info()[0])


# def beep(duration: int=100):
#     frequency = 2500  # Set Frequency To 2500 Hertz
#     duration = duration  # Set Duration To 1000 ms == 1 second
#     winsound.Beep(frequency, duration)

def start(speed: int=5):
    print('Starting with {0} second intervals'.format(speed))
    global kill_threads
    kill_threads = False
    run_thread = threading.Thread(target=run, args=(speed,))
    run_thread.start()

def stop():
    print('terminating function ...')
    global kill_threads
    kill_threads = True

def main():
    while True:
        txt: str = input('command: ')
        txt = txt.split()
        command = txt[0]
        if(command == 'start'):
            if len(txt)==2:
                start(int(txt[1]))
            else:
                start()
        elif command == 'stop':
            stop()
            time.sleep(2)
        elif command == 'exit':
            stop()
            time.sleep(2)
            break

main_thread = threading.Thread(target=main)

main_thread.start()
