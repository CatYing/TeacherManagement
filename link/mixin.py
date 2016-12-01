from link.models import Link


class LinkMixin(object):
    def get_context_data(self, **kwargs):
        context = super(LinkMixin, self).get_context_data(**kwargs)
        context['link_list'] = Link.objects.all()
        return context