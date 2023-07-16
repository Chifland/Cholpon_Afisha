from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()
