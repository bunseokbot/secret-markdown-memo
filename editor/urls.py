from django.urls import path

from . import views

urlpatterns = [
    path('editor/', views.Editor.as_view(), name='editor'),
    path('editor/<int:memo_id>/', views.Editor.as_view(), name='editor_by_id'),
    path('', views.all_memo),

]
