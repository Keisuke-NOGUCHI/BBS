from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('subjects', views.subjects, name='subjects'),
    path('club', views.club, name='club'),
    path('chat', views.chat, name='chat'),
    path('others', views.others, name='others'),
    path('subjects/cs_exercise/', views.cs_exercise, name='cs_exercise'),
    path('subjects/ls_exercise', views.ls_exercise, name='ls_exercise'),
    path('subjects/rw_exercise', views.rw_exercise, name='rw_exercise'),
    path('subjects/social', views.social, name='social'),
    path('subjects/basic', views.basic, name='basic'),
    path('subjects/practice', views.practice, name='practice'),
    path('<int:comment_id>/delete_cs', views.delete_cs, name='delete_cs'), #デリート追加
    path('<int:comment_id>/delete_ls', views.delete_ls, name='delete_ls'),
    path('<int:comment_id>/delete_rw', views.delete_rw, name='delete_rw'),
    path('<int:comment_id>/delete_so', views.delete_so, name='delete_so'),
    path('<int:comment_id>/delete_ba', views.delete_ba, name='delete_ba'),
    path('<int:comment_id>/delete_pr', views.delete_pr, name='delete_pr'),
    path('<int:comment_id>/delete_ch', views.delete_ch, name='delete_ch'),
    path('<int:comment_id>/delete_ot', views.delete_ot, name='delete_ot'),
    path('<int:comment_id>/delete_cl', views.delete_cl, name='delete_cl'),
]