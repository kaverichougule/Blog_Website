from django.shortcuts import render
from blog_app.models import Post, Category
# Create your views here.
def home(request):

    # loading posts from database
    posts = Post.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    data = {
        'posts' : posts,
        'cats' : cats
    }


    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'post.html', {'post':post, 'cats': cats})

def category(request, url):
    cat = Category.objects.get(url = url)
    posts = Post.object.filter( cat = cat)
    return render(request, "category.html", {'cat': cat, 'post': posts})
