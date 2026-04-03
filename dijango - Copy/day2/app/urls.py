from django.urls import path
from . import views

urlpatterns=[
    path('',views.student_details),
    path('delete/<int:id>/', views.delete_student),
    path('edit/<int:id>/',views.edit_student),
    #path('subject/',views.subject_details
]