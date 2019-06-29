from molten import App, Route
from wsgicors import CORS
from molten.openapi import Metadata, OpenAPIHandler, OpenAPIUIHandler

from feed_me import settings
from feed_me.order.routes import routes as order_routes

get_schema = OpenAPIHandler(
    metadata=Metadata(
        title="FeedMe API",
        description="An API for feeding people.",
        version="0.0.1",
    ),
)

get_docs = OpenAPIUIHandler()

routes = order_routes
routes += [Route("/_schema", get_schema), Route("/docs", get_docs), ]


def make_zbs_CORS(app):
    return CORS(app, headers="*", methods="*", origin="*", maxage="86400")


app = App(
    routes=routes,
    # components=[UserComponent()]
)

if __name__ == "__main__":
    import werkzeug

    options = {
        "hostname": settings.Server.host,
        "port": settings.Server.port,
        "use_debugger": True,
        "use_reloader": True,
    }
    cors_app = make_zbs_CORS(app)
    werkzeug.run_simple(application=cors_app, **options)
