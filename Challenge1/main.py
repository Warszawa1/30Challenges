import pandas as pd

columns = ['Names', 'Email']
dataFrame = pd.read_csv('excel.xls', names=columns)
print('DataFrame...\n', dataFrame, '\n')

for element in dataFrame['Email'].unique():
    print(element)

