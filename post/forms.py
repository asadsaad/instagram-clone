from django import forms
from .models import Post
from .models import Comments


class PostForm(forms.ModelForm):
	content=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'post_form','rows':'5','cols':'50','placeholder':'Write Something....'}))
	class Meta:
 		model=Post
 		fields=('content','img')

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['content'].widget.attrs['placeholder'] = 'Write Something'


class CommentForm(forms.ModelForm):
	comment_content=forms.CharField(label="Comment",widget=forms.Textarea(attrs={'class':'comment-form','rows':'1','cols':'40'}))
	class Meta:
 		model=Comments
 		fields=('comment_content',)       