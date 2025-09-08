from django import forms
from .models import InternshipApplication

class InternshipApplicationForm(forms.ModelForm):
    domains = forms.MultipleChoiceField(
        choices=[
            ('C', 'C'),
('Java', 'Java'),
('Python', 'Python'),
('AI', 'AI'),
('UI & UX Design', 'UI & UX Design'),
('MERN Stack', 'MERN Stack'),
('DCAC','DCAC'),
('DCAJAVA','DCAJAVA'),
('DCAPYTHON','DCAPYTHON'),

        ],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = InternshipApplication
        exclude = []
