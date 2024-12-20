#03-11-24
# from flask import Flask,request,redirect,url_for,render_template
# app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# app.run(debug=True)


#04-11-24
# from flask import Flask,request,redirect,url_for,render_template
# app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('welcome.html')
# @app.route('/create',methods=['GET','POST'])                          #to accept all vlaues
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#     return render_template('create.html')
# app.run(debug=True,use_reloader=True)


#05-12-24
# gyla exxd uayq asdz
# from flask import Flask,request,redirect,url_for,render_template
# from otp import genotp
# from cmail import sendmail
# app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('welcome.html')
# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         # print(genotp())
#         gotp=genotp()
#         subject=f'otp for Simple Notes App'
#         body=f'Verify email by using the otp {gotp}'
#         sendmail(to=uemail,subject=subject,body=body)
#         return 'mail sent'
#     return render_template('create.html')
# app.run(debug=True,use_reloader=True)


#06-12-24
# from flask import Flask,request,redirect,url_for,render_template,flash
# from otp import genotp
# from cmail import sendmail
# app=Flask(__name__)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')
# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         # print(genotp())
#         gotp=genotp()
#         subject=f'otp for Simple Notes App'
#         body=f'Verify email by using the otp {gotp}'
#         sendmail(to=uemail,subject=subject,body=body)
#         flash('OTP has sent to your email')
#         return redirect(url_for('otp',gotp=gotp))
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         if uotp==gotp:
#             return redirect(url_for('login'))
#         else:
#             return 'otp was wrong pls register again'
#     return render_template('otp.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')                   #otp url should not be seen so we use its dangerous
# app.run(debug=True,use_reloader=True)


#07-12-24   &  #10-12-24
# from flask import Flask,request,redirect,url_for,render_template,flash
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')
# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']

#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 return 'otp was wrong pls register again'
#     return render_template('otp.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')                  
# app.run(debug=True,use_reloader=True)


#11-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 
               
# app.run(debug=True,use_reloader=True)



#12-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask session import Session 
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 
# @app.route('/forgotpass')
# def forgotpass():
#     return render_template('forgotpass.html')
# @app.route('/addnotes')
# def addnotes():
#     return render_template('addnotes.html')
# @app.route('/viewallnotes')
# def viewallnotes():
#     return render_template('viewallnotes.html')
               
# app.run(debug=True,use_reloader=True)



#13-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash,session
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask_session import Session 
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.config['SESSION_TYPE']="filesystem"
# Session(app)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 session['users']=uemail
#                 print(session)
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 

# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     return render_template('add_notes.html')

# # @app.route('/forgotpass')
# # def forgotpass():
# #     return render_template('forgotpass.html')
# # @app.route('/addnotes')
# # def addnotes():
# #     return render_template('add_notes.html')
# # @app.route('/viewallnotes')
# # def viewallnotes():
# #     return render_template('viewallnotes.html')
               
# app.run(debug=True,use_reloader=True)



#14-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash,session
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask_session import Session 
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.config['SESSION_TYPE']="filesystem"
# Session(app)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 session['users']=uemail
#                 print(session)
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 

# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     if request.method=='POST':
#         title=request.form['title']
#         description=request.form['desc']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone()
#         if uid:
#             try:
#                 cursor.execute('insert into notes(title,description,userid) values(%s,%s,%s)',[title,description,uid[0]])
#                 mydb.commit()
#                 cursor.close()
#             except Exception as e:
#                 print(e)
#                 flash('Duplicate title entry')
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('Notes added successfully')
#                 return redirect(url_for('dashboard'))
#         else:
#             return 'Something went wrong to fetch uid'
#     return render_template('add_notes.html')

# @app.route('/viewallnotes')
# def viewallnotes():
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone() 
#         cursor.execute('select nid,title,created_at from notes where userid=%s',[uid[0]])
#         notesdata=cursor.fetchall()  #  1  dfgh   cvb         2024-12-14 17:34:58      5      #2  PYTHON FLEXIBLE    2024-12-14 17:39:58      5      #3  Java   OOP         2024-12-14 18:03:40      5 
#     except Exception as e:
#         print(e)
#         flash('No data found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('viewallnotes.html',notesdata=notesdata)        
# app.run(debug=True,use_reloader=True)



#16-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash,session
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask_session import Session 
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.config['SESSION_TYPE']="filesystem"
# Session(app)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 session['users']=uemail
#                 print(session)
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 

# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     if request.method=='POST':
#         title=request.form['title']
#         description=request.form['desc']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone()
#         if uid:
#             try:
#                 cursor.execute('insert into notes(title,description,userid) values(%s,%s,%s)',[title,description,uid[0]])
#                 mydb.commit()
#                 cursor.close()
#             except Exception as e:
#                 print(e)
#                 flash('Duplicate title entry')
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('Notes added successfully')
#                 return redirect(url_for('dashboard'))
#         else:
#             return 'Something went wrong to fetch uid'
#     return render_template('add_notes.html')

# @app.route('/viewallnotes')
# def viewallnotes():
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone() 
#         cursor.execute('select nid,title,created_at from notes where userid=%s',[uid[0]])
#         notesdata=cursor.fetchall()  #  1  dfgh   cvb         2024-12-14 17:34:58      5      #2  PYTHON FLEXIBLE    2024-12-14 17:39:58      5      #3  Java   OOP         2024-12-14 18:03:40      5 
#     except Exception as e:
#         print(e)
#         flash('No data found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('viewallnotes.html',notesdata=notesdata)    


# @app.route('/readnotes/<nid>')    
# def readnotes(nid):
#     try:

#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select * from notes where nid=%s',[nid])
#         notesdata=cursor.fetchone()    #  1, 'dfgh', 'cvb', 2024-12-14 17:34:58 .....    
#         cursor.close() 
#     except Exception as e:
#         print(e)
#         flash('Notes not found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('readnotes.html',notesdata=notesdata)
    

# @app.route('/updatenotes/<nid>',methods=['GET','POST'])
# def updatenotes(nid):
#     cursor=mydb.cursor(buffered=True)
#     cursor.execute('select * from notes where nid=%s',[nid])
#     notesdata=cursor.fetchone()
#     if request.method=='POST':
#         title=request.form['title']
#         content=request.form['desc']
#         cursor.execute('update notes set title=%s,description=%s where nid=%s',[title,content,nid])
#         mydb.commit()
#         flash('notes updated successfully')
#         return redirect(url_for('readnotes',nid=nid))
#     return render_template('updatenotes.html',notesdata=notesdata)

# @app.route('/delete/<nid>')
# def delete(nid):
#     cursor=mydb.cursor(buffered=True)
#     cursor.execute('delete from notes where nid=%s',[nid])
#     mydb.commit()
#     flash('notes deleted successfully')
#     return redirect(url_for('viewallnotes'))
# app.run(debug=True,use_reloader=True)



#17-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash,session
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask_session import Session 
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.config['SESSION_TYPE']="filesystem"
# Session(app)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 session['users']=uemail
#                 print(session)
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 

# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     if request.method=='POST':
#         title=request.form['title']
#         description=request.form['desc']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone()
#         if uid:
#             try:
#                 cursor.execute('insert into notes(title,description,userid) values(%s,%s,%s)',[title,description,uid[0]])
#                 mydb.commit()
#                 cursor.close()
#             except Exception as e:
#                 print(e)
#                 flash('Duplicate title entry')
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('Notes added successfully')
#                 return redirect(url_for('dashboard'))
#         else:
#             return 'Something went wrong to fetch uid'
#     return render_template('add_notes.html')

# @app.route('/viewallnotes')
# def viewallnotes():
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone() 
#         cursor.execute('select nid,title,created_at from notes where userid=%s',[uid[0]])
#         notesdata=cursor.fetchall()  #  1  dfgh   cvb         2024-12-14 17:34:58      5      #2  PYTHON FLEXIBLE    2024-12-14 17:39:58      5      #3  Java   OOP         2024-12-14 18:03:40      5 
#     except Exception as e:
#         print(e)
#         flash('No data found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('viewallnotes.html',notesdata=notesdata)    


# @app.route('/readnotes/<nid>')    
# def readnotes(nid):
#     try:

#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select * from notes where nid=%s',[nid])
#         notesdata=cursor.fetchone()    #  1, 'dfgh', 'cvb', 2024-12-14 17:34:58 .....    
#         cursor.close() 
#     except Exception as e:
#         print(e)
#         flash('Notes not found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('readnotes.html',notesdata=notesdata)
    

# @app.route('/updatenotes/<nid>',methods=['GET','POST'])
# def updatenotes(nid):
#     cursor=mydb.cursor(buffered=True)
#     cursor.execute('select * from notes where nid=%s',[nid])
#     notesdata=cursor.fetchone()
#     if request.method=='POST':
#         title=request.form['title']
#         content=request.form['desc']
#         cursor.execute('update notes set title=%s,description=%s where nid=%s',[title,content,nid])
#         mydb.commit()
#         flash('notes updated successfully')
#         return redirect(url_for('readnotes',nid=nid))
#     return render_template('updatenotes.html',notesdata=notesdata)

