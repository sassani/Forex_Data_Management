import os
import sys
import json
import sqlite3
# import asyncio
import pandas as pd
import numpy as np
ROOT = os.getcwd()
sys.path.append(ROOT)
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from src import constants as enums
from src.services.providers.Oanda import Oanda
from src.services.Instrument import Instrument
from src.services.LocalService import LocalService


# DATA_PATH = ROOT + '/data/'

class DataService:
    def __init__(self):
        pass

    def update_instrument(self, instrument: Instrument):
        clear()
        print('Updating...')
        print('Updating {0}_{1}_{2}'.format(instrument.provider.name, instrument.symbol.name, instrument.period.name))
        # find relative file
        ls: LocalService = LocalService()
        unix = ls.get_last_date(instrument.file_name)
        print('Last Unix:\t{0}'.format(unix))
        provider = Oanda()
        ohlcv, ohlcv_live = provider.get_ohlcv(instrument, unix)
        # save data on disk
        ls.update_hdf(instrument.file_name, ohlcv)
        # print('from:{0} to: {1}. count: {2}'.format(f, l, n))




if __name__ == '__main__':
    instrument: Instrument = Instrument(
        enums.Providers.oanda_fxp,
        enums.ForexPairs.eur_jpy,
        enums.Intervals.Wekly
        )
    ds: DataService = DataService()
    ds.update_instrument(instrument)
