import requests
from django.http.response import HttpResponseForbidden


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        user = request.user
        token = user.username

        headers = {"Authorization": "Token {}".format(token)}

        resp = requests.get(
            'http://localhost:8001/api/can-access/4/', headers=headers)

        status = resp.status_code

        print(status)

        if status != 200:
            return HttpResponseForbidden()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
