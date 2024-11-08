from django import forms
from .models import Role, Criteria, LinkedAssessment


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']


class CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ['name', 'weight', 'role']


class LinkedAssessmentForm(forms.ModelForm):
    class Meta:
        model = LinkedAssessment
        fields = ['name', 'description', 'role']
