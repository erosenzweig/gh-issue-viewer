# Getting Started

Have you always dreamed of an application you could run locally to view your Github Issues? If so, gh-issue-viewer is the app for you! 

### Start Backend

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

### Start UI

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
