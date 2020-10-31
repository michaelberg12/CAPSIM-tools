import pandas as pd

def getPromotion(price):
    df = pd.read_csv('Data\\promotion.csv')
    id = df['cost'].sub(price).abs().idxmin()
    return df.iloc[id]['percentage']

def getSales(price, oneProduct = True):
    df = pd.read_csv('Data\\sales1p.csv')
    if not(oneProduct):
        df = pd.read_csv('Data\\sales2p.csv')
    id = df['cost'].sub(price).abs().idxmin()
    return df.iloc[id]['percentage']

def getNextProm(current, spending):
    return current - (current * 0.33) + getPromotion(spending)

def getNextSales(current, spending, oneProducts = True):
    return current - (current * 0.33) + getSales(spending, oneProduct = oneProducts)