# Empathy Engine with Microsoft LUIS

This is the backend server for the conversational AI used in the implementation of Flood Disaster VR


#### New Features!

  - Handles converstaions as POST requests as a REST service
  - Uses LUIS to process the NLU
  - Handles NLP sentiment analysis


#### Tech

This project is built using `Python 3.6.1`


### Installation

This repository requires [Python](https://www.python.org/downloads/) v3.6 to run.

Install the dependencies and devDependencies and start the server running on `PORT 3000`

```sh
$ cd empathy-engine-luis
```
Create a `.env` file and put the keys and endpoints for LUIS as `LUIS_KEY` and `LUIS_ENDPOINT`

```sh
$ pip install -r requirements.txt
$ python app.py
```

#### Endpoints

* POST - /ml/api/v1.0/assistant 
  Request:
`
    {
	    "sentence":"the text to be sent"
    }
`

* GET - /ml/api/v1.0/reset 
  
`



