from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash(passsword:str):
    return pwd_context.hash(passsword)

def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password) #.verify will do the verification for use we do not need to do that and it will return if verified or not
