from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import ForeignKey

db = SQLAlchemy()

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }



class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    usuario: Mapped[str] = mapped_column(nullable=False)
    correo: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    foto: Mapped[str] = mapped_column(nullable=False)
    descripción: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    posts: Mapped[List["Post"]] = relationship(back_populates="user")
    seguidos: Mapped[List["Follower"]] = relationship(back_populates="user")
    seguidores: Mapped[List["Follower"]] = relationship(back_populates="user")
    coment: Mapped[List["Coment"]] = relationship(back_populates="coment")
    interaction: Mapped[List["Interaction"]] = relationship(back_populates="interaction")
    reciever: Mapped[List["Dm"]] = relationship(back_populates="user")
    sender: Mapped[List["Dm"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
    

class Coment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(nullable=False)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="coment")

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="coment")


    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
    

class Interaction(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    likes: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    saved: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    shrared: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="interaction")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="interaction")

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    publicacion: Mapped[str] = mapped_column(nullable=False)
    comentario: Mapped[str] = mapped_column(nullable=False)

    coment: Mapped[List["Coment"]] = relationship(back_populates="post")
    
    interaction: Mapped[List["Interaction"]] = relationship(back_populates="post")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts")


    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
    

class Dm(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    mensaje: Mapped[str] = mapped_column(nullable=False)
    
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="dm")

    receiver_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="dm")

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    seguido_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="seguidos")
    
    seguidor_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="seguidores")


    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }