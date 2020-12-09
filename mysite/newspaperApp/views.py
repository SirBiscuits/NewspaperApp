from django.shortcuts import render
from django.views.generic import ListView, DetailView # class based views
# list = all of my news articles, detail = one news article
# detailView used for individual article pages, but i may not need this
from .models import NewsArticle, Comment #, Category
from django.http import HttpResponse, JsonResponse

# Create your views here.

# def home(request):
# 	return render(request, 'home.html', {})

def Profile(response):
        return render(response, "Profile.html", {})


class Home(ListView):
	queryset = NewsArticle.objects.filter(category__in=["sports", "technology", "World"])
	template_name = 'home.html'

# def Profile():
# 	model = Category
# 	template_name = 'profile.html'

def create_comment(request):
    if request.method == "POST":
        comment = request.POST['comment']

        comment = Comment.objects.create(comment = comment, author=request.user)
        return JsonResponse({"created_date": comment.created_date, "comment": comment.comment})