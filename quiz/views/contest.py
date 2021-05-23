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
import json


@login_required(login_url = 'login')
def quizes(request, pk):
    category = Category.objects.get(pk = pk)
    quiz_list = Quiz.objects.filter(category=category)

    context = {
        'category': category,
        'quiz_list' : quiz_list,
    }
    return render(request, 'contest/contest_quiz_list.html', context = context)

@login_required(login_url = 'login')
def quiz_confirm(request, category_id, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    context = {
        'quiz': quiz,
    }
    return render(request, 'contest/contest_quiz_confirm.html', context = context)


@login_required(login_url = 'login')
def quiz_detail(request, category_id, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)


    if request.method == 'POST':
        form = QuizTestForm(request.POST, extra=questions, detail_result=0)
        
        if form.is_valid():
            final_result = save_result(request, form, quiz, questions)
            save_detail_result(form, questions, final_result)
            context = {
                'result': final_result,
                'quiz': quiz,
            }
            return redirect(reverse('results', kwargs={'result_id':final_result.id}))
            
    else:
        form = QuizTestForm(extra=questions,detail_result=0)
    context = {
       'form':form,
       'quiz':quiz,
    }
    return render(request, 'contest/contest_quiz_detail.html', context = context)

def show_results(request, result_id):
    result = Result.objects.get(id = result_id)
    quiz = result.quiz
    context = {
        'result':result,
        'quiz':quiz
    }
    return render(request, 'contest/contest_results.html', context = context )

def show_detail_result(request, result_id):
    result = get_object_or_404(Result, id = result_id)
    # detail_result = get_object_or_404(DetailResult, result=result) 
    questions = Question.objects.filter(quiz=result.quiz)
    form = QuizTestForm(extra=questions, detail_result=1)
    context = {
        'form':form,
    }
    return render(request, 'contest/contest_detail_result.html', context = context)

def save_result(request, form, quiz, questions):
    results = 0
    for question in questions:
        correct_answers = question.get_correct_answer
        user_answers = form.cleaned_data[f"{question.id}"]
        correct_answers_len = len(correct_answers)
        if correct_answers_len == len(user_answers):
            for i in range(len(correct_answers)):
                if str(correct_answers[i]) != user_answers[i]:
                    break
            results = results + question.score
    final_result = Result.objects.create(
        final_score = results, 
        quiz = quiz, 
        user = request.user
    )
    final_result.save()
    return final_result

def save_detail_result(form, questions, final_result):
    for question in questions:
        user_answers = form.cleaned_data[f'{question.id}']
        for answer in user_answers:
            detail_result = DetailResult.objects.create(
                result= final_result, 
                question=question,
                answer = answer
            )
            detail_result.save()
    return None
        
      
    

#TODO: handle when timeout
#check register
#show result
