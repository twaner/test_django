from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.loader import get_template
import datetime

def hello(request):
    return HttpResponse("Hello world")

""""def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
    
def current_datetime(request):
	def current_datetime(request):
    		now = datetime.datetime.now()
   		return(render(request,'time/current_datetime.html',{'current_date': now}))
   		"""
   		
def current_datetime(request):
	def current_datetime(request):
    		now = datetime.datetime.now()
    		return render(request, 'time/current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + \
	 datetime.timedelta(hours=offset)
	html = "<html><body>In %s hours(s), it will be %s.</body> \
	</html>" % (offset, dt)
	return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    
# GOOD (VERSION 1)
def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)

# GOOD (VERSION 2)
def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)

