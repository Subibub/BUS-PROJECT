from django.db import models

# Create your models here.
class Feed(models.Model):
    location = models.TextField()
    image = models.TextField()
    click = models.TextField()
    conv = models.TextField()

    def __str__(self):
        return self.location

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Feed, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment