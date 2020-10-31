class Model:

    _CONSTANT = [4.624179, 23.20088, -1.906446, -6.159904, 18.77025]

    _IDEAL = []

    _AGE = []

    _MTBF = []

    _ACC = []

    _AWAR = []

    _PRICE = []

    _ROOTMSE = []

    _SEGMENT = {'Trad':0, 'Low':1, 'High':2, 'Perf':3, 'Size':4}

    def __init__(self, constant, round, segment):
        self.constant = constant
        self.round = round
        self.segment = segment

    def results(age, price, awar, acc, pfmn, size, mtbf):
