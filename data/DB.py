import os
import sys
import json
import sqlite3
import pandas as pd
import numpy as np
ROOT = os.getcwd()
sys.path.append(ROOT)
from src import constants as enums


class DB():
    def __init__(self, root_path):
        self.data_path = root_path + '/data'
        self.conn = sqlite3.connect(self.data_path + '/manage.db')
        self.c = self.conn.cursor()

    def _clean_db(self):
        query = 'DELETE FROM files'
        self.c.execute(query)
        self.conn.commit()

    def initialize(self, provider: enums.Providers):
        self._clean_db()
        for symbol in enums.ForexPairs:
            for interval in enums.Intervals:
                # print(provider.name+'_'+symbol.name+'_'+interval.name)
                value = provider.name + '_' + symbol.name + '_' + interval.name
                query = 'INSERT INTO files (name) VALUES ("' + value + '")'
                self.c.execute(query)
        self.conn.commit()

if __name__ == '__main__':
    db: DB=DB(ROOT)
    db.initialize(enums.Providers.oanda_fxp)
