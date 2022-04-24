from django import forms
from .models import Post, Comment, Critique


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'author','body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),
        }


class CommentForm(forms.ModelForm):
    CHOICES = (
      ((0), (0)),
      ((1), (1)),
      ((2), (2)),
      ((3), (3)),
      ((4), (4)),
      ((5), (5)),
    )
    rating = forms.ChoiceField(label='Note', widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Comment
        fields = ('name', 'body', 'rating')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),

        }


class CritiqueForm(forms.ModelForm):
    class Meta:
        model = Critique
        fields = ('title', 'title_tag', 'body', 'author', 'body', 'header_image', 'title_second',
                  'comment')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),
            'title_second': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),
        }


class EditCritiqueForm(forms.ModelForm):
    class Meta:
        model = Critique
        fields = ('title', 'title_tag', 'body', 'title_second','comment')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),
            'title_second': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put a title..'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write here..'}),
        }

