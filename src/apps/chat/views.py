from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id) # relação reversa 'courses_joined' de students criada na model Course
    except:
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
