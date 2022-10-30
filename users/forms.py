from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
    
class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@example.com'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'password'})


    class Meta:
        model = CustomUser
        fields = ['email', 'password']