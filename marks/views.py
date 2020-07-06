from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from marks.models import StudentMark
from marks.forms import MarkForm


@login_required(login_url='/login/')
def home(request):
    user = request.user
    groups = user.groups.all()
    if groups.count() != 1:
        message = f'{user.email} is not related to some group or {user.email} related more than 1 group'
        context = {'message': message}
        return render(request, 'marks/home.html', context=context)
    group = groups[0]
    if group.name == 'Teachers':
        return redirect('teacher-dashboard')
    elif group.name == 'Students' or group.name == 'Mentor':
        return redirect('student-dashboard')
    message = 'Unsupported group'
    context = {'message': message}
    return render(request, 'marks/home.html', context=context)


@permission_required('marks.can_view_all_marks', login_url='/login/')
def teacher_dashboard(request):
    marks = StudentMark.objects.all().select_related('student')
    context = {'marks': marks,}
    return render(request, 'marks/teacher_dashboard.html', context)


class StudentView(PermissionRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'
    permission_required = ('marks.can_add_marks_yopta',)

    def get(self, request):
        form = MarkForm()
        context = {'form': form, }
        return render(request, 'hydrology/record.html', context)


class StudentDashboardView(PermissionRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'
    permission_required = ('marks.can_view_only_own_marks',)

    def get(self, request):
        user = request.user
        marks = StudentMark.objects.filter(student=user)
        context = {
            'student': user,
            'marks': marks,
        }
        return render(request, 'marks/student_dashboard.html', context=context)

