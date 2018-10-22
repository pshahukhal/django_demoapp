from django import forms

from blog_app.models import Comments,Posts

class PostForm(forms.ModelForm):
    class Meta():
        model = Posts
        fields = {'author','title','text'}
        widgets = {
        'text' : forms.Textarea(attrs={'class':'editable'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = {'author', 'text'}
        widgets = {
        'text' : forms.Textarea(attrs={'class':'editable'})
        }
