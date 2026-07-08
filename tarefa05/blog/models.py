from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    foto = models.ImageField(upload_to=("imgs"))
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo