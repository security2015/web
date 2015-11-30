import random
try:
    from hashlib import sha1 as sha_constructor
except ImportError:
    from django.utils.hashcompat import sha_constructor


def generate_sha1(string, salt=None):
    """
    Generates a sha1 hash for supplied string.

    :param string:
        The string that needs to be encrypted.

    :param salt:
        Optionally define your own salt. If none is supplied, will use a random
        string of 5 characters.

    :return: Tuple containing the salt and hash.

    """
    if not isinstance(string, (str, unicode)):
         string = str(string)
    if isinstance(string, unicode):
        string = string.encode("utf-8")
    if not salt:
        salt = sha_constructor(str(random.random())).hexdigest()[:5]
    hash = sha_constructor(salt+string).hexdigest()

    return (salt, hash)
