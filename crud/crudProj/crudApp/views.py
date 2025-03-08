from django.shortcuts import render, redirect
from . models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def addStudent(request):
    if request.method == 'POST':
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        dateOfBirth = request.POST["dateOfBirth"]
        course = request.POST["course"]
        enrollmentDate = request.POST["enrollmentDate"]

        newStudent = Student(firstName=firstName, lastName=lastName, email=email, dateOfBirth=dateOfBirth,  course=course, enrollmentDate=enrollmentDate)
        newStudent.save()

        return redirect('/')
    existing_emails = list(Student.objects.values_list('email', flat=True))
    return render(request, 'addStudent.html', {'existing_emails': existing_emails})

def editStudent(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'editStudent.html', {'student':student})

def updateStudent(request, id):
    student = Student.objects.get(id=id)
    student.firstName = request.POST["firstName"]
    student.lastName = request.POST["lastName"]
    student.email = request.POST["email"]
    student.dateOfBirth = request.POST["dateOfBirth"]
    student.course = request.POST["course"]
    student.enrollmentDate = request.POST["enrollmentDate"]
    student.save()

    return redirect('/')

def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')