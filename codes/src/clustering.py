# clustering the job skills
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import random

# pca cluster
cv = CountVectorizer(analyzer='word', max_features=5000, lowercase=True,
                     preprocessor=None, tokenizer=None, stop_words='english')
vectors = cv.fit_transform(x)
kmeans = KMeans(n_clusters=10, init='k-means++', random_state=0)
kmean_indices = kmeans.fit_predict(vectors)

pca = PCA(n_components=2)
scatter_plot_points = pca.fit_transform(vectors.toarray())

number_of_colors = 10

colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
          for i in range(number_of_colors)]

x_axis = [o[0]for o in scatter_plot_points]

y_axis = [o[1] for o in scatter_plot_points]


fig, ax = plt.subplots(figsize=(40, 20))

ax.scatter(x_axis, y_axis, c=[colors[d] for d in kmean_indices])

for i, txt in enumerate(jobs_plot.Job_Title.to_list()):
    ax.annotate(txt, (x_axis[i], y_axis[i]))


# try 33
h1b = pd.read_pickle("../data/h1b_clean.pkl")
data = h1b[['relatedSkills', 'Dice_job_title']]
df = data

Optimal_k = 33

WordVectorizer = TfidfVectorizer(stop_words='english')

X = WordVectorizer.fit_transform(df['relatedSkills'])

model = KMeans(n_clusters=Optimal_k, init='k-means++', max_iter=200, n_init=10)

model.fit(X)

df['Cluster'] = pd.DataFrame(model.labels_)

# elbow method
WordVectorizer = TfidfVectorizer(stop_words='english')

X = WordVectorizer.fit_transform(df['relatedSkills'])
df = h1b.dropna()

WordVectorizer = TfidfVectorizer(stop_words='english')

X = WordVectorizer.fit_transform(df['relatedSkills'])

# k means determine k
distortions = []
K = range(1, 30)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X)
    distortions.append(kmeanModel.inertia_)
# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal to 30')
plt.grid()
plt.show()
