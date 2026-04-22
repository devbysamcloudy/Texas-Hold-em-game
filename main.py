from app import create_app
from app import auth_bp   
from dotenv import load_dotenv
import os

load_dotenv()
app = create_app()

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)