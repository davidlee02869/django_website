from django import forms
from .models import Client, Job, Scheduler

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class SchedulerForm(forms.ModelForm):
    class Meta:
        model = Scheduler
        fields = '__all__'