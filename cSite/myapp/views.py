# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from myapp.models import Document
from myapp.models import upload_to_unqiue_folder
from myapp.forms import DocumentForm

import sys
import imghdr
import subprocess

from subprocess import check_output

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            
#############is vaild?#####################

	    filename = 'media/' + newdoc.docfile.name
	    extension = filename.rsplit('.')[-1]

	    #exception handle. jpg is a part of jpeg format
	    if(imghdr.what(filename)=='jpeg' and extension=='jpg'):
		syntax = 1
	    elif imghdr.what(filename) == extension:
		syntax = 1
	    else:
		syntax = 3


##############################test#########
      	    exVar = newdoc.docfile.name
            exx = check_output(['myapp/embed.py',exVar])
	    tmp_str = exx.rsplit('\n')[3]
	    if(tmp_str == 'no files found'):
		syntax = 1
	    else:
		if(syntax == 1):
		    syntax = 2
		else:
		    syntax = 4
###########################################

            # Json to the document list after POST
	    data = {
		    'result' : syntax,
      		    'tmp value' : tmp_str,
		    'extension' : imghdr.what(filename),
		    'message' : exx
		   }
	    return JsonResponse(data)

    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def error(request):
    return render_to_response('error.html')

