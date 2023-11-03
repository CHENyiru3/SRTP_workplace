from sklearn.ensemble import RandomForestClassifier  
from sklearn.model_selection import cross_val_score, cross_validate  
from sklearn.metrics import accuracy_score, precision_score, recall_score  
import pandas as pd  
import pickle  
  
def load_data(file_path):  
    with open(file_path, 'rb') as file:  
         data = pickle.load(file)  
    return data  
  
TCR_test = load_data('/mnt/volume1/2023SRTP/library/TCRdb/Output/Pickle/ncbi/test.pkl')  
  
rfc = RandomForestClassifier(bootstrap=True, criterion='gini', max_depth=14,   
                             max_features='auto', min_samples_leaf=1, min_samples_split=2,  
                             n_estimators=80, random_state=2)  
testdata = TCR_test.iloc[:, :501]  
labels = TCR_test.loc[:, 502]  
  
# 进行5折交叉验证  
scores = cross_validate(rfc, testdata, labels, cv=5,   
                        scoring=['accuracy', 'precision', 'recall'])  
  
# 输出交叉验证结果  
print("Accuracy: %0.2f (+/- %0.2f)" % (scores['test_accuracy'].mean(), scores['test_accuracy'].std() * 2))  
print("Precision: %0.2f (+/- %0.2f)" % (scores['test_precision'].mean(), scores['test_precision'].std() * 2))  
print("Recall: %0.2f (+/- %0.2f)" % (scores['test_recall'].mean(), scores['test_recall'].std() * 2))
     


# from sklearn.ensemble import RandomForestClassifier
# import pandas as pd
# import joblib
# import pickle
# import numpy as np
# with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/Pickle/ncbi/tfd1.pkl', 'rb') as file:
#     TCR_test = pickle.load(file)
# with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/Pickle/ncbi/tfd2.pkl', 'rb') as file:
#     unknow_data = pickle.load(file)  

# list_cdr3=[]
# for row in TCR_test:
#     x=row[1][0]
#     list_cdr3.append(x)

# # 创建DataFrame  
# df1 = pd.DataFrame(columns=['CDR3aa'])  
# for i in range(len(list_cdr3)):  
#     df1.loc[i, 'CDR3aa'] = list_cdr3[i]  
# print(df1)

# list_tissue = []
# for row in TCR_test:
#     list_tissue.append(row[2])

# list_celltype = []
# for row in TCR_test:
#     list_celltype.append(row[3])

# list_disease = []
# for row in TCR_test:
#     list_disease.append(row[4])

# p_list_cdr3 = []
# for row in unknow_data:
#     p_list_cdr3.append(row[1][0])
# df2 = pd.DataFrame(columns=["CDR3aa"])
# for i in range(len(p_list_cdr3)):  
#     df1.loc[i, 'CDR3aa'] = p_list_cdr3[i]  
# p_list_tissue = []
# for row in unknow_data:
#     p_list_tissue.append(row[2])
# p_list_celltype = []
# for row in unknow_data:
#     p_list_celltype.append(row[3])
# test_features = pd.DataFrame({
#     #'feature2':df1["CDR3aa"],
#     'feature3':list_tissue,
#     'feature4':list_celltype})
# unknow_features=pd.DataFrame({
#                            #'feature2':df2["CDR3aa"],
#                            'feature3':p_list_tissue,
#                            'feature4':p_list_celltype})
# #target is disease
# disease_lable=pd.DataFrame({'disease':list_disease})
# #bulid the random forest model
# print(test_features.shape, type(test_features))  
# print(disease_lable.shape, type(disease_lable))
# rfc = RandomForestClassifier(bootstrap= True, criterion ='gini', max_depth= 14, 
#                              max_features= 'auto', min_samples_leaf= 1, min_samples_split=2,
#                                n_estimators= 80, random_state= 2)

# rfc.fit(test_features,disease_lable)
# print(rfc.predict(unknow_features))
# #save the model
# #joblib.dump(rfc, '/mnt/volume1/2023SRTP/library/TCRdb/Output/model.joblib')
# #load model
# #loaded_model = joblib.load('model.joblib')