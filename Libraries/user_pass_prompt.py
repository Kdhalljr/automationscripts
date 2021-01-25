import getpass


def custom_fallback(prompt='Enter your password: ', stream = None):
        print '!!!Your password is not masked!!!'
        return getpass._raw_input(prompt)


def user_pass_prompt():
    username = raw_input('Enter domain admin username: ')
    getpass.fallback_getpass = custom_fallback
    password = getpass.getpass('Enter your password: ')
    return username, password
