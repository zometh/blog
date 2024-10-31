import uuid
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from blog.models import BlogPost
from .forms import SignupForm

def home(request):
    return HttpResponse("page d'accueil")
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Inscription réussie, merci")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

def get_data(request):
    all_blog = BlogPost.objects.all()
    data = {}
    for blog in all_blog:
        tmp_blog = {
            'title': blog.title,
            'slug': blog.slug,
            'content': blog.content
        }
        id_blog = uuid.uuid4()
        data[str(id_blog)] = tmp_blog
    json_response = JsonResponse(data=data)
    return json_response