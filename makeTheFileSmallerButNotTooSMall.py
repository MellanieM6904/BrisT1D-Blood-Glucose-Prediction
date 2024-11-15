import pandas as pd

if __name__ == "__main__":
    lineSize = 2500
    fileName = "Data/train.csv"
    newFile = "small.csv"
    data = pd.read_csv(fileName)
    copiedRows = data.iloc[350 : lineSize + 350]
    copiedRows.to_csv(newFile)
    
