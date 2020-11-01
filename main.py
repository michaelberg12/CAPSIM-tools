import dataGathering as dg
import marketing as mk
from model import Model
import pandas as pd

df = dg.readInSimData()

x = df[['Material', 'Size', 'MTBFABS']]

print(x)