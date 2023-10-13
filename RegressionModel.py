import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

dataset = pd.read_csv("Salary Data.csv")

dataset = dataset.dropna()

le_education = LabelEncoder()
dataset['Education Level'] = le_education.fit_transform(dataset['Education Level'])

le_gender = LabelEncoder()
dataset['Gender'] = le_gender.fit_transform(dataset['Gender'])

le_jobtitle = LabelEncoder()
dataset['Job Title'] = le_jobtitle.fit_transform(dataset['Job Title'])

X = dataset.drop("Salary", axis=1)
y = dataset["Salary"]


#ML Model
model = DecisionTreeRegressor(random_state=1)
model.fit(X.values, y.values)


#save model
data = {"model": model, "le_gender": le_gender, "le_education": le_education, "le_jobtitle": le_jobtitle}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)