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
            
	    filename = 'media/' + newdoc.docfile.name
	    extension = filename.rsplit('.')[-1]
#############is vaild?#####################
	    if(imghdr.what(filename)=='rgb' or imghdr.what(filename)=='gif' or imghdr.what(filename)=='pbm' or imghdr.what(filename)=='pgm' or imghdr.what(filename)=='ppm' or imghdr.what(filename)=='tiff' or imghdr.what(filename)=='rast' or imghdr.what(filename)=='xbm' or imghdr.what(filename)=='jpeg' or imghdr.what(filename)=='bmp' or imghdr.what(filename)=='png' or imghdr.what(filename)=='jpg'):

	        #exception handle. jpg is a part of jpeg format
	        if (imghdr.what(filename)=='jpeg' and extension=='jpg'):
		    extSyntax = 1
	        elif imghdr.what(filename) == extension:
		    extSyntax = 1
	        else:
		    extSyntax = 2
	    else:
		extSyntax = 0


##############################test#########
      	    exVar = newdoc.docfile.name
            exx = check_output(['myapp/embed.py','media/'+exVar])
	    tmp_str = exx.rsplit('\n')[3]
	    if(imghdr.what(filename) == 'gif' or imghdr.what(filename) == 'jpeg' or imghdr.what(filename) == 'jpeg' or imghdr.what(filename) == 'png'):
	        if(tmp_str == 'no files found'):
		    embSyntax = 1
	        else:
		    embSyntax = 2
		    tmp_str = exx.rsplit('\n')[4] + exx.rsplit('\n')[5]
	    else:
		embSyntax = 0
###########################################
	  


            # Json to the document list after POST
	    data = {
		    'original' : request.FILES['docfile'].name,
		    'filename' : newdoc.docfile.name.rsplit('/')[2],
		    'extension_result' : extSyntax,
		    'embedded_result' : embSyntax,
		    'embedded_message' : tmp_str,
		    'current' : extension,
		    'expected' : imghdr.what(filename)
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

