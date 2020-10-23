import mimetypes

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]
    file_names = {
        "/xxx/": "styles.css",
        "/logo.png/": "logo.png",
    }
    file_name = file_names.get(url, "index.html")

    status = "200 OK"
    headers = {
        # "Content-type": "image/png",
        "Content-type": mimetypes.guess_type(file_name)[0],
        # "Content-type": "content_type(url)"
    }
    payload = read_static(file_name)
    start_response(status, list(headers.items()))

    yield payload


# def application(environ, start_response):
#     url = environ["PATH_INFO"]
#     if url == "/xxx/":
#         file_name = "styles.css"
#         status = "200 OK"
#         headers = {
#             #"Content-type": "text/css",
#             #"Content-type": "mimetypes.guess_type(xxx.css)[0]",
#             #"Content-type": f"{content_type(url)}",
#         }
#         payload = read_from_styles_css()
#         start_response(status, list(headers.items()))
#
#         yield payload
#
#     elif url == "/logo.png/":
#         status = "200 OK"
#         headers = {
#             #"Content-type": "image/png",
#             #"Content-type": "mimetypes.guess_type(url)[0]",
#             "Content-type": "content_type(url)"
#         }
#         payload = read_from_logo()
#         start_response(status, list(headers.items()))
#
#         yield payload
#
#     else:
#         status = "200 OK"
#         headers = {
#             "Content-type": "text/html",
#         }
#
#         payload = read_from_index_html()
#
#         start_response(status, list(headers.items()))
#
#         yield payload
#
#
# def read_from_index_html():
#     path = DIR_STATIC / "index.html"
#
#     with path.open("r") as fp:
#         payload = fp.read()
#
#     payload = payload.encode()
#     return payload
#
#
# def read_from_styles_css():
#     path = DIR_STATIC / "styles.css"
#
#     with path.open("r") as fp:
#         payload = fp.read()
#
#     payload = payload.encode()
#     return payload
#
#
# def read_from_logo():
#     path = DIR_STATIC / "logo.png"
#
#     with path.open("rb") as fp:
#         payload = fp.read()
#
#     return payload


def content_type(url):
    c_type = mimetypes.guess_type(url)[0]
    return c_type


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    # payload = payload.encode()
    return payload


# from framework.consts import dir_static
#
#
# def application(environ, start_response):
#     url = environ["PATH_INFO"]
#     if url == "/xxx/":
#         status = "200 OK"
#         headers = {
#             "Content-type": "text/css",
#         }
#         payload = read_from_style_css()
#         start_response(status, list(headers.items()))
#
#         yield payload
#         # return None
#     else:
#
#         status = "200 OK"
#         headers = {
#             "Content-type": "text/html",
#         }
#         payload = read_from_index_html()
#
#         start_response(status, list(headers.items()))
#
#         yield payload
#
#
# def read_from_index_html():
#     path = dir_static / "index.html"
#
#     with path.open("r") as fp:
#         payload = fp.read()
#     fp.close()
#
#     payload = payload.encode()
#     return payload
#
#
# def read_from_style_css():
#     path = dir_static / "styles.css"
#
#     with path.open("r") as fp:
#         payload = fp.read()
#     fp.close()
#
#     payload = payload.encode()
#     return payload
