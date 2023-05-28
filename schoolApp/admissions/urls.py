from django.urls import path
from admissions.views import addAdmission,admissionReport,addVendor,deleteStudent,updateStudent
from admissions.views import firstClassBasedView,TeacherRead,GetTeacher,CreateTeacher,UpdateTeacher,DeleteTeacher
from django.contrib.auth.decorators import login_required,permission_required
urlpatterns = [

    path('newadm/', addAdmission),
    path('admreport/', admissionReport),
    path('newvendor/', addVendor),
    path('delete/<int:id>',deleteStudent),
    path('update/<int:id>',updateStudent),
    path('firstcbv/',login_required(firstClassBasedView.as_view())),
    path('teacherslist/',login_required(TeacherRead.as_view()),name='listteachers'),
    path('getteacherdetail/<int:pk>/',login_required(GetTeacher.as_view()),name='getteacher'),
    path('addteacher/',login_required(CreateTeacher.as_view())),
    path('updateteacher/<int:pk>/',login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/',login_required(DeleteTeacher.as_view())),
]

