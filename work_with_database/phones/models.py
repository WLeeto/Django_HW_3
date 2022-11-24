from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=20)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exist}, {self.slug}'
