def get_sftp():
    print("Get sftp")

def regist(name, sex, *args, **kwargs):
    print(f'Name: {name}')
    print(f'Sex: {sex}')
    print(f'Other options: {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(email)
    if phone:
        print(phone)