# @app.route('/deletenotes/<nid>')
# def deletenotes(nid):
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('delete from notes where nid=%s',[nid])
#         mydb.commit()
#     except Exception as e:
#         print(e)
#         flash('notes not found')
#         return redirect(url_for('dashboard'))
#     else:
#         flash('notes delted successfully')
#         return redirect(url_for('viewallnotes'))
    
# @app.route('/uploadfile',methods=['GET','POST'])
# def uploadfile():
#     try:
#         if request.method=='POST':
#             filedata=request.files['file']
#             print(filedata.filename)  #filedata.filename-->only filename will come;filedata.filename.read()
#             # f=open(filedata.filename,mode='r')
#             # print(f.read())
#             print(filedata.read())
#             return 'hi'
#     except Exception as e:
#         print(e)
#         flash('unable to upload file')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('fileupload.html')
# app.run(debug=True,use_reloader=True)



#18-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash,session,send_file
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask_session import Session 
# from io import BytesIO
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# app.config['SESSION_TYPE']="filesystem"
# Session(app)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         uemail=request.form['useremail']
#         password=request.form['psd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#         bdata=cursor.fetchone()
#         if bdata[0]==1:
#             cursor.execute('select password from users where useremail=%s',[uemail])
#             bpassword=cursor.fetchone()
#             if password==bpassword[0].decode('utf-8'):
#                 session['users']=uemail
#                 print(session)
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('password was wrong')
#                 return redirect(url_for('login'))
#         else:
#             flash('Email not registred plz register')
#             return redirect(url_for('create'))
#     return render_template('login.html')  

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html') 

# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     if request.method=='POST':
#         title=request.form['title']
#         description=request.form['desc']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone()
#         if uid:
#             try:
#                 cursor.execute('insert into notes(title,description,userid) values(%s,%s,%s)',[title,description,uid[0]])
#                 mydb.commit()
#                 cursor.close()
#             except Exception as e:
#                 print(e)
#                 flash('Duplicate title entry')
#                 return redirect(url_for('dashboard'))
#             else:
#                 flash('Notes added successfully')
#                 return redirect(url_for('dashboard'))
#         else:
#             return 'Something went wrong to fetch uid'
#     return render_template('add_notes.html')

# @app.route('/viewallnotes')
# def viewallnotes():
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone() 
#         cursor.execute('select nid,title,created_at from notes where userid=%s',[uid[0]])
#         notesdata=cursor.fetchall()  #  1  dfgh   cvb         2024-12-14 17:34:58      5      #2  PYTHON FLEXIBLE    2024-12-14 17:39:58      5      #3  Java   OOP         2024-12-14 18:03:40      5 
#     except Exception as e:
#         print(e)
#         flash('No data found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('viewallnotes.html',notesdata=notesdata)    


# @app.route('/readnotes/<nid>')    
# def readnotes(nid):
#     try:

#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select * from notes where nid=%s',[nid])
#         notesdata=cursor.fetchone()    #  1, 'dfgh', 'cvb', 2024-12-14 17:34:58 .....    
#         cursor.close() 
#     except Exception as e:
#         print(e)
#         flash('Notes not found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('readnotes.html',notesdata=notesdata)
    

# @app.route('/updatenotes/<nid>',methods=['GET','POST'])
# def updatenotes(nid):
#     cursor=mydb.cursor(buffered=True)
#     cursor.execute('select * from notes where nid=%s',[nid])
#     notesdata=cursor.fetchone()
#     if request.method=='POST':
#         title=request.form['title']
#         content=request.form['desc']
#         cursor.execute('update notes set title=%s,description=%s where nid=%s',[title,content,nid])
#         mydb.commit()
#         flash('notes updated successfully')
#         return redirect(url_for('readnotes',nid=nid))
#     return render_template('updatenotes.html',notesdata=notesdata)

# @app.route('/deletenotes/<nid>')
# def deletenotes(nid):
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('delete from notes where nid=%s',[nid])
#         mydb.commit()
#     except Exception as e:
#         print(e)
#         flash('notes not found')
#         return redirect(url_for('dashboard'))
#     else:
#         flash('notes delted successfully')
#         return redirect(url_for('viewallnotes'))
    
# @app.route('/uploadfile',methods=['GET','POST'])
# def uploadfile():
#     try:
#         if request.method=='POST':
#             filedata=request.files['file']
#             print(filedata)
#             print(filedata.filename)  #filedata.filename-->only filename will come;filedata.filename.read()
#             fdata=filedata.read()
#             filename=filedata.filename
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#             uid=cursor.fetchone()
#             cursor.execute('insert into file_data(filename,fdata,added_by) values(%s,%s,%s)',[filename,fdata,uid[0]])
#             mydb.commit()
#             cursor.close()
#             flash('file uploaded successfully')
#             return redirect(url_for('dashboard'))
#             # f=open(filedata.filename,mode='r')
#             # # print(f.read())
#             # print(filedata.read())
#             # return 'hi'
#     except Exception as e:
#         print(e)
#         flash('unable to upload file')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('fileupload.html')
    
