from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from Blog.forms import PostBlog
from Blog.models import Blog
# Create your views here.

def inicio(request):
    
    return render(request, "Blog/inicio.html")

def home(request):
    
    return render(request, "Blog/inicio2.html")

def about(request):

    return render(request, "Blog/about.html")

def about2(request):

    return render(request, "Blog/about2.html")

def PostBlogs(request):

    if request.method == "POST":

        myPost = PostBlog(request.POST)

        print(myPost)
        
        if myPost.is_valid:

            info = myPost.cleaned_data

            blog = Blog(titulo=info["titulo"], cuerpo=info["cuerpo"], autor=info["autor"], fecha=info["fecha"], equipo=info["equipo"], jugador_actual=info["jugador_actual"])

            blog.save()

            return render(request, "Blog/pages.html")
    
    else:

        myPost = PostBlog()

    return render(request, "Blog/postblog.html", {"myPost":myPost})

class page(ListView):

    model = Blog

class pagedetail(DetailView):

    model = Blog

class updatepage(UpdateView):

    model = Blog
    success_url = "/Pages"
    fields = ["titulo", "cuerpo", "autor", "fecha", "equipo", "jugador_actual"]

class deletepage(DeleteView):

    model = Blog
    success_url = "/Pages"

def pageserror(request):
    
    return render(request, "Blog/pageserror.html")