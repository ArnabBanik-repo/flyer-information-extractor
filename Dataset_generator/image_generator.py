from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageFilter
import random

# Open the original image
original_image = Image.open('speaker.jpg')

# Example: Apply a random filter to the image
def apply_filter(image):
    filters = [ImageFilter.BLUR, ImageFilter.EDGE_ENHANCE, ImageFilter.FIND_EDGES, ImageFilter.CONTOUR, ImageFilter.SHARPEN]
    return image.filter(random.choice(filters))

# Example: Adjust contrast of the image
def adjust_contrast(image, contrast_factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast_factor)

# Example: Add random noise to the image
def add_noise(image, noise_factor):
    import numpy as np

    image_array = np.array(image)
    noise = np.random.normal(0, noise_factor, image_array.shape)
    noisy_image_array = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    noisy_image = Image.fromarray(noisy_image_array)

    return noisy_image

# Example: Convert the image to grayscale
def convert_to_grayscale(image):
    return ImageOps.grayscale(image)

# Example: Invert colors of the image
def invert_colors(image):
    return ImageOps.invert(image)

# Example: Apply a posterize effect to the image
def posterize_image(image, bits):
    return ImageOps.posterize(image, bits)

# Generate n variations of the original image
n = int(input("Enter the number of speakers: ")) # Replace with the desired number of images
for i in range(n):
    transformed_image = original_image.copy()

    # Perform various transformations
    transformed_image = apply_filter(transformed_image)
    transformed_image = adjust_contrast(transformed_image, random.uniform(0.5, 1.5))
    transformed_image = add_noise(transformed_image, random.uniform(0, 10))
    transformed_image = convert_to_grayscale(transformed_image)
    transformed_image = invert_colors(transformed_image)
    transformed_image = posterize_image(transformed_image, random.randint(2, 8))

    # Save the transformed image
    transformed_image.save(f'dataset/speakers/speaker_{i}.jpg')
