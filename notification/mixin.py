# coding=utf8


class NotificationMixin(object):
    def get_context_data(self, **kwargs):
        context = super(NotificationMixin, self).get_context_data(**kwargs)
        context['noti_num'] = self.request.user.myuser.studentnotificationsonteacher.unread_count + self.request.user.myuser.studentnotificationonappointment.unread_count
        context['tea_num'] = self.request.user.myuser.studentnotificationsonteacher.unread_count
        context['app_num'] = self.request.user.myuser.studentnotificationonappointment.unread_count
        return context

