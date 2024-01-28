from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import re_path
from django.utils.encoding import force_str


class SingletonModelAdmin(admin.ModelAdmin):
    object_history_template = 'admin_singleton/object_history.html'
    change_form_template = 'admin_singleton/change_form.html'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def get_urls(self):
        urls = super(SingletonModelAdmin, self).get_urls()

        model_name = self.model._meta.model_name

        self.model._meta.verbose_name_plural = self.model._meta.verbose_name
        url_name_prefix = '%(app_name)s_%(model_name)s' % {
            'app_name': self.model._meta.app_label,
            'model_name': model_name,
        }
        custom_urls = [
            re_path(r'^history/$',
                    self.admin_site.admin_view(self.history_view),
                    {'object_id': '1'},
                    name='%s_history' % url_name_prefix),
            re_path(r'^$',
                    self.admin_site.admin_view(self.change_view),
                    {'object_id': '1'},
                    name='%s_change' % url_name_prefix),
        ]

        return custom_urls + urls

    def response_change(self, request, obj):
        msg = f'{force_str(obj)} було змінено успішно.'
        if '_continue' in request.POST:
            self.message_user(request, msg + ' Ви можете редагувати його знову нижче.')
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)
            return HttpResponseRedirect("../../")

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if object_id == '1':
            self.model.objects.get_or_create(pk=1)

        return super(SingletonModelAdmin, self).change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )
