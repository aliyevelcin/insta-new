from django.shortcuts import render
from core.models import Post , Story , Comment
from accounts.models import User
from django.views.generic import ListView, TemplateView , CreateView
from core.forms import StoryForm , CommentForm , PostForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


class MainView(ListView,FormMixin):
    template_name = "insta.html"
    model = User
    form_class = CommentForm
    success_url = reverse_lazy('core:main')
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-id')
        context["users"] = User.objects.order_by('-id')
        context["storys"] = Story.objects.order_by('-id')
        return context


     

    def form_valid(self, form):
        form.instance.account = self.request.user
        post = Post.objects.get(pk=int(self.request.POST['post']))
        form.instance.account_post = post
        form.save()
        return super().form_valid(form)




class ExploreView(ListView,FormMixin):
    model = Post
    template_name = 'explore.html'
    form_class = CommentForm
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    success_url = reverse_lazy('core:exp')

    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.account = self.request.user
        post = Post.objects.get(pk=int(self.request.POST['post']))
        form.instance.account_post = post
        form.save()
        return super().form_valid(form)
    
 
class StoryView(CreateView):
    model = Story
    template_name = 'story.html'
    form_class = StoryForm
    success_url = reverse_lazy('core:main')
     
    
    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)
    

class PostView(CreateView):
    model = Post
    template_name = 'post.html'
    form_class = PostForm
    success_url = reverse_lazy('core:main')
    def form_valid(self, form):
        form.instance.account = self.request.user
        form.save()
        return super().form_valid(form)
     
