import pandas as pd
data = {'이름' : ['Kim', 'Park', "Lee", "Ho"],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88]}

df = pd.DataFrame(data)
print(df, end="\n\n")

name1 = df['이름']
print(name1, end="\n\n")

name2 = df.loc[1]
name2 = df.loc[df['이름'] == 'Park']
print(name2, end="\n\n")

df.loc[df['이름']=='Ho', '수학'] = 90
print(df, end="\n\n")

df.loc[4] = ["Oh", 100, 70, 80]
print(df, end="\n\n")

df = df.drop([2], axis=0)
print(df, end='\n\n')
