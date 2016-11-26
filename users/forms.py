from users.models import User
from django import forms
from payments.models import Plan


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    plan = forms.ChoiceField(
        label="Plan",
        choices=Plan.objects.all(),
        widget=forms.Select()
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'plan', 'password', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        if len(self.cleaned_data['password']) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")

        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise forms.ValidationError("Passwords don't match")

        if User.objects.filter(username=self.cleaned_data['username'].lower()).exists():
            raise forms.ValidationError("A user with this Username already exists")

        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("A user with this Email already exists")

        self.cleaned_data['plan'] = Plan.objects.get(pk=self.cleaned_data['plan'])

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        choices = [(pt.id, unicode(pt)) for pt in Plan.objects.filter(deleted=0)]
        self.fields['plan'].choices = choices
