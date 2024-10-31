from django.contrib import admin

# Register your models here.
from blog.models import BlogPost
#admin.site.register(BlogPost)
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    #Si on veut ajouter des colones à la page d'aministration
    list_display = (
        "title",
        "slug",
        "published",
        "date",
        "author",
        "word_count"
    )
    
    # valeur par défaut pour les attributs qui ont des valeurs Nonde
    empty_value_display = "unknown"
    # Si on veut modifier directement les informations sans ouvrir un autre page
    list_editable = ( "published",)
    # Transformer un champ en lien
    list_display_links = ("date","title")
    # Filtrer les données
    search_fields = ("title", "content")
    # Filtre spécifique
    list_filter = ("date", )
    # Autocomplétion pour les filtres
    autocomplete_fields = ("author", )
    # limiter le nombre d'instances
    list_per_page = 100