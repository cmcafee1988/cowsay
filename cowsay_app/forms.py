from django import forms

class User_Input_Form(forms.Form):
    text = forms.CharField(max_length=120)