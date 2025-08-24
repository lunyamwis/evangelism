from django import forms
from .models import StudySchedule, LessonMaterial, OutreachTeamMember, VisitLog

class StudyScheduleForm(forms.ModelForm):
    class Meta:
        model = StudySchedule
        fields = ['date', 'time', 'location', 'topic', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LessonMaterialForm(forms.ModelForm):
    class Meta:
        model = LessonMaterial
        fields = ['title', 'author', 'resource_link', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class OutreachTeamMemberForm(forms.ModelForm):
    class Meta:
        model = OutreachTeamMember
        fields = ['name', 'role', 'contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class VisitLogForm(forms.ModelForm):
    class Meta:
        model = VisitLog
        fields = ['date', 'address', 'contact_person', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
