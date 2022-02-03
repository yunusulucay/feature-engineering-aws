
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

csv_path = os.path.join("/opt/ml/processing/input", "df_info.csv")
df = pd.read_csv(csv_path)

df.drop(["skin_color","name"], axis=1, inplace=True)

df = df[(df.weight>=0) & (df.height>=0)]

df = df[df.publisher.isin(["Marvel Comics", "DC Comics"])]

label_encoder = LabelEncoder()

df_encoded = pd.DataFrame({})
for col in df.drop("publisher", axis=1).columns:
    if col not in ["height", "weight"]:
        df_encoded[col] = label_encoder.fit_transform(df[col])
    else:
        df_encoded[col] = df[col].values
df_encoded["publisher"] = df["publisher"].values

# No missing values.
df_encoded.isnull().any().sum()

# %90 train and %10 holdout dataset

df_train, df_holdout = train_test_split(df_encoded, test_size=0.1, stratify=df_encoded["publisher"])

# Split holdout data into 50% validation and 50% test

df_val, df_test = train_test_split(df_holdout, test_size=0.5, stratify=df_holdout["publisher"])

df_train.to_csv("/opt/ml/processing/train/df_train.csv", index=False)

df_test.to_csv("/opt/ml/processing/test/df_test.csv", index=False)

df_val.to_csv("/opt/ml/processing/val/df_val.csv", index=False)
