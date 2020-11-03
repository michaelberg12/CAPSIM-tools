import numpy as np
from sklearn.linear_model import LinearRegression

import dataGathering as dg
import marketing as mk
from model import Model
import pandas as pd
from constants import Constants
from Calcualtions import Calculations
from pulp import *

round = 1
age = 1.1
size = 10
pfmn = 10
awar = 0.45
salesCurrent = 0.45
materialBase = 6.52

tradModel = Model(round, 'Trad')
tradCalc = Calculations(105000, 0.51, 6.52)
tradCalc.addSurvay(196)

con = Constants()

MTBF = LpVariable("mtbf", con.mtbf('Trad'), con.mtbf('Trad') + 5000)
promotion = LpVariable("promo", 0, 3229)
sales = LpVariable("sales", 0, 4642)
price = LpVariable("price", con.price(round, 'Trad'), con.price(round, 'Trad') + 10.00)

profit = LpProblem("myProblem", LpMaximize)
profit = ((price - tradCalc.getMaterialCost(MTBF, materialBase) - tradCalc.labor) * tradCalc.getMarketSize(tradModel.results(age,price, awar, mk.getNextSales(salesCurrent, sales), pfmn, size, MTBF)) - sales)

status = profit.solve()
print(status)