# @app.route('/allfiles')
# def allfiles():
#     try:
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#         uid=cursor.fetchone()
#         cursor.execute('select fid,filename,created_at from file_data where added_by=%s',[uid[0]])
#         filesdata=cursor.fetchall()
#     except Exception as e:
#         print(e)
#         flash('No files found')
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('allfiles.html',filesdata=filesdata)
    
# @app.route('/viewfile/<fid>')
# def viewfile(fid):
#     try:

#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select filename,fdata from file_data where fid=%s',[fid])
#         filedata=cursor.fetchone()
#         bytes_data=BytesIO(filedata[1])
#         return send_file(bytes_data,download_name=filedata[0],as_attachment=False)
#     except Exception as e:
#         print(e)
#         flash("couldnt load file")
#         return redirect(url_for('dashboard'))    
        
# @app.route('/downloadfile/<fid>')
# def downloadfile(fid):
#     try:

#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select filename,fdata from file_data where fid=%s',[fid])
#         filedata=cursor.fetchone()
#         bytes_data=BytesIO(filedata[1])
#         return send_file(bytes_data,download_name=filedata[0],as_attachment=True)
#     except Exception as e:
#         print(e)
#         flash("couldnt load file")
#         return redirect(url_for('dashboard')) 
    
# @app.route('/deletefile/<fid>')
# def deletefile(fid):
#     try:
#         cursor = mydb.cursor(buffered=True)
#         cursor.execute('delete from file_data where fid=%s',[fid])
#         mydb.commit()
#         flash('File deleted successfully')
#     except Exception as e:
#         print(e)
#         flash('Error deleting file')
#         return redirect(url_for('dashboard'))
#     else:
#         return redirect(url_for('dashboard'))
# app.run(debug=True,use_reloader=True)



#19-12-24

# from flask import Flask,request,redirect,url_for,render_template,flash,session,send_file
# from otp import genotp
# from cmail import sendmail
# from token_1 import encode,decode
# import mysql.connector
# from flask_session import Session 
# from io import BytesIO
# import flask_excel as excel
# mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
# app=Flask(__name__)
# excel.init_excel(app)
# app.config['SESSION_TYPE']="filesystem"
# Session(app)
# app.secret_key='manohar@2024'

# @app.route('/')
# def home():
#     return render_template('welcome.html')

# @app.route('/create',methods=['GET','POST'])                          
# def create():
#     if request.method=='POST':
#         print(request.form)
#         uname=request.form['username']
#         uemail=request.form['email']
#         pwd=request.form['psd']
#         cpwd=request.form['cpsd']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(*) from users where useremail=%s',[uemail])
#         var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
#         print(var1)
#         if var1[0]==0:
#         # print(genotp())
#             gotp=genotp()
#             udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
#             subject=f'otp for Simple Notes App'
#             body=f'Verify email by using the otp {gotp}'
#             sendmail(to=uemail,subject=subject,body=body)
#             flash('OTP has sent to your email')
#             return redirect(url_for('otp',gotp=encode(data=udata)))
#         elif var1[0]>0:
#             flash('Email already Existed')
#             return 'Email already Existed'
#     return render_template('create.html')

# @app.route('/otp/<gotp>',methods=['GET','POST'])
# def otp(gotp):
#     if request.method=='POST':
#         uotp=request.form['otp']
#         try:
#             dotp=decode(gotp)
#         except Exception as e:
#             print(e)
#             return 'something went wrong'
#         else:
#             if uotp==dotp['otp']:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
#                 mydb.commit()
#                 cursor.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash('otp wrong')
#                 return redirect(url_for('create'))
#     return render_template('otp.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if not session.get('users'):           #to know whether particular user login,when go back and come it shows that user login only ..,it wont ask login again,,because user login data is stored..(Ex:Recent Apps)
#         if request.method=='POST':
#             uemail=request.form['useremail']
#             password=request.form['psd']
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#             bdata=cursor.fetchone()
#             if bdata[0]==1:
#                 cursor.execute('select password from users where useremail=%s',[uemail])
#                 bpassword=cursor.fetchone()
#                 if password==bpassword[0].decode('utf-8'):
#                     session['users']=uemail
#                     print(session)
#                     return redirect(url_for('dashboard'))
#                 else:
#                     flash('password was wrong')
#                     return redirect(url_for('login'))
#             else:
#                 flash('Email not registred plz register')
#                 return redirect(url_for('create'))
#         return render_template('login.html') 
#     else:
#         return redirect(url_for('dashboard')) 

# @app.route('/dashboard')
# def dashboard():
#     if session.get('users'):
#         return render_template('dashboard.html') 
#     else:
#         return redirect(url_for('login'))        #we are giving / and going ,,but not we must first login then only

# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     if session.get('users'):

#         if request.method=='POST':
#             title=request.form['title']
#             description=request.form['desc']
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#             uid=cursor.fetchone()
#             if uid:
#                 try:
#                     cursor.execute('insert into notes(title,description,userid) values(%s,%s,%s)',[title,description,uid[0]])
#                     mydb.commit()
#                     cursor.close()
#                 except Exception as e:
#                     print(e)
#                     flash('Duplicate title entry')
#                     return redirect(url_for('dashboard'))
#                 else:
#                     flash('Notes added successfully')
#                     return redirect(url_for('dashboard'))
#             else:
#                 return 'Something went wrong to fetch uid'
#         return render_template('add_notes.html')
#     else:
#         return redirect(url_for('login'))

# @app.route('/viewallnotes')
# def viewallnotes():
#     if session.get('users'):
#         try:
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#             uid=cursor.fetchone() 
#             cursor.execute('select nid,title,created_at from notes where userid=%s',[uid[0]])
#             notesdata=cursor.fetchall()  #  1  dfgh   cvb         2024-12-14 17:34:58      5      #2  PYTHON FLEXIBLE    2024-12-14 17:39:58      5      #3  Java   OOP         2024-12-14 18:03:40      5 
#         except Exception as e:
#             print(e)
#             flash('No data found')
#             return redirect(url_for('dashboard'))
#         else:
#             return render_template('viewallnotes.html',notesdata=notesdata)  
#     else:
#         return redirect(url_for('login'))  


# @app.route('/readnotes/<nid>')    
# def readnotes(nid):
#     if session.get('users'):
#         try:

#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select * from notes where nid=%s',[nid])
#             notesdata=cursor.fetchone()    #  1, 'dfgh', 'cvb', 2024-12-14 17:34:58 .....    
#             cursor.close() 
#         except Exception as e:
#             print(e)
#             flash('Notes not found')
#             return redirect(url_for('dashboard'))
#         else:
#             return render_template('readnotes.html',notesdata=notesdata)
#     else:
#          return redirect(url_for('login'))  

    

# @app.route('/updatenotes/<nid>',methods=['GET','POST'])
# def updatenotes(nid):
#     if session.get('users'):
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select * from notes where nid=%s',[nid])
#         notesdata=cursor.fetchone()
#         if request.method=='POST':
#             title=request.form['title']
#             content=request.form['desc']
#             cursor.execute('update notes set title=%s,description=%s where nid=%s',[title,content,nid])
#             mydb.commit()
#             flash('notes updated successfully')
#             return redirect(url_for('readnotes',nid=nid))
#         return render_template('updatenotes.html',notesdata=notesdata)
#     else:
#         return redirect(url_for('login')) 


# @app.route('/deletenotes/<nid>')
# def deletenotes(nid):
#     if session.get('users'):
#         try:
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('delete from notes where nid=%s',[nid])
#             mydb.commit()
#         except Exception as e:
#             print(e)
#             flash('notes not found')
#             return redirect(url_for('dashboard'))
#         else:
#             flash('notes delted successfully')
#             return redirect(url_for('viewallnotes'))
#     else:
#         return redirect(url_for('login'))

    
# @app.route('/uploadfile',methods=['GET','POST'])
# def uploadfile():
#     if session.get('users'):
#         try:
#             if request.method=='POST':
#                 filedata=request.files['file']
#                 print(filedata)
#                 print(filedata.filename)  #filedata.filename-->only filename will come;filedata.filename.read()
#                 fdata=filedata.read()
#                 filename=filedata.filename
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#                 uid=cursor.fetchone()
#                 cursor.execute('insert into file_data(filename,fdata,added_by) values(%s,%s,%s)',[filename,fdata,uid[0]])
#                 mydb.commit()
#                 cursor.close()
#                 flash('file uploaded successfully')
#                 return redirect(url_for('dashboard'))
#                 # f=open(filedata.filename,mode='r')
#                 # # print(f.read())
#                 # print(filedata.read())
#                 # return 'hi'
#         except Exception as e:
#             print(e)
#             flash('unable to upload file')
#             return redirect(url_for('dashboard'))
#         else:
#             return render_template('fileupload.html')
#     else:
#         return redirect(url_for('login'))
    
