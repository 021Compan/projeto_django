from django.shortcuts import render,get_object_or_404
from galeria.models import Hero, Post, Hero_membro, Membro, Evento

def index (request):
    hero = Hero.objects.all()
    post = Post.objects.all()
    return render (request, 'galeria/index.html', {'chamada': post, 'hero': hero})

def about (request):
    hero = Hero_membro.objects.all()
    membro = Membro.objects.all()
    evento = Evento.objects.all()
    return render(request, 'galeria/about.html',{'hero-about': hero, 'nossa-equipe': membro, 'evento': evento})

def blog (request):
    post = Post.objects.all()
    return render(request, 'galeria/blog', {'conteudo': post})

def post (request, post_id):
    post = get_object_or_404(post, pk=post_id)
    return render(request, 'galeria/post', {'post': post})