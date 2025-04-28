from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    """
    This Python function retrieves a single blog post based on the provided ID, increments the view
    count for that post, and renders a template with the post data.
    
    :param request: The `request` parameter in the `blog_single` function is an HttpRequest object that
    represents the current HTTP request. It contains metadata about the request, such as headers,
    method, and user data. This parameter is typically passed to Django view functions to process and
    respond to incoming requests
    :param pid: The `pid` parameter in the `blog_single` function is typically used to identify the
    specific post that the user wants to view. It is usually the primary key (pk) of the post in the
    database. This function retrieves the post with the given `pid` from the database, increments the
    :return: The `blog_single` view function is returning a rendered template `blog/blog-single.html`
    with the context containing the specific post retrieved based on the `pid` parameter.
    """
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save(update_fields=['counted_view'])
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)


def blog_view(request):
    posts = Post.objects.filter(
        status=1, published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
