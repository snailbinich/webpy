import web
from pm6 import *

urls = ('/', 'hello',
	'/reslove','reslove'
	)

class hello(object):
	def GET(self):
		render = web.template.render('./')
		return  render.form()

class reslove(object):
	def POST(self):
	    i = web.input()
	    result = get6PmData(i.url)
	    render = web.template.render("./", globals={'str':str})
	    return render.result(result)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
