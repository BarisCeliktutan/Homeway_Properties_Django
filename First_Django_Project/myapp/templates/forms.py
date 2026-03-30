from django import forms

class CreateNewList(forms.Form):
    list_name = forms.CharField(label="Name", max_length=200)

class CreateNewItem(forms.Form):
    name = forms.CharField(label="To Do", max_length=200)
    check = forms.BooleanField(label="Done", required=False)

