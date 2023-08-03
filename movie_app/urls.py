from movie_app import views
from django.urls import path


urlpatterns = [
    path('directors/', views.director_list_api_view),
    path('directors/<int:director_id>/', views.director_detail_api_view),
    path('', views.movie_list_api_view),
    path('<int:movie_id>/', views.movie_detail_api_view),
    path('review/', views.review_list_api_view),
    path('review/<int:review_id>/', views.review_detail_api_view),
    path('reviewmovie/', views.movie_with_rating)
]
