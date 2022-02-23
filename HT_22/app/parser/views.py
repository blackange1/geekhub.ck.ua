from django.shortcuts import render

from app.celery import app
from .models import Parser
from .tasks import start_worker


def index(request):
    stories = Parser.stories
    req_form = request.GET.get('stories')
    run_parser = False

    if req_form in stories:
        run_parser = True
        start_worker.delay(req_form)
        # parser = Parser(req_form)
        # parser.run_parsing()
    context = {
        'stories': stories,
        'run_parser': run_parser,
    }
    return render(request, 'parser/index.html', context)
