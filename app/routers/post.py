from fastapi import FastAPI, Response,status,HTTPException, Depends, APIRouter
from .. import models,schemas,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional,List
from sqlalchemy import func

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""): #getting all posts
    # cursor.execute("""SELECT * FROM posts """)
    # posts=cursor.fetchall()
    # post=db.query(models.Post).filter(models.Post.owner_id ==current_user.id).all() this is when you want to get only post which the login user have available
    # post=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all() # this will get us all post but upper will get only post which loggedin user have psoted, .contains looks for the word in the database
    # results=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).all()
    # print(results)
    resuls = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return resuls

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post) #here we have used Post class to validate, it will do validation on its own
def createpost(post:schemas.PostCreate, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)): #creating a post
    
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,
    #         (post.title,post.content,post.published)) #here %s are the values that get passed to the database
    # new_post=cursor.fetchone()
    # conn.commit() #while working with postgrec we need to commit to make the date change i.e to update the data
    new_post=models.Post(**post.dict()) #what **post.dict() does is it convert all the data came from frontend and automatically saves to the variable that requires, we do not need to enter them manually
    new_post.owner_id=current_user.id
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.PostOut) #id is called path parameters
def get_post(id: int,db:Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)): #getting a post
    post=db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()    
    if not (post):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id=%s returning *""",(id,))
    # del_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post_query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} doesnot exist")
    if post.owner_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,id,))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesnot exist in datavbase")
    
    if post.owner_id!=current_user.id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()