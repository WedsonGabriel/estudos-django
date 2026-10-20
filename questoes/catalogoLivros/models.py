from django.db import models

class Livro(models.Model):
    titulo = models.CharField(verbose_name = 'titulo', max_length = 200, blank = False, null = False)
    autor = models.CharField(verbose_name = 'autor', max_length = 200, blank = False, null = False)
    ano = models.IntegerField(verbose_name = 'ano', blank = False, null = False)
    genero = models.CharField(verbose_name = 'genero', max_length = 200, blank = False, null = False)
    status = models.BooleanField(verbose_name = 'status', default = True)

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Gênero: {self.genero}"