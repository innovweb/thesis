from django.shortcuts import get_object_or_404, render

from articles.models import Article

def display(request, num_to_display):
	latest_articles = Article.objects.order_by('-pub_date')[:num_to_display]
	context = { 'latest_articles': latest_articles, 'num': num_to_display }
	return render(request, 'articles/index.html', context)

def index(request):
	return display(request, 10)

def change_display(request):
	try:
		num_to_display = int(request.GET['num_to_display'])
	except (KeyError, Choice.DoesNotExist):
		num_to_display = 10
	return display(request, num_to_display)

def articleid(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context = { 'article': article }
	return render(request, 'articles/articleid.html', context)

def department(request, dep):
	article = get_object_or_404(Article, pk=article_id)
	context = { 'article': article }
	return render(request, 'articles/department.html', context)
