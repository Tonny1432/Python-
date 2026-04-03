from django.shortcuts import render,redirect
from . models import students #subject

def student_details(request):
    if request.method =="POST":
         name = request.POST.get('s.name')
         age  = request.POST.get('s.age')
         reg_no = request.POST.get('s.reg')
         dept = request.POST.get('s.dept')
         email =request.POST.get('s.email')
         students.objects.create(
               s_name = name,
               s_age = age,
               s_reg = reg_no,
               s_dept = dept,
               s_email = email
               )
         return redirect('/')
    student_data = students.objects.all()
    return render(request,'data.html',{'std':student_data})

def delete_student(request,id):
     student_id = students.objects.get(id=id)
     student_id.delete()
     return redirect('/')

def edit_student(request, id):
    student = students.objects.get(id=id)

    if request.method == "POST":
        print(request.POST)

        # ✅ CORRECT MAPPING
        student.s_name = request.POST.get('name')
        student.s_age = request.POST.get('age')
        student.s_reg = request.POST.get('reg_no')
        student.s_dept = request.POST.get('department')

        student.save()
        return redirect('/')   # 🔥 MUST

    return render(request, 'edit.html', {"edit": student})
















































