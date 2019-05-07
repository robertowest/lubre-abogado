from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # usuarios
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'), 
         name='reset_password'),    

    # agregamos gestion propias
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),

    # aplicaciones
    # path('', views.home, name='home'),
    # path('ctactecli/', include('apps.ctactecli.urls')),
    # path('', include('apps.ctactecli.urls')),

    path('', include('apps.gestion.urls')),
]




from django.urls import include
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
