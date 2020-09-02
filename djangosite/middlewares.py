from rest_framework_simplejwt import authentication

def open_access_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response["Access-Control-Allow-Origin"] = '*'
        response["Access-Control-Allow-Headers"] = '*'
        return response
    return middleware

class BindCurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
        
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.user = authentication.JWTAuthentication().authenticate(request)[0]