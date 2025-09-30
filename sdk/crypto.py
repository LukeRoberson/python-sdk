"""
Module: sdk.crypt

This module provides cryptography services through the security service.

Classes:
    CryptoServices:
        Enables encryption and decryption of values.

Dependencies:
    - requests: For making HTTP requests to the Core service.
    - traceback: For handling exceptions and printing tracebacks.
"""


import requests
import logging
from typing import Tuple


class CryptoServices:
    """
    CryptoServices class to manage cryptographic operations.
    """

    def __init__(
        self,
        url: str,
    ) -> None:
        """
        Initialize the CryptoServices class with a URL to the crypto service.

        Args:
            url (str): The URL of the crypto service.

        Returns:
            None
        """

        self.url = url

    def __enter__(
        self
    ) -> 'CryptoServices':
        """
        Enter the runtime context related to this object.

        Args:
            None

        Returns:
            CryptoServices: The instance of the CryptoServices class.
        """

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ) -> None:
        """
        Exit the runtime context related to this object.
        Args:
            exc_type: The exception type.
            exc_value: The exception value.
            traceback: The traceback object.
        Returns:
            None
        """
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
            if traceback:
                print("Traceback:", traceback)

    def encrypt(
        self,
        plain_text: str,
    ) -> Tuple[str, str]:
        """
        Get the security service to encrypt a value.

        Args:
            plain_text (str): The plain-text to be encrypted.

        Returns:
            Tuple[str, str]:
                A tuple containing the encrypted value and salt.
                On error, returns a tuple with "error" and the error message.
        """

        # API call to the crypto service to encrypt the plain text
        try:
            response = requests.post(
                self.url,
                json={
                    "type": "encrypt",
                    "plain-text": plain_text
                }
            )
            data = response.json()

        except Exception as e:
            logging.error("Encryption failed: %s", e)
            return ("error", str(e))

        # Get the encrypted value and salt from the response
        if data and 'result' in data and data['result'] == "success":
            encrypted_value = data.get("encrypted", "")
            salt_value = data.get("salt", "")

        # Handle errors
        else:
            error = data.get("error", "Unknown error")
            logging.error(
                f"CryptoServices.Encrypt => "
                f"Encryption service returned an error: {error}"
            )
            return ("error", str(error))

        # Return the encrypted value and salt
        return (encrypted_value, salt_value)

    def decrypt(
        self,
        encrypted: str,
        salt: str,
    ) -> Tuple[str, str]:
        """
        Get the security service to decrypt a value.

        Args:
            encrypted (str): The encrypted value to be decrypted.
            salt (str): The salt used for encryption.

        Returns:
            Tuple[str, str]:
                A tuple containing the decrypted value and salt.
                On error, returns a tuple with "error" and the error message.
        """

        # API call to the crypto service to encrypt the plain text
        try:
            response = requests.post(
                self.url,
                json={
                    "type": "decrypt",
                    "encrypted": encrypted,
                    "salt": salt,
                }
            )
            data = response.json()

        except Exception as e:
            logging.error("Decryption failed: %s", e)
            return ("error", str(e))

        # Get the decrypted value from the response
        if data and 'result' in data and data['result'] == "success":
            decrypted_value = data.get("decrypted", "")

        # Handle errors
        else:
            error = data.get("error", "Unknown error")
            logging.error(
                f"CryptoServices.Decrypt => "
                f"Encryption service returned an error: {error}"
            )
            return ("error", str(error))

        # Return the encrypted value and salt
        return (decrypted_value, salt)
