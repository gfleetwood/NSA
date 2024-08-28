import modal

app = modal.App("nostr-flask-api")

image = (
    modal.Image.debian_slim()
    .copy_local_dir("./app/", remote_path = "/home/app/")
    .workdir("/home/app/")
    .run_commands(["apt-get update", "pip install --upgrade pip", "pip install wheel","apt-get install libglib2.0-0 -y", "apt-get install -y pkg-config"])
    .run_commands(["pip install --no-cache-dir -r requirements.txt", "pip install gunicorn"])
)

@app.function(image = image)
@modal.wsgi_app()
def api():
    
    from app import app as web_app

    return web_app

@app.local_entrypoint()
def main():
    api.remote()