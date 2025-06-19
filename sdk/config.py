"""
Module: sdk.config

This module provides a configuration management system for the SDK.

Classes:
    Config:
        Manages configuration settings for the application.
        Configuration is managed by the Core service.
        This class interacts with the Core service to manage config.

Dependencies:
    - requests: For making HTTP requests to the Core service.
    - traceback: For handling exceptions and printing tracebacks.
"""

import requests
import traceback as tb
import logging
import os
from typing import Tuple


logger = logging.getLogger("sdk.config")


class Config:
    """
    Config class to manage configuration settings for the application.

    Args:
        url (str): The URL to fetch the configuration from.
    """

    def __init__(
        self,
        url: str,
    ) -> None:
        """
        Initialize the Config class with a URL to fetch configuration from.

        Args:
            url (str): The URL to fetch the configuration from.

        Returns:
            None
        """

        self.url = url

    def __enter__(
        self
    ) -> 'Config':
        """
        Enter the runtime context related to this object.

        Args:
            None

        Returns:
            Config: The current instance of Config.
        """

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ) -> bool:
        """
        Exit the runtime context related to this object.

        Args:
            exc_type: The exception type.
            exc_value: The exception value.
            traceback: The traceback object.

        Returns:
            bool: True if the exception was handled, False otherwise.
        """

        # Handle any cleanup here if necessary
        if exc_type is not None:
            print("Exception occurred:")
            tb.print_exception(exc_type, exc_value, traceback)
            return False

        return True

    def read(
        self
    ) -> dict:
        """
        Fetch the current configuration from the Core service.
        """

        global_config = None
        try:
            response = requests.get(self.url, timeout=3)
            response.raise_for_status()
            global_config = response.json()

        except Exception as e:
            logging.critical(
                "Failed to fetch global config from core service."
                f" Error: {e}"
            )
            return {}

        if global_config is None:
            logging.critical(
                "Global configuration could not be loaded from core service."
            )
            return {}

        return global_config['config']

    def update(
        self,
        config: dict,
        reload_file: str,
    ) -> Tuple[bool, str]:
        """
        Update the configuration with the provided dictionary.

        Args:
            config (dict): The configuration dictionary to update.
            reload_file (str): The path to the file that triggers a reload
                of the uWSGI workers.

        Returns:
            Tuple[bool, str]: A tuple containing a success flag and a message.
        """

        # This method would typically send the config to the Core service
        print("Placeholder for update method.")

        # Forward the PATCH request to the core service
        try:
            resp = requests.patch(
                self.url,
                json=config,
                timeout=3
            )

            if resp.status_code != 200:
                return (
                    False,
                    resp.text
                )

        except Exception as e:
            logging.error("Failed to patch core service: %s", e)
            return (
                False,
                f"{e}"
            )

        # If successful, recycle the workers to apply the changes
        try:
            with open(reload_file, 'a'):
                os.utime(reload_file, None)
        except Exception as e:
            logging.error("Failed to update reload.txt: %s", e)

        return (
            True,
            "Configuration updated successfully."
        )
