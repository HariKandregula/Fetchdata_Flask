1. In the command prompt enter the command "python3 -m venv .venv" to install the virtual environment.
2. Enter the command ".venv\Scripts\activate" to activate the virtual environment.
3. Enter the command "pip install Flask" to install Flask.
4. Enter the command "**flask --app demo run**" to start the server.
5. Open a browser and enter the url https://127.0.0.1:5000/fetch-data to fetch the data.
6. Click on the button "Get the processed data set" to process the data fetched, which will be displayed in the below textarea.
7. This project fetches a sample json data and stores it in the file "raw_data.json". In the same location from where the python file is executed.
8. It also stores the processed data in the file "processed_data.json"