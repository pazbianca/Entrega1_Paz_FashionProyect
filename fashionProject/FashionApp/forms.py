from django import forms

class FashionIcons_form(forms.Form):
    name = forms.CharField(max_length=40)
    age = forms.IntegerField()
    dateOfBirth = forms.DateField()
    profession = forms.CharField(max_length=40) 
    description = forms.CharField(max_length=800)

class FashionBrands_form(forms.Form):
    name = forms.CharField(max_length=40)
    founder = forms.CharField(max_length=40)
    foundedDate = forms.DateField()
    headquarters = forms.CharField(max_length=40)
    description = forms.CharField(max_length=800)

class FashionShows_form(forms.Form):
    name = forms.CharField(max_length=40)
    brand = forms.CharField(max_length=40)
    collectionPresented = forms.CharField(max_length=40)
    fashionCapital = forms.CharField(max_length=40)
    date = forms.DateField()
    description = forms.CharField(max_length=800)

