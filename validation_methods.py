from validation_messages import validation_messages

def validate_mail(value: str):
    if "@" in value:
        return True
    else:
        return False

def validate_telephone_number(value: str):
    if len(value)==9 and value.isdecimal():
        return True
    else:
        return False

def validate_post_code(value: str):
    if len(value)==6 and value[2]=="/" and value[0:2].isdecimal() and value[3:4].isdecimal():
        return True
    else:
        return False

def validate_all(mail, telephone, code, language):
    if not validate_mail(mail):
        return validation_messages[language]["e-mail"]
    if not validate_telephone_number(telephone):
        return validation_messages[language]["telephone"]
    if not validate_post_code(code):
        return validation_messages[language]["code"]
    return ""

