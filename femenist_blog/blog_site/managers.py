from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, date_of_birth, password = None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have a email')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last_name')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, date_of_birth, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user