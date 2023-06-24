"""
Pandas: data műveletekre fejlesztett library - modul
felhasználói: data scientistec és data engineerek

3 objectum típusa van:
Series: mint egy oszlop az excelben
DataFrame: mint egy adatábázis tábla

Panel - nem fogjuk használni -> multi dimenzionális tömb

DataFrame Seriesekből áll

"""

import pandas as pd


my_list = [item for item in range(100, 105)]

s = pd.Series(my_list, index=['a', 'b', 'c', 'd', 'e'])

# print(s[['c', 'd', 'e']])
# print(s[['c', 'd', 'e']].median())
# print(s[['c', 'd', 'e']].count())

# object dtype -> szöveges adat
my_dict = {"day1": 420, "day2": None, "day3": 311}

s = pd.Series(my_dict)

# print(s)
# print(s.values)

s.fillna(s.median(), inplace=True)

# print(s)

#####################################################
data = {
    "calories": [430, 530, 1230],
    "duration": [120, 200, 400]
}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

# print(df.columns)
# print(df.dtypes)

# print(df[['calories', 'duration']])

df['valami'] = [item for item in range(100, 400, 100)]

import pandas as pd
file_path = r"C:\WORK\2023_aprilis_python\20. alkalom\employees.csv"
df = pd.read_csv(file_path)
final_data = df.to_dict(orient="records")

df['percentile'] = df.quantile(q=100).round()


# print()
print(df.dtypes.to_dict())
print(df['hire_date'])
# int64 - integer
# float64 - real, decimal, numeric
# object - text, varchar(mérete) pl .varchar(100)