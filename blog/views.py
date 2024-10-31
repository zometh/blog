from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse, Http404
import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from blog.models import BlogPost
from website.asgi import application


# Create your views here.
#@login_required // pour restreindre l'accès aux utilisateurs non connectés
#@user_passes_test(lambda u: "moderateurs" in  [group_name.name for group_name in u.groups.all()]) gérer l'accès avec des conditions
def index(request):
    #all_blog = BlogPost.objects.all()
    """response = HttpResponse(
        render_to_string("blog/index.html", context={'all': all_blog})
    )"""

    #return response
    all_blog = BlogPost.objects.all()
    name = "<script>alert('hello wordl')</script>"
    return render(request, 'blog/index.html', context={'all': all_blog, "name": name})
    ###HTTP RESPONSE
    """reponse = HttpResponse()
    reponse.content = "{'1': BonjourMouhaemed}"
    reponse.status_code = 404
    reponse['Content-Type'] = "application/json"
    return reponse"""
    ###JSON RESPONSE
    """data = {}
    for blog in all_blog:
        tmp_blog = {
            'title': blog.title,
            'slug': blog.slug,
            'content': blog.content
        }
        id_blog = uuid.uuid4()
        data[str(id_blog)] = tmp_blog
    json_response = JsonResponse(data=data)
    return json_response"""
    ### 404 Error
    """blog_post = get_object_or_404(BlogPost, pk=1)
    return HttpResponse(blog_post.content)
    try:
        blog_post =  BlogPost.objects.get(pk=8)
    except BlogPost.DoesNotExist:
        raise Http404("L'article n'existe pas")
    return HttpResponse(blog_post)"""
    ###REDIRECTION
    return redirect("https://www.google.com")
def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/post.html", context={"post": post})

