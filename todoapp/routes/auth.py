from flask import redirect,Blueprint,request,render_template,session,url_for
from ..extentions import db,create_access_token
from todoapp.models.user import User

import bcrypt
auth=Blueprint('auth',__name__)
@auth.route('/registration',methods=['GET','POST'])
def registration_page():
    if request.method=='POST':
        username= request.form['username']
        email = request.form['email']
        password = request.form['password']
        enc_password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        print('passtets=',password,",",enc_password)
        new_user=User(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('registration.html')


@auth.route('/', methods=['GET','POST'])
@auth.route('/login', methods=['GET','POST'])
def login_page():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter_by(email=email).first()
        print("testemail=",user,",",username,",",email,",",password)



        if not user:
            return render_template('login.html',login=False,msg=" User does not exist!")
        else:
            access_token=create_access_token(identity=username)
            print("accesstoken=",access_token)
            dict_user=user.to_dict()
            if dict_user['password']==password and dict_user['username']==username and dict_user['email'] == email:
                session['username'] = username
                return redirect(url_for('api.home_page')) 
            else:
                return render_template('login.html',login=False ,msg="Invalid credentials!")
    return render_template('login.html',login=True)
