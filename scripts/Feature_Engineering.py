import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, chi2
df = pd.read_csv("C:/Users/Sharath/Desktop/DataScience Intern/Feature-Engineering-Selection/data/train.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop(columns=["Cabin"], inplace=True)
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])
scaler = StandardScaler()
df[["Age","Fare"]] = scaler.fit_transform(df[["Age","Fare"]])
X = df[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
y = df["Survived"]
selector = SelectKBest(score_func=chi2, k=5)
X_new = selector.fit_transform(abs(X), y)
selected_features = X.columns[selector.get_support()]
print("Selected Features:")
print(selected_features)
engineered = pd.DataFrame(X_new, columns=selected_features)
engineered["Survived"] = y
engineered.to_csv("C:/Users/Sharath/Desktop/DataScience Intern/Feature-Engineering-Selection/output/engineered_features.csv", index=False)
print("engineered_features.csv created successfully!")
