

def close_peak(data, windowSize=500, startpoint=0):
    '''plot close price with its peak labels'''
    '''data: pandas.DataFrame (must have 'sell', 'buy' columns)'''
    endpoint = startpoint + windowSize
    df = data.iloc[startpoint:endpoint]
    df.close.plot(figsize=(20,8), alpha=.3)
    df[df['sell']].close.plot(style='.', lw=10, color='red', marker="v")
    df[df['buy']].close.plot(style='.', lw=10, color='green', marker="^")