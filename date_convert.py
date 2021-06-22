#!/usr/bin/env python
# coding: utf-8

# columns date format like 2017-10-15 12:30:46,000

import pandas as pd

def parse_date(x):
    return pd.to_datetime(str(x)[:10],format = '%Y-%m-%d')

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
