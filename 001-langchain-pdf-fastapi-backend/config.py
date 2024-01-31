import os
import boto3
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    app_name: str = "Full Stack PDF CRUD App"
    AWS_KEY: str
    AWS_SECRET: str
    AWS_S3_BUCKET: str = "pdf-basic-app"

    @staticmethod
    def get_s3_client():
        return boto3.client(
            's3',
            aws_access_key_id=Settings().AWS_KEY,
            aws_secret_access_key=Settings().AWS_SECRET
        )

    class Config:
        env_file = ".env"
        extra = "ignore"
