# City Search

City Search is a simple search engine to retrieve some basic information on the Italian cities. The data source has been taken from the https://www.istat.it/it/archivio/6789
In particular they were considered two files:
- Elenco dei codici e delle denominazioni delle unità territoriali
- Elenco dei comuni soppressi

## Project Structure
The project is structured in three main folders:
- **app** : ReactJS Project to interact with the back-end
- **cron-job**: Python scripts to download periodically the files from web and update the Elasticsearch DB
- **server**: Flask Project to expose the search api

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

