from datetime import datetime

from meetupselector.user.models import User


class UserBuilder:
    _email: str = "email@e.com"
    _description: str = "description"
    _is_staff: bool = False
    _is_superuser: bool = False
    _date_joined: datetime = datetime.now()
    _password: str = "Password10!"
    _is_active: bool = True

    def with_email(self, email) -> "UserBuilder":
        self._email = email
        return self

    def with_description(self, description: str) -> "UserBuilder":
        self._description = description
        return self

    def with_is_Staff(self, is_staff: bool) -> "UserBuilder":
        self._is_staff = is_staff
        return self

    def with_is_superuser(self, is_superuser: bool) -> "UserBuilder":
        self._is_superuser = is_superuser
        return self

    def with_date_joined(self, date_joined: datetime) -> "UserBuilder":
        self._date_joined = date_joined
        return self

    def with_password(self, password: str) -> "UserBuilder":
        self._password = password
        return self

    def with_is_active(self, is_active: bool) -> "UserBuilder":
        self._is_active = is_active
        return self

    def build(self) -> User:
        return User.objects.create_user(
            email=self._email,
            password=self._password,
            description=self._description,
            is_staff=self._is_staff,
            is_superuser=self._is_superuser,
            date_joined=self._date_joined,
            is_active=self._is_active,
        )
