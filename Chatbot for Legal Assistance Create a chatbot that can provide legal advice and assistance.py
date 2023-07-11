from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

# Load stopwords and initialize lemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Define legal information
legal_info = {
    'contracts': 'A contract is a legally binding agreement between two or more parties.',
    'intellectual property': 'Intellectual property refers to creations of the mind, such as inventions, literary and artistic works, symbols, names, and designs.',
    'immigration': 'Immigration law governs the legal status of people entering, staying, or leaving a country.'
}

# Process user input and generate response
def process_input(user_input):
    # Tokenize and lemmatize user input
    tokens = word_tokenize(user_input)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.lower() not in stop_words]

    # Identify the area of law mentioned in the user input
    area_of_law = None
    for token in lemmatized_tokens:
        if token in legal_info:
            area_of_law = token
            break

    # Generate response based on the identified area of law
    if area_of_law:
        response = legal_info[area_of_law]
    else:
        response = "I'm sorry, I can't provide information on that area of law."

    return response

# Define the chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['input']
    response = process_input(user_input)
    return jsonify({'response': response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
