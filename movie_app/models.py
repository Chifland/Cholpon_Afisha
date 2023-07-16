from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    director = models.ForeignKey('Director', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    @property
    def director_list(self) -> list:
        return self.director.all()


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)

    def __str__(self):
        return self.text

    @property
    def movie_list(self) -> list:
        return self.movie.all()
