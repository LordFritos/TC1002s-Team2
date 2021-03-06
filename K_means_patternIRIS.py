from numba import jit
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

colour=['b','green','orange']

def main():
	data = pd.read_csv('./data/iris.data')
	npData = data.to_numpy()
	npData = np.delete(npData,obj=4, axis=1)

	#KLEARN
	klearn = KMeans(n_clusters=3, random_state=0).fit(npData)
	print(klearn.cluster_centers_)
	print("It ran {} iterations".format(klearn.n_iter_))
	print(klearn.labels_)
	print(len(npData),len(klearn.labels_))

	plt.title('KMeans learn')

	#Cluster data
	for i in range(len(klearn.labels_)):
		X = npData[i,0]
		Y = npData[i,1]
		plt.scatter(X,Y,color=colour[klearn.labels_[i]])

	#cluster centers
	x = klearn.cluster_centers_[:,0]
	y = klearn.cluster_centers_[:,1]
	plt.scatter(x,y,color='r',marker='+',s=100)
	plt.show()


if __name__ == '__main__':
	main()