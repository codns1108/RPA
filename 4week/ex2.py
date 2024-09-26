import pandas as pd
data = {'이름' : ['Kim', 'Park', "Lee", "Ho"],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88]}

df = pd.DataFrame(data)

print("국어평균", df['국어'].mean(), end="\n\n")
print("국어중간", df['국어'].median(), end="\n\n")
print("국어촤소", df['국어'].min(), end='\n\n')
print("국어최대", df['국어'].max(), end='\n\n')

print("kim 총점", df.iloc[0, 1:4].sum(), end='\n\n')
print("kim 평균", df.iloc[0, 1:4].mean(), end='\n\n')

print('수학 4분위 \n', df['수학'].quantile([0.25,0.5,0.75]), end='\n\n')
print('수학분산', df['수학'].var(), end='\n\n')
print('수학표준편차', df['수학'].std(), end='\n\n')