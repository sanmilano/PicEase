import gradio as gr
from PIL import Image
import os

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    new_width, new_height = map(int, size.split(' x '))

    # Calculate the aspect ratio of the image and the target size
    image_aspect_ratio = original_image.width / original_image.height
    target_aspect_ratio = new_width / new_height

    # Resize the image to fit within the target size, maintaining aspect ratio
    if image_aspect_ratio > target_aspect_ratio:
        # If image is wider than the target size, constrain by height
        resized_image = original_image.resize((int(new_height * image_aspect_ratio), new_height))
    else:
        # If image is taller than the target size, constrain by width
        resized_image = original_image.resize((new_width, int(new_width / image_aspect_ratio)))

    # Calculate the area to be cropped
    left = (resized_image.width - new_width) / 2
    top = (resized_image.height - new_height) / 2
    right = (resized_image.width + new_width) / 2
    bottom = (resized_image.height + new_height) / 2

    # Crop the image to the target size
    cropped_image = resized_image.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_image.save(output_image_path, "PNG")

def resize_images_in_folder(input_folder, output_folder, size, progress=gr.Progress()):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    total_images = len([name for name in os.listdir(input_folder) if name.endswith(".jpg") or name.endswith(".png")])
    processed_images = 0

    for filename in progress.tqdm(os.listdir(input_folder), desc="Processing images"):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            resize_image(input_image_path, output_image_path, size)
            processed_images += 1

    return f"Processed {processed_images} of {total_images}. Images resized and saved in {output_folder}"

def gradio_interface(input_folder, output_folder, size, custom_width, custom_height, progress=gr.Progress()):
    if not input_folder:
        return "Error: Please provide an input folder."
    if not output_folder:
        return "Error: Please provide an output folder."
    if not size and (not custom_width or not custom_height):
        return "Error: Please select a resolution or enter a custom width and height."

    if custom_width and custom_height:
        size = f"{custom_width} x {custom_height}"

    return resize_images_in_folder(input_folder, output_folder, size, progress)


resolutions = ["1344 x 768", "768 x 1344", "1024 x 1024", "896 x 1088", "1088 x 896", "1152 x 896", "896 x 1152", "1216 x 832", "832 x 1216", "Custom"]

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(label="Input folder"),
        gr.Textbox(label="Output folder"),
        gr.Dropdown(resolutions, label="Resolution", type="value"),
        gr.Textbox(label="Custom Width"),
        gr.Textbox(label="Custom Height")
    ],
    outputs="text",
    title="RatioScope",
    description="## Organize images")

iface.queue().launch()