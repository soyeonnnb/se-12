from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# User Table 생성하기 위해 필요한 클래스
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError("The given User ID must be set")
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 유저 생성시
    def create_user(self, user_id=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(user_id, password, **extra_fields)

    # super user 생성시
    def create_superuser(self, user_id, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(user_id, password, **extra_fields)


# User table
class User(AbstractBaseUser, PermissionsMixin):

    """Custom User Model"""

    user_id = models.CharField(max_length=50, unique=True, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False)  # 이름 애트리뷰트
    password = models.CharField(max_length=45)  # Password 애트리뷰트
    phone = models.IntegerField(blank=True, null=True)  # 핸드폰번호 애트리뷰트
    email = models.EmailField(
        unique=True, blank=False, null=False
    )  # Email 애트리뷰트, 중복데이터 비허용
    is_host = models.BooleanField(default=False)  # 호스트 여부 필드

    # 장고 필수 필드
    date_joined = models.DateTimeField(blank=True, auto_now_add=True)  # 가입날짜 애트리뷰트
    is_staff = models.BooleanField(default=False)  # 스태프권한 애트리뷰트
    is_active = models.BooleanField(default=True)  # is_active 는 필수로 True 해야 로그인 가능
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)  # 최근 로그인날짜/시간 애트리뷰트
    objects = UserManager()  # User table을 위해 필요한 코드

    USERNAME_FIELD = "user_id"  # id가 식별자
    REQUIRED_FIELDS = ["name"]  # 필수입력값
