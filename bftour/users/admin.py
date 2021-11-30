from django.contrib import admin
from . import models


# User Admin 커스텀
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):  # Admin 페이지에 User 테이블 추가

    """User Admin Definition"""

    fieldsets = (  # User 애트리뷰트들 분류
        (
            "Basic Info",  # 기본 정보
            {
                "fields": (
                    "user_id",
                    "user_name",
                    "user_phone",
                    "user_email",
                    "is_host",
                )
            },
        ),
        (
            "Others",  # 추가 정보
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )
    list_display = (  # 메인 화면에서 해당 애트리뷰트들 보이기
        "user_id",
        "user_name",
        "user_email",
        "is_host",
        "is_staff",
    )
    ordering = (
        "user_id",
        "user_name",
    )  # 해당 애트리뷰트들로 순서
    list_filter = (
        "is_host",
        "is_staff",
    )  # 해당 애트리뷰트로 filtering 가능
