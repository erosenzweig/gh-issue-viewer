from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from requests.exceptions import RequestException
from backend.services.github_issues_service import GithubIssuesService


class GitHubIssuesViewSet(ViewSet):
    def list(self, *args, **kwargs):
        """
        Fetches issue(s) for a specific GitHub project.
        """
        # project_name is required
        project_name = self.request.query_params.get("project_name")

        # Optional and will be None by default. The GithubIssuesService handles this case.
        issue_number = self.request.query_params.get("issue_number")

        try:
            issues = GithubIssuesService.get_project_issues(project_name, issue_number=issue_number)
        except (RequestException, ValueError):
            # These errors could be more specific and helpful to the caller. For example, if a project is not
            # found (404) versus a networking error occurred, or when project_name (required) is not
            # provided - using this catch all for brevity.
            return Response({'error': 'Failed to fetch GitHub issues.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(issues)
