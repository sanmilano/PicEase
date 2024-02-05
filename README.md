# **PicEase**
Introducing a user-friendly image optimization app that effortlessly manages your image collection. Navigate through images, resize and crop them to your preferred resolution with ease. The application offers pre-configured SDXL common resolutions for quick adjustments, along with the flexibility to set up custom resolutions. It preserves original images in their pristine form, transforming them into .png format without altering the aspect ratio. Forget the hassle of dealing with large datasets using demanding software – this app simplifies batch resizing, ensuring images are enhanced effortlessly.

## **Automatic Installation for Windows:**

**Step 1:** Clone this repository or download all the files into a folder.

**Step 2:** Run `install.bat` - This will create a virtual environment and download all necessary files without affecting other Python installations on your system.

**Step 3:** Use `run.bat` to start the application.

## **Manual Installation:**

**Step 1:** Clone this repository or download all the files into a folder.

**Step 2:** Open cmd and type:
```bash
python -m venv venv
call venv\Scripts\activate
pip install pillow gradio
```

**Step 3:** Once everything is downloaded and installed, open cmd again and type:
```bash
call venv\Scripts\activate
python app.py
```
