from django import forms
from .models import Pictures, Albums

class UploadFileForm(forms.ModelForm):
    album = forms.CharField(max_length=50,label='',
                           widget=forms.Textarea(attrs={
                               'row': '3',
                                'placeholder':'Say something..',
                           }) )
    # file = forms.ImageField()
    class Meta:
        model = Albums
        fields = ('album',)





# Create your forms here.
class ImageForms(forms.ModelForm):
    image = forms.ImageField(label='')
    class Meta:
        model = Pictures
        fields = ('image',)


'''class AlbumForms(forms.ModelForm):
    body = forms.CharField(max_length=50, label='',
                           widget=forms.Textarea(attrs={
                               'row': '10',

                           }))

    class Meta:
        model = Albums
        fields = ('album',)'''
