from vaex.ml.catboost import CatBoostModel
import vaex
import vaex.ml.metrics
import numpy as np
features = [f'C{i}' for i in range(502)]
target = 'C502'
params = {
    'leaf_estimation_method': 'Gradient',
    'learning_rate': 0.1,
    'max_depth': 3,
    'bootstrap_type': 'Bernoulli',
    'subsample': 0.8,
    'sampling_frequency': 'PerTree',
    'colsample_bylevel': 0.8,
    'reg_lambda': 1,
    'objective': 'MultiClass',
    'eval_metric': 'MultiClass',
    'random_state': 42,
    'verbose': 0,
    }
df=vaex.open('/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/test_int_randomed.csv.hdf5')
df_train, df_test = df.ml.train_test_split(test_size=0.01, verbose=False)
booster = CatBoostModel(features=features, target=target, num_boost_round=23,
                        params=params, prediction_type='Class', batch_size=11_000_000)
booster.fit(df=df_train, progress='widget')

result=booster.predict(df_train)
print(result)
df_test = booster.transform(df_train)
print(df_test)

true_num=0
for i in range(len(result)):
    if np.any(df_test.catboost_prediction.values==df_test.C502.values):
        true_num+=1
print(true_num/len(result))