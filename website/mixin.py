# coding=utf8
from authentication.mixin import AuthMixin
from link.mixin import LinkMixin


class FrontMixin(AuthMixin, LinkMixin):
    def get_context_data(self, **kwargs):
        return super(FrontMixin, self).get_context_data(**kwargs)
