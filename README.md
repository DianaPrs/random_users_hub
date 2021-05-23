random_users_hub
================
Web application collects users data from [Random user generator](https://randomuser.me/) API,
stored it in mongo database and providing interface for simple CRUD operations.

# Settings
Configuration file config.py in webapp directory mast contain:

- MONGO_URI = "mongodb+srv://{username}:{password}@{clustername}.k1pbt.mongodb.net/"
- RANDOMUSER_URL = "https://randomuser.me/api/1.3/"
- SECRET_KEY = "{your_secret_key}"

# Ran in container
```
docker build -t random_users_hub .
docker run -p 5000:5000 random_users_hub
```

# Locally

Clone the repo:
```
git clone https://github.com/DianaPrs/random_users_hub.git
```
Create virtual environment:
```
python -m venv env
```
Activate virtual environment for Linux or Mac:
```
source env/bin/activate
```
for Windows:
```
env\Scripts\activate
```
Inatall packages and run:
```
pip install -r requirements.txt
./run.sh
```

