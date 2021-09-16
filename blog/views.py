from django.shortcuts import render,get_object_or_404
from .models import Blog,Tag,Category,Comments
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.
def blog_list(request):
    blogs=Blog.objects.all()
    paginator = Paginator(blogs,3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    context={
        "blog_list":blog_list
    }
    return render(request,"blogs/blog_list.html",context)

def blog_detail(request,id):
    blog=Blog.objects.get(id=id)
    tags=Tag.objects.all().filter(blogs=blog)
    recents=Blog.objects.all().order_by("-created_at")[:1]
    categories=Category.objects.all()
    comments=Comments.objects.all().filter(blog=blog)

    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            new_name=form.cleaned_data["name"]
            new_email=form.cleaned_data["email"]
            new_message=form.cleaned_data["message"]
            new_comment=Comments(blog=blog,name=new_name,email=new_email,message=new_message)
            new_comment.save()
    context={
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
        "comments":comments
    }
    return render(request,"blogs/blog_detail.html",context)
def blog_tag(request,tag):
    blog_list=Blog.objects.all().filter(tags__slug=tag)
    context={
        "blog_list":blog_list
    }
    return render(request,"blogs/blog_list.html",context)
    
def blog_category(request,category):
    blog_list=Blog.objects.all().filter(category__slug=category)
    context={
        "blog_list":blog_list
    }
    return render(request,"blogs/blog_list.html",context)
def search(request):
    if request.method=="GET":
        q=request.GET.get("search") 
        blog_list=Blog.objects.all().filter(title__icontains=q)  
        return render(request,"blogs/blog_list.html",{"blog_list":blog_list})

