from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.views import get_blog_queryset
from blog.models import BlogPost
# Create your views here.
BLOG_POSTS_PER_PAGE = 3
def index(request):
	context = {}
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)


	blog_post = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	

	#pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_post, BLOG_POSTS_PER_PAGE)

	try:
		blog_post = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_post = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_post = blog_posts_paginator.page(blog_posts_paginator.num_pages)		
		
	context['blog_posts'] = blog_post	
	return render(request, 'personal/index.html', context)