from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from werkzeug import secure_filename
import json
import os
import math

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
    
local_server = True    
    
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params["upload_location"]

app.config.update(
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = '465',
        MAIL_USE_SSL = True,
        MAIL_USERNAME =params["gmail-user"],
        MAIL_PASSWORD = params["gmail-password"],
        )
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
    
    
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)



class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(21), unique=True, nullable=False)
    content = db.Column(db.String(120),unique = False, nullable=False)
    tagline = db.Column(db.String(120),unique = False, nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)
    
@app.route('/')
def index():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params["number_of_posts"]))
    #[0:params["number_of_posts"]]
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params["number_of_posts"]) : (page-1)*int(params["number_of_posts"]) + int(params["number_of_posts"])] 
    #pagination logic
    #first
    if(page == 1):
        prev = "#"
        nextp = "/?page=" + str(page+1)
    elif(page == last):
        prev = "/?page=" + str(page-1)
        nextp =  "#"
    else:
        prev = "/?page=" + str(page-1)
        nextp = "/?page=" + str(page+1)
        
    
    
    return render_template('index.html',params = params,posts = posts,prev=prev,nextp=nextp)

#@app.route('/')
#def home():
#    posts = Posts.query.filter_by().all()[0:params["number_of_posts"]]
#    return render_template('index.html',params = params,posts = posts)

@app.route('/post/<string:post_slug>', methods = ["GET"])
def post_route(post_slug):
    post = Posts.query.filter_by(slug= post_slug).first()
    
    return render_template('post.html',params = params,post = post)


@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    
    if 'user' in session and session['user'] ==  params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html',params = params,posts = posts)
    
    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        
        if(username == params['admin_user'] and userpass == params['admin_password']):
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html',params = params,posts = posts)    
    else:
        return render_template('login.html',params = params)


@app.route('/about')
def about():
    return render_template('about.html',params = params)

@app.route('/edit/<string:sno>',methods=["GET","POST"])
def edit(sno):
    if 'user' in session and session['user'] ==  params['admin_user']:
        if request.method == "POST":
            title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            if sno == '0':
                entry = Posts(title = title,slug = slug,content = content, tagline=tline,img_file = img_file,date = date)
                db.session.add(entry)
                db.session.commit()
                #return redirect('/dashboard')
            
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.tagline = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                
                db.session.commit()
                
                return redirect('/edit/' + sno)
                
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params = params,post = post,sno=sno)
    
@app.route('/delete/<string:sno>',methods=["GET","POST"])
def delete(sno):
    if 'user' in session and session['user'] ==  params['admin_user']:
        post = Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
        
        return redirect("/dashboard")
                
@app.route('/uploader',methods=["GET","POST"])
def uploader():
    if 'user' in session and session['user'] ==  params['admin_user']:
        if request.method == "POST":
            f = request.files['file1']  
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded Successfully"
        
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')



@app.route('/add',methods=["GET","POST"])
def add():
    if 'user' in session and session['user'] ==  params['admin_user']:
        if request.method == "POST":
            title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            
            entry = Posts(title = title,slug = slug,content = content, tagline=tline,img_file = img_file,date = date)
            db.session.add(entry)
            db.session.commit()
            
            
    
        return render_template('add.html',params = params)
    

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        #add entry to the database
        name = request.form.get('name')
        email = request.form.get('email')
        phone_num= request.form.get('phone_num')
        mes= request.form.get('mes')
        
        entry = Contacts(name = name, phone_num = phone_num, mes = mes, email = email,date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New Message From : " + name,
                          sender = email,
                          recipients = [params["gmail-user"]],
                          body = mes + '\n' + phone_num)
         
    return render_template('contact.html',params = params)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001)