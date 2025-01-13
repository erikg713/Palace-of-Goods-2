def validate_register(data):
    errors = {}
    if 'username' not in data or len(data['username']) < 3:
        errors['username'] = "Username must be at least 3 characters."
    if 'password' not in data or len(data['password']) < 6:
        errors['password'] = "Password must be at least 6 characters."
    if 'email' not in data or '@' not in data['email']:
        errors['email'] = "Invalid email address."
    return errors

def validate_login(data):
    errors = {}
    if 'username' not in data:
        errors['username'] = "Username is required."
    if 'password' not in data:
        errors['password'] = "Password is required."
    return errors