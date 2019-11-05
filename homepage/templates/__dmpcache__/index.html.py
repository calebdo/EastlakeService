# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1572801587.2231002
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/other/Python/EastlakeService/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1>Eastlake High School</h1>\r\n    <h2>Community Service Portal</h2>\r\n    <br><br>\r\n')
        if request.user.is_authenticated:
            __M_writer('    <p><a href="/newService/">Submit service information</a></p>\r\n')
        else:    
            __M_writer('    <p>First time? <a href="/create/">Create a new account</a></p>\r\n        <p>Your username should be the beginning part of your LWSD email address (before @lwsd.org)</P>\r\n        <br>\r\n        <form method="POST"> \r\n            <table>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
            __M_writer('\r\n            </table>\r\n            <br>\r\n            <input type="submit" value="Submit">\r\n        </form>\r\n        <br><br>\r\n        <p><a href="/recover/">I forgot my password</a></p>\r\n')
        __M_writer('    <br><br>\r\n    <p>If you have any questions about this website or Eastlake community service, please send us an email at eastlakeservice@gmail.com</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/other/Python/EastlakeService/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 26, "50": 4, "59": 4, "60": 8, "61": 9, "62": 10, "63": 11, "64": 16, "65": 16, "66": 24, "72": 66}}
__M_END_METADATA
"""
