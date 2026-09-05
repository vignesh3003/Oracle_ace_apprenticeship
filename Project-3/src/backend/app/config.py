import os
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "OracleTelemetryX Engine"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    PORT: int = 8000

    OCI_CONFIG_FILE: str = os.path.expanduser("~/.oci/config")
    OCI_PROFILE: str = "DEFAULT"
    OCI_COMPARTMENT_ID: Optional[str] = None
    OCI_REGION: str = "us-ashburn-1"
    OCI_ONS_TOPIC_OCID: Optional[str] = None

    ORACLE_DB_USER: str = "admin"
    ORACLE_DB_PASSWORD: str = "YourStrongPassword23ai!"
    ORACLE_DB_DSN: str = "docuai23db_high"
    ORACLE_DB_POOL_MIN: int = 2
    ORACLE_DB_POOL_MAX: int = 10
    ORACLE_DB_WALLET_LOCATION: Optional[str] = None

    @property
    def is_demo_mode(self) -> bool:
        return self.APP_ENV.lower() == "development" or not self.OCI_ONS_TOPIC_OCID or "example" in (self.OCI_ONS_TOPIC_OCID or "")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
