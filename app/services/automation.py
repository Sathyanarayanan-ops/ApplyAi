from app.services.groq_client import GroqClient
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

groq_client = GroqClient()

def apply_to_job_smart(link, job_description):
    """
    Automates the process of applying to a job with Llama assistance.

    Args:
        link (str): Job application link.
        job_description (str): Text of the job description.

    Returns:
        str: Status message indicating success or failure.
    """
    try:
        # Initialize browser (e.g., Chrome)
        driver = webdriver.Chrome()
        driver.get(link)

        # Example: Use static values for known fields
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
        driver.find_element(By.ID, "resume").send_keys("/path/to/resume.pdf")

        # Example: Use Llama for dynamic fields
        dynamic_fields = ["cover_letter", "experience_summary"]
        for field in dynamic_fields:
            field_content = groq_client.process_field(field, job_description)
            driver.find_element(By.ID, field).send_keys(field_content)

        # Submit the form
        driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        driver.quit()

        return f"Successfully applied to {link} with Llama assistance"
    except Exception as e:
        return f"Failed to apply to {link}: {str(e)}"
