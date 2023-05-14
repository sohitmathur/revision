from django.shortcuts import render
# from django .http import HttpResponse
from.forms import StudentForm

# Create your views here.


def student_input_view(request):
  sent=False
  if request.method=='POST':
    form=StudentForm(request.POST)
    my_dict={'form':form}
    if form.is_valid():
     print('Form Validation Success and printing data')
     print('Name:',form.cleaned_data['name'])
     print('roll',form.cleaned_data['marks'])
     print('course:',form.cleaned_data['course'])
     sent=True
form=StudentForm()

    return render(request,'dsc/student.html',context=my_dict)

# def display(r):
#     my_dict= {'company':'tcs','sal':100000,'id':101}
#     return render(r,'dsc/student.html',context=my_dict)
