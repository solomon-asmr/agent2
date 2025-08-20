# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration module for the customer service agent."""

import os
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AgentModel(BaseModel):
    """Agent model settings."""

    name: str = Field(default="customer_service_agent")
    model: str = Field(default="gemini-2.0-flash-live-preview-04-09")


class Config(BaseSettings):
    """Configuration settings for the customer service agent."""

    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../.env"
        ),
        case_sensitive=True,
        extra="ignore",  # optional: ignore extra env vars instead of erroring
    )

    agent_settings: AgentModel = Field(default=AgentModel())
    app_name: str = "customer_service_app"

    GOOGLE_CLOUD_PROJECT: str = Field(default="my_project")
    GOOGLE_CLOUD_LOCATION: str = Field(default="us-central1")
    GOOGLE_GENAI_USE_VERTEXAI: str = Field(default="1")

    # Google Cloud Service Account Credentials (loaded from .env)
    GOOGLE_APPLICATION_CREDENTIALS: str | None = Field(
        default=None,
        description="Path to Google Cloud service account key file"
    )

    # Fix: match the .env exactly
    GOOGLE_API_KEY: str | None = Field(default=None, description="Google AI Studio / Gemini API key")

    # Gemini image identification endpoint key
    GEMINI_API_KEY: str | None = Field(default=None)

    BACKEND_API_BASE_URL: str = Field(default="http://127.0.0.1:5000/api")
