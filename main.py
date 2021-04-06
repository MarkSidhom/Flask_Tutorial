from flask import Flask , render_template



app = Flask(__name__)

#The root page of MarkS application
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


#The about page of MarkS application
@app.route('/about')
def about():
    return render_template('about.html')