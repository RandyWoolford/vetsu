import pandas as pd 
import openpyxl as xl 

df1 = pd.read_excel('/Users/rando/projects/vetsu/vetsu.xlsx', sheet_name='vetAgeSex')

print(df1.columns)

