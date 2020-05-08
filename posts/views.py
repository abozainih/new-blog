from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post',post.id)
    else : 
        form = PostForm()


    return render(request,'posts/create.html',{'form':form})
    
@login_required(login_url='/accounts/login')
def show(request):
    posts = Post.objects.all()

    return render(request,'posts/index.html',{'posts':posts})
@login_required
def details(request,id):
    post = Post.objects.get(pk = id)
    return render(request,'posts/post.html',{'post':post})

