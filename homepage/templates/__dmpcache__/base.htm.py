# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1572921610.2116883
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/other/Python/EastlakeService/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'header_maintenance', 'site_center']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n            <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('</title>\r\n        \r\n\r\n')
        __M_writer('        <script href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\jquery-3.3.1.min.js"></script>\r\n        <script href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\bootstrap-3.3.7-dist\\js\\bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\bootstrap-3.3.7-dist\\css\\bootstrap.min.css">\r\n        <link rel="icon" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/mountain.png">\r\n        \r\n')
        __M_writer('        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">\r\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>\r\n        \r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\r\n       \r\n\r\n        <header>\r\n                <nav class="navbar">\r\n                        <div class="container-fluid" id="site_navbar_top">\r\n                            <div class="navbar-header">\r\n                                <a href="/" title="Eastlake Service"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/mountain.png" id="site_img"/></a>\r\n                            </div>\r\n                            <ul class="nav navbar-nav">\r\n                                <li class="nav-item"><a class="nav-link-')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/">Home</a></li>\r\n')
        if request.user.is_authenticated:
            __M_writer('                                    <li class="nav-item"><a class="nav-link-')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'records' else '' ))
            __M_writer('" href="/records/">My Service</a></li>\r\n')
        __M_writer('                            </ul>\r\n                        </nav>\r\n                            \r\n                        </div>\r\n                       \r\n        </header>\r\n\r\n        <main>\r\n         \r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            \r\n            \r\n        </main>\r\n\r\n        <footer class="page-footer">\r\n')
        __M_writer('            &copy;Copyright 2019 -- Olson Web Design. All rights reserved.\r\n')
        __M_writer('        </footer>\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_maintenance():
            return render_header_maintenance(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/other/Python/EastlakeService/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "32": 2, "37": 7, "38": 11, "39": 11, "40": 11, "41": 12, "42": 12, "43": 13, "44": 13, "45": 14, "46": 14, "47": 17, "48": 22, "49": 23, "50": 23, "55": 27, "56": 34, "57": 34, "58": 37, "59": 37, "60": 38, "61": 39, "62": 39, "63": 39, "64": 41, "69": 52, "70": 60, "71": 62, "77": 7, "88": 27, "99": 51, "105": 51, "111": 105}}
__M_END_METADATA
"""
