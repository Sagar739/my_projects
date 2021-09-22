from django import forms
from .models import Person, Participant, Student
import datetime

class PersonForm(forms.ModelForm):
    dob = forms.DateField(
        label='Date of Birth',
        widget=forms.SelectDateWidget(years=range(1970,datetime.datetime.now().year))
    )

    class Meta:
        model = Person
        fields = ("__all__")

class ParticipantForm(forms.ModelForm):
    ## set the label name of the date field.
    dob = forms.DateField(
        label='Date of birth', 
        # Set the years range from 1985 to (current year - 15)
        widget=forms.SelectDateWidget(years=range(1985, datetime.date.today().year-15))
    )
    
    class Meta:
        model = Participant
        fields = ("__all__")

class StudentForm(forms.ModelForm):
    s_no = forms.CharField(label='Student Number')
    s_name = forms.CharField(label='Student Name')
    s_percentage = forms.FloatField(label='Student Percentage',
                   widget=forms.NumberInput(attrs={'step':any}))

    class Meta:
        model = Student
        fields = ("__all__")