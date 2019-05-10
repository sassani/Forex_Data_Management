import datetime
import json
import threading
import time
import winsound
from subprocess import Popen

from src import constants as enums
from src.services.DataService import DataService
from src.services.Instrument import Instrument
# from src.utilities.RepeatedTimer import RepeatedTimer

watch_list = json.load(open('watch_list.json'))
watch_list = watch_list['items']


ds: DataService = DataService()

kill_threads = False

def run(timer: int = 5, sound: bool = False):
    while True:
        time.sleep(timer)
        global kill_threads
        if kill_threads:
            print('function was terminated')
            break
        if sound:
            beep()
            for item in watch_list:
                inst: Instrument = Instrument(
                    enums.Providers[item['provider']],
                    enums.ForexPairs[item['symbol']],
                    enums.Intervals[item['interval']]
                )
                last_request_done = ds.update_instrument(inst)
        if sound:
            beep(250)


def beep(duration: int=100):
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = duration  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def start():
    global kill_threads
    kill_threads = False
    run_thread = threading.Thread(target=run, args=(1,))
    run_thread.start()

def stop():
    print('terminating function ...')
    global kill_threads
    kill_threads = True

def main():
    while True:
        command = input('command: ')
        if(command == 'start'):
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
