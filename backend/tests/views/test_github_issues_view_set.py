import mock
from rest_framework.test import APITestCase


class GithubIssuesViewSetTestCase(APITestCase):
    """
    Tests the viewsets functionality independently from the underlying service.
    """

    def setUp(self):
        self.multi_mocked_issues = [
            {
                "url": "https://api.github.com/repos/dagster-io/dagster/issues/16418",
                "repository_url": "https://api.github.com/repos/dagster-io/dagster",
                "labels_url": "https://api.github.com/repos/dagster-io/dagster/issues/16418/labels{/name}",
                "comments_url": "https://api.github.com/repos/dagster-io/dagster/issues/16418/comments",
                "events_url": "https://api.github.com/repos/dagster-io/dagster/issues/16418/events",
                "html_url": "https://github.com/dagster-io/dagster/pull/16418",
                "id": 1888706711,
                "node_id": "PR_kwDOB9hbPs5Z7n8i",
                "number": 16418,
                "title": "add indirect execution context access",
                "user": {
                    "login": "schrockn",
                    "id": 28738937,
                    "node_id": "MDQ6VXNlcjI4NzM4OTM3",
                    "avatar_url": "https://avatars.githubusercontent.com/u/28738937?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/schrockn",
                    "html_url": "https://github.com/schrockn",
                    "followers_url": "https://api.github.com/users/schrockn/followers",
                    "following_url": "https://api.github.com/users/schrockn/following{/other_user}",
                    "gists_url": "https://api.github.com/users/schrockn/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/schrockn/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/schrockn/subscriptions",
                    "organizations_url": "https://api.github.com/users/schrockn/orgs",
                    "repos_url": "https://api.github.com/users/schrockn/repos",
                    "events_url": "https://api.github.com/users/schrockn/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/schrockn/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "labels": [],
                "state": "open",
                "locked": False,
                "assignee": None,
                "assignees": [],
                "milestone": None,
                "comments": 1,
                "created_at": "2023-09-09T11:40:48Z",
                "updated_at": "2023-09-09T11:43:49Z",
                "closed_at": None,
                "author_association": "MEMBER",
                "active_lock_reason": None,
                "draft": True,
                "pull_request": {
                    "url": "https://api.github.com/repos/dagster-io/dagster/pulls/16418",
                    "html_url": "https://github.com/dagster-io/dagster/pull/16418",
                    "diff_url": "https://github.com/dagster-io/dagster/pull/16418.diff",
                    "patch_url": "https://github.com/dagster-io/dagster/pull/16418.patch",
                    "merged_at": None
                },
                "body": "## Summary & Motivation\n\n## How I Tested These Changes\n",
                "reactions": {
                    "url": "https://api.github.com/repos/dagster-io/dagster/issues/16418/reactions",
                    "total_count": 0,
                    "+1": 0,
                    "-1": 0,
                    "laugh": 0,
                    "hooray": 0,
                    "confused": 0,
                    "heart": 0,
                    "rocket": 0,
                    "eyes": 0
                },
                "timeline_url": "https://api.github.com/repos/dagster-io/dagster/issues/16418/timeline",
                "performed_via_github_app": None,
                "state_reason": None
            },
            {
                "url": "https://api.github.com/repos/dagster-io/dagster/issues/16417",
                "repository_url": "https://api.github.com/repos/dagster-io/dagster",
                "labels_url": "https://api.github.com/repos/dagster-io/dagster/issues/16417/labels{/name}",
                "comments_url": "https://api.github.com/repos/dagster-io/dagster/issues/16417/comments",
                "events_url": "https://api.github.com/repos/dagster-io/dagster/issues/16417/events",
                "html_url": "https://github.com/dagster-io/dagster/pull/16417",
                "id": 1888691829,
                "node_id": "PR_kwDOB9hbPs5Z7k6B",
                "number": 16417,
                "title": "Asset Execution Context exploraation",
                "user": {
                    "login": "schrockn",
                    "id": 28738937,
                    "node_id": "MDQ6VXNlcjI4NzM4OTM3",
                    "avatar_url": "https://avatars.githubusercontent.com/u/28738937?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/schrockn",
                    "html_url": "https://github.com/schrockn",
                    "followers_url": "https://api.github.com/users/schrockn/followers",
                    "following_url": "https://api.github.com/users/schrockn/following{/other_user}",
                    "gists_url": "https://api.github.com/users/schrockn/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/schrockn/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/schrockn/subscriptions",
                    "organizations_url": "https://api.github.com/users/schrockn/orgs",
                    "repos_url": "https://api.github.com/users/schrockn/repos",
                    "events_url": "https://api.github.com/users/schrockn/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/schrockn/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "labels": [],
                "state": "open",
                "locked": False,
                "assignee": None,
                "assignees": [],
                "milestone": None,
                "comments": 1,
                "created_at": "2023-09-09T10:57:06Z",
                "updated_at": "2023-09-09T11:54:24Z",
                "closed_at": None,
                "author_association": "MEMBER",
                "active_lock_reason": None,
                "draft": True,
                "pull_request": {
                    "url": "https://api.github.com/repos/dagster-io/dagster/pulls/16417",
                    "html_url": "https://github.com/dagster-io/dagster/pull/16417",
                    "diff_url": "https://github.com/dagster-io/dagster/pull/16417.diff",
                    "patch_url": "https://github.com/dagster-io/dagster/pull/16417.patch",
                    "merged_at": None
                },
                "body": "## Summary & Motivation\n\n## How I Tested These Changes\n",
                "reactions": {
                    "url": "https://api.github.com/repos/dagster-io/dagster/issues/16417/reactions",
                    "total_count": 0,
                    "+1": 0,
                    "-1": 0,
                    "laugh": 0,
                    "hooray": 0,
                    "confused": 0,
                    "heart": 0,
                    "rocket": 0,
                    "eyes": 0
                },
                "timeline_url": "https://api.github.com/repos/dagster-io/dagster/issues/16417/timeline",
                "performed_via_github_app": None,
                "state_reason": None
            },
        ]

    def test_retrieving_issues_from_endpoint(self):
        with mock.patch(
            "backend.services.github_issues_service.GithubIssuesService.get_project_issues",
            return_value=self.multi_mocked_issues
        ):
            only_project_name_response = self.client.get("/api/github_issues?project_name=testproject")
            self.assertEqual(only_project_name_response.status_code, 200)

            # assertJSONEqual requires the JSON object to be a str so check the response content rather than data.
            self.assertJSONEqual(only_project_name_response.content, self.multi_mocked_issues)

            project_name_and_issue_number_response = self.client.get(
                "/api/github_issues?project_name=testproject&issue_number=123"
            )
            self.assertEqual(project_name_and_issue_number_response.status_code, 200)
            self.assertDictEqual(project_name_and_issue_number_response.data[0], self.multi_mocked_issues[0])




