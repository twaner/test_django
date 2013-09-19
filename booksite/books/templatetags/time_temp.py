from django import template

register = template.Library()

#<p>The time is {% current_time "%Y-%m-%d %I:%M %p" %}.</p>\
#register.tag('current_time', do_current_time)
@register.tag(name="current_time")
def do_current_time(parser, token):
	try:
		#split contents() knows to split quoted strings
		tag_name, format_string  = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' \
		%token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	return CurrentTimeNode(format_string[1:-1])

#{% current_time2 "%Y-%M-%d %I:%M %p" %}	
@register.tag(name="current_time2")
def do_current_time2(parser, token):
	try:
		tag_name, format_string  = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' \
		%token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	return CurrentTimeNode2(format_string[1:-1])
	
	def do_current_time(parser, token):
		#uses regex to parse contents
		try:
			#splitting by None = splitting by spaces
			tag_name, arg = token.contents.split(None, 1)
		except ValueError:
			msg = '%r tag requires arguments' % token.contents[0]
			raise(template.TemplateSyntaxError(msg))
	
	m = re.search(r'(.*?) as (\w+)', arg)
	if m:
		fmt, var_name = m.groups()
	else:
		msg = '%r tag had invalid arguments' % tag_name
		raise(template.TemplateSyntaxError(msg))
		
	if not (fmt[0] == fmt[1] and fmt[0] in ('"',"'") ):
		msg = "%r tag's argument should be in quotes" % tag_name
		raise(template.TemplateSyntaxError(msg))
		
	return(CurrentTimeNode3(fmt[1:-1], var_name))	

@register.simple_tag
def current_time4(format_string):
	try:
		return(datetime.datetime.now().strftime(str(format_string)))
	except UnicodeEncodeError:
		return('')
	
#register.simple_tag(current_time)
	

