from django.db import connection, models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=300, null=True)
