import requests
from urllib.parse import unquote


# Separating this functionality out into its own service allows for
# unit testing independently of the django or the django rest framework.
class GithubIssuesService:
    """
    Service class used to interface with the github API and retrieve issues for a project.
    """
    @staticmethod
    def get_project_issues(project_name):
        """
        Fetches issues for the specified project.

        :param project_name: A string that represents the repo to fetch issues for from github.
        :returns: A list of github issues for a project.
        """
        # Value and type checks for params.
        if project_name is None or not isinstance(project_name, str):
            raise ValueError("project_name is required and must be a string.")

        # Allows for public repos with multiple applications and special characters in the name e.g dagster-io/dagster
        project_name = unquote(project_name)

        # Assume we're retrieving a list of issues
        github_api_url = f"https://api.github.com/repos/{project_name}/issues"

        # Perform the GET request to get issues for the project_name
        gh_issues_response = requests.get(github_api_url)

        # When making a request, it's typical to check if the request was successful (response.status_code == 200).
        # Here we opt to raise an exception if any have occurred. This allows the caller to handle
        # different types of exceptions or all exceptions in a try...except block. An alternative implementation
        # would be to define the error states this service class could emit and handle them appropriately within the
        # rest of the application or by the caller.
        #
        # The requests documentation on the different types of exceptions, their conditions, and a note on
        # the base exception class can be found here
        # https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
        gh_issues_response.raise_for_status()

        return gh_issues_response.json()
