from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class GitHubIssuesViewSet(ViewSet):
    def list(self, *args, **kwargs):
        """
        Fetches issues for a specific GitHub project.
        """

        # Multiple example issues to return
        mock_issues = [
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

        return Response(mock_issues)

    def retrieve(self, *args, **kwargs):
        """
        Fetches a single issue for a specific GitHub project.
        """
        issue_number = self.kwargs.get("pk")

        # Single example issues to return
        mock_issue = {
            "url": "https://api.github.com/repos/dagster-io/dagster/issues/16393",
            "repository_url": "https://api.github.com/repos/dagster-io/dagster",
            "labels_url": "https://api.github.com/repos/dagster-io/dagster/issues/16393/labels{/name}",
            "comments_url": "https://api.github.com/repos/dagster-io/dagster/issues/16393/comments",
            "events_url": "https://api.github.com/repos/dagster-io/dagster/issues/16393/events",
            "html_url": "https://github.com/dagster-io/dagster/issues/16393",
            "id": 1887748214,
            "node_id": "I_kwDOB9hbPs5whMB2",
            "number": 16393,
            "title": "Dagster Cloud slack alert template",
            "user": {
                "login": "caio-eiq",
                "id": 111778420,
                "node_id": "U_kgDOBqmadA",
                "avatar_url": "https://avatars.githubusercontent.com/u/111778420?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/caio-eiq",
                "html_url": "https://github.com/caio-eiq",
                "followers_url": "https://api.github.com/users/caio-eiq/followers",
                "following_url": "https://api.github.com/users/caio-eiq/following{/other_user}",
                "gists_url": "https://api.github.com/users/caio-eiq/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/caio-eiq/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/caio-eiq/subscriptions",
                "organizations_url": "https://api.github.com/users/caio-eiq/orgs",
                "repos_url": "https://api.github.com/users/caio-eiq/repos",
                "events_url": "https://api.github.com/users/caio-eiq/events{/privacy}",
                "received_events_url": "https://api.github.com/users/caio-eiq/received_events",
                "type": "User",
                "site_admin": False
            },
            "labels": [
                {
                    "id": 918555701,
                    "node_id": "MDU6TGFiZWw5MTg1NTU3MDE=",
                    "url": "https://api.github.com/repos/dagster-io/dagster/labels/type:%20bug",
                    "name": "type: bug",
                    "color": "d73a4a",
                    "default": False,
                    "description": "Something isn't working"
                }
            ],
            "state": "open",
            "locked": False,
            "assignee": {
                "login": "dpeng817",
                "id": 17576880,
                "node_id": "MDQ6VXNlcjE3NTc2ODgw",
                "avatar_url": "https://avatars.githubusercontent.com/u/17576880?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/dpeng817",
                "html_url": "https://github.com/dpeng817",
                "followers_url": "https://api.github.com/users/dpeng817/followers",
                "following_url": "https://api.github.com/users/dpeng817/following{/other_user}",
                "gists_url": "https://api.github.com/users/dpeng817/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/dpeng817/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dpeng817/subscriptions",
                "organizations_url": "https://api.github.com/users/dpeng817/orgs",
                "repos_url": "https://api.github.com/users/dpeng817/repos",
                "events_url": "https://api.github.com/users/dpeng817/events{/privacy}",
                "received_events_url": "https://api.github.com/users/dpeng817/received_events",
                "type": "User",
                "site_admin": False
            },
            "assignees": [
                {
                    "login": "dpeng817",
                    "id": 17576880,
                    "node_id": "MDQ6VXNlcjE3NTc2ODgw",
                    "avatar_url": "https://avatars.githubusercontent.com/u/17576880?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/dpeng817",
                    "html_url": "https://github.com/dpeng817",
                    "followers_url": "https://api.github.com/users/dpeng817/followers",
                    "following_url": "https://api.github.com/users/dpeng817/following{/other_user}",
                    "gists_url": "https://api.github.com/users/dpeng817/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/dpeng817/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/dpeng817/subscriptions",
                    "organizations_url": "https://api.github.com/users/dpeng817/orgs",
                    "repos_url": "https://api.github.com/users/dpeng817/repos",
                    "events_url": "https://api.github.com/users/dpeng817/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/dpeng817/received_events",
                    "type": "User",
                    "site_admin": False
                }
            ],
            "milestone": None,
            "comments": 3,
            "created_at": "2023-09-08T14:00:12Z",
            "updated_at": "2023-09-08T20:57:16Z",
            "closed_at": None,
            "author_association": "NONE",
            "active_lock_reason": None,
            "body": "### Dagster version\n\n1.21.1\n\n### What's the issue?\n\nThere was a template update for the Dagster Cloud slack alerts which is displaying the color red for both success and failures.\r\n\r\n![image](https://github.com/dagster-io/dagster/assets/111778420/249cea59-4e3b-4405-b665-87e82dca8d47)\r\n \n\n### What did you expect to happen?\n\nSuccessful jobs should be in the color green\r\nFailed jobs should be in the color red\n\n### How to reproduce?\n\n- Create a \"catch all\" Dagster Cloud alert policy\r\n- Run a job to completion and check the slack alert notification. It will be displayed in a red color.\n\n### Deployment type\n\nNone\n\n### Deployment details\n\n_No response_\n\n### Additional information\n\n_No response_\n\n### Message from the maintainers\n\nImpacted by this issue? Give it a 👍! We factor engagement into prioritization.",
            "closed_by": None,
            "reactions": {
                "url": "https://api.github.com/repos/dagster-io/dagster/issues/16393/reactions",
                "total_count": 5,
                "+1": 5,
                "-1": 0,
                "laugh": 0,
                "hooray": 0,
                "confused": 0,
                "heart": 0,
                "rocket": 0,
                "eyes": 0
            },
            "timeline_url": "https://api.github.com/repos/dagster-io/dagster/issues/16393/timeline",
            "performed_via_github_app": None,
            "state_reason": None
        }

        return Response(mock_issue)
