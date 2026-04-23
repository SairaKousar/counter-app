from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Alphabet Counter</h2>
        <form action="/count">
            <input name="word" placeholder="Enter word">
            <button type="submit">Count</button>
        </form>
    '''

@app.route('/count')
def count():
    word = request.args.get('word', '')
    return f"Length: {len(word)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))