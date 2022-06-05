from core.models import Contact
from django import forms



from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class AllAuthSignupForm(forms.Form):

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
        attrs={
            'required_score':0.50,
        }
    )
    )

    def save(self, request, user):
        user = super(AllAuthSignupForm, self).save(request)
        return user

from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
        attrs={
            'required_score':0.50,
        }

    )
    )


    # def login(self, *args, **kwargs):

    #     Add your own processing here.

    #     You must return the original result.
    #     return super(MyCustomLoginForm, self).login(*args, **kwargs)
class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=100, label='Nombre', widget=forms.TextInput(attrs={
        'placeholder': "Tu Nombre",
    }))
    email = forms.EmailField(label='Correo', widget=forms.TextInput(attrs={
        'placeholder': "Tu Correo Electronico"
    }))
    message = forms.CharField(max_length=100, label='Mensaje', widget=forms.TextInput(attrs={
        'placeholder': "Tu Mensaje"
    }))
