import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Form, Button, Table } from 'react-bootstrap';

interface Issue {
  id: number;
  title: string;
  html_url: string;
}

const GithubIssues: React.FC = () => {
  const [repoName, setRepoName] = useState<string>('');
  const [issues, setIssues] = useState<Issue[]>([]);
  const [loading, setLoading] = useState<boolean>(false);

  const fetchIssues = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:8000/api/github_issues?project_name=${repoName}`);
      setIssues(response.data);
    } catch (error) {
      console.error(`Error fetching issues: ${error}`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (repoName) {
      fetchIssues();
    }
  }, [repoName]);

  return (
    <Container>
      <Row>
        <Col>
          <Form>
              <Form.Group as={Row}>
                <Form.Label column className="col-sm-2">Repository Name:</Form.Label>
                <Col sm={6} className="col-sm-8">
                  <Form.Control
                    id="repoNameInput"
                    type="text"
                    placeholder="Enter repo (e.g. facebook/react)"
                    value={repoName}
                    onChange={(e) => setRepoName(e.target.value)}
                  />
                </Col>
                <Button id="fetchIssuesButton" variant="primary" onClick={fetchIssues} className="fetch-button col-sm-2">
                  Fetch Issues
                </Button>
            </Form.Group>
          </Form>
        </Col>
      </Row>
      <Row className="mt-4">
        <Col>
          {loading ? (
            <p>Loading...</p>
          ) : (
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Title</th>
                  <th>Link</th>
                </tr>
              </thead>
              <tbody>
                {issues.map((issue) => (
                  <tr key={issue.id} data-testid="data-row">
                    <td>{issue.id}</td>
                    <td>{issue.title}</td>
                    <td>
                      <a href={issue.html_url} target="_blank" rel="noopener noreferrer">
                        View Issue
                      </a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          )}
        </Col>
      </Row>
    </Container>
  );
};

export default GithubIssues;
