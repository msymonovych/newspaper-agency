from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Topic, News, Redactor


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional Information", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                 "Additional Information",
                 {
                     "fields": (
                         "first_name",
                         "last_name",
                         "years_of_experience",
                     )
                 },
            ),
        )
    )


admin.site.register(Topic)
admin.site.register(News)
