from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_handler import process_file

router = APIRouter()

@router.post("/upload-job-links/")
async def upload_job_links(file: UploadFile = File(...)):
    """
    Endpoint to upload a file containing job links.

    Args:
        file (UploadFile): The uploaded text file with job links.

    Returns:
        dict: Response with the number of job links processed.
    """
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Only text files are allowed.")
    
    job_links = await process_file(file)
    return {"message": "Job links processed successfully", "total_links": len(job_links)}
