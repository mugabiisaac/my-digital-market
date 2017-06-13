from django import forms


class NewSellerForm(forms.Form):
    agree = forms.BooleanField(label='agree to terms', widget=forms.CheckboxInput)
