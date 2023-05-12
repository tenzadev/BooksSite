from .models import Order, Product, Comment
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
