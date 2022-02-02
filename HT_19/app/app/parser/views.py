from django.shortcuts import render
from django.http import HttpResponse

from .models import Parser


def index(request):
    stories = Parser.stories
    req_form = request.GET.get('stories')
    run_parser = False
    if req_form in stories:
        run_parser = True
        parser = Parser(req_form)
        parser.run_parsing()
    context = {
        'stories': stories,
        'run_parser': run_parser,
    }
    return render(request, 'parser/index.html', context)
