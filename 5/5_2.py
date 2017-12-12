
from sklearn.cluster import KMeans
import numpy as np

X_train = [[1,3], [1,2], [2,1], [2,2], [2,3], [3,2], [5,3], [4,3], [4,5], [5,4], [5,5], [6,4], [6,5]]
X = np.array(X_train)

clusterCenters = [[0,4],[6,5]]
clusterCenters = np.array(clusterCenters)

kmeans = KMeans(n_clusters=2, init=clusterCenters).fit(X)

print(kmeans.labels_)
print(kmeans.cluster_centers_)
