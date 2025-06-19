"""
Module: sdk.responses

A simple response class for responding to API calls and web requests.
    This is to cut down on repeated code in other modules.

Fucntions:
    - error_response:
        Creates a standardized error response with a message and status code.
    - success_response:
        Creates a standardized success response with optional message and data.

Dependencies:
    - flask: For creating JSON responses and handling HTTP status codes.
"""


from flask import jsonify, make_response, Response
from typing import Optional


def error_response(
    message: str,
    status: int = 400,
) -> Response:
    """
    A helper function to create an error response.

    Args:
        message (str): The error message to return.
        status (int): The HTTP status code for the error response.
            If not provided, defaults to 400 (Bad Request).

    Returns:
        Response: A Flask Response object with the error message
            and status code.
    """

    return make_response(
        jsonify(
            {
                'result': 'error',
                'message': message
            }
        ),
        status
    )


def success_response(
    message: Optional[str] = None,
    data: Optional[dict] = None,
    status: int = 200,
) -> Response:
    """
    A helper function to create a success response.

    Args:
        message (str): A success message to include in the response.
            This is optional and can be omitted for a success.
        data (dict): Additional data to include in the response.
            Used if we are returning more than just a success message.
        status (int): The HTTP status code for the success response.
            If not provided, defaults to 200 (OK).

    Returns:
        Response: A Flask Response object with the success message
            and status code.
    """

    # Standard response structure
    resp = {
        'result': 'success'
    }

    # Update with custom message or data if provided
    if message:
        resp['message'] = message
    if data:
        resp.update(data)

    return make_response(
        jsonify(
            resp
        ),
        status
    )
