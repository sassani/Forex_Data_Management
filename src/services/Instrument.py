from src import constants as enums
class Instrument():
    def __init__(self,
            provider: enums.Providers,
            symbol: enums.ForexPairs,
            period: enums.Intervals = enums.Intervals.min01):
        self.provider = provider
        self.symbol = symbol
        self.period = period

        self.file_name = provider.name + '_' + symbol.name + '_' + period.name
