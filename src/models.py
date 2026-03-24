from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

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

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
    

class Coment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(primary_key=True)


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
    user_id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    publicacion: Mapped[str] = mapped_column(nullable=False)
    comentario: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(primary_key=True)


    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
    

class Dm(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    mensaje: Mapped[str] = mapped_column(nullable=False)
    reciever_id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(primary_key=True)


    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Followers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    seguido_id: Mapped[int] = mapped_column(primary_key=True)
    seguidores_id: Mapped[int] = mapped_column(primary_key=True)


    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }