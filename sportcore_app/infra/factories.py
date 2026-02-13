import os
from sportcore_app.infra.pagos import PagoReal, PagoMock


class PagoFactory:

    @staticmethod
    def create():
        if os.getenv("ENV") == "PROD":
            return PagoReal()
        return PagoMock()
