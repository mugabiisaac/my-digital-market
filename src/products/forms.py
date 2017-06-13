from django import forms

from .models import Product
from django.utils.text import slugify

PUBLISH_CHOICES = (
    ('', ""),
    ('publish', "Publish"),
    ('draft', "Draft"),
)
class ProductAddForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    publish = forms.ChoiceField(choices=PUBLISH_CHOICES, required=False)


    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than $1")
        elif price >= 99.99:
            raise forms.ValidationError("price muse be less than $100")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characters long.")


class ProductModelForm(forms.ModelForm):
    tags = forms.CharField(label='related tags', required=False)
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "media",
        ]
        widgets = {
            "description": forms.Textarea(
                    attrs={
                        "placeholder": "new Description"
                    }
            )
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
    #    title = cleaned_data.get("title")
    #    slug = slugify(title)
    #    qs = Product.objects.filter(slug=slug).exists()
    #    if qs:
    #        raise forms.ValidationError("Title is taken, try new title")
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("price must be greater than $1.00")
        elif price >= 100.00:
            raise forms.ValidationError("price must be less than $100.00")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("title must be greater than 3 characters long")
