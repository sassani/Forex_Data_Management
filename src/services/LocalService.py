import os
import sys
import json
import sqlite3
import pandas as pd
import datetime

ROOT = os.getcwd()


class LocalService:
    def __init__(self):
        self.data_path = ROOT + '/data'
        self.conn = sqlite3.connect(self.data_path + '/manage.db')
        self.c = self.conn.cursor()

    def get_last_date(self, file_name: str):
        try:
            query = 'SELECT lastUpdateAt, unixTime FROM files WHERE name = "{0}"'.format(file_name)
            self.c.execute(query)
            record = self.c.fetchone()
            if record:
                return (record[0], record[1])
            else:
                return (None, None)
        except sqlite3.Error as e:
            print("An error occurred in GET LAST DATE:", e.args[0])

    def _set_last_date(self, file_name: str, last_date: int):
        try:
            query = 'UPDATE files SET lastUpdateAt = "{0}", dateTime = "{1}", unixTime = {2} WHERE name = "{3}"'.format(
                str(datetime.datetime.now()),
                str(datetime.datetime.fromtimestamp(last_date)),
                str(last_date),
                file_name
	        )
            self.c.execute(query)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("An error occurred in SET LAST DATE:", e.args[0])
            return False

    def update_csv(self, file_name: str, df: pd.DataFrame):
        try:
            with(open(self.data_path+'/'+file_name+'.csv', mode='a', newline='')) as f:
                df.to_csv(f, header=f.tell() == 0, index=None)
                if not df.empty:
                    first_unix_time = int(float(df.head(1)['date']))
                    last_unix_time = int(float(df.tail(1)['date']))
                    if (self._set_last_date(file_name, last_unix_time)):
                        log_txt = '{0}- {1}'.format(str(datetime.datetime.now()), file_name)
                        log_txt += ' | from:{0} to: {1}. count: {2}\n'.format(first_unix_time, last_unix_time, df.shape[0])
                        self._logdata(self.data_path+'/log.txt', log_txt)
                        return True
            return False
        except:
            print('An error occurred in UPDATE CSV')
            return False

    def _logdata(self,file: str, msg: str):
        try:
            with(open(file, mode='a')) as f:
                f.write(msg)
        except:
            print('LOG ERROR')
            pass

if __name__ == "__main__":
    from providers.Oanda import Oanda
    from Instrument import Instrument
    sys.path.append(ROOT)
    from src import constants as enums

    inst: Instrument = Instrument(
        enums.Providers.oanda_fxp,
        enums.ForexPairs.aud_cad,
        enums.Intervals.Mntly
    )
    ls: LocalService = LocalService()
    date, unix = ls.get_last_date(inst.file_name)
    provider = Oanda()
    print('geting %s ...' % inst.file_name)
    ohlcv, ohlcv_live = provider.get_ohlcv(inst, unix)
    print('update csv file %s ...' % inst.file_name)
    ls.update_csv(inst.file_name, ohlcv)
    # print('number of new record = ', n)
