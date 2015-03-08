from django.shortcuts import get_object_or_404, render

from articles.models import Article

def display(request, num_to_display, display_type):
	if (display_type == 'Date'):
		latest_articles = Article.objects.order_by('-pub_date')[:num_to_display]
	elif (display_type == 'Name'):
		latest_articles = Article.objects.order_by('title')[:num_to_display]		
	context = { 'latest_articles': latest_articles, 'num': num_to_display, 'display_type': display_type }
	return render(request, 'articles/index.html', context)

def index(request):
	return display(request, 10, 'Date')

def change_display(request):
	num_to_display = int(request.GET.get('num_to_display', 10))
	display_type = request.GET.get('display_type', None)
	return display(request, num_to_display, display_type)

def articleid(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context = { 'article': article }
	return render(request, 'articles/articleid.html', context)

def department(request, dep):
	article = get_object_or_404(Article, pk=article_id)
	context = { 'article': article }
	return render(request, 'articles/department.html', context)

def search(request):
	keywords = request.GET.get('search_keywords', None)
	print(keywords)
	if keywords:
		search_articles = Article.objects.filter(title__icontains=keywords)
	else:
		search_articles = None
	context = { 'keywords': keywords , 'search_articles': search_articles}
	return render(request, 'articles/search.html', context)