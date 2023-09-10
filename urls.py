from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from backend.views import GitHubIssuesViewSet

router = DefaultRouter()
router.register(r"github_issues", GitHubIssuesViewSet, basename="github_issues")

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/", include(router.urls)),
]

