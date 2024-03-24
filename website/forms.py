from django.forms import ModelForm 
from .models import JobSeeker,Vacancy,JobPost
from django import forms


class JobSeekerForm(ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['qualification_id',
                        'position_id',
                        'first_name',
                        'last_name',
                        'phone_number',
                        'email',
                        'work_experience',
                        'current_police_check',
                        'children_check',
                        'address',
                        'cv',
                        'qualification_pdf']


        labels = {
            'qualification_id': 'Qualification',
            'position_id': 'Position'
        }


class VacancyForm(ModelForm):


    class Meta:
        model = Vacancy

        proposed_commencement_Date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

        fields = '__all__'


        







