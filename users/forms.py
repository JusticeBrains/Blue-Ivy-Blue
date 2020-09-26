from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User

class CustomUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {
            'duplicate_username': _('Username already in use by another user')
        }
    )

    class Meta:
        model = User
    
    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            User.objects.get(username=username)
        
        except User.DoesNotExist:
            return username

        raise ValidationError(
        self.error_messages['duplicate_username']
    )

