class AppSetting:
    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, defl):
        from django.conf import Settings

        return getattr(Settings, self.prefix + name, defl)

    @property
    def PATH_LENGTH(self):
        return self._setting("PATH_LENGTH", 200)

app_setting = AppSetting("DRF_TRACKING_")