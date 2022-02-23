from app.celery import app
from parser.models import Parser


@app.task
def start_worker(req_form):
    print('good')
    print(req_form)
    parser = Parser(req_form)
    parser.run_parsing()
