#from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
import datetime
#from django import template
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.conf import settings
from .models import Author, Tag, Category, Post
from .forms import FeedbackForm, MyFeedbackForm
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm

#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django_project import helpers

def index(request):
	return HttpResponse("Hello Django");
	
def today_is(request):
	now = datetime.datetime.now()
	#t = template.loader.get_template('blog/datetime.html')
	#c = template.Context({'now':now})
	#return HttpResponse(t.render(c))
	return render(request, 'blog/datetime.html',{'now':now, 'template_name':'blog/nav.html', 	
		'base_dir' : settings.BASE_DIR,}
	)

def post_list(request):
	post_list = Post.objects.order_by("pub_date").all()
	
	posts = helpers.pg_records(request, post_list, 5)
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return HttpResponseNotFound("Page not found")
	return render(request, 'blog/post_detail.html',{'post': post})


# view function to display post by category
def post_by_category(request, category_slug):

    #category = Category.objects.get(slug=category_slug)
	category = get_object_or_404(Category, slug=category_slug)
	#posts = Post.objects.filter(category__slug=category_slug)
	posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
	posts = helpers.pg_records(request, posts, 5)
	context = {
        'category': category,
        'posts': posts
    }
    #print(category)
	return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	#tag = Tag.objects.get(slug=tag_slug)
	posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
	posts = helpers.pg_records(request, posts, 5)
	#posts = Post.objects.filter(tags__name=tag)
	context = {
		'tag': tag,
		'posts': posts
	}
	return render(request, 'blog/post_by_tag.html', context )

def test_redirect(request):
	return HttpResponseRedirect('/')
	
def feedback(request):
	if request.method == 'POST':
		f = FeedbackForm(request.POST)
		if f.is_valid():
			f.save()
			return redirect('feedback')
	else:
		f = FeedbackForm()
	return render(request, 'blog/feedback.html', {'form':f})

def myfeedback(request):
	if request.method == 'POST':
		f = MyFeedbackForm(request.POST)
		if f.is_valid():
			f.save()
			return redirect('myfeedback')
	else:
		f = MyFeedbackForm()
	return render(request, 'blog/myfeedback.html', {'form':f})

def test_cookie(request):
	if not request.COOKIES.get('color'):
		response = HttpResponse("Cookie Set")
		response.set_cookie('color','blue',3600*24*365*2)
		return response
	else:
		return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))

def track_user1(request):	
	if not request.COOKIES.get('visits'):
		response = HttpResponse("This is your first visit to the site\n.From now I will track your visits.")
		response.set_cookie('visits','1',3600*24*365*2)
	else:
		visits = int(request.COOKIES['visits']) + 1
		response = HttpResponse("This is your {0} visit".format(visits))
		response.set_cookie('visits',str(visits),3600*24*365*2)
	return response
	
def track_user(request):	
	response = render(request, 'blog/track_user.html')
	if not request.COOKIES.get('visits'):
		response.set_cookie('visits','1',3600*24*365*2)
	else:
		visits = int(request.COOKIES['visits']) + 1
		response.set_cookie('visits',str(visits),3600*24*365*2)
	return response
	
def stop_tracking(request):
	if request.COOKIES.get('visits'):
		response = HttpResponse("Cookies Cleared")
		response.delete_cookie('visits')
	else:
		response = HttpResponse("We are not tracking you.")
	return response

def test_session(request):
	request.session.set_test_cookie()
	return HttpResponse("Testing session cookie")

def test_delete(request):
	if request.session.test_cookie_worked():
		request.session.delete_test_cookie()
		response = HttpResponse("Cookie test passed")
	else:
		response = HttpResponse("Cookie test failed")
	return response
	
def lousy_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username == 'root' and password == 'pass':
			request.session['logged_in'] = True
			return redirect('lousy_secret')
		else:
			messages.error(request, 'Error wrong username/password')
	return render(request, 'blog/lousy_login.html')

def lousy_secret(request):
	if not request.session.get('logged_in'):
		return redirect('lousy_login')
	return render(request, 'blog/lousy_secret_page.html')

def lousy_logout(request):
	try:
		del request.session['logged_in']
	except KeyError:
		return redirect('lousy_login')
	return render(request, 'blog/lousy_logout.html')
	
def login(request):
	if request.user.is_authenticated():
		return redirect('admin_page')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('admin_page')
		else:
			messages.error(request, 'Error wrong username/password')
	return render(request, 'blog/login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'blog/logout.html')

def admin_page(request):
	if not request.user.is_authenticated():
		return redirect('blog_login')
	return render(request, 'blog/admin_page.html')

def register(request):
	if request.method == "POST":
		f = UserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully. Plese login using credentials')
			return redirect('blog_login')
	else:
		f = UserCreationForm()
	return render(request, 'blog/register.html',{'form':f})	
	