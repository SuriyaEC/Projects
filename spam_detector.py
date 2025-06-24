import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

spam_csv = 'C:/Users/Admin/Desktop/resume_projects/spam_project/SMSSpamCollection'

df = pd.read_csv(spam_csv, sep='\t', header=None, names=['label', 'text'])

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

print("Sample data:")
print(df.head())
print("\nTotal messages:", len(df))
print("Label distribution:\n", df['label'].value_counts())

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\n✅ Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Confusion Matrix:")
print(cm)

sample = ["Congratulations! You've won a ₹10,000 prize. Call now!"]
sample_tfidf = vectorizer.transform(sample)
prediction = model.predict(sample_tfidf)[0]
print("\nSample Message Prediction:")
print(f"Message: {sample[0]}")
print("Predicted Label:", "Spam" if prediction == 1 else "Ham")
