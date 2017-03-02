import SimpleHTTPServer
import SocketServer
import templates

PORT = 9898

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		mypath=self.path.split("?")
		if(mypath[0] == "/" or mypath[0] == "/index.html"):
			self.wfile.write(open("index.html","r").read())
		elif(mypath[0] == "/character.css"):
			self.wfile.write(open("character.css","r").read())
		elif(mypath[0] =="/character"):
			args=mypath[1].split("&")
			self.wfile.write(templates.CharacterTemplate(args[0].split("=")[1],args[1].split("=")[1]))


SocketServer.TCPServer.allow_reuse_address=True
httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.allow_reuse_address = True

print "serving at port", PORT
try:
    httpd.serve_forever()
finally:
    httpd.server_close()

