BASE_ROUTE = "documents"


def register_routes(api, app, root="api"):
    from .controller import api as test_api
    api.add_namespace(test_api, path=f"/{root}/{BASE_ROUTE}")