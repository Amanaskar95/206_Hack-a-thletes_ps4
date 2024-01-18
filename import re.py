import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


from flask import Flask, render_template,request,jsonify
import os/:
import pickle
from sklearn.feature_extraction.text import TfidVectorizer
 from sklearn.metrics.pairwise import cosine similarity
 import re
 import nltk  
 #nltk.download('punkt')
 from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
 from nltk.stem import PorterStemmer
 import csv
 from docx import Document
 import textract
 from PyPDF2 import PdfReader
 from sentence_transformers, import SentenceTransformer, util
from nltk.stem import PorterStemmer
app Flask (_name_)
def preprocess_text(text):
# Convert text to lowercase
text = text.lower()

#Remove punctuation and special character's 
text = re.sub([^a-zA-Z0-9\s)',", text)

# Tokenize the text.
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop words]

# Stem words
stemmer PorterStemmer()
words = [stemmer.stem(word) for word in words]

#Join the words back into a single string
from sentence_transformers import SentenceTransformer, util

#Join the words back into a single string
 preprocessed_text= ' ',join(words)

return preprocessed_text
# Load the pre-processed data from the pickle file

 new ds pickle,load(open('preprocess_data1.pkl', 'rb'))

 new_ds['In Simple_Words'] = new_ds['Description'].apply(lambda x: (re.search(r'in Simple Words\s*([^"]+)?, x, re.DOTALL | re. IGNORECASE).group(1).strip() if me.search(r'in SimpleWords\s*([^"]+)?, x, re.DOTALL | re. IGNORECASE) and re.search(r'in Simple Words\s*([^"]+)?,x,re.DOTALL | re.IGNORANCE) and re.search(r' in Simple Words',x,re.IGNORECASE) and research( r' in Simple Words',x, re.IGNORECASE) els '')

#Load a pre-trained model for sentence embeddings
 model = Sentence Transformer("paraphrase-MiniLM-L6qv2")

def suggest_sections(complaint, dataset, min_suggestions=5):

# Preprocess the complaint 
preprocessed_complaint = preprocess_text(complaint)

# Calculate embeddings for the complaint and section descriptions
complaint_embedding model.encode(preprocessed_complaint) section_embeddings model.encode(dataset['Combo'].tolist())

# Calculate cosine similarity between the complaint embedding and section embeddings 
similarities = util.pytorch_cos_sim(complaint_embedding, section_embe

# Start with a high similarity threshold
similarity_threshold = 0.9
relevant_indices = []

# Iterate until you get enough suggestions 
while len(relevant_indices) < min_suggestions and similarity_threshol 
# Filter out suggestions below the dynamic similarity threshold
relevant_indices [1 for 1, sim in enumerate(similarities) if similarity_threshold 0.05

# Adjust the step size based on you

sorted_indices = sorted(relevant_indices, key-lambda i: similarities[ suggestions = dataset.iloc[sorted_indices][['Description', 'In_Simple_Words', 'Offense', 'Punishment', 'Cognizable', 'Bailable', 'Court']].to_dict(orient='records)

return suggestions
@app.route('/')
 def index():
 return render template('index.html')
 
 @app.route('/submit', methods=['POST']) 
 def submit()
   complaint request.fors['complaint']
  suggested_sections suggest_sections(complaint, new_ds)
  
  if suggested_sections:
   return render template('result.html', complaint = complaint, suggest