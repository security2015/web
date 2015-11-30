# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
import datetime

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


def upload_to_unqiue_folder(instance, filename):
    """
    Uploads a file to an unique generated Path to keep the original filename
    """
    fileext = filename.encode("utf-8")
    salt, hash = generate_sha1('{}{}'.format(fileext, datetime.datetime.now().time()))
    tmp = fileext.split('.')
    return  "documents/tmp/" + '%(hash_path)s.%(fileext)s' % {
                                               'hash_path': hash[:10],
                                               'fileext': tmp[-1]}

class Document(models.Model):
    docfile = models.FileField(upload_to=upload_to_unqiue_folder)
    path = models.CharField(max_length=30)

