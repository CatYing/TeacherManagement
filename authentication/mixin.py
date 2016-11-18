# coding=utf8


class AuthMixin(object):
    def get_context_data(self, **kwargs):
        context = super(AuthMixin, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            myuser = self.request.user.myuser.name
            context['myuser'] = myuser
        return context