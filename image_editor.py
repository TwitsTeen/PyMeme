from PIL import Image, ImageDraw, ImageFont

font_path = "./ArialNarrow7-9YJ9n.ttf"


def write_text_on_image(image_name, text, font_size, text_position, text_color, save_name):
    try:
        # Open an image file
        image = Image.open(image_name)

        # Initialize ImageDraw
        draw = ImageDraw.Draw(image)

        # Define the font
        font = ImageFont.truetype(font_path, font_size)

        # Add text to image
        draw.text(text_position, text, font=font, fill=text_color)

        # Save the edited image
        image.save("./static/images/"+save_name)
    except Exception as e:
        raise e
    return save_name