# @app.route('/allfiles')
# def allfiles():
#     if session.get('users'):
#         try:
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#             uid=cursor.fetchone()
#             cursor.execute('select fid,filename,created_at from file_data where added_by=%s',[uid[0]])
#             filesdata=cursor.fetchall()
#         except Exception as e:
#             print(e)
#             flash('No files found')
#             return redirect(url_for('dashboard'))
#         else:
#             return render_template('allfiles.html',filesdata=filesdata)
#     else:
#         return redirect(url_for('login'))
    
# @app.route('/viewfile/<fid>')
# def viewfile(fid):
#     if session.get('users'):
#         try:

#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select filename,fdata from file_data where fid=%s',[fid])
#             filedata=cursor.fetchone()
#             bytes_data=BytesIO(filedata[1])
#             return send_file(bytes_data,download_name=filedata[0],as_attachment=False)
#         except Exception as e:
#             print(e)
#             flash("couldnt load file")
#             return redirect(url_for('dashboard')) 
#     else:
#         return redirect(url_for('login'))   
        
# @app.route('/downloadfile/<fid>')
# def downloadfile(fid):
#     if session.get('users'):
#         try:

#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select filename,fdata from file_data where fid=%s',[fid])
#             filedata=cursor.fetchone()
#             bytes_data=BytesIO(filedata[1])
#             return send_file(bytes_data,download_name=filedata[0],as_attachment=True)
#         except Exception as e:
#             print(e)
#             flash("couldnt load file")
#             return redirect(url_for('dashboard'))
#     else:
#         return redirect(url_for('login'))
    
# @app.route('/deletefile/<fid>')
# def deletefile(fid):
#     if session.get('users'):
#         try:
#             cursor = mydb.cursor(buffered=True)
#             cursor.execute('delete from file_data where fid=%s',[fid])
#             mydb.commit()
#             flash('File deleted successfully')
#         except Exception as e:
#             print(e)
#             flash('Error deleting file')
#             return redirect(url_for('dashboard'))
#         else:
#             return redirect(url_for('dashboard'))
#     else:
#         return redirect(url_for('login'))



# @app.route('/logout')
# def logout():
#     if session.get('users'):
#         session.pop('users')
#         return redirect(url_for('login'))
#     else:
#         return redirect(url_for('login'))
    
# @app.route('/getexceldata')
# def getexceldata():
#         if session.get('users'):
#             try:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('select userid from users where useremail=%s',[session.get('users')])
#                 uid=cursor.fetchone() 
#                 cursor.execute('select nid,title,description,created_at from notes where userid=%s',[uid[0]])
#                 notesdata=cursor.fetchall()  
#             except Exception as e:
#                 print(e)
#                 flash('No data found')
#                 return redirect(url_for('dashboard'))
#             else:
#                 array_data=[list(i) for i in notesdata]           #list comprehension we used..,fro not writing many lines.
#                 columns=['nid','title','description','created_at']
#                 array_data.insert(0,columns)
#                 return excel.make_response_from_array(array_data,'xlsx',filename='notesdata')
#         else:
#             return redirect(url_for('login')) 

# app.run(debug=True,use_reloader=True)



#20-12-24

from flask import Flask,request,redirect,url_for,render_template,flash,session,send_file
from otp import genotp
from cmail import sendmail
from token_1 import encode,decode
import mysql.connector
from flask_session import Session 
from io import BytesIO
import flask_excel as excel
import re
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='snm')
app=Flask(__name__)
excel.init_excel(app)
app.config['SESSION_TYPE']="filesystem"
Session(app)
app.secret_key='manohar@2024'

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/create',methods=['GET','POST'])                          
def create():
    if request.method=='POST':
        print(request.form)
        uname=request.form['username']
        uemail=request.form['email']
        pwd=request.form['psd']
        cpwd=request.form['cpsd']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select count(*) from users where useremail=%s',[uemail])
        var1=cursor.fetchone() #(only one record)   #fetchall(table lo all records)
        print(var1)
        if var1[0]==0:
        # print(genotp())
            gotp=genotp()
            udata={'username':uname,'useremail':uemail,'password':pwd,'otp':gotp}
            subject=f'otp for Simple Notes App'
            body=f'Verify email by using the otp {gotp}'
            sendmail(to=uemail,subject=subject,body=body)
            flash('OTP has sent to your email')
            return redirect(url_for('otp',gotp=encode(data=udata)))
        elif var1[0]>0:
            flash('Email already Existed')
            return 'Email already Existed'
    return render_template('create.html')

