from django.shortcuts import render, redirect, get_object_or_404, redirect
from blog.forms import PostForm
from blog.models import Post, Author, Category, Tag

def post_add(request):
	if request.method == "POST":
		f = PostForm(request.POST)
		#chech wheather form is valid or not
		#if the form is valid, save the data to the database
		#and redirect the user back to the add post form
				
		if f.is_valid():
			f.save()
			return redirect('post_add')
	else:
		f = PostForm()
	return render(request, 'cadmin/post_add.html', {'form':f})

def post_update(request, pk):
	post = get_object_or_404(Post, pk=pk)
	
	if request.method == "POST":
		f = PostForm(request.POST, instance=post)
		if f.is_valid():
			f.save()
			return render(request, 'blog/post_detail.html',{'post': Post.objects.get(pk=pk)})
			#return render(request, 'blog/post_detail.html', {id=f.id})
			#return render(request, 'cadmin/post_update.html', {pk=post.id})
	else:
		f = PostForm(instance=post)
	return render(request, 'cadmin/post_update.html',{'form':f,'post':post})