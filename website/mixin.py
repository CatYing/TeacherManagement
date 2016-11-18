# coding=utf8
from authentication.mixin import AuthMixin


class FrontMixin(AuthMixin):
    def get_context_data(self, **kwargs):
        return super(FrontMixin, self).get_context_data(**kwargs)