import pandas as pd 
import openpyxl as xl 

vetsu_ageSex = pd.read_excel('/Users/rando/projects/vetsu/vetsu.xlsx', sheet_name='vetAgeSex')
nonVet_ageSex = pd.read_excel('/Users/rando/projects/vetsu/vetsu.xlsx', sheet_name='NonVetAgeSex')


vetsu_ageSex.rename(columns={ vetsu_ageSex.columns[0]:  'year',
                     vetsu_ageSex.columns[1]:  'ageGroup',
                     vetsu_ageSex.columns[2]:  'vet_su',
                     vetsu_ageSex.columns[3]:  'vet_pop',
                     vetsu_ageSex.columns[4]:  'vet_rate_100K_crude',
                     vetsu_ageSex.columns[5]:  'vet_male_su',
                     vetsu_ageSex.columns[6]:  'vet_male_pop',                   
                     vetsu_ageSex.columns[7]:  'vet_male_rate_100K_crude',
                     vetsu_ageSex.columns[8]:  'ageGroup2',
                     vetsu_ageSex.columns[9]:  'vet_female_su',
                    vetsu_ageSex.columns[10]: 'vet_female_pop',
                    vetsu_ageSex.columns[11]: 'vet_female_rate_100K_crude'}
                    ,inplace=True)

nonVet_ageSex.rename(columns={ nonVet_ageSex.columns[0]:  'year',
                     nonVet_ageSex.columns[1]:  'ageGroup',
                     nonVet_ageSex.columns[2]:  'vet_su',
                     nonVet_ageSex.columns[3]:  'vet_pop',
                     nonVet_ageSex.columns[4]:  'vet_rate_100K_crude',
                     nonVet_ageSex.columns[5]:  'vet_male_su',
                     nonVet_ageSex.columns[6]:  'vet_male_pop',                   
                     nonVet_ageSex.columns[7]:  'vet_male_rate_100K_crude',
                     nonVet_ageSex.columns[8]:  'ageGroup2',
                     nonVet_ageSex.columns[9]:  'vet_female_su',
                    nonVet_ageSex.columns[10]: 'vet_female_pop',
                    nonVet_ageSex.columns[11]: 'vet_female_rate_100K_crude'}
                    ,inplace=True)

print(nonVet_ageSex.columns)