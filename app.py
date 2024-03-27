from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import LoginManager
from flask import flash



app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://duda:63524178@127.0.0.1:3306/login'

app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)


    def verify_password(self, password):
            return check_password_hash(self.password, password)


    def get_id(self):
        return str(self.iduser)  
        # Convertendo o ID para string


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('login'))  # Redireciona para a página de produtos após o login
        else:
            flash('Credenciais inválidas. Por favor, verifique seu email e senha e tente novamente.', 'error')
            return render_template('login.html')  # Redireciona de volta para a página de login em caso de falha no login
    return render_template('meses.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()  # Adiciona o commit para persistir as alterações no banco de dados
                                                                                                                                                    
    return render_template('register.html')




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html', current_user=current_user)



@app.route('/meses')
def meses():
    return render_template('meses.html')



@app.route('/janeiro')
def janeiro():
    return render_template('janeiro.html')


@app.route('/fevereiro')
def fevereiro():
    return render_template('fevereiro.html')


@app.route('/marco')
def marco():
    return render_template('marco.html')



@app.route('/abril')
def abril():
    return render_template('abril.html')



@app.route('/maio') 
def maio():
    return render_template('maio.html')



@app.route('/junho')
def junho():
    return render_template('junho.html')



@app.route('/julho')
def julho():
    return render_template('julho.html')



@app.route('/agosto')
def agosto():
    return render_template('agosto.html')



@app.route('/setembro') 
def setembro():
    return render_template('setembro.html')



@app.route('/outubro')
def outubro():
    return render_template('outubro.html')



@app.route('/novembro')
def novembro():
    return render_template('novembro.html')



@app.route('/dezembro')
def dezembro():
    return render_template('dezembro.html')










#fazer a aplicação rodar
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

