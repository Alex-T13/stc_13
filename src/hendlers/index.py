from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handle_index(_request: RequestT) -> ResponseT:
    base_html = read_static("_base.html", str)
    index_html = read_static("index.html", str)

    payload = base_html.format(source_html=index_html)
    payload = payload.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    return ResponseT(status, headers, payload)
