from django import forms
from .models import Mentor

class BecomeMentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = [
            'first_name',
            'second_name',
            'education_info',
            'bio_info',
            'skills',
            'social_media_profiles',
            'contact_details',
            'mentor_type',
            'profile_pic',
        ]
        widgets = {
            'education_info': forms.Textarea(attrs={'rows': 3}),
            'bio_info': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'social_media_profiles': forms.Textarea(attrs={'rows': 3}),
            'contact_details': forms.Textarea(attrs={'rows': 3}),
        }
