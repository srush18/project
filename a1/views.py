from django.shortcuts import render, redirect
from django.http import Http404  # Create your views here.
from a1.models import Student
from django.contrib import messages
from django.conf import settings


def register(request):

    if request.method == "POST":

        # personal info
        student_image = request.POST['student_image']
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        # academic info
        college_name = request.POST['college_name']
        enrollment_year = request.POST['enrollment_year']
        course = request.POST['course']
        branch = request.POST['branch']
        roll_no = request.POST['roll_no']

        college_email = request.POST['college_email']
        current_cgpa = request.POST['current_cgpa']
        # contact info
        personal_email = request.POST['personal_email']
        phone = request.POST['contact_number']
        current_address = request.POST['current_address']
        permanent_address = request.POST['permanent_address']
        if Student.objects.all().filter(roll_no=roll_no).exists():
            messages.info(request, "roll number already exists")
            return redirect(register)
        elif Student.objects.all().filter(college_email=college_email).exists():
            messages.info(request, "email already registres")
            return redirect(register)
        elif Student.objects.all().filter(phone=phone).exists():
            messages.info(request, "phone number already registres")
            return redirect(register)

        s = Student(student_image=student_image, name=name, personal_email=personal_email, phone=phone, gender=gender, dob=dob, current_address=current_address, permanent_address=permanent_address,
                    college_name=college_name, enrollment_year=enrollment_year, course=course, branch=branch, roll_no=roll_no, college_email=college_email, current_cgpa=current_cgpa)
        s.save()
        messages.info(request, "successfully registred")
    return render(request, "index.html")


def qr(request, pk):
    try:
        stu = Student.objects.all().filter(roll_no=pk)
        # img = Student.objects.filter(file_type='student_image')
        # st = [stu, img]
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'qr.html', {'students': stu})


def student(request, pk):
    try:
        stu = Student.objects.all().filter(roll_no=pk)
        link="http://127.0.0.1:8000/student/update/"+pk
        # img = Student.objects.filter(file_type='student_image')
        # st = [stu, img]
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'd.html', {'students': stu,'link':link})

    # return render(request, 'd.html', {'students': st, 'media_url': settings.MEDIA_URL})


def update(request, pk):
    stu = Student.objects.get(roll_no=pk)
    if request.method == "POST":
        stu.personal_email = request.POST['personal_email']
        stu.phone = request.POST.get('contact_number', None)
        stu.current_address = request.POST.get('current_address', None)
        stu.permanent_address = request.POST.get('permanent_address', None)
        stu.current_cgpa = request.POST.get('current_cgpa', None)
        stu.save()
        messages.info(request, "Information updated successfully")
    return render(request, 'update.html', {'student': stu})


def delete(request):
    if request.method == "POST":
        pk = request.POST['roll_no']
        try:
            stu = Student.objects.get(roll_no=pk)
        except Student.DoesNotExist:
            raise Http404("Student does not exist") 
        stu.delete()
        messages.info(request, "User deleted successfully")
    return render(request, 'delete.html')
