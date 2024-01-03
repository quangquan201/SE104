var form_fields = document.getElementsByTagName('input')
form_fields[2].placeholder = 'Họ và tên đệm';
form_fields[3].placeholder = 'Tên';
form_fields[4].placeholder = 'Tên đăng nhập';
form_fields[5].placeholder = 'Email';
form_fields[6].placeholder = 'Mật khẩu';
form_fields[7].placeholder = 'Nhập lại mật khẩu';

for (var field in form_fields)
{
    form_fields[field].className += 'form-control'
}