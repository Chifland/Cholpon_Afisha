from rest_framework.decorators import api_view  # [GET, POST, PUT, DELETE]
from rest_framework.response import Response  # Return Result
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        # 1. Get list of news
        directors = Director.objects.all()

        # 2. Convert list of news to list of dictionary
        data = DirectorSerializer(instance=directors, many=True).data

        # 3. Return Dictionary as JSON
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        directors = Director.objects.create(
            name=name
        )
        return Response(data=DirectorSerializer(directors).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(data={'message': 'Director object does ot exists!'},
                        status=404)
    if request.method == "GET":
        data = DirectorSerializer(instance=director, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        return Response(data=DirectorSerializer(director).data)
    else:
        director.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movies = Movie.objects.create(
            title=title, description=description,
            duration=duration, director_id=director_id
        )
        return Response(data=MovieSerializer(movies).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Movie object does ot exists!'},
                        status=404)
    if request.method == 'GET':
        data = MovieSerializer(instance=movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')

        return Response(data=MovieSerializer(movie).data)
    else:
        movie.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        reviews = Review.objects.create(
            text=text, stars=stars, movie_id=movie_id
        )
        return Response(data=ReviewSerializer(reviews).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Review object does ot exists!'},
                        status=404)
    if request.method == 'GET':
        data = ReviewSerializer(instance=review, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie = request.data.get('movie')
        return Response(data=ReviewSerializer(review).data)
    else:
        review.delete()
        return Response(status=204)


@api_view(['GET'])
def movie_with_rating(request):
    movie = Movie.objects.all()
    data = MovieReviewSerializer(instance=movie, many=True).data
    return Response(data=data)
