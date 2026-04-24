import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    data = pd.read_csv("sample_data.csv")

    X = data[["size_match", "description_match", "price"]]
    y = data["return"]

    model = LogisticRegression()
    model.fit(X, y)

    return model