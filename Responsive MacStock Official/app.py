from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/macstock'
db = SQLAlchemy(app)


class Contact(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(200), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search")
def search():
    return render_template('search.html')    

@app.route("/post1")
def post1():
    return render_template('post.html')    

@app.route("/post2")
def post2():
    return render_template('post1.html')  

@app.route("/post3")
def post3():
    return render_template('post2.html')  

@app.route("/post4")
def post4():
    return render_template('post3.html')  

@app.route("/post5")
def post5():
    return render_template('post4.html')  

@app.route("/post6")
def post6():
    return render_template('post5.html')      

@app.route("/posts")
def posts():
    return render_template('posts.html')   

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        entry = Contact(name=name, message=message, email=email )
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')


app.run(debug=True)


