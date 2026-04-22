import jwt
from datetime import datetime,timezone,timedelta
import os


SECRET_KEY=os.getenv("JWT_SECRET")
ALGORITHM="HS256"

def generate_token(id):

    now=datetime.now(timezone.utc)
    payload={
        "id":id,
        "exp":now+timedelta(hours=24),
        "iat":now
    }

    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)


def verify_token(token:str):
    try:
        decoded=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded
    except:
        return None
        