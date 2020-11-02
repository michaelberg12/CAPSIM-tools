class Calculations:

    def __init__(self, segmentSize, growth, laborCost):
        self.segmentSize = segmentSize * (1 + growth)
        self.survaySum = 0
        self.labor = laborCost
        self.market = laborCost
    
    def getMaterialCost(mtbf, baseCost):
        return baseCost + (mtbf/1000)*0.30

    def effectiveAuto(self, autoLevel, autoLevelLow):
        return autoLevel*0.5 + autoLevelLow*0.5

    def addSurvay(self, survay):
        self.survaySum = self.survaySum +  survay

    def setMarket(self, size, growth):
        self.market = size * (1+growth)

    def getMarketSize(self,survay):
        return survay/self.survaySum * self.market

