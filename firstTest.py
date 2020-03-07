import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

np.random.seed(11)
#
# means = [[2, 2], [8, 3], [3, 6]]
# cov = [[1, 0], [0, 1]]
# N = 500
# X0 = np.random.multivariate_normal(means[0], cov, N)
# X1 = np.random.multivariate_normal(means[1], cov, N)
# X2 = np.random.multivariate_normal(means[2], cov, N)
#
# X = np.concatenate((X0, X1, X2), axis=0)
# print(X.shape)
# label = np.asarray([0] * N + [1] * N + [2] * N).T
#
#
# def display(X, label):
#     X0 = X[label == 0, :]
#     X1 = X[label == 1, :]
#     X2 = X[label == 2, :]
#
#     plt.plot(X0[:, 0], X0[:, 1], 'rd', markersize=4)
#     plt.plot(X1[:, 0], X1[:, 1], 'gd', markersize=4)
#     plt.plot(X2[:, 0], X2[:, 1], 'bd', markersize=4)
#     plt.axis('equal')
#     plt.show()


# display(X,label)

# def kmeans(X,label):


file = open('WSCD.csv')
a = list(file)
arr = []
for i in range(1, len(a)):
    txt = a[i]
    txt.strip()
    point = txt.split(',')
    x = []
    for item in point:
        x.append(int(item))
    arr.append(x)
file.close()
X = np.asarray(arr)
print(X)


def center_init(X, K):
    a = np.random.choice(X.shape[0], K, replace=False)
    return X[a]


def dist(X, Y):
    return np.linalg.norm(X - Y, keepdims=False)


def find_cluster(X, center):
    a = np.zeros(center.shape[0])
    D = []
    for i in range(a.shape[0]):
        t = dist(X, center[i])
        D.append(t)
    distance = np.asarray(D)
    distance.reshape((center.shape[0]))
    return np.argmin(distance)


def find_center(X, cluster, k):
    cen = []
    for i in range(k):
        a = X[cluster == i, :]
        b = np.mean(a, axis=0)
        cen.append(b)
    t = np.asarray(cen)
    t.reshape((k, X.shape[1]))
    return t


def kmeans(X, center_init):
    center = [center_init]
    count = 0
    while True:
        cluster = []
        for i in range(X.shape[0]):
            ind = find_cluster(X[i], center[-1])
            cluster.append(ind)

        cluster = np.asarray(cluster)
        a = find_center(X, cluster, center_init.shape[0])
        center.append(a)
        count += 1
        if np.linalg.norm(center[-1] - center[-2]) < 1e-3 or count >= 100000:
            break
    return center


K = 4
cti = center_init(X, K)
print(cti)

cen = kmeans(X, cti)
print(cen[-1])

cluster = []
for i in range(X.shape[0]):
    ind = find_cluster(X[i], cen[-1])
    cluster.append(ind)
for i in range(K):
    print("item in cluster %d :"%(i))
    for j in range(len(cluster)):
        if cluster[j] == i :
            print(j)


# cluster = []
# for i in range(X.shape[0]):
#      ind = find_cluster(X[i], cti)
#      cluster.append(ind)
#
# print(cluster)
# cluster = np.asarray(cluster)

# cen = []
# for i in range(K):
#     a = X[cluster == i, :]
#     b =np.mean(a,axis=0)
#     cen.append(b)
# cen = np.asarray(cen)
# print(cen)

# print(find_center(X,cluster,K))
#vcl