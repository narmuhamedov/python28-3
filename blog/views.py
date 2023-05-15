from django.http import HttpResponse
from django.shortcuts import render
from . import models

#Первый вывод на джанго
def hello_view(request):
    return HttpResponse("Hello This is my first project Django")


#Список блогов на веб странице (логика отображения)
def blog_view(request):
    blog = models.Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})
