## 4. Initialize Centroids ##

cols_to_keep = ['Age', 'Spending Score']

customers = customers[cols_to_keep].copy()

centroids = customers.sample(2)

def fetch_coordinates(df):
    age_centroid_1 = df.iloc[0,0]
    score_centroid_1 = df.iloc[0,1]
    age_centroid_2 = df.iloc[1,0]
    score_centroid_2 = df.iloc[1,1]
    
    return age_centroid_1, score_centroid_1, age_centroid_2, score_centroid_2

age_centroid_1, score_centroid_1, age_centroid_2, score_centroid_2 = fetch_coordinates(centroids)

plt.scatter(customers['Age'], customers['Spending Score'])
plt.scatter(centroids['Age'], centroids['Spending Score'], color='red', s=100)
plt.show()

## 5. Distances Between the Points ##

customers = pd.read_csv('mall_customers.csv')

cols_to_keep = ['Age', 'Spending Score']

customers = customers[cols_to_keep].copy()

centroids = customers.sample(2)

def fetch_coordinates(df):
    age_centroid_1 = df.iloc[0, 0]
    score_centroid_1 = df.iloc[0, 1]
    age_centroid_2 = df.iloc[1, 0]
    score_centroid_2 = df.iloc[1, 1]
    return age_centroid_1, score_centroid_1, age_centroid_2, score_centroid_2

age_centroid_1, score_centroid_1, age_centroid_2, score_centroid_2 = fetch_coordinates(centroids)

def calculate_distance(s, age_centroid, score_centroid):
    distance = np.sqrt((s.loc['Age'] - age_centroid)**2 + (s.loc['Spending Score'] - score_centroid)**2)
    
    return distance

customers['dist_centroid_1'] = customers.apply(calculate_distance, args=(age_centroid_1, score_centroid_1), axis=1)
customers['dist_centroid_2'] = customers.apply(calculate_distance, args=(age_centroid_2, score_centroid_2), axis=1)

print(customers.head())

## 6. Assigning Clusters ##

import matplotlib.pyplot as plt
import seaborn as sns


def calculate_distance_assign_clusters(customers, centroids):
    age_centroid_1, score_centroid_1, age_centroid_2, score_centroid_2 = fetch_coordinates(centroids)
    customers['dist_centroid_1'] = customers.apply(calculate_distance, args=(age_centroid_1, score_centroid_1), axis=1)
    customers['dist_centroid_2'] = customers.apply(calculate_distance, args=(age_centroid_2, score_centroid_2), axis=1)
    customers['cluster'] = np.where(customers['dist_centroid_1'] < customers['dist_centroid_2'], 1, 2)
    return customers

customers = calculate_distance_assign_clusters(customers, centroids)

sns.scatterplot('Age', 'Spending Score', hue='cluster',
               palette='tab10', data=customers, s=50)
sns.scatterplot('Age', 'Spending Score', color='red', data=centroids, s=100)
plt.show()

## 7. Creating New Clusters ##

new_centroids = customers.groupby('cluster')['Age', 'Spending Score'].mean().reset_index()
new_centroids.drop('cluster', axis=1, inplace=True)

customers = calculate_distance_assign_clusters(customers, new_centroids)

sns.scatterplot(x='Age', y='Spending Score', hue='cluster', data=customers, palette='tab10', s=50)
sns.scatterplot(x='Age', y='Spending Score', data=new_centroids, color='red', s=100)
plt.show()

## 8. Wrapping in a Function ##

cols_to_keep = ['Age', 'Spending Score']

customers = customers[cols_to_keep].copy()

def create_clusters(df):
    centroids = df.sample(2)
    df = calculate_distance_assign_clusters(df, centroids)
    new_centroids = df.groupby('cluster')['Age', 'Spending Score'].mean().reset_index()
    new_centroids.drop('cluster', axis=1, inplace=True)
    customers = calculate_distance_assign_clusters(df, new_centroids)
    
    return df['cluster']

clusters = create_clusters(customers)