from django.urls import path
from galeria.views import index, blog, post, about,store, login

urlpatterns = [
    path("", index, name='home'),
    path('blog', blog, name='blog'),
    path('post/<int:post_id>', post, name= 'post'),
    path('about', about, name='about'),
    path('store', store, name= 'store' ),
    path('login', login, name='login'),
]