# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:38:20 2020

@author: Randy
"""

import pandas as pd

#Get data from the csv
def get_data_csv(csvFilePath):
    try:
        #Read in the data from the provided CSV
        dfData = pd.read_csv(csvFilePath)
    except Exception as e:
        #Placeholder for better exception handling when dealing with the file (could be a bad file, may not exist, poorly formed data, etc)
        print("Error encountered")
        print(str(e))
    
    #Return the new dataframe populated with the data from the csv
    return dfData

#Get the list of columns
def get_columns(dfData):
    #Get the list of columns
    lColumns = list(dfData.columns)
    
    #Put those columns as values in a Column field in a new dataframe
    dfColumns = pd.DataFrame(columns=['Col_Name'], data=lColumns)
    return dfColumns

#Get the type for each column
def get_col_types(dfData, dfColumns):
    dfColumns['Type'] = list(dfData.dtypes)
    
    return dfColumns

def calc_num_blanks(dfData, dfColumns):
    #Add the number of blank rows for each column as a new field in the columns dataframe
    #***Need some error processing in case the columns in the Columns dataframe don't match with the columns in the Data dataframe
    dfColumns['Num_Blank'] = list(dfData.isnull().sum())
    
    return dfColumns

def calc_num_values(dfData, dfColumns):
    #Add the number of unique values for each column in a new field in the columns dataframe
    #***Need some error processing in case the columns in the Columns dataframe don't match with the columns in the Data dataframe
    dfColumns['Num_Unique'] = list(dfData.nunique(dropna=False))
    
    return dfColumns

def calc_variability(dfData, dfColumns):
    #***Need some error processing in case the columns in the Columns dataframe don't match with the columns in the Data dataframe
    #Determine the total number of rows in each column (this will be denominator for the probability of finding each value in each column)
    num_rows = dfData.shape[0]
    
    #Convert all NaNs to blank strings
    dfData = dfData.fillna('')
    
    #Initialize the a column variability list
    lColVariability = []
    
    #Loop through each column
    for column in dfColumns['Col_Name']:
        #print("Column: "+str(column))
        
        #Initialize variability probability component to 0
        varProbComponent = 0
        
        #For the current column, loop through the unique values for that column
        for value in dfData[column].unique().tolist():
            #print("Value: "+str(value))
            #Create a new df for just those rows with the current value
            dfIsValue = dfData[dfData[column] == value]
            
            #Count the rows for that value
            valueCount = dfIsValue.shape[0]
            #print("Value count: "+str(valueCount))
            
            #Calculate the probability of the value within the column (count of the value / total # rows)
            valueProb = valueCount/num_rows
            #print("Value prob: "+str(valueProb))
            
            #Add the square of the probability for the current value to the probability component of the variability calc
            varProbComponent = varProbComponent + valueProb**2
            #print("Variability probability component: "+str(varProbComponent))
            
        #Calc the variability for the current column    
        colVariability = 1 - varProbComponent
        lColVariability.append(colVariability)
        
        #print(colVariability)
        #print("\n")
    
    #Add the column variability list to the dfColumns dataframe as a new column
    dfColumns['Variability'] = lColVariability
    
    return dfColumns

def calc_num_stats(dfData, dfColumns):
    #Get the stats for all numeric columns using the describe function and transpose so the column names are the index
    numStats = dfData.describe().transpose()
    #Add the new stats for the numeric columns to the Columns dataframe
    dfColumns = pd.concat([dfColumns.set_index('Col_Name'), numStats], axis=1)
    dfColumns.index.name='Col_Name'
    
    return dfColumns

def process_csv(csvFilePath):
    dfCSVData = get_data_csv(csvFilePath)
    dfCols = get_columns(dfCSVData)
    dfCols = get_col_types(dfCSVData, dfCols)
    dfCols = calc_num_blanks(dfCSVData, dfCols)
    dfCols = calc_num_values(dfCSVData, dfCols)
    dfCols = calc_variability(dfCSVData, dfCols)
    dfCols = calc_num_stats(dfCSVData, dfCols)
    
    return dfCols