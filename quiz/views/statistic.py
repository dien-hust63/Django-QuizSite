from quiz.models import *
from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse

def statistic(request):
    return render(request, 'statistic/statistic.html')

def do_quiz_chart(request):
    labels = []
    data = []

    # queryset = Result.objects.values('quiz__title').annotate(Count('id'))
    # for entry in queryset:
    #     labels.append(entry['quiz__title'])
    #     data.append(entry['id__count'])
    # import pdb
    # pdb.set_trace()

    quizzes = Quiz.objects.all()
    count = 0
    for quiz in quizzes:
        try:
            count = Result.objects.filter(quiz=quiz).count()
        except:
            count = 0
        labels.append(quiz.title)
        data.append(count)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
def category_bar_chart(request):
    labels = []
    data = []

    queryset = Category.objects.all()
    for category in queryset:
        labels.append(category.content)
        data.append(category.quiz_set.all().count())

    return render(request, 'statistic/category-bar-chart.html', {
        'labels': labels,
        'data': data,
    })
