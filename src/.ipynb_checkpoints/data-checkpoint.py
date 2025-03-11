import pandas as pd

df = pd.read_csv("./data/train_all.csv")

# 90% train data = new train file 
train = int(len(df) * 0.90)
df_train = df.iloc[:train]
df_train.to_csv("./data/train.csv", index=False)

# 10% train data = validation
validation = len(df)
df_validation = df.iloc[train:validation]
df_validation.to_csv("./data/validation.csv", index=False)