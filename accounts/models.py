from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    @classmethod
    def normalize_email(cls, email):
        """
        Wholly override the normalize method, to make the whole email lowercase.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name.lower() + "@" + domain_part.lower()
        return email

    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError("Users must have a valid e-mail address")

        # Create a random username if none is given
        # We use emails as the final identity, so users don't even need to know
        # what their usernames are...
        username = kwargs.get("username")
        if not kwargs.get("username"):
            username = self.make_random_password()

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            # first_name=kwargs.get("first_name", None),
            # last_name=kwargs.get("last_name", None),
            is_active=kwargs.get("is_active", False),
        )

        user.set_password(password)
        user.save()
        return user

    def create(self, *args, **kwargs):
        """
        The normal create it piped through the create owners method
        :param args:
        :param kwargs:
        :return:
        """
        return self.create_user(*args, **kwargs)

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. " "Letters, digits and @/./+/-/_ only."
        ),
        validators=[
            validators.RegexValidator(
                r"^[\w.@+-]+$",
                _(
                    "Enter a valid username. This value may contain only "
                    "letters, numbers "
                    "and @/./+/-/_ characters."
                ),
            ),
        ],
        error_messages={
            "unique": _("A owners with that username already exists."),
        },
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_(
            "Remember: Your login requires your email."
            "When you change it here, it also changes for the login - so "
            "use this new email when next you log in."
        ),
        validators=[validators.EmailValidator(_("Enter a valid email address"))],
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the owners can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this owners should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    date_modified = models.DateTimeField(_("last modified"), auto_now=True)
    contact_num = models.CharField(
        _("contact number"),
        max_length=15,
        blank=True,
        null=True,
        validators=[validate_msisdn],
        help_text=_(
            "Your cellphone number. If you elect to receive SMS notifications "
            "for some events, this number will be used."
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")