from django import forms 

from .models import Post, Show

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UploadFileForm(forms.Form):
    title=forms.CharField(max_length=100)
    platform=forms.CharField(max_length=100)
    genre=forms.CharField(max_length=100)
    score_audience=forms.CharField(max_length=100)
    score_critic=forms.CharField(max_length=100)
    img=forms.CharField(max_length=200)

    class Meta:
        model = Show
        fields = ('title', 'platform','genre',"score_audience","score_critic",'img',)