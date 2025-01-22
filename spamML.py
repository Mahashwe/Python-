from sklearn.feature_extraction.text import CountVectorizer  # to change the words to vectors
from sklearn.naive_bayes import MultinomialNB  # performing Naive Bayes classification
from sklearn.model_selection import train_test_split  # to split the data into training and testing

# Sample dataset with messages and labels (spam/ham)
dataset = [
    ("Win money now!", "spam"),
    ("Call me later", "ham"),
    ("Limited time offer, win a prize!", "spam"),
    ("How are you?", "ham"),
    ("Congratulations! You've won!", "spam"),
    ("Can we meet tomorrow?", "ham")
]

# Separate messages and labels into two lists
messagebox = []
labelbox = []

# Append individual messages and labels to their respective lists
for message, label in dataset:
    messagebox.append(message)  # Append the message
    labelbox.append(label)      # Append the corresponding label

# Initialize CountVectorizer to convert messages into feature vectors
vectorizer = CountVectorizer()

# Convert the list of messages into a sparse matrix of word counts
x = vectorizer.fit_transform(messagebox)

# Labels (ham or spam)
y = labelbox

# Split the dataset into training and testing sets (70% train, 30% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Initialize the Naive Bayes classifier
model = MultinomialNB()

# Train the model on the training data
model.fit(x_train, y_train)

# Now, we prompt the user for input messages
while True:
    # Get input from the user for test messages
    user_input = input("Enter a message to classify as spam or not spam - enter 'exit' to end: ")

    # Exit condition
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Transform the user's message using the vectorizer (pass a list of messages)
    user_input_features = vectorizer.transform([user_input])

    # Predict the label for the user's message
    prediction = model.predict(user_input_features)

    # Print the predicted label
    print(f"Message: '{user_input}' -> Classified as: {prediction[0]}")
