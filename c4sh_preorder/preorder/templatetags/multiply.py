from django import template

# this is LOL, but it finally works.

register = template.Library()

@register.filter 
def multiply(value, arg):
	if value and arg:
		return float(value) * float(arg) 
	else:
		return
