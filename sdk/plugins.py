"""
Module: sdk.plugins

This module provides a plugin management system for the SDK.

Classes:
    PluginManager:
        Manage plugins through API calls to the Core service.
        Supports CRUD operations.

Dependencies:
    - requests: For making HTTP requests to the Core service.
    - traceback: For handling exceptions and printing tracebacks.
"""


import requests
import traceback as tb
import logging
from typing import Optional


logger = logging.getLogger("sdk.plugins")


class PluginManager:
    """
    Class to manage plugins. Uses API calls to the Core service.

    Args:
        url (str): The URL to fetch the configuration from.
    """

    def __init__(
        self,
        url: str,
    ) -> None:
        """
        Initialize the class with a URL for the API plugin endpoint
            on the core service.

        Args:
            url (str): The URL to fetch the configuration from.

        Returns:
            None
        """

        self.url = url

    def __enter__(
        self
    ) -> 'PluginManager':
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

    def _plugin_request(
        self,
        method: str,
        config: dict
    ) -> bool:
        """
        Make a request to the Core API to manage plugins.
            Used with create, update, and delete operations.

        Args:
            method (str): The HTTP method to use
                (e.g., 'POST', 'PATCH', 'DELETE').
            config (dict): The configuration for the plugin to manage.

        Returns:
            bool: True if the request was successful, False otherwise.
        """

        if not config:
            logging.error("No configuration provided for the plugin.")
            return False

        try:
            response = requests.request(
                method,
                self.url,
                json=config,
                timeout=3
            )

            if response.status_code != 200:
                logging.error(
                    "Core service failed to %s plugin:\n %s",
                    method,
                    response.text
                )
                return False

        except Exception as e:
            logging.error("Error accessing the plugins API: %s", e)
            return False

        return True

    def create(
        self,
        config: dict
    ) -> bool:
        """
        Add a new plugin using the Core API.

        Args:
            config (dict): The configuration for the plugin to add.

        Returns:
            bool: True if the plugin was added successfully, False otherwise.
        """

        return self._plugin_request(
            'POST',
            config,
        )

    def read(
        self,
        name: Optional[str] = 'all',
    ) -> list:
        """
        Fetch the plugin configuration from the core service.

        Args:
            name (Optional[str]): The name of the plugin to fetch.
                Fetches all plugins by default.

        Returns:
            list: A list of plugins and configuration loaded
                from the core service.

        Raises:
            RuntimeError: If the plugin configuration cannot be loaded.
        """

        plugin_config = None
        try:
            response = requests.get(
                self.url,
                headers={'X-Plugin-Name': name},
                timeout=3,
            )
            response.raise_for_status()
            plugin_config = response.json()

        except Exception as e:
            logging.critical(
                "Failed to fetch plugin config from core service."
                f" Error: {e}"
            )
            return []

        if plugin_config is None:
            logging.critical(
                "Plugin configuration could not be loaded from core service."
            )
            return []

        return plugin_config['plugins']

    def update(
        self,
        config: dict
    ) -> bool:
        """
        Update an existing plugin using the Core API.

        Args:
            config (dict): The updated configuration for the plugin.

        Returns:
            bool: True if the plugin was updated successfully, False otherwise.
        """

        return self._plugin_request(
            'PATCH',
            config
        )

    def delete(
        self,
        config: dict
    ) -> bool:
        """
        Delete a plugin using the Core API.

        Args:
            config (dict):
                The configuration containing the name of the plugin to delete.

        Returns:
            bool: True if the plugin was deleted successfully, False otherwise.
        """

        return self._plugin_request(
            'DELETE',
            config
        )
