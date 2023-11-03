from vaex.ml.catboost import CatBoostModel
import vaex
from catboost import sum_models
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
name_list=[f'booster{i}' for i in range(2)]

for i in range(2):
    df=vaex.open('/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/test_int_randomed.csv.hdf5')
    df_train, df_test = df.ml.train_test_split(test_size=0.01, verbose=False)
    tem_booster = CatBoostModel(features=features, target=target, num_boost_round=23,
                        params=params, prediction_type='Class', batch_size=2000000)
    a= tem_booster.fit(df=df_train, progress='widget')
    
# sum_booster=sum_models(name_list)
#sum_booster.save_model(fname="/mnt/volume1/2023SRTP/library/TCRdb/Output/CBM_out1.cbm",format="cbm",export_parameters=None,pool=None)
# sum_booster.predict(df_test)







# from vaex.ml.catboost import CatBoostModel
# import vaex
# from catboost import sum_models
# features = [f'C{i}' for i in range(502)]
# target = 'C502'
# params = {
#     'leaf_estimation_method': 'Gradient',
#     'learning_rate': 0.1,
#     'max_depth': 3,
#     'bootstrap_type': 'Bernoulli',
#     'subsample': 0.8,
#     'sampling_frequency': 'PerTree',
#     'colsample_bylevel': 0.8,
#     'reg_lambda': 1,
#     'objective': 'MultiClass',
#     'eval_metric': 'MultiClass',
#     'random_state': 42,
#     'verbose': 0,
#     }
# booster_list=[]
# name_list=[f'booster{i}' for i in [0,0]]
   
# for i in [0,0]:
#     df=vaex.open(f'/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/result/second_one_last.csv_chunk_{i}.hdf5')
#     df_train = df
#     name_list[i] = CatBoostModel(features=features, target=target, num_boost_round=23,
#                         params=params, prediction_type='Class')
#     name_list[i]=name_list[i].fit(df=df_train, progress='widget')

# sum_models=sum_models(name_list)