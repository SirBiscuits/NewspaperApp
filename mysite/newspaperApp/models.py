# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class NewsArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default="unknown")
    created_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    #likes = models.ManyToManyField(User, related_name="news_articles")
    # likes = models.ForeignKey(Like, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Like(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    numOfLikes = models.IntegerField(default=0)


class Comment(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	# article = models.ForeignKey(NewsArticle,on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	comment = models.TextField()

	def __str__(self):
		return str(self.author) + ' | ' + self.comment
	# likes = models.IntegerField()
	# newsArticle = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
	# comment is in 1 news article, but news article can have many comments
    # replies =