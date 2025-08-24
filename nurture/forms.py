from django import forms
from .models import ChurchMember, BaptizedMember, FollowUpInteraction

class ChurchMemberForm(forms.ModelForm):
    class Meta:
        model = ChurchMember
        fields = ['full_name', 'contact_info']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class BaptizedMemberForm(forms.ModelForm):
    class Meta:
        model = BaptizedMember
        fields = ['full_name', 'baptism_date', 'contact_info', 'originating_outreach', 'assigned_follower', 'notes']
        widgets = {
            'baptism_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class FollowUpInteractionForm(forms.ModelForm):
    class Meta:
        model = FollowUpInteraction
        fields = ['date', 'method', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    