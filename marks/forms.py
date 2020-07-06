from django.forms import ModelForm

from marks.models import StudentMark


class MarkForm(ModelForm):
    class Meta:
        model = StudentMark
        fields = ['mark', 'comment',]