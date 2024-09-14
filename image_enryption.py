from PIL import Image

def encrypt_image(image_path, operation, value):
    # Open the image using Pillow
    with Image.open(image_path) as img:
        width, height = img.size
        pixels = list(img.getdata())

    # Apply the chosen operation to each pixel
    if operation == 'swap':
        pixels = swap_pixels(pixels, value)
    elif operation == 'add':
        pixels = add_to_pixels(pixels, value)
    elif operation == 'sub':
        pixels = sub_from_pixels(pixels, value)
    elif operation == 'mul':
        pixels = mul_pixels(pixels, value)
    elif operation == 'div':
        pixels = div_pixels(pixels, value)
    else:
        raise ValueError("Invalid operation")

    return width, height, pixels
def swap_pixels(pixels, value):
    return [tuple(min(255, component + value) for component in pixel) for pixel in pixels]

def add_to_pixels(pixels, value):
    return [tuple(min(255, component + value) for component in pixel) for pixel in pixels]

def sub_from_pixels(pixels, value):
    return [tuple(max(0, component - value) for component in pixel) for pixel in pixels]

def mul_pixels(pixels, value):
    return [tuple(min(255, component * value) for component in pixel) for pixel in pixels]

def div_pixels(pixels, value):
    return [tuple(max(0, component // value) for component in pixel) for pixel in pixels]

# Get user input
image_path = input("Enter the input image path (e.g., input_image.ppm): ")
operation = input("Enter the operation (e.g., swap, add, sub, mul, div): ")
value = int(input("Enter the value for the operation: "))

# Encrypt the image
width, height, encrypted_pixels = encrypt_image(image_path, operation, value)

# Save the encrypted image
with Image.new('RGB', (width, height)) as img:
    img.putdata(encrypted_pixels)
    img.save('encrypted_image.ppm')

print("Encrypted image saved as encrypted_image.ppm")
