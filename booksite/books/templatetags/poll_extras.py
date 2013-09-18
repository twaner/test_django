from django impport template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
	return(value.replace(arg,''))
