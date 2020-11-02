import numpy as np
from sklearn.linear_model import LinearRegression

import dataGathering as dg
import marketing as mk
from model import Model
import pandas as pd
from constants import Constants as con
from Calcualtions import Calculations
import pulp

round = 1
age = 1.1
size = 10
pfmn = 10

tradModel = Model(round, 'Trad')
tradCalc = Calculations(105000, 0.51, 6.52)

diffIdeal = con.diffIdeal(round, 'Trad', size, pfmn)

MTBF = LpVariable("mtbf", con.mtbf('Trad'), con.mtbf('Trad') + 5000)
promotion = LpVariable("promo", 0, 3229)
sales = LpVariable("sales", 0, 4642)
price = LpVariable("price", con.price(round, 'Trad'), con.price(round, 'Trad') + 10.00)

proft = price * 




