# ZeroShotCTW
A backend for processing images for Capture the world (CTW).

## Local Development 
For local development create the python venv with the following code

Creating the venv 
```bash
python -m venv venv
```
Activating the venv
```bash
./venv/Scripts/activate # type "deactivate" to deactivate
```

Installing the requirements, note pytorch must be manually installed, order matters.
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 
pip install -r requiremnts.txt
```

## Deployment
The project is ment to be deployed with docker.