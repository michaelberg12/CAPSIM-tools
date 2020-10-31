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

    def __init__(self, constant, round, segment):
        self.constant = constant
        self.round = round
        self.segment = segment

    def results(age, price, awar, acc, pfmn, size, mtbf):
