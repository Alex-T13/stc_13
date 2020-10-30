from src.hendlers import handle_index
from src.hendlers import handle_logo
from src.hendlers import handle_styles
from src.hendlers import system_handlers

handlers = {
    "/": handle_index,
    "/styles.css/": handle_styles,
    "/logo.png/": handle_logo,
}


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handler = handlers.get(url, system_handlers.handle_404)

    status, headers, payload = handler(environ)

    start_response(status, list(headers.items()))

    yield payload
