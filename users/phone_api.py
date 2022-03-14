import requests
from random import randint
from django.utils import timezone

def send_verfication_code(user):
    user.update_vcode_send_timer()
    from_number = 'NUMBER'
    user_number = user.phone_number
    verification_code = user.verification_code
    message_text = 'کد شما برای ثبت نام در همگرایی ' + verification_code +  ' می باشد '
    p_user_name = 'PLATFORM_USER'
    p_password = 'PLATFORM_PASS'
    domain = '0098'
    url = 'https://www.0098sms.com/sendsmslink.aspx?FROM=' + from_number + '&TO=' + user_number + '&TEXT=' + message_text + '&USERNAME=' + p_user_name + '&PASSWORD=' + p_password + '&DOMAIN='  + domain
    response = requests.post(url)
    
    return response.text.split('\n', 1)[0]

def generate_verification_code():
    n = 6
    return ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

def test_send_verfication_code(phone):
    from_number = 'NUMBER'
    user_number = phone
    verification_code = '123456'
    message_text = 'کد شما برای ثبت نام در همگرایی ' + verification_code +  ' می باشد '
    p_user_name = 'PLATFORM_USER'
    p_password = 'PLATFORM_PASS'
    domain = '0098'
    url = 'https://www.0098sms.com/sendsmslink.aspx?FROM=' + from_number + '&TO=' + user_number + '&TEXT=' + message_text + '&USERNAME=' + p_user_name + '&PASSWORD=' + p_password + '&DOMAIN='  + domain
    response = requests.post(url)
    print(response.text.split('\n', 1)[0])
    if(response.text.split('\n', 1)[0]==0):
        return 'success'
    else:
        return 'failed'

