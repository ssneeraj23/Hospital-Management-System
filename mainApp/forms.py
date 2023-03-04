from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinValueValidator

from .models import *

class LoginForm(AuthenticationForm): # borrowed from Vishal's code
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Stakeholder ID'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

class PatientRegForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PatientRegForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['dob'].widget.attrs['placeholder'] = 'DOB'
        self.fields['gender'].widget.attrs['placeholder'] = 'Gender'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Email-ID'

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'
        self.fields['roomID'].widget.attrs['placeholder'] = 'roomID'
        self.fields['startTime'].widget.attrs['placeholder'] = 'Start Time'
        self.fields['endTime'].widget.attrs['placeholder'] = 'End Time'

class DischargeForm(forms.Form):
    patientID = forms.ModelChoiceField(queryset=Patient.objects.all())

    def __init__(self, *args, **kwargs):
        super(DischargeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'


class MakeAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patientID', 'doctorID', 'startTime', 'priority']

    def __init__(self, *args, **kwargs):
        super(MakeAppointmentForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'
        self.fields['doctorID'].widget.attrs['placeholder'] = 'Doctor ID'
        self.fields['startTime'].widget.attrs['placeholder'] = 'Start Time'
        self.fields['priority'].widget.attrs['placeholder'] = 'Priority'

# handled by data entry operator
class FileAppointmentReportForm(forms.Form):
    appointmentID = forms.ModelChoiceField(queryset=Appointment.objects.filter(appReport__isnull=True), required=True)
    appReport = forms.FileField(allow_empty_file=False, required=True)
    def __init__(self, *args, **kwargs):
        super(FileAppointmentReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['appointmentID'].widget.attrs['placeholder'] = 'Appointment ID'
        self.fields['appReport'].widget.attrs['placeholder'] = 'Appointment Report'

# doctor's form
class PrescriptionForm(forms.Form):
    appointmentID = forms.ModelChoiceField(queryset=Appointment.objects.filter(prescription__isnull=True), required=True)
    prescription = forms.Textarea()
    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        
    
# front end operator
class ScheduleTestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['testName', 'patientID', 'scheduledTime']
    def __init__(self, *args, **kwargs):
        super(ScheduleTestForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'
        self.fields['testName'].widget.attrs['placeholder'] = 'Test'
        self.fields['scheduledTime'].widget.attrs['placeholder'] = 'Scheduled Time'

# data entry operator
class UploadTestReportForm(forms.Form):
    testID = forms.ModelChoiceField(Test.objects.filter(testReport__isnull=True), required=True)
    testReport = forms.FileField(allow_empty_file=False, required=True)
    def __init__(self, *args, **kwargs):
        super(UploadTestReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

class ScheduleOperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['opName', 'patientID', 'doctorID', 'opTheatre', 'startTime']
    
    def __init__(self, *args, **kwargs):
        super(ScheduleOperationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['opName'].widget.attrs['placeholder'] = 'Operation Name'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'
        self.fields['doctorID'].widget.attrs['placeholder'] = 'Doctor ID'
        self.fields['startTime'].widget.attrs['placeholder'] = 'Start Time'
        self.fields['opTheatre'].widget.attrs['placeholder'] = 'Operation Theatre'

class UploadOperationReportForm(forms.Form):
    operationID = forms.ModelChoiceField(Operation.objects.filter(operationReport__isnull=True), required=True)
    opReport = forms.FileField(allow_empty_file=False, required=True)
    def __init__(self, *args, **kwargs):
        super(UploadOperationReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
