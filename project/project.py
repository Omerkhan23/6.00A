from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pos.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Employee Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50))  # Cashier, Admin, etc.

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = Employee.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        token = create_access_token(identity=user.username)
        return jsonify(access_token=token, role=user.role)
    return jsonify({"msg": "Invalid credentials"}), 401

# Protected Route (Example)
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    return jsonify({"msg": "Welcome to the POS Dashboard!"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

