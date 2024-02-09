from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import login, logout


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        elif request.user.is_student:
            return redirect('students:quiz_list')
        else:
            return redirect('admin:index')
    return render(request, 'classroom/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'classroom/home.html')