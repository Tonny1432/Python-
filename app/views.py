from django.shortcuts import render
from .models import Student
def student_list(request):
    student =Student.objects.all() #Get ALL student data from database”
    return render(request,'student.html',{'students':student})
# Create your views here.
