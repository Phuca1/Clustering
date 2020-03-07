import numpy as np

np.random.seed(11)


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

