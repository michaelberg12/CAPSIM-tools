import dataGathering as dg
import marketing as mk
from model import Model

dg.generateChartData()


print(mk.getNextProm(0.8, 1500))

hello = Model(4, 'Trad')
print(hello.results(1.1, 24.68, 0.78, 0.65, 6.2, 14.1, 19000))