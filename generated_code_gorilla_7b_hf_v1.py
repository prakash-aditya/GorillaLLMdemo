from transformers import AutoTokenizer, AutoModel

def load_model():
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')
    model = AutoModel.from_pretrained('microsoft/codebert-base')
    return tokenizer, model

def process_data(tokenizer, model, input_text):
    # Tokenize and generate embeddings
    inputs = tokenizer(input_text, return_tensors='pt')
    embeddings = model(**inputs).last_hidden_state
    return embeddings

input_text = 'print(1)'

# Load the model and tokenizer
tokenizer, model = load_model()

# Process the data
embeddings = process_data(tokenizer, model, input_text)
print(embeddings)