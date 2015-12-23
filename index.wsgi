# coding: UTF-8
import os
import sae
import web
 
from weixinInterface import WeixinInterface
# url������һ������ƥ��URL��������ʽ���ڶ������ǽ��������������
urls = (
'/weixin', 'WeixinInterface'
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
# ����һ���о�url��application
app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)