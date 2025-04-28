from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import instaloader
import os
import shutil
import uuid

app = FastAPI(
    title="Instagram Post Downloader API",
    description="API para baixar posts do Instagram a partir de uma URL ou Shortcode e gerar um arquivo zipado.",
    version="1.0.0"
)

# Modelo de requisição
class DownloadRequest(BaseModel):
    url: str = None
    shortcode: str = None

# Funções auxiliares
def download_post_from_code(shortcode, folder_name):
    if shortcode:
        L = instaloader.Instaloader(dirname_pattern=folder_name, download_video_thumbnails=False, save_metadata=False)
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target="post")

def extract_shortcode(url):
    if url:
        if url[-1] != "/":
            url += "/"
        return url.split("/")[-2]
    return None

# Rota principal
@app.post("/download-instagram-post", summary="Baixar post do Instagram", response_description="Arquivo ZIP do post")
async def download_instagram_post(request: DownloadRequest):
    url = request.url
    shortcode = request.shortcode

    if not url and not shortcode:
        raise HTTPException(status_code=400, detail="You must provide a 'url' or a 'shortcode'.")

    if url:
        shortcode = extract_shortcode(url)

    if not shortcode:
        raise HTTPException(status_code=400, detail="Invalid URL or shortcode.")

    unique_folder = f"downloads_{uuid.uuid4()}"
    os.makedirs(unique_folder, exist_ok=True)

    try:
        download_post_from_code(shortcode, unique_folder)

        # Compactar
        zip_path = f"{unique_folder}.zip"
        shutil.make_archive(unique_folder, 'zip', unique_folder)

        return FileResponse(zip_path, filename="instagram_post.zip", media_type="application/zip")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(unique_folder):
            shutil.rmtree(unique_folder)

