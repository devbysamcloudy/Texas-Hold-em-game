from dotenv import load_dotenv
from prisma import Prisma
from flask import Flask, jsonify,Blueprint
import asyncio

from student import students_bp

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(students_bp, url_prefix='/students')
    app.run(debug=True)
    