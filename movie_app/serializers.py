from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'stars text'.split()


class MovieSerializer(serializers.ModelSerializer):
    movies_review = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title duration description director_str rating movies_review'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title rating'.split()


class DirectorSerializer(serializers.ModelSerializer):
    directors_movies = MovieReviewSerializer(many=True)

    class Meta:
        model = Director
        fields = 'id name movie_count directors_movies'.split()


class DirectorValidteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField(max_value=5)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist!')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    stars = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField(required=False, max_length=100)
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exist!')
        return movie_id
