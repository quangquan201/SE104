from dataclasses import field
from operator import mod
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Comment

class CreateUserForm(UserCreationForm):

    """
    Lớp tạo form đăng kí

    ...

    Thuộc tính
    ----------
    first_name : str
        họ và tên đệm của người dùng
    last_name : str
        tên của người dùng

    Phương thức
    -------
    clean_password2():
        Kiểm tra password2 có giống password1 không.
    
    clean_email():
        Kiểm tra email đã tồn tại hay chưa.
    """


    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    class Meta:

        """
        Lớp dữ liệu

        ...

        Thuộc tính
        ----------
        model : model.User
            Dữ liệu bảng User
        fields : field
            các trường dữ liệu

        """

        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

    def clean_password2(self):

        '''So sánh password1 và password2, returns password2 '''

        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']

            if len(password1) < 8:
                raise forms.ValidationError("Mật khẩu hơn 8 kí tự")

            if password1 == password2 and len(password1) >= 8:
                return password2
            

        raise forms.ValidationError("Mật khẩu nhập lại không khớp")
    
    #def clean_username(self):
        #username = self.cleaned_data['username']
        #if User.objects.filter(username = self.cleaned_data['username']):
        #    raise forms.ValidationError("Tên đăng nhập đã tồn tại")
        #if len(username) < 5 :
        #    raise forms.ValidationError("Tên đăng nhập hơn 5 kí tự")
        #if len(username) > 15 :
        #    raise forms.ValidationError("Tên đăng nhập không quá 15 kí tự")

    def clean_email(self):

        '''Kiểm tra email đã tồn tại hay chưa '''

        if User.objects.filter(username = self.cleaned_data['email']):
            raise forms.ValidationError("Email đã được đăng kí")

