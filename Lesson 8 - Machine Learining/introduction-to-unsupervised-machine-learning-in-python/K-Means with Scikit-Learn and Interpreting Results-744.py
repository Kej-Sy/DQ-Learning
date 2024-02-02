## 6. Interpreting Results — Numerical Variables ##

import matplotlib.pyplot as plt
import seaborn as sns

numeric_columns = ['Age', 'Annual Income', 'Spending Score']
print('m')

fig = plt.figure(figsize=(20, 10))

for i, column in enumerate(numeric_columns):
    df_plot = customers.groupby('Cluster')[column].mean()
    
    ax = fig.add_subplot(2, 2, i+1)
    ax.bar(df_plot.index, df_plot, color=sns.color_palette('Set1'), alpha=0.6)
    ax.set_title(f'Average {column.title()} per Cluster', alpha=0.5)
    ax.xaxis.grid(False)
    
plt.tight_layout()
plt.show()

## 8. Interpreting Results — Categorical Variables ##

plot_df = pd.crosstab(
  index=customers['Cluster'], columns=customers['Gender'],
  values=customers['Gender'], aggfunc='size', normalize='index'
)
fig, ax = plt.subplots(figsize=(12,6))

plot_df.plot.bar(stacked=True, ax=ax, alpha=0.6)
ax.set_title(f'% Gender per Cluster', alpha=0.5)
ax.set_ylim(0, 1.4)
ax.legend(frameon=False)
ax.xaxis.grid(False)

plt.tight_layout()
plt.show()