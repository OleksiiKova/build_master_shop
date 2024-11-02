from django.db import models


class ContactMessage(models.Model):
    """
    Model for storing contact messages from users.

    This model captures messages sent by users, including their name,
    email, and the message content. It also includes a flag to indicate
    whether the message has been read.

    Attributes:
        name (CharField): The name of the person sending the message.
        email (EmailField): The email address of the person sending
        the message.
        message (TextField): The content of the message.
        read (BooleanField): Indicates whether the message has been read.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
