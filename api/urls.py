# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    #path('', MemberProjectMessagesListView.as_view(), name='member-project-messages-list'),
    #path('api/members/create/', create_member, name='member-create'),
    #path('api/members/edit/', views.edit_member, name='member'),
    #path('api/members/delete/', views.delete_member, name='member'),
    path('api/feedback/create/', FeedbackCreateView.as_view(), name='create-feedback'),
    

]
