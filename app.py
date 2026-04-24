from model import train_model

model = train_model()

def predict_return(size_match, description_match, price):
    prediction = model.predict([[size_match, description_match, price]])
    return prediction[0]

if __name__ == "__main__":
    print("Return Prediction System")

    size_match = int(input("Size match? (1=yes, 0=no): "))
    description_match = int(input("Description accurate? (1=yes, 0=no): "))
    price = int(input("Price: "))

    result = predict_return(size_match, description_match, price)

    if result == 1:
        print("⚠️ High chance of return")
    else:
        print("✅ Low chance of return")