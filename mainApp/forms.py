from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinValueValidator
from datetime import datetime
from .models import *


class LoginForm(AuthenticationForm):  # borrowed from Vishal's code
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
        exclude = ['endTime']

    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'
        self.fields['roomID'].widget.attrs['placeholder'] = 'roomID'
        self.fields['startTime'].widget.attrs['placeholder'] = 'Start Time'


class DischargeForm(forms.Form):
    patientID = forms.ModelChoiceField(queryset=Patient.objects.filter(pk__in=Admission.objects.filter(endTime__isnull=True).values('patientID')))

    def __init__(self, *args, **kwargs):
        super(DischargeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['patientID'].widget.attrs['placeholder'] = 'Patient ID'

    def save(self):
        data = self.cleaned_data
        admObj = Admission.objects.get(
            patientID=data['patientID'], endTime__isnull=True)
        admObj.roomID.available = True
        admObj.endTime = datetime.now()
        admObj.save()


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
    appointmentID = forms.ModelChoiceField(
        queryset=Appointment.objects.filter(appReport=""), required=True)
    appReport = forms.FileField(allow_empty_file=False, required=True)

    def __init__(self, *args, **kwargs):
        super(FileAppointmentReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['appointmentID'].widget.attrs['placeholder'] = 'Appointment ID'
        self.fields['appReport'].widget.attrs['placeholder'] = 'Appointment Report'

    def save(self):
        data = self.cleaned_data
        appObj = data['appointmentID']
        appObj.appReport = data['appReport']
        appObj.reportGenerationTime = datetime.now()
        appObj.save()

# doctor's form


class PrescriptionForm(forms.Form):
    appointmentID = forms.ModelChoiceField(
        queryset=Appointment.objects.filter(prescription__isnull=True), required=True)
    prescription = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    def save(self):
        data = self.cleaned_data
        appObj = data['appointmentID']
        appObj.prescription = data['prescription']
        appObj.save()


# front desk operator
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
    testID = forms.ModelChoiceField(Test.objects.filter(
        testReport=''), required=True)
    testReport = forms.FileField(allow_empty_file=False, required=True)

    def __init__(self, *args, **kwargs):
        super(UploadTestReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields['testID'].widget.attrs['placeholder'] = 'Test ID'

    def save(self):
        data = self.cleaned_data
        testObj = data['testID']
        testObj.testReport = data['testReport']
        testObj.reportGenerationTime = datetime.now()
        testObj.save()


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
    operationID = forms.ModelChoiceField(Operation.objects.filter(
        operationReport=""), required=True)
    opReport = forms.FileField(allow_empty_file=False, required=True)

    def __init__(self, *args, **kwargs):
        super(UploadOperationReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    def save(self):
        data = self.cleaned_data
        operationObj = data['operationID']
        operationObj.operationReport = data['opReport']
        operationObj.reportGenerationTime = datetime.now()
        operationObj.save()


class PatientInfoForm(forms.Form):
    patientID = forms.ModelChoiceField(Patient.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        super(PatientInfoForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
