import numpy as np
from sklearn.linear_model import LinearRegression

import dataGathering as dg
import marketing as mk
from model import Model
import pandas as pd
from constants import Constants as con
import pulp


MTBFM = LpVariable("mtbf", con.mtbf('Trad'), con.mtbf('Trad') + 5000)

