import pandas as pd

if __name__ == "__main__":
    lineSize = 500
    fileName = "Data/train.csv"
    newFile = "small.csv"
    data = pd.read_csv(fileName)
    copiedRows = data.iloc[0:lineSize]
    copiedRows.to_csv(newFile, index=False)
    
