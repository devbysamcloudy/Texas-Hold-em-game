from flask import Flask, jsonify
from prisma import Prisma




app = Flask(__name__)
@app.route('/students', methods=['GET'])
async def list_Students():
    prisma = Prisma()
    await prisma.connect()













    
    user = await prisma.users.find_first()

    student_dict = user.model_dump()
    prisma.disconnect()


    return jsonify(student_dict),200

if __name__ == '__main__':
    app.run(debug=True)


