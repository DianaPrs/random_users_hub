random_users_hub
================
Web application collects users data from [Random user generator](https://randomuser.me/) API,
stored it in mongo database and providing interface for simple CRUD operations.

# Settings
Configuration file in webapp directory mast contain:

MONGO_URI = "mongodb+srv://<username>:<password>@<clustername>.k1pbt.mongodb.net/<dbname>?retryWrites=true&w=majority"
RANDOMUSER_URL = "https://randomuser.me/api/1.3/"
SECRET_KEY = "<your_secret_key>"

# Ran in container
```
docker build -t random_users_hub
docker run -p 5000:5000 random_users_hub
```

# Locally
```
git clone https://github.com/DianaPrs/random_users_hub.git
pip install -r requirements.txt
./run.sh
```

