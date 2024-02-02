## 2. Inertia ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def kmeans(df, k, n_iterations=100):
    variables = df.columns

    centroids, coords = get_centroids(df, k)

    for i in range(n_iterations):
        last_coords = coords.copy()

        df, dists = calculate_distance(df, coords)

        df['cluster'] = df[dists].idxmin(axis=1).str.split('_').str[-1]

        centroids = round(df.groupby('cluster')[variables].mean(), 4)
        coords = centroids.values.tolist()

        if last_coords == coords:
      	    break
            
    df['sqrt_dist_centroid'] = df[dists].min(axis=1)**2
    inertia = df['sqrt_dist_centroid'].sum()
    
    print(f'Total Iterations: {i + 1}')

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(variables[0], variables[1], hue='cluster', palette='tab10', data=df, s=50, ax=ax)
    sns.scatterplot(variables[0], variables[1], color='black', data=centroids, s=100, ax=ax)


    plt.tight_layout()
    plt.show()

    return df['cluster'], inertia


customers = pd.read_csv('mall_customers.csv')

cols_to_keep = ['Annual Income', 'Spending Score']
customers = customers[cols_to_keep].copy()

clusters, inertia = kmeans(customers, 2)

## 3. Calculating More Inertias ##

inertias = []

for i in range(1, 11):
    clusters, inertia = kmeans(customers, i)
    inertias.append(inertia)
    
print(inertias)

'''
The inertia decreased as the number of clusters increased. That makes perfect sense because if the number of clusters keeps increasing until it reaches the number of observations in the dataset, inertia will be zero.
'''

## 4. The Elbow Curve ##

inertias = [269981.27999999997, 184131.88502826, 106348.37306241, 
            73679.78903966, 44448.45544817, 38718.38226857,
            34918.93964226, 30176.132287570003, 29068.11150443,
            21063.88614989]

import matplotlib.pyplot as plt

plt.plot(range(1,11), inertias, marker='o')
plt.show()

## 5. Choosing K ##

customers = pd.read_csv('mall_customers.csv')

cols_to_keep = ['Annual Income', 'Spending Score']
customers = customers[cols_to_keep].copy()

clusters, inertia = kmeans(customers, k=5, plot=True)