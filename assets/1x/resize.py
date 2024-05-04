from PIL import Image

def upscale_pixel_art(input_image_path, output_image_path):
    # Open the image
    image = Image.open(input_image_path)

    # Double the size
    new_size = (image.width * 2, image.height * 2)
    resized_image = image.resize(new_size, Image.NEAREST)  # NEAREST resampling preserves pixelation

    # Save the resized image
    resized_image.save(output_image_path)

# Example usage
_id = "gateway"
input_image_path = "c_cry_"+_id+".png"
output_image_path = "../2x/c_cry_"+_id+".png"
upscale_pixel_art(input_image_path, output_image_path)
