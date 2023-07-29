from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def movie_count(self):
        return self.directors_movies.count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='directors_movies')

    def rating(self):
        total = self.movies_review.all().count()
        if total == 0:
            return 0
        sum = 0
        for i in self.movies_review.all():
            sum += i.stars
        return round(sum/total, 2)

    def __str__(self):
        return self.title

    def director_str(self):
        if self.director:
            return self.director.name
        return None

    @property
    def director_list(self) -> list:
        return self.director.all()


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movies_review')
    stars = models.IntegerField(default=0)

    @property
    def movie_list(self) -> list:
        return self.movie.all()

    def __str__(self):
        return self.text
