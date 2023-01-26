from django.urls import path 
from . import views 


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('account/', views.userAccount, name='account'),
    path('edit_account/', views.editAccount, name='edit_account'),
    path('add_skill/', views.addSkill, name='add_skill'),
    path('edit_skills/<str:pk>/', views.editSkills, name='edit_skills'),
    path('delete_skill/<str:pk>/', views.deleteSkill, name='delete_skill'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user_profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.messageView, name='message'),
    path('create_message/<str:pk>/', views.createMessage, name='create_message'),
]
