from blog.models import Post, Comment, Tag, Category, Guest_book
from blog.forms import PostForm, CommentForm, GuestForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from django.utils import timezone



#render function 3rd attribute==dictionary^
#렌더함수 세번째 인자가 사전, 템플릿 안에 쓸 이름 같게 해줘
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def bio(request):
    return render(request, 'blog/bio.html')

def post_list(request):
    post_list=Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': post_list} )

def post_detail(request):
    return render(request, 'blog/post_detail.html')

def category_list(request):
    category_list=Category.objects.all()
    return render(request, 'blog/category_list.html', {'category_list':category_list} )

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'blog/category_detail.html', {'category':category} )

def guest_list(request):
    guest_list=Guest_book.objects.all()
    return render(request, 'blog/guest_list.html', {'guest_list':guest_list})

def guest_detail(request, pk):
    guest = Guest_book.objects.get(pk=pk)
    return render(request, 'blog/guest_detail.html', {'guest':guest} )

def tag_list(request):
    return render(request, 'blog/tag_list.html')

def tag_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    return render(request, 'blog/tag_detail.html', {'tag':tag})

'''
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})'''

post_detail=DetailView.as_view(model=Post)

@login_required
def post_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            '''(commit=False)
            post.author = request.user
            post.save()'''
            return redirect('blog.views.post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form,
        })


@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog.views.post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form,
        })

def comment_new(request, post_pk):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.debug(request, '새로운 댓글을 등록했습니다.')
            return redirect('blog.views.post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form,
        })


def comment_edit(request, post_pk, pk):
    #comment = Comment.objects.get(pk=pk)
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog.views.post_detail', post_pk)
    else:
        form = CommentForm(instance =comment)
    return render(request, 'blog/comment_form.html', {'form':form,
        })


def guest_new(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            '''(commit=False)
            post.author = request.user
            post.save()'''
            return redirect('blog.views.guest_detail', guest.pk)
    else:
        form = GuestForm()
    return render(request, 'blog/guest_form.html', {'form': form,
        })

def guest_edit(request, pk):
    guest = Guest_book.objects.get(pk=pk)

    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            guest = form.save()
            return redirect('blog.views.guest_detail', guest.pk)
    else:
        form = GuestForm(instance=guest)
    return render(request, 'blog/guest_form.html', {'form': form,
        })


