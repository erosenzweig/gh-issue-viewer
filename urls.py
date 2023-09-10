from django.contrib import admin
from django.urls import path, re_path
from backend.views import GitHubIssuesViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/github_issues", GitHubIssuesViewSet.as_view({"get": "list"})),
]

