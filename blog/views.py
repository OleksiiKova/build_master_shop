from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.views += 1
    post.save()
    return render(request, 'blog/post.html', {'post': post})


def all_blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/all_blog_posts.html', {'posts': posts})


@login_required
def add_blog_post(request):
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