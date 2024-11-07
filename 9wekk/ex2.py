import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

w = pd.read_csv('moving_keyword.csv')
print(w, end="\n\n")
print(w.head(10), end="\n\n")

w_n = w.iloc[:,1:5]
print(w_n, end="\n\n")
w_cor = w_n.corr(method='pearson')
print(w_cor, end="\n\n")
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

sns.pairplot(w_n)


plt.figure(figsize=(10,7))
sns.heatmap(w_cor, annot=True, cmap="Blues")
plt.show()