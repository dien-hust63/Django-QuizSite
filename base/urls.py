
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from quiz.views.user import register
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', RedirectView.as_view(url='accounts/login/', permanent=True)),
]

