from django import forms
from django.utils import timezone


from .models import *

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields = [
            'expedition_name',
            'expedition_id',
            'expedition_image',
            'description'
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'image',
            'subject',
            'caption',
            'article_id',
            'expedition_id',
            'tags'
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'text',
            'article_id',
            'expedition_id',
            'tags'
        ]


class JeepForm(forms.ModelForm):
    class Meta:
        model = Jeep
        fields = [
            'jeep_name',
            'image',
            'history',
            'specs'
        ]


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'name',
            'profile_pic',
            'resume_pdf',
            'certification_pdf',
            'introduction',
            'about',
            'education_1',
            'education_2'
        ]



