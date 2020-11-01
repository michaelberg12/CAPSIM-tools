from PIL import Image
import pandas as pd
from statistics import mean
import numpy as np


def extractGraph(file_path, box):
    im = Image.open(file_path)

    im = im.crop(box)
    px = im.load()

    width, height = im.size
    for x in range(width):
        for y in range(height):
            if not(px[x,y][0] >= 200 and px[x,y][1] <= 200 and px[x,y][2] <= 200):
                px[x,y] = (255,255,255)
            else:
                 px[x,y] = (0,0,0)


    cost = [] #x
    percentage = [] #y

    for x in range(width):
        curAvg = []
        for y in range(height):
            if (px[x,y] == (0,0,0)):
                curAvg.append(y)
        if(curAvg != []):
            percentage.append(mean(curAvg))
            cost.append(x)

    df = pd.DataFrame(columns=['cost', 'percentage'])
    df['cost'] = cost
    df['percentage'] = percentage
    return df

def formatData(maxCost, maxPercent, df):
    df['cost'] = ((df['cost'] - df['cost'].min())/ (df['cost'].max() - df['cost'].min()))*maxCost
    df['percentage'] = maxPercent - (((df['percentage'] - df['percentage'].min())/(df['percentage'].max() - df['percentage'].min()))*maxPercent)
    return df
    
def generateChartData():
    imagePath = 'Photos\\figure_4_2.png'
    box = (51,37,384,248)
    df = extractGraph(imagePath, box)
    df = formatData(3229, 0.5, df)
    df.to_csv('Data\\promotion.csv')
    print(df)

    imagePath = 'Photos\\sales-1p.png'
    box = (52,98,571,247)
    df = extractGraph(imagePath, box)
    df = formatData(4642, 0.3529, df)
    df.to_csv('Data\\sales1p.csv')
    print(df)

    imagePath = 'Photos\\sales-2p.png'
    box = (52,98,571,247)
    df = extractGraph(imagePath, box)
    df = formatData(4642, 0.3529, df)
    df.to_csv('Data\\sales2p.csv')
    print(df)

def readInSimData():
    return pd.read_csv(r'D:\documents\Capsim Data\CleanedData.csv')