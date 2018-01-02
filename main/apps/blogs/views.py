from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("list of blogs")

def new(request):
    return HttpResponse("add new blog")
    
def create(request):
    return redirect('/')

def show(request, blog_id):
    print blog_id
    return HttpResponse("display blog here)

def edit(request, blog_id):
    return HttpResponse("edit blog here")
    
def delete(request, blog_id):
    return redirect('/')
