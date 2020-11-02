import math

class Constants:
    _PFMN = [5,1.7,8.9,9.4,4]
    _SIZE = [15,18.3,11.1,16,10.6]

    _PFMN_D = [0.7,0.5,0.9,1,0.7]
    _SIZE_D = [-0.7,-0.5,-0.9,-0.7,-1]

    _AGE = [2.0,7.0,0.0,1.0,1.5]

    _MTBF = [14000,12000,20000,22000,16000]

    _PRICE = [20.00,15.00,30.00,25.00,25.00]

    _SEGMENT = {'Trad':0, 'Low':1, 'High':2, 'Perf':3, 'Size':4}

    def pfmn(self, round, segment):
        seg = self._SEGMENT[segment]
        return self._PFMN[seg] + round*self._PFMN_D[seg]

    def size(self, round, segment):
        seg = self._SEGMENT[segment]
        return self._SIZE[seg] + round*self._SIZE_D[seg]

    def difIdeal(round, segment, size, pfmn):
       math.sqrt(math.pow(self.size(round, segment) - size,2) + math.pow(self.pfmn(round, segment) - pfmn,2))

    def age(self, segment):
        seg = self._SEGMENT[segment]
        return self._AGE[seg]

    def mtbf(self, segment):
        seg = self._SEGMENT[segment]
        return self._MTBF[seg]

    def price(self, round, segment):
        seg = self._SEGMENT[segment]
        return self._PRICE[seg] - round*0.5

