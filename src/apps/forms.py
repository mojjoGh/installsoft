from django import forms
from .models import App

class AppForm(forms.ModelForm):
    title           = forms.CharField(
        label='', 
        widget=forms.TextInput(
            attrs={"placeholder": "your title"}
        )
    )
    description     = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "new-class-name two",
                "rows": 20,
                "cols": 120
            }
        )
    )
    category           = forms.IntegerField(
        label='', 
        widget=forms.TextInput(
            attrs={"placeholder": "category"}
        )
    )

    class Meta:
        model = App
        fields = [
            'title',
            'description',
            'category'
        ]

    # def clean_title(self, *args, **kwargs):
    #     pass
    #     # title = self.cleaned_data.get("title")
    #     # if not "CFE" in title:
    #     #     raise forms.ValidationError("This is not a valid title")
    #     # if not "news" in title:
    #     #     raise forms.ValidationError("This is not a valid title")
    #     # return title

