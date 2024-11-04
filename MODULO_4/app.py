from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"

login_Manager = LoginManager()
db.init_app(app)
login_Manager.init_app(app)
login_Manager.login_view = 'login'

with app.app_context():
    db.create_all()

@login_Manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def authenticate_user(username, password):
    """
    Função para verificar as credenciais do usuário.
    Retorna o usuário se as credenciais estiverem corretas; caso contrário, retorna None.
    """
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    print(f"Dados recebidos: {data}")  # Debugging: verificar o JSON recebido

    if username and password:
        user = authenticate_user(username, password)  # Chama a função de autenticação

        if user:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso!"})

    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

@app.route('/user', methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User(username=username, password=password, role='user')
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso!"})

    return jsonify({"message": "Dados invalidos"}), 400

@app.route('/user/<int:id_user>', methods=["GET"])
def read_user(id_user):
    user = User.query.get(id_user)

    if user:
        return {"username": user.username}
    return jsonify ({"message": "Usuario nao encontrado"}), 404

@app.route('/user/<int:id_user>', methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)

    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify({"message": f"Usuario {id_user} atualizado com sucesso!"})

    return jsonify ({"message": "Usuario nao encontrado."}), 404


@app.route('/user/<int:id_user>', methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)
    if id_user ==current_user.id:
        return jsonify({"message": "Deleçao nao permetida"}), 403
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuario {id_user} foi deletado"})

    return jsonify ({"message": "Usuario nao encontrado"}), 404

if __name__ == '__main__':
        app.run(debug=True)
