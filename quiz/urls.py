from django.urls import include, path, reverse, re_path
from .views import category, contest, user, index, statistic
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #register
    re_path(r"^register/", user.register, name="register"),
    #contest
    path('index/', index.index, name='index'),
    path('contest/', login_required(category.CategoryListView.as_view(
        template_name = "contest/contest_category_list.html")), name='contest'),
    path('contest/<int:pk>/quiz', contest.quizes, name='quiz'),
    path('contest/<int:category_id>/quiz/<int:quiz_id>', contest.quiz_confirm, name='quiz-confirm'),
    path('contest/<int:category_id>/quiz/<int:quiz_id>/doquiz', contest.quiz_detail, name='quiz-detail'),
    path('result/<int:result_id>',contest.show_results, name='results'),
    path('result/<int:result_id>/detail', contest.show_detail_result, name='detail-result'),
    #history
    path('users/<int:user_id>', user.history, name='history'),

    #statistic
    path('statistics/', statistic.statistic , name='statistic'),
    path('do-quiz-chart/', statistic.do_quiz_chart, name='do-quiz-chart'),
    path('category-bar-chart/', statistic.category_bar_chart, name='category-bar-chart'),

    #category crud
    path('category/create', category.CategoryCreate.as_view(), name='create-category'),
    path('category/list', category.CategoryListView.as_view(
        template_name = "category/category_list.html"), name='category-list'),
    path('category/<int:pk>/delete', category.CategoryDeleteView.as_view(), name='delete-category'),
    path('category/<int:pk>/update', category.CategoryUpdateView.as_view(), name='update-category'),
    path('category/<int:category_id>/', category.category_detail_view, name='category-detail'),
    
    # path('quiz/create/', views.create_quiz_view, name = 'create-quiz'),
    # path('contest/<int:category_id>/quiz/<int:quiz_id>/results', views.results, name='results'), 
]

