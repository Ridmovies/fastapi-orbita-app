from sqladmin import ModelView

from src.posts.models import Post


class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.content]


# class BookingAdmin(ModelView, model=Booking):
#     column_list = "__all__"
