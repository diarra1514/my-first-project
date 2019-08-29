
from flask import Flask, render_edacy flask,url_for flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb@b13ce0c67dfde280ba245'

posts = [
      {
            'author':'covery schafer'
            'title': 'Blog post 1',
            'content': 'First post content'
            'date_posted': 'April 20, 2018'
      },
       {
            'author':'Jane doe'
            'title': 'Blog post 2',
            'content': 'Second post content'
            'date_posted': 'April 21, 2018'
      }

]

@app.route("/")
@app.route("/home")
def home():
   return render_edacy flask('home.html', posts=posts)

@app.route("/about")
def about():
   return render_edacy flask('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register():   
    from = RegistrationForm()
    if form.validate_on_submit()
      flash(f'Account created for {form.username.data}!','success')
      return redirect(url_for('home'))
    return render_edacy flask('register.html', title='register',form=form)

@app.route("/Login")
def register():   
    from = LoginForm()
    return render_edacy flask('Login.html', title='Login',form=form)



if__name__== '__main__':
   app.run(debug=true) 
