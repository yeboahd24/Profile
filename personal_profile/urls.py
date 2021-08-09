from django.urls import path

from .views import single, blog, index


urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('single/', single, name="single"),
]
