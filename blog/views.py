from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import decorators 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import post 
from .forms import registration_form, profile_form, user_form
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def home(request):
	posts = post.objects.all()
	all_pages = Paginator(posts,2)
	c_page = request.GET.get('page')
	posts = all_pages.get_page(c_page)
	return render(request, 'blog/home.html', {'posts':posts})

def about(request):
	return render(request, 'blog/about.html')

@decorators.login_required
def profile(request):
	if request.method == 'POST':
		p_form = profile_form(request.POST, request.FILES, instance = request.user.profile)
		u_form = user_form(request.POST, instance = request.user)
		if p_form.is_valid() and u_form.is_valid():
			p_form.save()
			u_form.save()
			return redirect('user-profile') 
	else:
		u_form = user_form(instance = request.user)
		p_form = profile_form(instance = request.user.profile)
	return render(request, 'blog/profile.html', {'u_form':u_form, 'p_form':p_form})

def register(request):
	if request.method == 'POST':
		form = registration_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog-home')	
	else:
		form = registration_form()
	return render(request, 'blog/register.html', {'form':form})

class listview(ListView):
	model = post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date']

class user_posts(ListView):
	model = post
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	paginate_by = 3
	def get_queryset(self):
		x = get_object_or_404(User, username = self.kwargs.get('username'))
		return post.objects.filter(author = x).order_by('-date')

class detail(DetailView):
	model = post
	template_name = 'blog/detail.html'
	context_object_name = 'post'

class create(LoginRequiredMixin, CreateView):
	model = post
	fields = ('title','description')
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = post
	fields = ('title', 'description')
	def test_func(self):
		if self.get_object().author == self.request.user:
			return True
		return False
	
class delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = post
	success_url = '/'	
	def test_func(self):
		if self.get_object().author == self.request.user:
			return True
		return False