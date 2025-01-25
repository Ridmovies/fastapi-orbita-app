from sqladmin import ModelView

from src.posts.models import Post
from src.tanks.model import Branch, Tank


class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.content]


class BranchAdmin(ModelView, model=Branch):
    column_list = "__all__"

class TankAdmin(ModelView, model=Tank):
    column_list = "__all__"
