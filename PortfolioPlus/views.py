from django.shortcuts import render


def index(request):
    return render(request, "closed.html", {})


def pronation(request):
    return render(request, "pronation.html", {})


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response
