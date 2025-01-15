import requests
from app.core.config import settings

class GroqClient:
    def __init__(self):
        self.api_key = settings.groq_api_key
        self.endpoint = settings.groq_endpoint

    def process_field(self, field_name: str, job_description: str):
        """
        Use Llama on Groq to process dynamic fields based on job description.

        Args:
            field_name (str): Name of the form field.
            job_description (str): Text of the job description.

        Returns:
            str: Suggested content for the field.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "input": {
                "field_name": field_name,
                "job_description": job_description
            }
        }

        response = requests.post(f"{self.endpoint}/llama/process_field", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("output", "Default value")
        else:
            raise Exception(f"Groq API Error: {response.status_code} - {response.text}")
