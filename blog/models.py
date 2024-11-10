from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    """
    A model representing a blog post.

    This model contains the essential fields for a blog post: title, content,
    slug, published date, view count, and an image. The slug is automatically
    generated from the title if not provided.

    Attributes:
        title (str): The title of the blog post.
        content (str): The main content of the blog post.
        slug (str): The URL-friendly version of the title.
        published_date (datetime): The date and time the blog post was
        published.
        views (int): The number of views the blog post has received.
        image (Image): An optional image associated with the blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a slug from the title if it's not
        provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the string representation of the BlogPost, which is the title.
        """
        return self.title
