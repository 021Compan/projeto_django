from django.contrib import admin
from galeria.models import Post, Hero, Hero_membro, Membro, Evento, Produto

class listando_post(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')

class lista(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')

admin.site.register(Post, listando_post)
admin.site.register(Hero)
admin.site.register(Hero_membro, lista)
admin.site.register(Membro, lista)
admin.site.register(Evento,lista)
admin.site.register(Produto,lista)