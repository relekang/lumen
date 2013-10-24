# -*- coding: utf-8 -*-
import web
import json
from utils import blink

urls = (
    '/', 'GithubHook',
)

render = web.template.render('.')

ERROR = '<h1 style="text-align:center;">I am sorry, but I cannot ' +\
        'allow you to do this!</h1><p style="text-align:center;">' +\
        'If you found this url in a git webhook read more at ' +\
        '<a href="http://rolflekang.com/blog/2012/09/the-github-lamp/"' +\
        'style="color:black;">rolflekang.com/blog/2012/09/the-github-' +\
        'lamp/</a></p>'


class GithubHook:
    def POST(self):
        blink()
        data = json.loads(web.input().payload)
        if 'homepage' in data['repository']:
            homepage = data['repository']['homepage']
        else:
            homepage = ''
        print "%s pushed to %s - %s" % (
            data['pusher']['name'],
            data['repository']['name'],
            homepage
        )
        return ""

    def GET(self):
        return ERROR

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

application = web.application(urls, globals(), True).wsgifunc()
