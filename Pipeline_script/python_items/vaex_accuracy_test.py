import vaex.ml.metrics
from sklearn.linear_model import LogisticRegression

df = vaex.datasets.iris()
df_train, df_test = df.split_random([0.8, 0.2], random_state=55)

features = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
target = 'class_'

model = LogisticRegression(random_state=42)
vaex_model = Predictor(features=features, target=target, model=model, prediction_name='pred')

vaex_model.fit(df=df_train)

df_test = vaex_model.transform(df_test)
print(type(df_test))
print(df_test.ml.metrics.classification_report(df_test.class_, df_test.pred, average='macro'))