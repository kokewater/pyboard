from django import forms

from .models import Thread, Comment


class ThreadCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-4'

    class Meta:
        model = Thread
        fields = ('title', 'description')


class ThreadCommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-4'

    class Meta:
        model = Comment
        fields = ('name','body')