from flask import Flask, render_template, request
from text_summarizer import summarize_text  # Import the summarize_text function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        summarized_text = summarize_text(user_text)  # Call the summarize_text function
        return render_template('index.html', user_text=user_text, summarized_text=summarized_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)