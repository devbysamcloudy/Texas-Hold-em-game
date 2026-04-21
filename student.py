from flask import Flask, jsonify
# from prisma import Prisma
# from app import create_app
from flask import Blueprint




# app = create_app()

students_bp = Blueprint('students', __name__)


# app = Flask(__name__)

@students_bp.route('/', methods=['GET'])
async def list_Students():
    return jsonify({'message': 'List of students'})


    # prisma = Prisma()
    # await prisma.connect()













    
    # user = await prisma.users.find_first()

    # student_dict = user.model_dump()
    # prisma.disconnect()

@students_bp.route('/add', methods=['POST'])
async def add_Student():
    return jsonify({'message': 'Student added successfully'})

    # prisma = Prisma()
    # await prisma.connect()
    # user = await prisma.users.create(
    #     data={
    #         'name': 'John Doe',
    #         'email': 'john.doe@example.com'
    #     }
    # )
    # prisma.disconnect()

    # return jsonify(user.model_dump()),201   

@students_bp.route('/<int:student_id>', methods=['GET'])
async def get_Student(student_id):
    return jsonify({'message': f'Student with ID {student_id} retrieved successfully'})

@students_bp.route('/del/<int:student_id>', methods=['DELETE'])
async def delete_Student(student_id):
    return jsonify({'message': f'Student with ID {student_id} deleted successfully'})



