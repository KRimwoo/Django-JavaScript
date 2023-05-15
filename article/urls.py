from django.urls import path
from .views import new, detail, edit, destroy,post_comment,post_like,destroy_comment

app_name = 'article'

urlpatterns = [
    path("new/", new, name="new"),
    path("<int:id>", detail, name="detail"),
    path("edit/<int:id>", edit, name="edit"),
    path("destroy/<int:id>", destroy, name="destroy"),
    path("new_comments/<int:id>", post_comment, name="new_comment"),
    path("create/<int:id>", destroy_comment, name="create_comment"),
    path("like/<int:id>", post_like, name="likes"),
]