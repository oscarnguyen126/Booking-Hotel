import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_page(request):
    data = json.loads(request.body)

    username = data["username"]
    password = data["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({"current_user_id": user.id}))
    else:
        return HttpResponse({"msg": "Invalid username or password"})


@csrf_exempt
def logout_page(request):
    logout(request)
    return HttpResponse(json.dumps({"msg": "Logout successful"}))


# verify User
#    user = authenticate(request, username=username, password=password)
#    if user: <class 'users.models.User'>
#       login(request, user)
#    else:
#       raise exception


# login
# logout
#    session.flush()