@app.route('/otp/<gotp>',methods=['GET','POST'])
def otp(gotp):
    if request.method=='POST':
        uotp=request.form['otp']
        try:
            dotp=decode(gotp)
        except Exception as e:
            print(e)
            return 'something went wrong'
        else:
            if uotp==dotp['otp']:
                cursor=mydb.cursor(buffered=True)
                cursor.execute('insert into users(username,useremail,password)values(%s,%s,%s)',[dotp['username'],dotp['useremail'],dotp['password']])
                mydb.commit()
                cursor.close()
                return redirect(url_for('login'))
            else:
                flash('otp wrong')
                return redirect(url_for('create'))
    return render_template('otp.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if not session.get('users'):           #to know whether particular user login,when go back and come it shows that user login only ..,it wont ask login again,,because user login data is stored..(Ex:Recent Apps)
        if request.method=='POST':
            uemail=request.form['useremail']
            password=request.form['psd']
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
            bdata=cursor.fetchone()
            if bdata[0]==1:
                cursor.execute('select password from users where useremail=%s',[uemail])
                bpassword=cursor.fetchone()
                if password==bpassword[0].decode('utf-8'):
                    session['users']=uemail
                    print(session)
                    return redirect(url_for('dashboard'))
                else:
                    flash('password was wrong')
                    return redirect(url_for('login'))
            else:
                flash('Email not registred plz register')
                return redirect(url_for('create'))
        return render_template('login.html') 
    else:
        return redirect(url_for('dashboard')) 

@app.route('/dashboard')
def dashboard():
    if session.get('users'):
        return render_template('dashboard.html') 
    else:
        return redirect(url_for('login'))        #we are giving / and going ,,but not we must first login then only

@app.route('/addnotes',methods=['GET','POST'])
def addnotes():
    if session.get('users'):

        if request.method=='POST':
            title=request.form['title']
            description=request.form['desc']
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select userid from users where useremail=%s',[session.get('users')])
            uid=cursor.fetchone()
            if uid:
                try:
                    cursor.execute('insert into notes(title,description,userid) values(%s,%s,%s)',[title,description,uid[0]])
                    mydb.commit()
                    cursor.close()
                except Exception as e:
                    print(e)
                    flash('Duplicate title entry')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Notes added successfully')
                    return redirect(url_for('dashboard'))
            else:
                return 'Something went wrong to fetch uid'
        return render_template('add_notes.html')
    else:
        return redirect(url_for('login'))

@app.route('/viewallnotes')
def viewallnotes():
    if session.get('users'):
        try:
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select userid from users where useremail=%s',[session.get('users')])
            uid=cursor.fetchone() 
            cursor.execute('select nid,title,created_at from notes where userid=%s',[uid[0]])
            notesdata=cursor.fetchall()  #  1  dfgh   cvb         2024-12-14 17:34:58      5      #2  PYTHON FLEXIBLE    2024-12-14 17:39:58      5      #3  Java   OOP         2024-12-14 18:03:40      5 
        except Exception as e:
            print(e)
            flash('No data found')
            return redirect(url_for('dashboard'))
        else:
            return render_template('viewallnotes.html',notesdata=notesdata)  
    else:
        return redirect(url_for('login'))  


@app.route('/readnotes/<nid>')    
def readnotes(nid):
    if session.get('users'):
        try:

            cursor=mydb.cursor(buffered=True)
            cursor.execute('select * from notes where nid=%s',[nid])
            notesdata=cursor.fetchone()    #  1, 'dfgh', 'cvb', 2024-12-14 17:34:58 .....    
            cursor.close() 
        except Exception as e:
            print(e)
            flash('Notes not found')
            return redirect(url_for('dashboard'))
        else:
            return render_template('readnotes.html',notesdata=notesdata)
    else:
         return redirect(url_for('login'))  

    

@app.route('/updatenotes/<nid>',methods=['GET','POST'])
def updatenotes(nid):
    if session.get('users'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select * from notes where nid=%s',[nid])
        notesdata=cursor.fetchone()
        if request.method=='POST':
            title=request.form['title']
            content=request.form['desc']
            cursor.execute('update notes set title=%s,description=%s where nid=%s',[title,content,nid])
            mydb.commit()
            flash('notes updated successfully')
            return redirect(url_for('readnotes',nid=nid))
        return render_template('updatenotes.html',notesdata=notesdata)
    else:
        return redirect(url_for('login')) 


@app.route('/deletenotes/<nid>')
def deletenotes(nid):
    if session.get('users'):
        try:
            cursor=mydb.cursor(buffered=True)
            cursor.execute('delete from notes where nid=%s',[nid])
            mydb.commit()
        except Exception as e:
            print(e)
            flash('notes not found')
            return redirect(url_for('dashboard'))
        else:
            flash('notes delted successfully')
            return redirect(url_for('viewallnotes'))
    else:
        return redirect(url_for('login'))

    
@app.route('/uploadfile',methods=['GET','POST'])
def uploadfile():
    if session.get('users'):
        try:
            if request.method=='POST':
                filedata=request.files['file']
                print(filedata)
                print(filedata.filename)  #filedata.filename-->only filename will come;filedata.filename.read()
                fdata=filedata.read()
                filename=filedata.filename
                cursor=mydb.cursor(buffered=True)
                cursor.execute('select userid from users where useremail=%s',[session.get('users')])
                uid=cursor.fetchone()
                cursor.execute('insert into file_data(filename,fdata,added_by) values(%s,%s,%s)',[filename,fdata,uid[0]])
                mydb.commit()
                cursor.close()
                flash('file uploaded successfully')
                return redirect(url_for('dashboard'))
                # f=open(filedata.filename,mode='r')
                # # print(f.read())
                # print(filedata.read())
                # return 'hi'
        except Exception as e:
            print(e)
            flash('unable to upload file')
            return redirect(url_for('dashboard'))
        else:
            return render_template('fileupload.html')
    else:
        return redirect(url_for('login'))
    
@app.route('/allfiles')
def allfiles():
    if session.get('users'):
        try:
            cursor=mydb.cursor(buffered=True)
            cursor.execute('select userid from users where useremail=%s',[session.get('users')])
            uid=cursor.fetchone()
            cursor.execute('select fid,filename,created_at from file_data where added_by=%s',[uid[0]])
            filesdata=cursor.fetchall()
        except Exception as e:
            print(e)
            flash('No files found')
            return redirect(url_for('dashboard'))
        else:
            return render_template('allfiles.html',filesdata=filesdata)
    else:
        return redirect(url_for('login'))
    
@app.route('/viewfile/<fid>')
def viewfile(fid):
    if session.get('users'):
        try:

            cursor=mydb.cursor(buffered=True)
            cursor.execute('select filename,fdata from file_data where fid=%s',[fid])
            filedata=cursor.fetchone()
            bytes_data=BytesIO(filedata[1])
            return send_file(bytes_data,download_name=filedata[0],as_attachment=False)
        except Exception as e:
            print(e)
            flash("couldnt load file")
            return redirect(url_for('dashboard')) 
    else:
        return redirect(url_for('login'))   
        
@app.route('/downloadfile/<fid>')
def downloadfile(fid):
    if session.get('users'):
        try:

            cursor=mydb.cursor(buffered=True)
            cursor.execute('select filename,fdata from file_data where fid=%s',[fid])
            filedata=cursor.fetchone()
            bytes_data=BytesIO(filedata[1])
            return send_file(bytes_data,download_name=filedata[0],as_attachment=True)
        except Exception as e:
            print(e)
            flash("couldnt load file")
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))
    
