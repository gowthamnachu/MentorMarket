from django import forms
from .models import Mentor

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = [
            'username', 'first_name', 'second_name', 'email',
            'phone', 'experience', 'skills', 'mentor_type'
        ]
