class Request:
    def send(self):
        print('send')

print(Request.send)
print(type (Request.send))

request = Request()

print(request.send())