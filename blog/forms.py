from django import forms
from blog.models import Post, Comment, Guest_book

#ModelForm is much shorter, more convenient
class PostForm(forms.ModelForm):
    is_agree  =forms.BooleanField(label='약관동의',
        error_messages={'required':'약관에 동의해주셔야 서비스이용이 가능합니다'})

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['message']
        #','있으면 튜플. 파이썬 문법;튜플로 해야 걔만 나옴, 그게 아님 리스트로 쓰세요!별차이없음

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest_book
        fields = '__all__'
