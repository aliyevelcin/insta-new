from django import forms 
from core.models import Story , Comment , Post

class StoryForm(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Story
        fields = ("image", )

class CommentForm(forms.ModelForm):
    description = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Yorum ekle',
                'class' : 'comment',
            }))

    class Meta:
        model = Comment 
        fields = ('description',)

class PostForm(forms.ModelForm):
    image = forms.FileField()
    description = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'description',
                'class' : 'login-input',
            }))
    likes =  forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'like',
                'class' : 'login-input',
            }))
    
    class Meta:
        model = Post
        fields = ("image" , "description","likes",)
