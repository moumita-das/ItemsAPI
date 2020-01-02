from django import forms
from .models import ItemList

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model =ItemList
        fields = ['fname','lname','dob','img']

    def clean(self):
        fname = self.cleaned_data.get('fname')
        lname = self.cleaned_data.get('lname')
        #img = self.cleaned_data.get('img',False)
        #if not self.instance.img == img:
         #   self.add_error("Uploaded image format is wrong")
        if not fname.isalpha():
            self.add_error("Only letters allowed in first name")
        if not lname.isalpha():
            self.add_error("Only letters allowed in lat name")