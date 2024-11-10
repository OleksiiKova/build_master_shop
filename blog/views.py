from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


def blog_post(request, slug):
    """
    View for displaying a single blog post.

    This view retrieves the blog post by its slug, increments the view count,
    and then renders the 'post.html' template with the blog post data.

    Attributes:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the blog post to retrieve.

    Returns:
        HttpResponse: The rendered HTML page for the blog post.
    """
    post = get_object_or_404(BlogPost, slug=slug)
    post.views += 1
    post.save()
    return render(request, 'blog/post.html', {'post': post})


def all_blog_posts(request):
    """
    View for displaying all blog posts.

    This view retrieves all blog posts from the database and renders them
    in the 'all_blog_posts.html' template.

    Attributes:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying all blog posts.
    """
    posts = BlogPost.objects.all()
    return render(request, 'blog/all_blog_posts.html', {'posts': posts})


@login_required
def add_blog_post(request):
    """
    View for adding a new blog post.

    This view allows only superusers (store owners) to add a new blog post.
    It handles both GET and POST requests. If the request is a POST, the form
    is validated and the new post is created. If successful, a success message
    is displayed, and the user is redirected to the new post's page. Otherwise,
    an error message is shown.

    Attributes:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with the form for adding a post,
                       or a redirect to the new post if successful.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect('blog_post', slug=post.slug)
        else:
            messages.error(
                request,
                'Failed to update post. Please ensure the form is valid.'
            )
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog_post.html', {'form': form})


@login_required
def edit_blog_post(request, slug):
    """
    View for editing an existing blog post.

    This view allows only superusers (store owners) to edit a blog post.
    It retrieves the blog post based on the slug, displays the form pre-filled
    with the current post data, and saves the updated post if the form is
    valid.
    A success message is displayed upon successful update, and an error message
    is shown if the form is invalid.

    Attributes:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the blog post to be edited.

    Returns:
        HttpResponse: The rendered HTML page with the edit form, or a redirect
                       to the post page if the update is successful.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect('blog_post', slug=post.slug)
        else:
            messages.error(
                request,
                'Failed to update post. Please ensure the form is valid.'
            )
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_blog_post(request, slug):
    """
    View for deleting a blog post.

    This view allows only superusers (store owners) to delete a blog post.
    It retrieves the post based on the slug, and if the request is a POST,
    the post is deleted. A success message is displayed, and the user is
    redirected to the list of all blog posts. If the request is a GET, a
    confirmation page is shown.

    Attributes:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the blog post to be deleted.

    Returns:
        HttpResponse: A redirect to the list of blog posts if the deletion
        is successful, or the confirmation page if it's a GET request.
    """
    """Delete a blog post"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('all_blog_posts'))

    template = 'blog/delete_post.html'
    context = {
        'post': post,
    }
    return render(request, template, context)
