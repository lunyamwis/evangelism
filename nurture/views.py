from django.shortcuts import render, redirect, get_object_or_404
from .models import ChurchMember, BaptizedMember, FollowUpInteraction
from .forms import ChurchMemberForm, BaptizedMemberForm, FollowUpInteractionForm

def dashboard_home(request):
    # A dashboard overview - customize as needed
    return render(request, 'nurture/dashboard_home.html')

def church_member_list(request):
    members = ChurchMember.objects.all()
    if request.method == 'POST':
        form = ChurchMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('church_member_list')
    else:
        form = ChurchMemberForm()
    return render(request, 'nurture/church_member_list.html', {'members': members, 'form': form})

def baptized_member_list(request):
    members = BaptizedMember.objects.all().order_by('-baptism_date')
    if request.method == 'POST':
        form = BaptizedMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baptized_member_list')
    else:
        form = BaptizedMemberForm()
    return render(request, 'nurture/baptized_member_list.html', {'members': members, 'form': form})

def followup_list(request, member_id):
    member = get_object_or_404(BaptizedMember, id=member_id)
    followups = member.follow_ups.all().order_by('-date')
    return render(request, 'nurture/followup_list.html', {'member': member, 'followups': followups})

def followup_add(request, member_id):
    member = get_object_or_404(BaptizedMember, id=member_id)
    if request.method == 'POST':
        form = FollowUpInteractionForm(request.POST)
        if form.is_valid():
            followup = form.save(commit=False)
            followup.member = member
            followup.save()
            return redirect('followup_list', member_id=member.id)
    else:
        form = FollowUpInteractionForm()
    return render(request, 'nurture/followup_form.html', {'form': form, 'member': member})
