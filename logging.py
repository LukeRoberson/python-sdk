class Logger:
    def __init__(self, log_service_url):
        self.log_service_url = log_service_url

    def log_info(self, message):
        self._send_log("INFO", message)

    def log_error(self, message):
        self._send_log("ERROR", message)

    def log_debug(self, message):
        self._send_log("DEBUG", message)

    def _send_log(self, level, message):
        # Here you would implement the logic to send the log to the log service
        # For example, using requests to send a POST request to the log service
        import requests

        log_entry = {
            "level": level,
            "message": message
        }
        try:
            response = requests.post(self.log_service_url, json=log_entry)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to send log: {e}")
