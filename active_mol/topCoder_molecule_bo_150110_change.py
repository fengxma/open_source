
# coding: utf-8

# In[58]:

import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier

# suggested way to set column names for the dataframe
col_names = ["ADMET_Solubility", "ADMET_Solubility_Level", "ADMET_Unknown_AlogP98", "ADMET_BBB",
                      "ADMET_BBB_Level", "ADMET_Absorption_Level", "ALogP", "LogD", "Molecular_Solubility",
                      "Molecular_SurfaceArea", "Molecular_PolarSurfaceArea", "Num_H_Acceptors", "Num_H_Donors",
                      "Molecular_Weight", "Molecular_Formula", "Num_Atoms", "Num_Bonds", "Num_RingBonds",
                      "Num_RotatableBonds", "Num_BridgeBonds", "Num_Rings", "Num_AromaticRings", "ActivityValue"]

# Read in the training data set with column names as defined in col_names
training_set = pd.read_csv("example_data.csv", names=col_names)

# this way to set headers will overwrite data in the first row
# Set column headers
# training_set.columns = ["ADMET_Solubility", "ADMET_Solubility_Level", "ADMET_Unknown_AlogP98", "ADMET_BBB",
#                      "ADMET_BBB_Level", "ADMET_Absorption_Level", "ALogP", "LogD", "Molecular_Solubility",
#                      "Molecular_SurfaceArea", "Molecular_PolarSurfaceArea", "Num_H_Acceptors", "Num_H_Donors",
#                      "Molecular_Weight", "Molecular_Formula", "Num_Atoms", "Num_Bonds", "Num_RingBonds",
#                      "Num_RotatableBonds", "Num_BridgeBonds", "Num_Rings", "Num_AromaticRings", "ActivityValue"]


# Peak at the data, note that the "activity" is measured as a continuous variable
# print training_set.head(1)


# In[59]:

# Supervised learning, excluding the dependent variable from data frame
# first convert the data frame into a numpyArray

# construct the predictor X with multiple features from the sample
X_cols = [ col for col in col_names if col not in ["Molecular_Formula", "ActivityValue"]]
# drop rows with nan values and take the first 3000 rows as the training set
training = training_set.dropna()
X = np.array(training[X_cols])
y = np.array(training["ActivityValue"])
X_training = X[:3000, :]
y_training = y[:3000]
# artificial test set from part of the sample
X_test = X[-400:, :]
y_test = y[-400:]

# set the n_neighbors to be the total number of molecules; need to change this to be a dynamic value later
neigh = KNeighborsClassifier(n_neighbors=len(X_training))
neigh.fit(X_training, y_training)

# show the new molecule -- X_test[1, :]'s nearest 3 neighbors
# in the result printed, 1st array shows the distance,
# 2nd array shows the position of nearest 3 neighbors in X_training

print(neigh.kneighbors(X_test[1, :], n_neighbors=3, return_distance=True))


#print(tuple1)


# In[60]:

# method to compute a tanimoto distance, base on
# http://stn.spotfire.com/spotfire_client_help/hc/hc_tanimoto_coefficient.htm

# def tanimotoCoef(A, B):
#     result = 0.0
#     sumTermA = 0.0
#     sumTermB = 0.0
#     crossTermAB = 0.0
#
#     if(len(A) != len(B)):
#         result = nan
#         print("ERROR: Length of two lists need to match")
#         return result
#     else:
#         for i in range(len(A)):
#             # the criteria here is that the values from both lists can not be strings or empty
#             if( (isinstance(A[i], str) == False and isinstance(B[i], str) == False) and
#                (np.isnan(A[i]) == False and np.isnan(B[i]) == False) ):
#                 sumTermA += A[i] **2
#                 sumTermB += B[i] **2
#                 crossTermAB += A[i] * B[i]
#         result = crossTermAB/(sumTermA + sumTermB - crossTermAB)
#         return result
#
#
# # In[61]:
#
# # test on tanimotoCoef()
# t1 = feature_array[9]
# t2 = feature_array[100]
# print(t1)
#
# tanimotoCoef(t1, t1)
#
# # In[62]:
#
# def similarity(molecularID):
#     # this could be merge with the main class in java, trainingSet.similarity(int index)
#     training_set = feature_array
#     selectedTuple = training_set[molecularID]
#     result = []
#
#     for row in range(training_set.shape[0]):
#         result.append(tanimotoCoef(selectedTuple, training_set[row]))
#     return result
#
#
# # In[63]:
#
# # test
# similarity(2)[1:10]


# In[ ]:




# In[15]:

# Arvhive of old dummy methods: not using any more.
# def greaterAbs(A, B):
#     if( absolute(A) >= absolute(B) ):
#         return absolute(A)
#     else:
#         return absolute(B)
#
# def computeDistance(A, B):
#     result = 0.0
#     if(len(A) != len(B)):
#         result = nan
#         return result
#     else:
#         for i in range(len(A)):
#             if( (isinstance(A[i], str) == False and isinstance(B[i], str) == False) and
#                (isnan(A[i]) == False and isnan(B[i]) == False) ):
#                 result += ( absolute(A[i] - B[i]) / greaterAbs(A[i], B[i]) )**2
#         return result


# In[137]:



