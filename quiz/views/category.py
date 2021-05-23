from django.shortcuts import render, redirect
from quiz.models import *
from django.views import generic
from django.shortcuts import get_object_or_404
from quiz.forms import QuizTestForm, CustomUserCreationForm, QuizForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse

def category_detail_view(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    quizes = category.quiz_set.all()
    context ={
        'category': category,
        'quizes': quizes,
    }
    return render(request, 'category/category_detail.html', context=context)

class CategoryListView(generic.ListView):
    model = Category

class CategoryCreate(CreateView):
    model = Category
    fields = ("__all__")
    template_name = "category/category_create_form.html"

    def get_success_url(self):
        return reverse('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/category_confirm_delete.html"
    
    def get_success_url(self):
        return reverse('category-list')
    

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['content']
    template_name = "category/category_update_form.html"

    def get_success_url(self):
        return reverse('category-list')
