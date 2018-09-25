import pandas as pd


def find(city):
    df = pd.read_excel('Cities.xlsx', skiprows=1)
    temp = df.loc[df['Город'] == city]

    dc = temp.as_matrix()

    d = {'list': dc[0][0],
         'city': dc[0][1],
         'reg': dc[0][2],
         'federal': dc[0][3],
         'people': dc[0][4],
         'date': dc[0][5]}

    return d
