#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
# парсер даты
def parse_date(x):
    return pd.to_datetime(str(x)[:10],format = '%Y-%m-%d')
# определить колонки с датами

#date_columns = ['StartDate','PlanDate']
def convert_columns(date_columns, df):
    for i in date_columns:
        df[i] = df[i].apply(lambda x:parse_date(x))
    return df
    
if __name__ == '__main__':
    file = input('Введіть назву файлу: ')
    df = pd.read_csv(file,delimiter=';',parse_dates=False)
    print(f'Колонки датафрейму: {df.columns}')
    date_columns = input('Введіть назви колонок з датами для конвертації: ').split(',')
    result= convert_columns(date_columns, df)
    print('Результат збережено в датафрейм result')
    
    


# In[ ]:




