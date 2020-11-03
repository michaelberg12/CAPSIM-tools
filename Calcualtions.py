import pulp

class Calculations:

    def __init__(self, segmentSize, growth, laborCost):
        self.market = segmentSize * (1 + growth)
        self.survaySum = 0
        self.labor = laborCost
    
    def getMaterialCost(self, mtbf, baseCost):
        return baseCost + (mtbf)*0.30/1000

    def effectiveAuto(self, autoLevel, autoLevelLow):
        return autoLevel*0.5 + autoLevelLow*0.5

    def addSurvay(self, survay):
        self.survaySum = self.survaySum +  survay

    def getMarketSize(self,survay):
        return survay/self.survaySum * self.market

