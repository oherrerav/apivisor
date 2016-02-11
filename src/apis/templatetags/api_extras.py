from django import template
 
register = template.Library()
 
class SetVarNode(template.Node):
 
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value
 
    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value
        return u""
 
def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3])
 
register.tag('set', set_var)

@register.filter
def lookupId(d, value):

    return d.get(name=value).id

@register.filter
def lookup(d, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    # prefetch = Prefetch(arg_list[0], queryset=arg_list[1], to_attr=arg_list[1])
    data = str("uri")
    # return d.prefetch_related(prefetch).get()
    return d.get(name=arg_list[0]).uri

@register.filter
def lookupByKey(d, key):
    data = str('uri')
    return d[key]


@register.filter
def lookupUri(d, value):
      return d.get(name=value).uri

@register.filter
def lookupCharType(d, value):
      return d.get(name=value).name