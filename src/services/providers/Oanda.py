import os
import sys
import json
import requests as req
import pandas as pd
import numpy as np

ROOT = os.getcwd()
sys.path.append(ROOT)

from src.services.Instrument import Instrument

INTERVALS_MAP = {
	'sec05': 'S5',
	'sec10': 'S10',
	'sec15': 'S15',
	'sec30': 'S30',
	'min01': 'M1',
	'min02': 'M2',
	'min04': 'M4',
	'min05': 'M5',
	'min10': 'M10',
	'min15': 'M15',
	'min30': 'M30',
	'min60': 'H1',
	'hour1': 'H2',
	'hour2': 'H3',
	'hour3': 'H4',
	'hour4': 'H6',
	'hour6': 'H8',
	'hour8': 'H12',
	'daily': 'D',
	'wekly': 'W',
	'mntly': 'M'
}

SYMBOLE_MAP = {
    'aud_cad': "AUD_CAD",
    'aud_chf': "AUD_CHF",
    'aud_jpy': "AUD_JPY",
    'aud_nzd': "AUD_NZD",
    'aud_usd': "AUD_USD",
    'cad_chf': "CAD_CHF",
    'cad_jpy': "CAD_JPY",
    'chf_jpy': "CHF_JPY",
    'eur_aud': "EUR_AUD",
    'eur_cad': "EUR_CAD",
    'eur_chf': "EUR_CHF",
    'eur_gbp': "EUR_GBP",
    'eur_jpy': "EUR_JPY",
    'eur_nzd': "EUR_NZD",
    'eur_usd': "EUR_USD",
    'gbp_aud': "GBP_AUD",
    'gbp_cad': "GBP_CAD",
    'gbp_chf': "GBP_CHF",
    'gbp_jpy': "GBP_JPY",
    'gbp_nzd': "GBP_NZD",
    'gbp_usd': "GBP_USD",
    'nzd_jpy': "NZD_JPY",
    'nzd_usd': "NZD_USD",
    'usd_cad': "USD_CAD",
    'usd_chf': "USD_CHF",
    'usd_jpy': "USD_JPY",
    'usd_sgd': "USD_SGD"
}

class Oanda:
    def __init__(self):
        settings = json.load(open(ROOT + '/settings.json'))
        self.base_url = settings['oanda']['baseUrl']
        self.api_key = settings['oanda']['apiKey']

    def _get_candles(self, instrument: Instrument, fromDate: int, count: int):
        symbol = SYMBOLE_MAP[instrument.symbol.name]
        period = INTERVALS_MAP[instrument.period.name]
        url = self.base_url + '/v3/instruments/' + symbol + '/candles'
        # if fromDate is None:
        #     fromDate = 1262304000 # datetime in Unix (1262304000 = 01/01/2010 @ 12:00am (UTC))
        response = req.get(
            url,
            params={
                'from': fromDate,
                'granularity': period,
                'count': count
            },
            headers={
                'Authorization': self.api_key,
                'Accept-Datetime-Format': 'UNIX',
                'Content-Type': 'application/json',
                'Host': 'api-fxpractice.oanda.com',
                'accept-encoding': 'gzip, deflate',
            }
        )
        data = response.json()
        return data['candles']

    def get_ohlcv(self, instrument: Instrument, fromDate: int = None, count: int = 5000):
        if fromDate is None:
            fromDate = 1262304000 # datetime in Unix (1262304000 = 01/01/2010 @ 12:00am (UTC))
        candles = self._get_candles(instrument, fromDate=fromDate, count=count)
        data= {}
        ohlcv_live = {}
        for candle in candles:
            index = int(float(candle['time']))
            if index > fromDate:
                if candle['complete']:
                    data[index] = [
                        # index,
                        float(candle['mid']['o']),
                        float(candle['mid']['h']),
                        float(candle['mid']['l']),
                        float(candle['mid']['c']),
                        int(float(candle['volume']))
                    ]
                else:
                    ohlcv_live = {
                        'date': index,
                        'open': float(candle['mid']['o']),
                        'high': float(candle['mid']['h']),
                        'low': float(candle['mid']['l']),
                        'close': float(candle['mid']['c']),
                        'volume': int(float(candle['volume']))
                    }
        ohlcv = pd.DataFrame.from_dict(data,
            orient='index',
            columns=['open', 'high', 'low', 'close', 'volume'])
        return (ohlcv, ohlcv_live)


if __name__ == '__main__':
    from src import constants as enums
    rs: Oanda = Oanda()
    inst = Instrument(
        enums.Providers.oanda_fxp,
        enums.ForexPairs.eur_aud,
        enums.Intervals.Mntly
    )
    print(rs.get_ohlcv(inst))
