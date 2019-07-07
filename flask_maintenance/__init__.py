import os
from flask import (
    abort,
    current_app,
    _app_ctx_stack,
    _request_ctx_stack,
    request
)


__all__ = ['Maintenance']


class Maintenance:
    """
    Add Maintenance mode feature to your flask application.
    """

    def __init__(self, app=None):
        """
        :param app:
            Flask application object.
        """

        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initalizes the application with the extension.

        :param app:
            Flask application object.
        """

        app.before_request_funcs.setdefault(None, []).append(self._handler)

    def _handler(self):
        """
        Maintenance mode handler.
        """
        actx = _app_ctx_stack.top
        rctx = _request_ctx_stack.top

        if actx and rctx:
            if request.endpoint != 'static':
                ins_path = os.path.join(current_app.instance_path,
                                        'under_maintenance')

                if os.path.exists(ins_path) and os.path.isfile(ins_path):
                    abort(503)
