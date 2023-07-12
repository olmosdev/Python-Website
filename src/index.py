from flask import Flask, render_template

# Indicating this is the main file that will run the application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Is this the main file and not a module? Run this with "python index.py"
if __name__ == '__main__':
    app.run(debug=True)