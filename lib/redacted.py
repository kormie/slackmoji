from PIL import Image, ImageDraw, ImageFont
import os
import sys

string = sys.argv[1].upper()
output_dir = sys.argv[2]

frames = []

# Create the base image with transparent background
base = Image.new('RGBA', (128, 64), (0, 0, 0, 0))

# Create the font
# Increase the font size until the text width is just smaller than the image width
font_size = 1
padding = 10  # padding on each side of the image
fnt = None
text_width = 0
while text_width < base.width - 2*padding:
    font_size += 1
    fnt = ImageFont.truetype('../fonts/Courier New Bold Italic.ttf', font_size)
    text_width, text_height = ImageDraw.Draw(base).textsize(string, font=fnt)
font_size -= 1  # decrease font size by 1 to ensure text fits within image width
fnt = ImageFont.truetype('../fonts/Courier New Bold Italic.ttf', font_size)
text_width, text_height = ImageDraw.Draw(base).textsize(string, font=fnt)

# Draw the text in the middle of the base image
draw = ImageDraw.Draw(base)
text_x = (base.width - text_width) // 2
text_y = (base.height - text_height) // 2
draw.text((text_x, text_y), string, font=fnt, fill=(0, 0, 0))

# Calculate the height of the black bar to be slightly larger than the text
bar_height = text_height + 2  # adjust this value as necessary

num_frames = 48

for i in range(num_frames):
    # Copy the base image
    frame = base.copy()
    d = ImageDraw.Draw(frame)
    
    # Calculate the position of the black bar using a linear curve
    pos = i / num_frames
    
    # Calculate the left and right x-coordinates of the black bar
    left = 0
    right = pos * (frame.width + padding)
    
    top = (frame.height - (text_height+4)) / 2
    # Draw the black bar
    d.rectangle([left, top, right, bar_height+top+6], fill=(0, 0, 0))
    
    # Save the frame as a PNG image
    frame.save(f'{output_dir}/frame_{i:03d}.png')
