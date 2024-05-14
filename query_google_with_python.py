import json
import requests
import sys


def json_load(json_file_path):
    """
    Description:
    The json_load function will Function to load the JSON file and extract the API key and search engine ID.
    The api_key and engine_key are encapsulated to be used in the later query string formation.

    Args:
        json_file_path: The path to the JSON file that contains the Google API key and search engine ID.

    Returns:
        json_data: The JSON data that is read from the JSON file.
        api_key: The Google API key that is read from the JSON file.
        engine_id: The Google Search Engine ID that is read from the JSON file.
      """
    try:
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
            api_key = json_data["key"]
            engine_id = json_data["search_engine_id"]
            return api_key, engine_id

    #Error handling for JSON file deocding issues
    except json.decoder.JSONDecodeError as json_error:
        print(f"An error occured during the JSON file decoding: {json_error}")
        return None, None

    #Error handling for JSON file reading issues
    except FileNotFoundError as file_error:
        print(f"An error occured during the JSON file reading: {file_error}")
        return None, None

    #Error handling for JSON file key reading issues
    except KeyError as key_error:
        print(f"An error occured during the API key reading: {key_error}")
        return None, None


def google_search(api_key, engine_id, input_search_query):
    """
    Description:
    The google_search function performs the API request to the Google Search API.
    It utilizes the base url along with the params to form the query string.
    The HTTP header is printed and an error if displayed if it is not 200.

    Args:
        api_key: The Google API key that is read from the JSON file.
        engine_id: The Google Search Engine ID that is read from the JSON file.
        input_search_query: The search query that is entered by the user.

    Returns:
        status_code: The HTTP status code that is returned from the API request.
        headers: The HTTP headers that are returned from the API request.
        response_data: The JSON response data that is returned from the API request.
      """
    
    #The base URL for the Google Search API request
    base_url = "https://customsearch.googleapis.com/customsearch/v1"

    #Query string parameters for the Google Search API request
    url_params = {
        'q': input_search_query,
        'key': api_key,
        'cx': engine_id
    }

    #Requests.get() used to send a GET request to the Google Search API
    try:
        #GET method contains the above-specified URL and query parameters
        response = requests.get(base_url,params= url_params, allow_redirects = True, timeout = 5)
        #Raises an HTTPErrors if the response status code is not 200
        response.raise_for_status()
        status_code = response.status_code
        if response.status_code == 200:
            #If the response status code is 200, the response data and headers are returned
            response_data = response.json()
        headers = response.headers
        return status_code, headers, response_data, response
    
    except requests.RequestException as request_error:
        print(f"An error occured during the API request: {request_error}")
        return None, None, None


#Ensure that just the Python project file and JSON file are provided as command line arguements
if len(sys.argv) < 2:
    print("Please provide the JSON file path as an argument. {Python file} {JSON file path}")
    sys.exit(1)

#Read the JSON file path from the command line arguements
else:
    json_file_path = sys.argv[1]
api_key, engine_id = json_load(json_file_path)


# Main program loop to prompt the user for search queries
while True:
    input_search_query = input("Search term? Enter 'stop' to end the query session. ").strip()

    #Condition that breaks the loop if the user enters 'stop'
    if input_search_query.lower() == 'stop':
        break

    #Function call to the google_search function
    status_code, headers, response_data, response  = google_search(api_key, engine_id, input_search_query)
    if response_data:
        print(f"\nHTTP response status code: {status_code}\n")
        print("HTTP response headers:")
        for header, value in headers.items():
            print(f"{header} : {value}")
        print("\nSearch term results:")
        #Iterate through the search results and get each individual item.
        #If "items" doesn't exist then provide an empty list instead of a KeyError
        for item in response_data.get("items", []):
            #Encapsulate the URL title as requested in the project guidelines
            title = item.get("title")
            #Encapsulate the URL link as requested in the project guidelines
            link = item.get("link")
            #If the list item meets the qualifying conditions then print the title and link to the terminal
            if title and link:
                print(f"{title} ----- {link}")
        print("\n")