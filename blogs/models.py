from django.db import connection, models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=300, null=True)

class PostView(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.CharField(max_length=300, null=True)

    class Meta:
        managed = False
        db_table = 'post_view'  # Set the name of the PostgreSQL view

def generate_post_view():
    with connection.cursor() as cursor:
        # Check if the view already exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='post_view';")
        if cursor.fetchone() is not None:
            # Drop the view if it already exists
            cursor.execute("DROP VIEW post_view;")
        
        # Create the view
        cursor.execute("""
            CREATE VIEW post_view AS
            SELECT
                post.id,
                post.title,
                post.content,
                category.name AS category_name,
                post.pub_date,
                post.image
            FROM
                blogs_post AS post
            INNER JOIN
                blogs_category AS category ON post.category_id = category.id
        """)

generate_post_view()
