import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

def SMA(df, column="close", period=20):

    # sma = df[column].rolling(window=period).mean()
    return df[column].rolling(window=period).mean()
    # return df.join(sma.to_frame('SMA{0}'.format(str(period))))



def EMA(df, column="close", period=20):

    # ema = df[column].ewm(span=period).mean()
    return df[column].ewm(span=period).mean()
    # return df.join(ema.to_frame('EMA{0}'.format(str(period))))



def RSI(df, column="close", period=14):
    # wilder's RSI
 
    delta = df[column].diff()
    up, down = delta.copy(), delta.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    rUp = up.ewm(com=period - 1,  adjust=False).mean()
    rDown = down.ewm(com=period - 1, adjust=False).mean().abs()

    # rsi = 100 - 100 / (1 + rUp / rDown)    

    return 100 - 100 / (1 + rUp / rDown)    
    # return df.join(rsi.to_frame('RSI{0}'.format(str(period))))



def BollingerBand(df, column="close", period=20):

    sma = df[column].rolling(window=period).mean()
    std = df[column].rolling(window=period).std()

    upper = (sma + (std * 2)).to_frame('BBANDUP{0}'.format(str(period)))
    lower = (sma - (std * 2)).to_frame('BBANDLO{0}'.format(str(period)))
    return df.join(upper).join(lower)

def Extremum(df, column='close', period=21):
    '''Return extremum points of column in the middle of the period'''
    _df = df.copy()
    ilocs_min = argrelextrema(_df[column].values, np.less_equal, order=period)[0]
    ilocs_max = argrelextrema(_df[column].values, np.greater_equal, order=period)[0]

    _df['MAX'] = 0
    _df['MIN'] = 0
    _df['MID'] = 1
    _df.loc[_df.iloc[ilocs_min].index, 'MAX'] = 1
    _df.loc[_df.iloc[ilocs_max].index, 'MIN'] = 1
    _df.loc[_df.iloc[ilocs_min].index, 'MID'] = 0
    _df.loc[_df.iloc[ilocs_max].index, 'MID'] = 0
    
    return _df[['MAX', 'MIN', 'MID']]