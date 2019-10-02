# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569797786.3502598
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/sprint3/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n       <h1 class="text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Products' if category is None else category.name ))
        __M_writer('</h1>\r\n        <div id="catalog">\r\n')
        for product in products:
            __M_writer('                <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('"></span>\r\n')
        __M_writer('        </div>\r\n\r\n        <div id="paginator" class="text-right">\r\n            <ul class="pagination">\r\n                <li><a class="btn btn-secondary" href="/catalog/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
        __M_writer('/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 if page > 0 else '' ))
        __M_writer('">Previous</a></li>\r\n                <li><a class="btn btn-secondary" href="/catalog/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
        __M_writer('/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 if page < numpages else page ))
        __M_writer('">Next</a></li>\r\n           </ul>  \r\n           \r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/sprint3/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "43": 1, "44": 2, "49": 19, "55": 4, "66": 4, "67": 5, "68": 5, "69": 7, "70": 8, "71": 8, "72": 8, "73": 10, "74": 14, "75": 14, "76": 14, "77": 14, "78": 15, "79": 15, "80": 15, "81": 15, "87": 81}}
__M_END_METADATA
"""