@app.route('/deletefile/<fid>')
def deletefile(fid):
    if session.get('users'):
        try:
            cursor = mydb.cursor(buffered=True)
            cursor.execute('delete from file_data where fid=%s',[fid])
            mydb.commit()
            flash('File deleted successfully')
        except Exception as e:
            print(e)
            flash('Error deleting file')
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    if session.get('users'):
        session.pop('users')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/getexceldata')
def getexceldata():
        if session.get('users'):
            try:
                cursor=mydb.cursor(buffered=True)
                cursor.execute('select userid from users where useremail=%s',[session.get('users')])
                uid=cursor.fetchone() 
                cursor.execute('select nid,title,description,created_at from notes where userid=%s',[uid[0]])
                notesdata=cursor.fetchall()  
            except Exception as e:
                print(e)
                flash('No data found')
                return redirect(url_for('dashboard'))
            else:
                array_data=[list(i) for i in notesdata]           #list comprehension we used..,fro not writing many lines.
                columns=['nid','title','description','created_at']
                array_data.insert(0,columns)
                return excel.make_response_from_array(array_data,'xlsx',filename='notesdata')
        else:
            return redirect(url_for('login')) 

@app.route('/search',methods=['GET','POST'])
def search():
    if session.get('users'):
        if request.method=='POST':
            search=request.form['searchdata']
            strg=['A-Za-z0-9']
            pattern=re.compile(f'^{strg}',re.IGNORECASE)
            if (pattern.match(search)):
                cursor=mydb.cursor(buffered=True)
                cursor.execute('select * from notes where nid like %s or title like %s or description like %s or created_at like %s',[search+'%',search+'%',search+'%',search+'%'])
                sdata=cursor.fetchall()
                cursor.close()
                return render_template('dashboard.html',sdata=sdata)
            else:
                flash('No data found')
                return redirect(url_for('dashboard'))
        else:
            return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

app.run(debug=True,use_reloader=True)


                 

