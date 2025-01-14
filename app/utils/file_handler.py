async def process_file(file):
    """
    Reads and processes a file containing job links.

    Args:
        file (UploadFile): The uploaded file.

    Returns:
        list: A list of job links.
    """
    contents = await file.read()
    job_links = contents.decode("utf-8").splitlines()
    return [link.strip() for link in job_links if link.strip()]
