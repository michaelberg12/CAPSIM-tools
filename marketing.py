import pandas as pd
import pulp
import math

def getPromotion(price):
    return 5E-18*price**5 - 4E-14*price**4 + 1E-10*price**3 - 2E-07*price**2 + 0.0003*price - 0.0053

def getSales(price):
    return 8E-18*price**5 - 6E-14*price**4 + 1E-10*price**3 - 7E-08*price**2 + 7E-05*price - 0.0028

def getNextProm(current, spending):
    return current - (current * 0.33) + getPromotion(spending)

def getNextSales(current, spending, oneProducts = True):
    return current - (current * 0.33) + getSales(spending, oneProduct = oneProducts)