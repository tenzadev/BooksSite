from django import forms
from .models import TGUser


class BookForm(forms.Form):
    title = forms.CharField(max_length=200, label="Kitob nomi", widget=forms.TextInput(attrs={"placeholder": "Kitobning to'liq nomi"}))
    description = forms.CharField(max_length=3000, widget=forms.Textarea, label="Batafsil ma'lumot", help_text="Kitob janri haqida")
    publish_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}), disabled=True)
    image = forms.ImageField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    copy_count = forms.IntegerField(min_value=1, max_value=10000)
    langs = forms.TypedChoiceField(choices=(
        (None, "Choose language"),
        ("eng", "English"),
        ("rus", "Russian"),
        ("uzb", "Uzbek")
    ), coerce=str.upper)
    is_active = forms.NullBooleanField()
    password = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput)

    def save(self, commit=True):
        # print(self)
        pass


class TGUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.PasswordInput)
    birth_day = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = TGUser
        fields = "__all__"


