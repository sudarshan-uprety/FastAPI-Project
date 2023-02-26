from fastapi import APIRouter, Depends,status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from .. import database,schemas,models,utils,oauth2

router=APIRouter(tags=["Authentication"])

@router.post('/login',response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm=Depends() ,db:session=Depends(database.get_db)):
    #username= this form automatically ask fro username(email) and password
    #passsword=
    user = db.query(models.User).filter(models.User.email==user_credentials.username).first() #the reason we use user_credential.username is because OAuth2PasswordRequestForm says username instead of
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    
    access_token=oauth2.create_access_token(data={'user_id':user.id})
    # create a token
    # return token
    return {"access_token":access_token,"token_type":"bearer"}