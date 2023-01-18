from django import forms

from app.models import Review, Item


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("reviewed_by", "reviewed_by_email", "review", )

        widgets = {
            'reviewed_by': forms.TextInput(attrs={'class': 'form-control'}),
            'reviewed_by_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }
