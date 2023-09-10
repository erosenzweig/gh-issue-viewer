import axios from 'axios';
import React from 'react';
import { act } from 'react-dom/test-utils';
import {render, screen, waitFor} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';

// Mock Axios GET method
jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

test('renders page with no github issues data', () => {
    render(<App/>);
    const headerElement = screen.getByText(/Github Issue Viewer/i);
    expect(headerElement).toBeInTheDocument();
});

test('renders page with github issues data', async () => {
    const mockedIssues = [
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
                "site_admin": false
            },
            "labels": [],
            "state": "open",
            "locked": false,
            "assignee": null,
            "assignees": [],
            "milestone": null,
            "comments": 1,
            "created_at": "2023-09-09T11:40:48Z",
            "updated_at": "2023-09-09T11:43:49Z",
            "closed_at": null,
            "author_association": "MEMBER",
            "active_lock_reason": null,
            "draft": true,
            "pull_request": {
                "url": "https://api.github.com/repos/dagster-io/dagster/pulls/16418",
                "html_url": "https://github.com/dagster-io/dagster/pull/16418",
                "diff_url": "https://github.com/dagster-io/dagster/pull/16418.diff",
                "patch_url": "https://github.com/dagster-io/dagster/pull/16418.patch",
                "merged_at": null
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
            "performed_via_github_app": null,
            "state_reason": null
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
                "site_admin": false
            },
            "labels": [],
            "state": "open",
            "locked": false,
            "assignee": null,
            "assignees": [],
            "milestone": null,
            "comments": 1,
            "created_at": "2023-09-09T10:57:06Z",
            "updated_at": "2023-09-09T11:54:24Z",
            "closed_at": null,
            "author_association": "MEMBER",
            "active_lock_reason": null,
            "draft": true,
            "pull_request": {
                "url": "https://api.github.com/repos/dagster-io/dagster/pulls/16417",
                "html_url": "https://github.com/dagster-io/dagster/pull/16417",
                "diff_url": "https://github.com/dagster-io/dagster/pull/16417.diff",
                "patch_url": "https://github.com/dagster-io/dagster/pull/16417.patch",
                "merged_at": null
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
            "performed_via_github_app": null,
            "state_reason": null
        },
    ];

    mockedAxios.get.mockResolvedValueOnce({
        data: mockedIssues
    });

    render(<App/>);

    // Find elements
    const repoNameInput = screen.getByPlaceholderText('Enter repo (e.g. facebook/react)') as HTMLInputElement;
    const fetchButton = screen.getByText('Fetch Issues') as HTMLButtonElement;

    act(() => {
        // Update repo name and click fetch issues button
        userEvent.type(repoNameInput, 'dagster-io/dagster');
        userEvent.click(fetchButton);
    });

    // Wait for table to be populated and then perform checks
    await waitFor(() => {
      const rows = screen.getAllByRole('row');
      expect(rows).toHaveLength(3); // 2 data rows + 1 header row
    });
});
