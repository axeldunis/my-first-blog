from django.shortcuts import render, redirect 
from django.utils import timezone

from .models import Show
from django.http import HttpResponseRedirect
from.forms import UploadFileForm
import csv
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts' : posts}) 

def post_detail(request,pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request,'blog/post_detail.html',{'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def home(request):
    shows = Show.objects.all()
    return render(request,'Home.html',{'shows':shows})

def netflix(request):
    shows = Show.objects.all()
    return render(request,'Netflix.html',{'shows':shows})

def prime(request):
    shows = Show.objects.all()
    return render(request,'Prime_video.html',{'shows':shows})

def paramount(request):
    shows = Show.objects.all()
    return render(request,'Paramount_plus.html',{'shows':shows})