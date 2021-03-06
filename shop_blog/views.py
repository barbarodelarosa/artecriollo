import random
from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.mail import send_mail
from artecriollo.settings import EMAIL_HOST_USER
from .models import Post,Categoria,RedesSociales,Web,Suscriptor
from .utils import *
from .forms import ContactoForm

class Inicio(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

     
        categorias = list(Categoria.objects.filter(
                estado = True,
                post__estado=True,
                post__publicado = True,
                ).values_list('id',flat = True))
        


        categoria1 = random.choice(categorias)
        categorias.remove(categoria1)

        categoria2 = random.choice(categorias)
        categorias.remove(categoria2)
        
        try:
            post_categoria1 = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(id = categoria1)
                                ).latest('fecha_publicacion')
        except:
            post_categoria1 = None

        try:
            post_categoria2 = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(id = categoria2)
                            ).latest('fecha_publicacion')
        except:
            post_categoria2 = None

        if post_categoria1==post_categoria2:
            categoria2 = random.choice(categorias)
            try:
                post_categoria2 = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(id = categoria2)
                                ).latest('fecha_publicacion')
            except:
                post_categoria2 = None



        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_categoria1':post_categoria1,
            'post_categoria2':post_categoria2,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
        }

        return render(request,'blog/index.html',contexto)

class Listado(ListView):

    def get(self,request,slug,*args,**kwargs):
        contexto = generarCategoria(request,slug)
        return render(request,'blog/categoria.html',contexto)

class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'blog/contacto.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_blog:index')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'blog/contacto.html',contexto)

class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        contexto = {
            'post':post,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
        }
        return render(request,'blog/post.html',contexto)

class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE A BLOG.DEV!'
        mensaje = 'Te haz suscrito exitosamente a Blog.Dev, Gracias por tu preferencia!!!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('shop_blog:index')
