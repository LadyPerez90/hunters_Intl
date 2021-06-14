from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('create_post', views.create_post),
    path('add_comment/<int:id>', views.add_comment),
    path('like/<int:id>', views.like),
    path('user_profile/<int:id>', views.profile),
    path('edit_pg/<int:id>', views.edit_pg),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete_post),
    path('delete_comment/<int:id>', views.delete_comment),
    # path('upload', views.upload),
]