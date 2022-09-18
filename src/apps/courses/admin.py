from django.contrib import admin
from apps.courses.models import Course, Module, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "created"]
    list_filter = ["created", "subject"]
    search_filed = ["title", "overview"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ModuleInline]


# usa o site de índice para administração memcache
admin.site.index_template = 'memcache_status/admin_index.html'