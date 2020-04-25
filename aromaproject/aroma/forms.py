from django import forms
from .models import *


class BookForm(forms.ModelForm): #было forms.Form
    # title = forms.CharField(max_length=128)
    # author = forms.CharField(max_length=128)
    # genre = forms.CharField(max_length=128)
    # pages = forms.IntegerField()
    # format = forms.CharField(max_length=64)
    # publish_year = forms.IntegerField()
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # author.widget.attrs.update({'class': 'form-control'})
    # genre.widget.attrs.update({'class': 'form-control'})
    # pages.widget.attrs.update({'class': 'form-control'})
    # format.widget.attrs.update({'class': 'form-control'})
    # publish_year.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pages', 'format', 'publish_year']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.TextInput(attrs={'class': 'form-control'}),
            'format': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_year': forms.TextInput(attrs={'class': 'form-control'})
        }

    # def clean_author(self):
    #     new_author = self.cleaned_data['author'].lower().title()
    #     self.author = new_author
    #     return self.author

    #def save(self):
    #    new_book = Book.objects.create(
    #        title=self.cleaned_data['title'],
    #        author=self.cleaned_data['author'],
    #        genre=self.cleaned_data['genre'],
    #        pages=self.cleaned_data['pages'],
    #        format=self.cleaned_data['format'],
    #        publish_year=self.cleaned_data['publish_year'])
    #    new_book.author = self.clean_author() # моё добавление
    #    return new_book

#bk = Book({'title': 'dscdds', 'author': 'fdsvvs', 'genre': '32d', 'pages': '1212', 'format': 'enak', 'publish_year': '1212'})