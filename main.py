from PIL import Image
import os
import math

def create_sprite_sheet(input_folder: str, output_file: str, sprite_size: int, sprites_per_row: int):
    images = [os.path.join(input_folder, f) for f in sorted(os.listdir(input_folder)) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    
    if not images:
        print("No images found in the folder.")
        return
    
    print("Sorted images by name:")
    for img in images:
        print(img)  # Print each image path to verify the order

    num_images = len(images)
    rows = math.ceil(num_images / sprites_per_row)

    sheet_width = sprites_per_row * sprite_size
    sheet_height = rows * sprite_size

    sprite_sheet = Image.new("RGBA", (sheet_width, sheet_height))

    for index, image_path in enumerate(images):
        with Image.open(image_path) as img:
            img = img.resize((sprite_size, sprite_size), Image.Resampling.LANCZOS)
            x_offset = (index % sprites_per_row) * sprite_size
            y_offset = (index // sprites_per_row) * sprite_size
            sprite_sheet.paste(img, (x_offset, y_offset))

    sprite_sheet.save(output_file)
    print(f"Sprite sheet created and saved as {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a sprite sheet from images in a folder.")
    parser.add_argument("input_folder", help="Path to the folder containing images.")
    parser.add_argument("output_file", help="Path to save the sprite sheet image.")
    parser.add_argument("sprite_size", type=int, help="Width and height of each sprite in pixels.")
    parser.add_argument("sprites_per_row", type=int, help="Number of sprites per row in the sprite sheet.")

    args = parser.parse_args()
    create_sprite_sheet(args.input_folder, args.output_file, args.sprite_size, args.sprites_per_row)
