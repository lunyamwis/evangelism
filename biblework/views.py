from django.shortcuts import render, redirect, get_object_or_404
from .models import StudySchedule, LessonMaterial, OutreachTeamMember, VisitLog
from .forms import StudyScheduleForm, LessonMaterialForm, OutreachTeamMemberForm, VisitLogForm


def home(request):
    studies = StudySchedule.objects.all().order_by('date', 'time')
    materials = LessonMaterial.objects.all()
    team_members = OutreachTeamMember.objects.all()
    visits = VisitLog.objects.all().order_by('-date')

    context = {
        'studies': studies,
        'materials': materials,
        'team_members': team_members,
        'visits': visits,
    }
    return render(request, 'biblework/home.html', context)



def study_schedule_list(request):
    studies = StudySchedule.objects.all().order_by('date', 'time')
    if request.method == 'POST':
        form = StudyScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_schedule_list')
    else:
        form = StudyScheduleForm()
    return render(request, 'biblework/study_schedule.html', {'studies': studies, 'form': form})


def lesson_material_list(request):
    materials = LessonMaterial.objects.all()
    if request.method == 'POST':
        form = LessonMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_material_list')
    else:
        form = LessonMaterialForm()
    return render(request, 'biblework/lesson_materials.html', {'materials': materials, 'form': form})


def outreach_team_list(request):
    team_members = OutreachTeamMember.objects.all()
    if request.method == 'POST':
        form = OutreachTeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outreach_team_list')
    else:
        form = OutreachTeamMemberForm()
    return render(request, 'biblework/outreach_teams.html', {'team_members': team_members, 'form': form})


def visit_log_list(request):
    visits = VisitLog.objects.all().order_by('-date')
    if request.method == 'POST':
        form = VisitLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_log_list')
    else:
        form = VisitLogForm()
    return render(request, 'biblework/visit_logs.html', {'visits': visits, 'form': form})
