from flask import Flask,make_response,request,render_template,redirect,url_for
from form import LoginForm
app=Flask(__name__)
app.config['SECRET_KEY']='hardsecretkey'

@app.route("/")
def index():
    #name="Anu"
    context={
        "name":"marco",
        "text":"all is well"
    }
    return render_template('index.html',data=context)

@app.route("/contact")
def contacts():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

#dynamic URL routing
@app.route("/contact/<name>")
def user(name):
    return "<h1>welcome {}</h1>".format(name)

#flask cookies
@app.route("/setcookie")
def setCookie():
    response=make_response(" i have set the cookie")
    response.set_cookie("myapp","flask web development")
    return response

@app.route("/get")
def getCookie():
    myapp=request.cookies.get("myapp")
    return "cookie content is"+str(myapp)

#custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')

@app.route('/login',methods=['GET','POST'])
def  Login():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html',title='Login',form=form)

if __name__=="__main__":
    app.run(debug=True)