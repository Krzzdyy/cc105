from django.shortcuts import render, redirect
from .models import Student
from . import views
from django.shortcuts import render, redirect, get_object_or_404    


def index(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        course = request.POST['course']
        enrollment_date = request.POST['enrollment_date']

        student = Student(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
            course=course,
            enrollment_date=enrollment_date
        )
        student.save()
        return redirect('index')

    return render(request, 'student_management_sys/index.html')

def read(request):
    students = Student.objects.all()
    return render(request, 'student_management_sys/read.html', {'students': students})

def update(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.student_id = request.POST['student_id']
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.date_of_birth = request.POST['date_of_birth']
        student.course = request.POST['course']
        student.enrollment_date = request.POST['enrollment_date']
        student.save()
        return redirect('read')
    return render(request, 'student_management_sys/update.html', {'student': student})

def delete(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        student.delete()
        return redirect('read')
    return render(request, 'student_management_sys/delete.html', {'student': student})


