import string
import re
def norm_token(token):
    if not token:
        return ''
    token = remove_punctuation(token)
    return re.sub(' +', '_', token).strip().lower()

def remove_punctuation(token):
    return ''.join(filter(lambda x: x not in string.punctuation, token))

