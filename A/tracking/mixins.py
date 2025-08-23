from .basemixins import BaseLoggingMixin
from .models import APIRequestLog


class LoggingMixin(BaseLoggingMixin):
    def handle_log(self):
        # APIRequestLog(**self.log).save()
        print(self.log)
