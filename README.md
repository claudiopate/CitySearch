# City Search

City Search is a simple search engine to retrieve some basic information on the Italian cities. The data source has been taken from the https://www.istat.it/it/archivio/6789
In particular they were considered two files:
- Elenco dei codici e delle denominazioni delle unità territoriali
- Elenco dei comuni soppressi

## Project Structure
The project is structured in three main folders:
- **app** : ReactJS Project to interact with the back-end
- **cron-job**: Python scripts to download periodically the files from web and update the Elasticsearch DB
- **server**: Flask Project to expose the search api and interact with the Elasticsearch DB to retrieve the records

<details>
  <summary>Project Structure in details</summary>
  
```
📦CitySearch
 ┣ 📂app
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┣ 📜ControlSearch.js
 ┃ ┃ ┃ ┣ 📜Result.js
 ┃ ┃ ┃ ┣ 📜SearchButton.js
 ┃ ┃ ┃ ┗ 📜SearchTextField.js
 ┃ ┃ ┣ 📜App.js
 ┃ ┣ 📜Dockerfile
 ┣ 📂cron-job
 ┃ ┣ 📂elasticsearch
 ┃ ┃ ┗ 📜write_db.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 📜generic_utils.py
 ┃ ┃ ┣ 📜handler.py
 ┃ ┃ ┣ 📜hash_utils.py
 ┃ ┃ ┗ 📜manage_files.py
 ┃ ┣ 📜crontab
 ┃ ┣ 📜cron_job.py
 ┃ ┣ 📜Dockerfile
 ┃ ┗ 📜requirements.txt
 ┣ 📂server
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📜search_docs.py
 ┃ ┣ 📂elasticsearch
 ┃ ┃ ┗ 📜write_db.py
 ┃ ┣ 📜app.py
 ┃ ┣ 📜Dockerfile
 ┃ ┗ 📜requirements.txt
 ┣ 📜docker-compose.yml
 ┗ 📜README.md
```

</details>

## Cron Job
The cron job is a python script to perform periodically some task, like:
- Download once a day the files from the web site
- Unzip the files
- Check if the hash value is changed from the version already saved
- Write the new records in an index called "cities" in the Elasticsearch DB

The script is containerized in a custom Docker image.  


## Back-end
The back-end part is a python script and expose a search api made with Flask. The server is listening at the port 5000, exposing the "/search/\<city-name\>" endopoint. This api will send a request to the elasticsearch db and retrieve data. 


## Front-end
The front-end was developed in ReactJS, starting from the package *create-react-app* . For the graphic layout it was used the Material UI Framework and in particular the following components:
- Text Field: where insert the city to search
- Button: Run the search
- Controls: Choose the search mode
- Grid: Show the results

Instead to perform the request to the server it was used the package *react-axios*

## Run the project

### Requirements
- Docker: version 20.10.5
- Docker-Compose: version 1.29.0

### How to start

```

cd <root of the project>
docker-compose up

```
