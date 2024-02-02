## 1. Initialize K Centroids ##

import pandas as pd

cols_to_keep = ['Annual Income', 'Spending Score']

customers = pd.read_csv('mall_customers.csv')
customers = customers[cols_to_keep]

def get_centroids(df, k):
    centroids = df.sample(k).reset_index(drop=True)
    
    return centroids, centroids.values.tolist()

centroids, coords = get_centroids(df=customers, k=2)
print(centroids)
print(coords)    

## 2. Calculating Distances ##

def calculate_distance(df, centroids_coords):
    names = []
    for i, centroid in enumerate(centroids_coords):
        name = f'dist_centroid_{i+1}'
        df[name] = np.sqrt((df.iloc[:,0] - centroid[0])**2 + 
                           (df.iloc[:,1] - centroid[1])**2)
        names.append(name)
        
    return df, names

customers, dist_names = calculate_distance(customers, coords)
print(customers)
print(dist_names)

## 3. Assigning Clusters ##

customers['cluster'] = customers[dist_names].idxmin(axis=1).str.split('_').str[-1]

sns.scatterplot('Annual Income', 'Spending Score', data=customers, hue='cluster', palette='tab10',s=50)
sns.scatterplot('Annual Income', 'Spending Score', data=centroids, color='red', s=100)
plt.show()

## 4. Recalculating Centroids ##

variables = customers.columns[:2]

new_centroids = round(customers.groupby('cluster').mean()[variables], 4)

new_coords = new_centroids.values.tolist()

print(new_centroids)
print(new_coords)

## 5. Creating an Iterative Process ##

customers = pd.read_csv('mall_customers.csv')

cols_to_keep = ['Annual Income', 'Spending Score']
customers = customers[cols_to_keep].copy()

variables = customers.columns

centroids, coords = get_centroids(customers, 2)

for i in range(100):
    customers, dist_names = calculate_distance(customers, coords)
    
    customers['cluster'] = customers[dist_names].idxmin(axis=1).str.split('_').str[-1]
    
    centroids = round(customers.groupby('cluster')[variables].mean(), 4)
    coords = centroids.values.tolist()
    
print(f'Total Iterations: {i+1}')

sns.scatterplot('Annual Income', 'Spending Score', data=customers, hue='cluster', palette='tab10', s=50)
sns.scatterplot('Annual Income', 'Spending Score', data=centroids, color='red', s=100)
plt.show()

## 7. Finishing the Algorithm ##

customers = pd.read_csv('mall_customers.csv')

cols_to_keep = ['Annual Income', 'Spending Score']
customers = customers[cols_to_keep].copy()

def kmeans(df, k, n_iterations):
    variables = df.columns
    
    centroids, coords  = get_centroids(df, k)
    
    for i in range(n_iterations):
        last_coords = coords.copy()
    
        df, dist_names = calculate_distance(df, coords)

        df['cluster'] = df[dist_names].idxmin(axis=1).str.split('_').str[-1]

        centroids = round(df.groupby('cluster')[variables].mean(), 4)
        coords = centroids.values.tolist()
    
        if last_coords == coords:
            break
        
    print(f'Total Iterations: {i + 1}')
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(variables[0], variables[1], hue='cluster', palette='tab10', data=df, s=50, ax=ax)
    sns.scatterplot(variables[0], variables[1], color='black', data=centroids, s=100, ax=ax)

    plt.tight_layout()
    plt.show()
    
    return df['cluster']

clusters = kmeans(customers, 2, 100)