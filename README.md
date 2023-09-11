# Github Issue Viewer

Have you always dreamed of an application you could run locally to view your Github Issues? If so, gh-issue-viewer is the app for you! 

### Quickstart

The quickest way to get this application started is docker. Simply run
```shell
docker compose up -d 
```

This will spin up a `backend` container that includes the django API. It also spins up a `ui` container with 
the React UI for this app. 

### Non-Containerized Development

If you're more of the [Cetaphobia](https://www.fearof.net/fear-of-whales-phobia-cetaphobia/#:~:text=Hundreds%20of%20thousands%20of%20people,the%20Greek%20God%20of%20fear.) type, you can also run this app locally with a virtual environment by following the steps below. 

#### Start Backend

You can start the Django API server for this application by following the steps below. 

1. In the root directory of this project, create a virtual environment and activate it
```sh
# OPTIONAL: install the virtualenv package if not already installed
pip install virtualenv 

python -m virtualenv venv 

source ./venv/bin/activate
```
2. Install the project dependencies
```sh
pip install -r requirements.txt
```
3. Run API backend
```sh
./manage.py runserver
```

##### Running Tests (Django)

Test can be run with the following command.

_NOTE: ensure a virtual environment exists, dependencies are installed in the virtual environment, and it is activated. See above for those steps._

1. In the root directory of this project, create a virtual environment if one does not exist then activate it.
```sh
./manage.py test
```
with an expected output similar to 
```sh
nosetests --verbosity=1
Creating test database for alias 'default'...
.....
----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
Destroying test database for alias 'default'...
```

#### Start UI

You can start the UI for this application by following the steps below. 

1. Navigate to the `ui` folder. 
```sh
cd ui
```
2. Install the ui dependencies.
```sh
npm install
```
3. Run the ui
```sh
npm run start
```

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

##### Running Tests (React)

Test can be run with the following command.

1. In the `ui` directory of this project, run
```sh
npm run test
```
which should result in something similar to 
```shell
 PASS  src/App.test.tsx (6.467 s)
  ✓ renders page with no github issues data (20 ms)
  ✓ renders page with github issues data (131 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        7.241 s
Ran all test suites.
```

### Future Enhancements

Below are just a few of many considerations for enhancements in the future:

###### Backend

- standardize errors emitted from GithubIssuesService
- more helpful error messages back to callers

###### Frontend

- create a custom view / components for previewing single github issues instead of a link.
- debounce input into the `Repository Name` input. 
- better consolidation of styling instead of inline styles. 
- better compartmentalization of components to promote [low coupling and high cohesion](https://enterprisecraftsmanship.com/posts/cohesion-coupling-difference/#:~:text=In%20essence%2C%20high%20cohesion%20means,base%20as%20much%20as%20possible.). 

###### DevOps

- productionize docker images instead of running development servers.
- add CI/CD pipelines for automated testing and triggering of deployment.
