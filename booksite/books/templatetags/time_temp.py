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
	

