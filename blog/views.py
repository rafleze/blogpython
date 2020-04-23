from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    articoli = Post.objects.filter(publish=True)
    return render(request, "home.html", context={"articoli": articoli})
