# Pythonic-Google-Search-Engine
Python program that queries Google based on the user-provided search term.

## Introduction
This Python script interacts with the Google Search API to perform searches based on user input. It reads the users API key and search engine ID from a JSON file referenced in the command line and allows users to input search queries. The script then retrieves search results from the Google Search API and displays them.

## Note
Please note that in order to use this project, you'll need to create your own JSON file that holds YOUR Google search engine ID and API key. The format should be as follows:
```json
{
"key" : "YOUR API KEY",
"search_engine_id" : "YOUR SEARCH ENGINE ID"
}
```

## Features

- **Search Execution**: Users can input search queries and retrieve results from the Google Search API.
- **Error Handling**: Provides error messages for failed API requests and invalid JSON files.
- **User Interface**: Utilizes a command-line interface for interaction.

## Installation
Ensure you have Python installed on your system. Additionally, you need to have the `requests` library installed. You can install it via pip:

```bash
pip install requests
```

## Usage
1. Create a JSON file with your Google API key and search engine ID.
2. Run the Python script providing the path to your JSON file as a command-line argument:

```bash
python query_google_with_python.py path/to/json_file.json
```

## Contributing
Contributions are welcome. Please submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
