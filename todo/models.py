from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=120, verbose_name="title")
    body = models.TextField(verbose_name="body")

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
    def __str__(self):
        return self.title