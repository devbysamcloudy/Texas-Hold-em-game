from flask import Blueprint, request, jsonify
from app.bcrypt import bcrypt
from app.prisma import with_prisma
from prisma import Prisma
from app.jwt import generate_token


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
async def register():
    prisma  = Prisma()
    await prisma.connect()
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username:
        return jsonify({"custom": True, "message": "Username is required"}), 400
    
    if not email:
        return jsonify({"custom": True, "message": "Email is required"}), 400
    

    if not password:
        return jsonify({"custom": True, "message": "Password is required"}), 400
    

    if len(password) < 6:
        return jsonify({"custom": True, "message": "Password must be at least 6 characters long"}), 400
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    print("User email is ", email)
    print("User password is ", password)
    print("Username is ", username)
    print("Hashed password is ", hashed_password)

    player_exists= await prisma.player.find_unique(
        where={
            "email": email
            }
            )
    
    if player_exists:
        return jsonify({"custom": True, "message": "Email already exists"}), 400
    
    transaction = None

    async with prisma.tx() as tx:
        new_player = await tx.player.create(
            data={
                "name": username,
                "email": email
            }
        )

        new_player = await tx.player_password.create(
            data={
                "player_id": new_player.id,
                "password": hashed_password
            }
        )

        transaction = new_player

        return jsonify(transaction.model_dump())
    
@auth_bp.route('/login', methods=['POST'])
async def login(prisma):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email:
        return jsonify({"custom": True, "message": "Email is required"}), 400
    
    if not password:
        return jsonify({"custom": True, "message": "Password is required"}), 400
    
    if email == request.get_json().get('email') and password == request.get_json().get('password'):
        return jsonify({"message": "Invalid credentials"}), 401
    
    player = await prisma.player.find_unique(
        where={
            "email": email
        },
        include={
            "password": True
        }
    )
    if not player:
        return jsonify({"message": "Invalid credentials"}), 401
    player_password = player.password.password

    if not player_password:
        return jsonify({"message": "Invalid credentials"}), 401
    
    is_valid = bcrypt.check_password_hash(
        player_password, 
        password
        )
    if not is_valid:
        return jsonify({"message": "Invalid email or password"}), 401
    
    token = generate_token(id = player.id)
    return jsonify({"player": player.model_dump(), "token": token})
    


    return jsonify({"message": "Login successful"})
    
    