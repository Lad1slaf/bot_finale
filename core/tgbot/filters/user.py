from django.contrib.auth.models import User
import typing
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class UsersFilter(BoundFilter):

    def __init__(self, is_user: typing.Optional[bool] = None):
        self.is_user = is_user

    async def users_check(self, message: types.Message):
        username = message.from_user.username.lower()
        return User.objects.filter(username=username).count() > 0 == self.is_user
