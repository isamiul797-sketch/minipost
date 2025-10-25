from django.shortcuts import render
from posts.models import Posts
from posts.forms import PostsForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'posts/index.html')

def post_list(request):
   post=Posts.objects.all().order_by('-created_at')
   return render(request,'posts/post_list.html',{'post':post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostsForm()
    return render(request,'posts/post_form.html',{'form':form})

@login_required
def post_edit(request,post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostsForm(instance=post)
    return render(request,'posts/post_form.html',{'form':form})

@login_required  
def post_delete(request,post_id):
    post = get_object_or_404(Posts, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request,'posts/post_confirm_delete.html',{'post':post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()

    return render(request,'posts/register.html',{'form':form})

