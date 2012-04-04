from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):

    return render_to_response("disorder/index.html", dict(),
                               context_instance=RequestContext(request))
                               
def predicted(request):

    return render_to_response("disorder/predicted.html", dict(),
                              context_instance=RequestContext(request))

# temp static pages of results                          
def iupred_short_one(request):

    return render_to_response("disorder/predicted/iupred-short/1.html", dict(),
                            context_instance=RequestContext(request))
                            
def iupred_short_two(request):

    return render_to_response("disorder/predicted/iupred-short/2.html", dict(),
                            context_instance=RequestContext(request))
                            
def iupred_short_three(request):

    return render_to_response("disorder/predicted/iupred-short/3.html", dict(),
                            context_instance=RequestContext(request))

def iupred_short_four(request):

    return render_to_response("disorder/predicted/iupred-short/4.html", dict(),
                            context_instance=RequestContext(request))            
                            
def iupred_long_one(request):

    return render_to_response("disorder/predicted/iupred-long/1.html", dict(),
                            context_instance=RequestContext(request))

def iupred_long_two(request):

    return render_to_response("disorder/predicted/iupred-long/2.html", dict(),
                            context_instance=RequestContext(request))

def iupred_long_three(request):

    return render_to_response("disorder/predicted/iupred-long/3.html", dict(),
                            context_instance=RequestContext(request))

def iupred_long_four(request):

    return render_to_response("disorder/predicted/iupred-long/4.html", dict(),
                            context_instance=RequestContext(request))

def vsl2b_one(request):

    return render_to_response("disorder/predicted/vsl2b/1.html", dict(),
                            context_instance=RequestContext(request))

def vsl2b_two(request):

    return render_to_response("disorder/predicted/vsl2b/2.html", dict(),
                            context_instance=RequestContext(request))

def vsl2b_three(request):

    return render_to_response("disorder/predicted/vsl2b/3.html", dict(),
                            context_instance=RequestContext(request))

def vsl2b_four(request):

    return render_to_response("disorder/predicted/vsl2b/4.html", dict(),
                            context_instance=RequestContext(request))                            