import os
import sys
import json
import sqlite3
import pandas as pd
import datetime

ROOT = os.getcwd()
sys.path.append(ROOT)
from src.utilities import indicators


class LabelService(object):
    def __init__(self):
        self.data_path = ROOT + '/data'
        # self.conn = sqlite3.connect(self.data_path + '/manage.db')
        # self.c = self.conn.cursor()

    def update_labels(self, file_name: str):
        data_raw = self.data_path+'/'+file_name+'.h5'
        data_labeled = self.data_path+'/labeled/'+file_name+'.h5'
        last_unix = None
        #load raw data
        try:
            with pd.HDFStore(data_raw) as raw_store:
                # print(raw_store['data'])
                df = pd.read_hdf(raw_store, key='data')
                # df = indicators.SMA(df,period=3)
                # df = indicators.SMA(df,period=5)
                # df = indicators.SMA(df,period=7)
                # df = indicators.SMA(df,period=10)
                # df = indicators.SMA(df,period=15)
                # df = indicators.RSI(df,period=3)
                # df = indicators.RSI(df,period=5)
                # df = indicators.RSI(df,period=7)
                df = indicators.RSI(df,period=10)
                df = indicators.RSI(df,period=15)
                # df = df.join(
                #     sma3.to_frame('SMA3'),
                #     sma5.to_frame('SMA5'),
                #     sma7.to_frame('SMA7'),
                #     sma10.to_frame('SMA10'),
                #     sma15.to_frame('SMA15'),
                #     )
                print(df)
        except Exception as e:
            print("An error occurred in GET LAST DATE")

        try:
            with pd.HDFStore(data_labeled) as store:
                if len(store.keys()) >0:
                    last_unix = int(float(store.select('data', start=-1).index[0]))
                
        except:
            print("An error occurred in GET LAST DATE")


if __name__ == "__main__":
    print(__name__)
    from providers.oanda import Oanda
    from instrument import Instrument
    sys.path.append(ROOT)
    from src import constants as enums

    inst: Instrument = Instrument(
        enums.Providers.oanda_fxp,
        enums.ForexPairs.eur_usd,
        enums.Intervals.min01
    )
    ls: LabelService = LabelService()
    ls.update_labels(inst.file_name)

