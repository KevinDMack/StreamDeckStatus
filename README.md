# StreamDeckStatus
This application is designed to run in a container and be able to be to get / update a status that will be displayed on a magic mirror. 

# Pre-requisites:
The following will run to install the requirements:
```bash
pip install -r requirements.txt
```
To confirm run the following:
```bash
pip list
```

# Running in the devcontainer:
The following command will run the app in the devcontainer:
```bash
python3 ./status-api.py 
```

This command will execute a post to create a status message:
```bash
curl -X POST http://127.0.0.1:5000/api/status -H "Content-Type: application/json" -d '{"status_message":"test"}'
```

This command will retrieve the status:
```bash
curl -X GET http://127.0.0.1:5000/api/status
```