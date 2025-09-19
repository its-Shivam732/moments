# Moments

# Demo https://uic.zoom.us/rec/share/5WfgNjCoWNX-rj8I6qE_CtEGfDA79dTA6SwaX11OhoaJ3djwwyW1HWZynGDZnf0v.ZGSwQFL_b56kO2pD

A photo app built with Python and Flask, extended with **machine learning features**.  
In addition to the core functionality (accounts, uploads, comments, tags, collections), this version adds:

- **Automatic alternative text generation** for uploaded photos (improves accessibility).  
- **ML-powered image search** using detected objects/tags.


![Screenshot](dog.png)

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```

Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate    # On macOS/Linux
# .venv\Scripts\activate     # On Windows PowerShell![Uploading image.png…]()

```

Install dependencies:

```
pip install -r requirements.txt
```

Configuration

Set up environment variables for Azure Vision API (needed for ML-powered captions & tags). Put the keys in .flaskenv

```
export AZURE_VISION_ENDPOINT="https://<your-endpoint>.cognitiveservices.azure.com/"
export AZURE_VISION_KEY="<your-key>"
```
To initialize the app, run the `flask init-app` command:

```
$ flask init-app
```


Now you can run the app:

```
$flask run
* Running on http://127.0.0.1:5000/
```
1. Now you can try creat new account with emailid and password. After you create the account you would be able to  upload the photos.
2. Click the upload button(+ symbol) in top right to add photo.
3. After successfully uploading the photo, click the addded photo, you would see description/tag on right side.
