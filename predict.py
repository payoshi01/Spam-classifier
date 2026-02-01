import pickle

# Load saved model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predict_message(message):
    message_vec = vectorizer.transform([message])
    result = model.predict(message_vec)[0]
    return "Spam" if result == 1 else "Not Spam"

