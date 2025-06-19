# Python SDK for REST API Communication

This Python SDK provides a simple and efficient way for Docker containers to communicate with each other through REST APIs. It includes functionality for configuration management, logging, and core service interactions.

## Features

- **Configuration Management**: Load and access configuration settings from the core service.
- **Logging**: Send logs to a centralized log service with various log levels.
- **Core Service Interaction**: Fetch and send data to the core service seamlessly.
- **Utility Functions**: Helper functions for common tasks.

## Installation

You can install the SDK using pip:

```bash
pip install git+https://github.com/yourusername/python-sdk.git
```

Replace `yourusername` with your GitHub username.

## Usage

### Configuration

To use the configuration management feature:

```python
from sdk.config import Config

config = Config()
config.load_config()
setting_value = config.get_setting('your_setting_key')
```

### Logging

To log messages:

```python
from sdk.logging import Logger

logger = Logger()
logger.log_info("This is an info message.")
logger.log_error("This is an error message.")
```

### Core Service Interaction

To interact with the core service:

```python
from sdk.core import CoreService

core_service = CoreService()
data = core_service.fetch_data('your_endpoint')
core_service.send_data('your_endpoint', data)
```
