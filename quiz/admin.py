from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html


class QuizInline(admin.TabularInline):
    model = Quiz
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'view_list_quiz')
    search_fields = ('id', 'content')
    inlines = [QuizInline]
    
    def view_list_quiz(self, obj):
        url = (
            reverse("admin:quiz_quiz_changelist")
            + "?"
            + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">List quiz</a>', url)

    view_list_quiz.short_description = "List quiz"

class QuestionInline(admin.TabularInline):
    model = Question
    show_change_link = True


class QuizAdmin(admin.ModelAdmin):
    list_display=(
        'id','title', 'category', 
        'max_time', 'score_to_pass', 'level', 
        'view_list_question',
    )
    search_fields = ('id', 'category', 'title')
    list_filter = ("category", )
    inlines = [QuestionInline]
    def view_list_question(self, obj):
        url = (
            reverse("admin:quiz_question_changelist")
            + "?"
            + urlencode({"quiz__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">List question</a>', url)

    view_list_question.short_description = "List question"


admin.site.register(Quiz, QuizAdmin)

class AnswerInline(admin.TabularInline):
    model = Answer
    show_change_link = True
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'score', 
        'quiz', 'technique', 'view_list_answer'
    )
    search_fields = ('id', 'content', 'quiz__title')
    inlines = [AnswerInline]
    list_filter = ("quiz__title", )

    def view_list_answer(self, obj):
        url = (
            reverse("admin:quiz_answer_changelist")
            + "?"
            + urlencode({"question__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">List answer</a>', url)

    view_list_answer.short_description = "List answer"

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content',
        'is_correct_answer', 'question'
    )
    search_fields = ('id', 'question__content')
    list_filter = ('question__content',)
admin.site.register(Answer, AnswerAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'final_score', 'quiz', 'user', 'created')
    search_field = ('id', 'quiz', 'user')
    list_filter = ('user__username', 'quiz__title')

admin.site.register(Result, ResultAdmin)

class DetailResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'question', 'answer', )
    search_field = ('id', 'result')

admin.site.register(DetailResult, DetailResultAdmin)

class BaseUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_manager_admin', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, BaseUserAdmin)




