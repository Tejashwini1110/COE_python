special_char=['@','#','$','%','^']
def check_password(password):
    if len(password)<10 or len(password)>15:
        return "Weak:Password exceeds or less than the limit"
    elif not any(char.isupper() for char in password):
        return "Moderate:use atleast 1 uppercase character"
    elif not any(char.islower() for char in password):
        return "Moderate:use atleast 1 lowercase character"
    elif not any(char.isdigit() for char in password):
        return "Moderate:use atleast 1 digit character"
    elif any(char.isspace() for char in password):
        return "Moderate:uses a space character"
    elif not any(char in special_char for char in password):
        return "Moderate:use atleast 1 special character"
    elif password[-1]=='.' or password[-1]=='@':
        return "Moderate:should not end with a . or @"
    else:
        return "Strong:password is strong"
password=input("enter a password:")
print(check_password(password))
