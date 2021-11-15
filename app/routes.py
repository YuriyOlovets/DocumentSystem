def register_routes(api, app, root="agent"):
    from app.documents import register_routes as attach_test_api

    attach_test_api(api, app)

