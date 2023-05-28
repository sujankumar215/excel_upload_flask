from django.shortcuts import render
from admissions.models import Student,Teacher
from admissions.forms import StudentModelForm,VendorForm
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse
from django.urls import  reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

#function based views 
@login_required
def homePage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'registration/logout.html')

@login_required
def addAdmission(request):
    form = StudentModelForm
    studentform = {'Form':form}
    #values = {"name":"Sujan","age":36,"adderss":"Kavali"}
    if request.method=='POST':
        # check if the method we get the data is Post or not 
        form = StudentModelForm(request.POST) # check if the data is valid or not 
        if form.is_valid():
            form.save()
        return homePage(request) # return to home page after submission
    return render(request,'admissions/add-admissions.html',studentform)

@login_required
def admissionReport(request):
    #get sll the records from the table
    #store it in dictionary students 
    results = Student.objects.all() # Select * from students
    students={'allstudents':results}
    return render(request,'admissions/admission-report.html',students)

@login_required
def addVendor(request):
    vform = VendorForm
    vendortform = {'Form':vform}
    
    if request.method=='POST':
        # check if the method we get the data is Post or not 
        form = StudentModelForm(request.POST) # check if the data is valid or not 
        if form.is_valid():
            print(vform.cleaned_data['name'])
            print(vform.cleaned_data['address'])
            print(vform.cleaned_data['contact'])
            print(vform.cleaned_data['item'])
        return homePage(request) # return to home page after submission
    return render(request,'admissions/add-vendor.html',vendortform)

@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s= Student.objects.get(id=id) # select * from admission_student where id=id 
    s.delete() # Delete Selected Student
    return admissionReport(request)

@login_required
@permission_required('admissions.change_student')
def updateStudent(request,id):
    s= Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form':form}

    if request.method=='POST':
        # check if the method we get the data is Post or not 
        form = StudentModelForm(request.POST,instance=s) # check if the data is valid or not  ,do changes on existing student
        if form.is_valid():
            form.save()
        return admissionReport(request)  # return redirect('adm/admreport')
    # return to home page after submission
    return render(request,'admissions/update-admission.html',dict)

#@login_required
class firstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1> Hello ... this my first base view</h1>")
        
    
#@login_required
class TeacherRead(ListView):
    model=Teacher

#@login_required
class GetTeacher(DetailView):
    model=Teacher

#@login_required
class CreateTeacher(CreateView):
    model=Teacher
    fields= ('name','subject','exp','contact')

#@login_required
class UpdateTeacher(UpdateView):
    model=Teacher
    fields= ('name','contact')

#@login_required
class DeleteTeacher(DeleteView):
    model=Teacher
    success_url =reverse_lazy('listteachers')