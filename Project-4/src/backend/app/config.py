import os
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "OracleGenAI-RAG Knowledge Assistant"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    PORT: int = 8000

    OCI_CONFIG_FILE: str = os.path.expanduser("~/.oci/config")
    OCI_PROFILE: str = "DEFAULT"
    OCI_COMPARTMENT_ID: Optional[str] = None
    OCI_REGION: str = "us-chicago-1"
    OCI_GENAI_ENDPOINT: str = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
    OCI_GENAI_MODEL_ID: str = "cohere.command-r-plus"

    ORACLE_DB_USER: str = "admin"
    ORACLE_DB_PASSWORD: str = "YourStrongPassword23ai!"
    ORACLE_DB_DSN: str = "docuai23db_high"
    ORACLE_DB_WALLET_LOCATION: Optional[str] = None

    @property
    def is_demo_mode(self) -> bool:
        return self.APP_ENV.lower() == "development" or not self.OCI_COMPARTMENT_ID or "example" in (self.OCI_COMPARTMENT_ID or "")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
