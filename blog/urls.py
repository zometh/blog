from django.urls import path


from .views import index

app_name = 'blog'
urlpatterns = [
    path('', index, name="blog"),


]