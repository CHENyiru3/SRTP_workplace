import xgboost as xgb      
import vaex    
from sklearn.model_selection import train_test_split      
from sklearn.metrics import accuracy_score      

data = vaex.open("/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/result/second_one_last.csv_chunk_0.hdf5")  
list_read=[f"C{i}" for i in range(502)]
X = data[list_read]  # 特征变量，前面几列    
y = data['C502']  # 目标变量，最后一列    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)      
  
model = xgb.XGBClassifier(objective='binary:logistic', n_estimators=100)      
model.fit(X_train, y_train)
    
predictions = vaex.open("/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/result/second_one_last.csv_chunk_1.hdf5")

X_predict = predictions[list_read]  # 特征变量，前面几列    
y_predict = model.predict(X_predict)      
print(y_predict)