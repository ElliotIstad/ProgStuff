from PIL import Image

# Create a new image (20x20 pixels) with a white background
img = Image.new('RGB', (20, 20), color='white')

# Save the image to a file
img.save('plain_white_image.png')

# Optionally, show the image
img.show()
