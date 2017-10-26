from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pg_records(request, list, num):
	print request
	#create paginator object
	paginator = Paginator(list,num)
	
	#Get the page parameter from the query string
	#if the page is not available get() method will return empty string
	page = request.GET.get('page')
	#posts = Post.objects.all()
	try:
		#create page object for the given page
		page_object = paginator.page(page)
	except PageNotAnInteger:
		#if page parameter in the query is string is not available, return first page
		page_object = paginator.page(1)
	except EmptyPage:
		#if the value of the page parameter exceeds num_pages then return last page
		page_object = paginator.page(paginator.num_pages)
	return page_object