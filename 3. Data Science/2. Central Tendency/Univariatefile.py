import pandas as pd
import numpy as np

class Univar:
    
    def quanQual(dataset):
        quan = []
        qual = []
        for columnName in dataset.columns:
            if dataset[columnName].dtype == 'O': 
                qual.append(columnName)
            else: 
                quan.append(columnName)
        return quan, qual
    
   
    def calculate_descriptive_statistics(dataset, columns):
        descriptive = pd.DataFrame(index=["Mean", "Median", "Mode"], columns=columns)
        for column in columns:
            descriptive[column]["Mean"] = dataset[column].mean()
            descriptive[column]["Median"] = dataset[column].median()
            descriptive[column]["Mode"] = dataset[column].mode()[0]  
        return descriptive

    def create_descriptive(dataset, columns):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%"],columns=columns)
        for columnName in columns:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]

        return descriptive