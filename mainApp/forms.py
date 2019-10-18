from django import forms


class HomeForm(forms.Form):
    n_users = forms.IntegerField(label='Получить N пользователей с randomuser.me', initial=7)
