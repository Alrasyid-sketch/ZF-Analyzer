import pandas as pd

def ema(data, period=20):
    return data.ewm(span=period, adjust=False).mean()

def sma(data, period=20):
    return data.rolling(period).mean()

def rsi(data, period=14):
    delta = data.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))
