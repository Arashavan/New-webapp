from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# def blog_view(request):
#     posts = Post.objects.filter(status=1)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)

def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(
        status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(
        status=1, published_date__lte=timezone.now()).order_by('published_date')
    post = get_object_or_404(posts, pk=pid)

    post.counted_view += 1
    post.save(update_fields=['counted_view'])

    next_post = posts.filter(published_date__gt=post.published_date).order_by(
        'published_date').first()
    prev_post = posts.filter(published_date__lt=post.published_date).order_by(
        '-published_date').first()

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
    }
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(
        status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



