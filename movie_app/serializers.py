from rest_framework import serializers
from movie_app.models import Director, Movie, Review



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

