from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_hello(request: RequestT) -> ResponseT:
    name = (request.form_data.get("name") or [None])[0]
    address = (request.form_data.get("address") or [None])[0]

    base = read_static("_base.html")
    base_html = base.content.decode()
    hello_html = read_static("hello.html").content.decode()

    document = hello_html.format(
        name_header=name or "anon",
        name_value=name or "",
        address_header=address or "nowhere",
        address_value=address or "",
    )
    document = base_html.format(source_html=document)

    resp = ResponseT(
        status=build_status(200),
        headers={"Content-Type": base.content_type},
        payload=document.encode(),
    )
    return resp
