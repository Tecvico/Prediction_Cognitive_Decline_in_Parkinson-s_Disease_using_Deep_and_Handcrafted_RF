import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from skrebate import ReliefF
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

genetic_data = pd.read_csv('https://github.com/EpistasisLab/scikit-rebate/raw/master/data/'
                           'GAMETES_Epistasis_2-Way_20atts_0.4H_EDM-1_1.tsv.gz',
                           sep='\t', compression='gzip')

features, labels = genetic_data.drop('class', axis=1).values, genetic_data['class'].values

clf = ReliefF(n_features_to_select=2, n_neighbors=100)

clf.fit(features, labels)
clf.transform(features)
ffname = clf.top_features_[:2]
features = features[ffname]
print(ffname)

print('aaa')
# print(np.mean(cross_val_score(clf, features, labels)))