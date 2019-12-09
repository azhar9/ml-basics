import pandas as pd
import numpy as np

CSV_PATH = 'DataScience/PastHires.csv'
df = pd.read_csv(CSV_PATH)
print(df.head(8))#if no int is passed to head it will print first 5 rows other wise int rows it prints from first
print(df.tail(4))#if no int is passed to tail it will print last 5 rows other wise int rows it prints from last
print(df.shape) #gives (rows,cols)
print(df.size) #gives rows*cols which is equal to no of cells
print(len(df)) #gives rows
print(df.columns)#gives all the columns
print(df['Hired']) #gives the whole column Hired data
print(df['Hired'][:5]) #slicing and index just works like string

tdf = df[['Years Experience', 'Hired']] #to get multiple cols data and slicing and indexing works too
print(tdf)

print(df.sort_values(['Years Experience'])) #it sorts the data frame ascend to descend based on the col specified

degree_counts = df['Level of Education'].value_counts() #gives the number of times a value is repeated in a col
print(degree_counts)

degree_counts.plot(kind='bar') #to plot the above degree_counts in a bar char or histogram
import matplotlib.pyplot as plt #this line and below line is added to show the graph on screen
plt.show()      #pandas internally uses matplotlib to graphing

#question
'''
Try extracting rows 5-10 of our DataFrame, preserving only the "Previous employers" and "Hired" columns.
 Assign that to a new DataFrame, and create a histogram plotting the distribution of the previous 
 employers in this subset of the data.
'''

newdf = df[['Previous employers','Hired']][5:10]
histdf = newdf['Previous employers'].value_counts()
print(histdf)
histdf.plot(kind='bar')
plt.show()
