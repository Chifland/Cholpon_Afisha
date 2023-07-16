from rest_framework.decorators import api_view  # [GET, POST, PUT, DELETE]
from rest_framework.response import Response  # Return Result
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def director_list_api_view(request):
    # 1. Get list of news
    directors = Director.objects.all()

    # 2. Convert list of news to list of dictionary
    data = DirectorSerializer(instance=directors, many=True).data

    # 3. Return Dictionary as JSON
    return Response(data=data)


@api_view(['GET'])
def director_detail_api_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(data={'message': 'Director object does ot exists!'},
                        status=404)
    data = DirectorSerializer(instance=director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Movie object does ot exists!'},
                        status=404)
    data = MovieSerializer(instance=movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Review object does ot exists!'},
                        status=404)
    data = ReviewSerializer(instance=review, many=False).data
    return Response(data=data)


