import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

class MinMaxScale():
    def __init__(self, df:pd.DataFrame):
        self.mins = df.min()
        self.maxs = df.max()
        self.delta = self.maxs - self.mins

    def normalize(self, df: pd.DataFrame):
        return (df - self.mins)/self.delta

    def denormalize(self, df: pd.DataFrame):
        return df * self.delta + self.mins