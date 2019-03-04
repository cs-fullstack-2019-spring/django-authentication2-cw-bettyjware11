from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPosts
from django.contrib.auth.decorators import login_required

# function to test
def index(request):
    return HttpResponse("Testing.")

# function to display blog posts per user
# user must be logged in
@login_required
def myBlogPosts(request):
    blogPost_list = BlogPosts.objects.filter(user_name=request.user)
    context = {'blogPost_list': blogPost_list}
    return render(request, 'authentication2App/myBlogPosts.html',context)