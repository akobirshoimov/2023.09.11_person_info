from django.urls import path
from .views import AllInfoView,DetailInfoView,UpdateInfoView,CreateInfoView,DeleteInfoView,Find_H_View

urlpatterns = [
    path('all/',AllInfoView.as_view()),
    path('detail/<int:info_id>/',DetailInfoView.as_view()),
    path('update/<int:info_id>/',UpdateInfoView.as_view()),
    path('create/',CreateInfoView.as_view()),
    path('delete/<int:info_id>/',DeleteInfoView.as_view()),
    path('find/',Find_H_View.as_view())
]