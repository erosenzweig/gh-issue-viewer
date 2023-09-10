import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import GithubIssues from './components/GithubIssues';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>GitHub Issue Viewer</h1>
      </header>
      <main>
        <GithubIssues />
      </main>
    </div>
  );
};

export default App;

