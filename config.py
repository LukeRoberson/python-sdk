class Config:
    def __init__(self, config_source):
        self.config_source = config_source
        self.settings = self.load_config()

    def load_config(self):
        # Logic to load configuration from the core service
        # This is a placeholder for actual implementation
        return {}

    def get_setting(self, key):
        return self.settings.get(key)

    @property
    def some_specific_setting(self):
        return self.get_setting('some_specific_setting')
