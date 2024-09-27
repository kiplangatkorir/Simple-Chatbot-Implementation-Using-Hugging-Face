from flask import render_template, request, session
from app import create_app
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

app = create_app()

# Load pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text generation pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(user_input, context):
    full_input = context + " " + user_input
    response = chatbot(full_input, max_length=150, num_return_sequences=1)[0]['generated_text']
    new_context = response.replace(context + " " + user_input, "").strip()
    return new_context

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if 'context' not in session:
        session['context'] = ""
    response = generate_response(user_input, session['context'])
    session['context'] += " " + user_input + " " + response
    return response
