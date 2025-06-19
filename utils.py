def format_response(response):
    # Function to format the API response
    return response.json() if response else None


def handle_error(error):
    # Function to handle errors
    return {"error": str(error)}
