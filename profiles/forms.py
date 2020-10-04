from django import forms
from .models import Profile, RelationShip


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'bio', 'avatar' )