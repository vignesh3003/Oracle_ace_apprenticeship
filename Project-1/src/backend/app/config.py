import os
from typing import List, Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "OracleDocuAI API"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    PORT: int = 8000
    API_V1_PREFIX: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    # Oracle Cloud Infrastructure (OCI) Credentials
    OCI_CONFIG_FILE: str = os.path.expanduser("~/.oci/config")
    OCI_PROFILE: str = "DEFAULT"
    OCI_COMPARTMENT_ID: Optional[str] = None
    OCI_REGION: str = "us-ashburn-1"
    OCI_BUCKET_NAME: str = "docu-ai-bucket"
    OCI_NAMESPACE: Optional[str] = None
    OCI_VISION_ENDPOINT: Optional[str] = None

    # Oracle Autonomous Database 23ai
    ORACLE_DB_USER: str = "admin"
    ORACLE_DB_PASSWORD: str = "YourStrongPassword23ai!"
    ORACLE_DB_DSN: str = "docuai23db_high"
    ORACLE_DB_WALLET_LOCATION: Optional[str] = None
    ORACLE_DB_WALLET_PASSWORD: Optional[str] = None
    ORACLE_DB_THIN_MODE: bool = True

    @property
    def is_demo_mode(self) -> bool:
        """Returns True if running in development / demo simulation mode without OCI credentials."""
        return self.APP_ENV.lower() == "development" or not self.OCI_COMPARTMENT_ID or "example" in (self.OCI_COMPARTMENT_ID or "")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
