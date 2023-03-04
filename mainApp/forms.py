from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinValueValidator

from .models import *

class LoginForm(AuthenticationForm): # borrowed from Vishal's code
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Stakeholder ID (e.g. 20CS10031)'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

class patientRegForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(patientRegForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class admissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(admissionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class dischargeForm(forms.ModelForm):
    patientID = forms.ModelChoiceField(queryset=Patient.objects.all())

    def __init__(self, *args, **kwargs):
        super(dischargeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class makeAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patientID', 'doctorID', 'startTime', 'priority']

    def __init__(self, *args, **kwargs):
        super(makeAppointment, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

# handled by data entry operator
class appointmentReportForm(forms.Form):
    appointmentID = forms.ModelChoiceField(queryset=Appointment.objects.filter(appReport__isnull=True))
    appReport = forms.FileField(allow_empty_file=False)
    def __init__(self, *args, **kwargs):
        super(appointmentReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

# doctor's form
class prescriptionForm(forms.Form):
    appointmentID = forms.ModelChoiceField(queryset=Appointment.objects.filter(prescription__isnull=True))
    prescription = forms.Textarea
    def __init__(self, *args, **kwargs):
        super(prescriptionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
    

class testScheduleForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['testName', 'patientID', 'scheduledTime']
    def __init__(self, *args, **kwargs):
        super(testScheduleForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
