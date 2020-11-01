from constants import Constants
import math

class Model:
    _CONSTANT = [4.624179, 23.20088, -1.906446, -6.159904, 18.77025]

    _IDEAL = [-6.180388,-7.161307,-10.58551,-6.918329,-15.60442]
    
    _AGE = [-10.95321,0,0,0,-6.980425]

    _MTBF = [0.0033093,0.0029849,0.0034718,0.0042419,0.0019682]

    _ACC = [0.7575042,0.5828234,0.6449276,0.225565,0.2771687]

    _AWAR = [0,0,0,0.232305,0.1575408]

    _PRICE = [-2.498672,-4.299724,0,0,0]

    _ROOTMSE = [3.4652,2.3686,3.251,2.4371,1.0513]

    _SEGMENT = {'Trad':0, 'Low':1, 'High':2, 'Perf':3, 'Size':4}

    def __init__(self, round, segment):
        self.round = round
        self.segment = segment

    def results(self, age, price, awar, acc, pfmn, size, mtbf):
        con = Constants()

        seg = self._SEGMENT[self.segment]

        pfmn_i = con.pfmn(self.round, self.segment)
        size_i = con.size(self.round, self.segment)

        dif_ideal = math.sqrt(pow(pfmn - pfmn_i,2) + pow(size - size_i,2))
        dif_age = age - con.age(self.segment)
        dif_mtbf = mtbf - con.mtbf(self.segment)
        dif_price = price - con.price(self.round, self.segment)

        return (self._CONSTANT[seg] + self._IDEAL[seg] * dif_ideal + self._AGE[seg] * dif_age + self._MTBF[seg] * dif_mtbf + self._ACC[seg] * (100 * acc) + self._AWAR[seg] * (100 * awar) + self._PRICE[seg] * dif_price)

