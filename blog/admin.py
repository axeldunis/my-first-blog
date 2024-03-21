from django.contrib import admin
from .models import Post, Show
from import_export import resources
from import_export.admin import ImportMixin

class ShowResource(resources.ModelResource):
    class Meta:
        model = Show
        fields = ("title", 'platform', 'genre', 'score_audience', "score_critic", "img",)

class ShowAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = ShowResource

admin.site.register(Post)
admin.site.register(Show, ShowAdmin)
