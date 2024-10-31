from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()
    def __str__(self):
        return self.name

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField(default="")
    class Meta:
        #Changer le titre de tous les objets
        verbose_name = "Article"
        # ordonner les données
        ordering = ["-date", "-published"]
    # voir la page associée au model
    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug})
    
    @property
    def publish_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article est inaccessible"

    def __str__(self):
        return f"Titre: {self.title}\nSlug: {self.slug}\nContent: {self.content}"

    def save(self, *args, **kwargs):
        if not self.slug:

            #self.slug = "-".join(str(self.title).split(" ")).lower()
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    @property
    def word_count(self):
        return len(self.content.split())




