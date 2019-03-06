from django import forms


class VideoForms(forms.Form):
    videoname = forms.CharField(max_length=200,
        widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Name',
        'id':'InputName'
        }))
    videodesc = forms.CharField(widget=forms.Textarea({
    'class':'form-control',
    'rows':'5',
    'id':'comment',
    'placeholder':'Comment'
    }))
