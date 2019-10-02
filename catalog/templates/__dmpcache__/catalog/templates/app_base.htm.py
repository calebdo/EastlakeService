# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552593714.1479208
_enable_loop = True
_template_filename = 'C:/Users/Caleb/Sprint1/catalog/templates/app_base.htm'
_template_uri = '/catalog/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_left', 'page_title', 'navbar_items', 'login_navbar']


from catalog import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        def login_navbar():
            return render_login_navbar(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login_navbar'):
            context['self'].login_navbar(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <ul id="category-list">\r\n    <li class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category is None else '' ))
        __M_writer('"><a href="/catalog/index/">All Products</a></li>\r\n')
        for cat in cmod.Category.objects.order_by('name'):
            __M_writer('      <li class="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category == cat else '' ))
            __M_writer('"><a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.id ))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.name ))
            __M_writer('</a></li>\r\n')
        __M_writer('  </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('FOMO')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n      \r\n        <li class="dropdown">\r\n          <a class="dropdown-toggle" data-toggle="dropdown" href="#">Welcome, ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( user.first_name ))
        __M_writer('\r\n          <span class="caret"></span></a>\r\n          <ul class="dropdown-menu">\r\n            <li><a class="dropdown-item" href="/account/index/">Account</a></li>\r\n            <li><a class="dropdown-item" href="/account/logout/">Logout</a></li>\r\n          </ul>\r\n        </li>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login_navbar():
            return render_login_navbar(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li><a class="dropdown-item" href="/account/login/">Login</a></li>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/Sprint1/catalog/templates/app_base.htm", "uri": "/catalog/templates/app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "47": 1, "48": 2, "53": 12, "58": 14, "63": 28, "68": 33, "74": 5, "82": 5, "83": 7, "84": 7, "85": 8, "86": 9, "87": 9, "88": 9, "89": 9, "90": 9, "91": 9, "92": 9, "93": 11, "99": 14, "105": 14, "111": 16, "119": 16, "120": 20, "121": 20, "127": 31, "133": 31, "139": 133}}
__M_END_METADATA
"""
