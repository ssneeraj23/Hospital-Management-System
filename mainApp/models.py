from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, AbstractUser


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = [
        ('d', 'Doctor'),
        ('fdo', 'Front Desk Operator'),
        ('deo', 'Data Entry Operator'),
    ]
    role = models.CharField(max_length=3, choices=ROLES, default='d')

    def __str__(self):
        return str(self.username)

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100, default="John Doe")
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.pk) + " - " + self.name  # necessary typecast


class Room(models.Model):
    roomType = [('w', "Ward"), ('o', 'Operation Theatre')]
    type = models.CharField(max_length=10, choices=roomType, default='w')
    available = models.BooleanField(default=False)

    def __str__(self):
        if self.type == 'w':
            return "Room " + str(self.pk) + ' - Ward'
        elif self.type == 'o':
            return "Room " + str(self.pk) + ' - Operation Theatre'
        


class Doctor(models.Model):
    username = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Vijay")
    address = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    department = models.CharField(max_length=20)
    officeNumber = models.CharField(max_length=10, validators=[RegexValidator(
        r'^\d{1,5}', message="Office number should be between 1 and 5 digits")])

    def __str__(self):
        return str(self.pk) + " " + self.name  # necessary typecast


class Appointment(models.Model):
    patientID = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_booked')
    doctorID = models.ForeignKey(
        Doctor, related_name='doctor_assigned', on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    # endTime = models.DateTimeField(null=True, blank=True)
    prescription = models.TextField(null=True, blank=True)
    priorityChoices = [
        (0, "Low"),
        (1, "Medium"),
        (2, "High")
    ]
    priority = models.IntegerField(choices=priorityChoices, default=0)
    appReport = models.FileField(null=True, blank=True)
    reportGenerationTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.pk) + " - " + str(self.patientID) + " - " + self.startTime.strftime("%d/%m/%Y, %H:%M:%S")


class Admission(models.Model):
    def _validate_room(value):
        if Room.objects.get(pk=value).type != 'w':
            raise ValidationError('This room is not an admission ward')
    patientID = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_admitted')
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE,
                               related_name='patient_admitted', validators=[_validate_room])
    startTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if Admission.objects.filter(patientID=self.patientID).filter(endTime__isnull=True).exists():
            raise ValidationError(
                'Cannot admit the same patient again before discharging them')


class Test(models.Model):
    testName = models.CharField(max_length=50)
    patientID = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_tested')
    scheduledTime = models.DateTimeField()
    testReport = models.FileField(null=True, blank=True)
    reportGenerationTime = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return "Test ID - " + str(self.pk)


class Operation(models.Model):
    def _validate_room(value: Room):
        if Room.objects.get(pk=value).type != 'o':
            raise ValidationError('This room is not suitable for operations.')
    opName = models.CharField(max_length=50)
    patientID = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient_operated')
    doctorID = models.ManyToManyField(Doctor, related_name='doctors')
    opTheatre = models.ForeignKey(Room, related_name='where', validators=[
        _validate_room], on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True, blank=True)
    operationReport = models.FileField(null=True, blank=True)
    reportGenerationTime = models.DateTimeField(null=True, blank=True)
