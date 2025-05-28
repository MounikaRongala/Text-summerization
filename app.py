from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form.get('text')
    if text and len(text.split()) > 5:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    else:
        summary = "Please enter a longer piece of text to summarize."
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
