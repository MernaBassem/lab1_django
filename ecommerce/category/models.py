from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)
    @classmethod
    def get_all_category(cls):
        return [(obj.id,obj.title) for obj in cls.objects.all()]
    def __str__(self):
        return self.title
