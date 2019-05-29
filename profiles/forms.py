from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_img','cover_img','location','education','work_at','bio')