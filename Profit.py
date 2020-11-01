
class Profit:

    _SEGMENT = {'Trad':0, 'Low':1, 'High':2, 'Perf':3, 'Size':4}


    def __init__(self, segmentSize, growth):
        self.segmentSize = segmentSize * (1 + growth)
        self.survaySum = 0
    
    def 