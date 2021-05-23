from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    class Meta: 
        abstract = True
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    content = models.CharField(_('Content'), max_length=255, unique=True)

    def __str__(self):
        return f"{self.id}. {self.content}"
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')

class Quiz(BaseModel):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    title = models.CharField(_('Title'), max_length=255)
    max_time = models.IntegerField(_('Max Time'), help_text='minutes')
    score_to_pass = models.IntegerField(_("Score to pass"))
    LEVEL_CHOICES = [
        ('N', 'Newbie'),
        ('F', 'Fresher'),
        ('M', 'Middle'),
        ('S', 'Senior'),
    ]
    level = models.CharField(max_length=6, choices= LEVEL_CHOICES, default='M')

    def __str__(self):
        return f"{self.id}. {self.title}"

    @property
    def total_score(self):
        questions = self.question_set.all()
        total = 0
        for question in questions: 
            total = total + question.score
        return total
    
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quiz')

class Question(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(_('Title'), max_length=255, null = True, blank = True)
    content = models.TextField(_('Content'))
    score = models.IntegerField()
    quiz = models.ForeignKey("Quiz", on_delete=models.DO_NOTHING)

    TYPE = (
        (0, _('Multiple Choice')),
        (1, _('Free Text')),
    )
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question"))

    @property   
    def list_answer(self):
        return self.answer_set.all()
    
    @property
    def get_correct_answer(self):
        return self.answer_set.filter(is_correct_answer = True)

    def __str__(self):
        return f"{self.id}. {self.content}"

    
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')   

class Answer(BaseModel):
    id = models.AutoField(primary_key = True)
    content = models.TextField()
    is_correct_answer = models.BooleanField()
    question = models.ForeignKey("Question", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Anwers')
    
    def __str__(self):
        return f"{self.content}"

class Result(BaseModel):
    id = models.AutoField(primary_key = True)
    final_score = models.IntegerField(_('Final Score'))
    quiz = models.ForeignKey("Quiz",on_delete=models.DO_NOTHING)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.user.username}"

    class Meta:
        verbose_name = _('Result')
        verbose_name_plural = _('Results')

class DetailResult(BaseModel):
    id = models.AutoField(primary_key=True)
    result = models.ForeignKey("Result", on_delete=models.CASCADE)
    question =  models.ForeignKey("Question", on_delete=models.SET_NULL, null=True, blank = True)
    answer = models.ForeignKey("Answer", on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def list_question(self):
        return self.question_set.all()
    
    @property
    def list_answer(self):
        return self.answer_set.all()
        
    class Meta:
        verbose_name = _('Detail Result')
        verbose_name_plural = _('Detail Results')

class User(AbstractUser, BaseModel):
    id = models.AutoField(primary_key = True)
    username = models.EmailField(
        max_length=255,
        unique=True,
        help_text='Required. Email only.',
    )
    is_manager_admin = models.BooleanField(default=False)



