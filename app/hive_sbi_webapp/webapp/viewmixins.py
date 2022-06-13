from django.views.generic import View


class BaseMixinView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_home'] = False
        context['active_userinfo'] = False
        context['active_richlist'] = False
        context['active_transaction_history'] = False

        return context