from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path('register', views.registration, name='register'),


    # Path for login
    path('login', views.login_user, name='login'),  # Added trailing slash
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    # Path for logout
    path('logout/', views.logout_user, name='logout'),
    path('get_cars/', views.get_cars, name='getcars'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # Paths for dealer reviews and adding reviews (to be implemented)
    # path('dealers/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='dealer_reviews'),
    # path('add_review/', views.add_review, name='add_review'),
    path(route='add_review', view=views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)