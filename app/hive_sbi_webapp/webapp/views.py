import json
import logging
import requests

from django.conf import settings
from django.views.generic import TemplateView

from .viewmixins import BaseMixinView
from .forms import UseInfoForm


logger = logging.getLogger('webapp')


class HomeView(BaseMixinView, TemplateView):
    template_name = "webapp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_home'] = True
        return context


class UserInfoForm(BaseMixinView, TemplateView):
    template_name = "webapp/userinfo_form.html"

    def get_user(self, **kwargs):
        return self.request.GET.get('user')

    def get_userinfo_form(self, **kwargs):
        user = self.get_user()

        initial = {}

        if user:
            initial = {'user': user}

        return UseInfoForm(initial=initial)

    def get_userinfo(self, **kwargs):
        user = self.get_user()
        userinfo = None

        if not user:
            return userinfo


        userinfo = {
            "status_code": None,
            "success": False,
            "data": None,        
            "error": None,
        }

        try:
            response = requests.get(
                "{}/getUserInfo?user={}".format(settings.SBI_API_URL, user),
            )

            userinfo["status_code"] = response.status_code

            if response.status_code == 200:
                content = json.loads(response.content.decode("utf-8"))

                userinfo["success"] = content["success"]

                if userinfo["success"]:
                    userinfo["data"] = content["data"]
                else:
                    userinfo["error"] = content["error"]

        except requests.exceptions.ConnectionError:
            userinfo["error"] = "Connection Error"

        return userinfo

    def get_userinfo_hive(self, **kwargs):
        user = self.get_user()
        userinfo_hive = None

        if not user:
            return userinfo_hive


        userinfo_hive = {
            "status_code": None,
            "success": False,
            "data": None,        
            "error": None,
        }

        #try:
        response = requests.get(
            "{}/users/{}/".format(settings.SBI_API_URL_V1, user),
        )

        userinfo_hive["status_code"] = response.status_code

        if response.status_code == 200:
            content = json.loads(response.content.decode("utf-8"))

            userinfo_hive["success"] = content["success"]

            if userinfo_hive["success"]:
                userinfo_hive["data"] = content["data"]
            else:
                userinfo_hive["error"] = content["error"]

        #except requests.exceptions.ConnectionError:
        #    userinfo_hive["error"] = "Connection Error"

        return userinfo_hive

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_userinfo'] = True
        context['user'] = self.get_user()
        context['userinfo_form'] = self.get_userinfo_form()

        context['userinfo'] = self.get_userinfo()
        context['userinfo_hive'] = self.get_userinfo_hive()

        return context


class RichListView(BaseMixinView, TemplateView):
    template_name = "webapp/rich_list.html"

    def get_richlist(self, **kwargs):
        LIMIT = 200

        ordering = self.request.GET.get("ordering", "")

        try:
            offset = int(self.request.GET.get("offset", 0))
        except ValueError:
            offset = 0

        richlist = {
            "status_code": None,
            "previous": None,
            "next": None,
            "active_page_number": None,
            "prev_page_number": None,
            "next_page_number": None,
        }

        try:
            params = ""

            if ordering:
                params = "?ordering={}".format(ordering)

            if offset:
                if params:
                    params = "{}&offset={}".format(params, offset)
                else:
                    params = "?offset={}".format(offset)


            response = requests.get(
                "{}/v1/members/{}".format(settings.SBI_API_URL_V1, params),
            )

            richlist["status_code"] = response.status_code

            if response.status_code == 200:
                content = json.loads(response.content.decode("utf-8"))

                if content["previous"]:
                    richlist["previous"] = content["previous"].split("?")[1]

                if content["next"]:
                    richlist["next"] = content["next"].split("?")[1]

                active_page_number = offset / LIMIT + 1

                richlist["active_page_number"] = int(active_page_number)
                richlist["prev_page_number"] = int(active_page_number - 1)

                if offset + 200 < content["count"]:
                    richlist["next_page_number"] = int(active_page_number + 1)

                richlist["results"] = content["results"]

        except requests.exceptions.ConnectionError:
            richlist["content"] = "Connection Error"

        return richlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_richlist'] = True

        context['richlist'] = self.get_richlist()

        context['shares_ascending_active'] = False
        context['shares_descending_active'] = False
        context['bonus_shares_ascending_active'] = False
        context['bonus_shares_descending_active'] = False
        context['pending_balance_ascending_active'] = False
        context['pending_balance_descending_active'] = False
        context['next_upvote_estimate_ascending_active'] = False
        context['next_upvote_estimate_descending_active'] = False
        context['estimate_rewarded_ascending_active'] = False
        context['estimate_rewarded_descending_active'] = False

        ordering = self.request.GET.get("ordering", "")

        if ordering == "shares":
            context['shares_ascending_active'] = True
        if ordering == "-shares":
            context['shares_descending_active'] = True
        if ordering == "bonus_shares":
            context['bonus_shares_ascending_active'] = True
        if ordering == "-bonus_shares":
            context['bonus_shares_descending_active'] = True
        if ordering == "estimate_rewarded":
            context['estimate_rewarded_ascending_active'] = True
        if ordering == "-estimate_rewarded":
            context['estimate_rewarded_descending_active'] = True

        return context
