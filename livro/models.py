from django.db import models



class Livro(models.Model):
    nome = models.CharField(max_length = 50)
    figura = models.ImageField()
    autor = models.CharField(max_length = 30, default='anonymous')
    document = models.FileField(upload_to='documents/')
    email = models.EmailField(blank = True)
    descricao = models.TextField(default = '4Linux Django')
    def __str__(self):
        return self.nome
