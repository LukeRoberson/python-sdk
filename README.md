# Python SDK for REST API Communication

This Python SDK provides a simple and efficient way for Docker containers to communicate with each other through REST APIs. It includes functionality for configuration management, logging, and core service interactions.
</br></br>


## Features

- **Configuration Management**: Load and access configuration settings from the core service.
- **Logging**: Send logs to a centralized log service with various log levels.
- **Core Service Interaction**: Fetch and send data to the core service seamlessly.
- **Utility Functions**: Helper functions for common tasks.
</br></br>


## Installation

You can install the SDK using pip:

```bash
pip install git+https://github.com/LukeRoberson/python-sdk.git
```
</br></br>



----
# Usage
## Configuration

To use the configuration management feature:

```python
from sdk.config import Config

config = Config()
config.load_config()
setting_value = config.get_setting('your_setting_key')
```
</br></br>


## Logging

To log messages to the logging service (so they appear on the alerts page of the Web-UI):


Import the module:

```python
from sdk.logging import SystemLog
```
</br></br>


Instantiate the object, and setup the default values:

```python
logger = SystemLog(
    logging_url = 'http://logging:5100/api/log',
    source = 'The source of the event',
    destination = ['web', 'teams'],
    group = 'The log group',
    category = 'The log category',
    alert = 'The alert type',
    severity = 'the severity of the alert',
    teams_chat_id = 'The teams chat ID',
)
```

| Field         | Type   | Description                       | Example                     |
| ------------- | ------ | --------------------------------- | --------------------------- |
| logging_url   | String | The URL of the logging API        | http://logging:5100/api/log |
| source        | String | Represents the source             | Core Service                |
| destination   | List   | A list of destinations to send to | ['web', 'teams']            |
| group         | String | The event group                   | System                      |
| category      | String | The event category                | Authentication              |
| alert         | String | The event type                    | Failure                     |
| severity      | String | Severity level                    | Info, Warning               |
| teams_chat_id | String | The optional ID of the Teams chat |                             |

</br></br>


Send a log:

```python
logger.log(
    message="This is a message that will be logged."
)
```
</br></br>

Note, any of the default values can be overwritten. A different Teams message can also be sent.

For example:

```python
logger.log(
    message="This is an error log",
    severity="error",
    teams_msg="An error message has been received, please check the alerts page.",
)
```


## Core Service Interaction

To interact with the core service:

```python
from sdk.core import CoreService

core_service = CoreService()
data = core_service.fetch_data('your_endpoint')
core_service.send_data('your_endpoint', data)
```
</br></br>


