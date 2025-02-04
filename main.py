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
        print(img)

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
    use_default = input("Do you want to use default input/output? (Y/n): ").strip().lower()
    
    if use_default == "n":
        input_folder = input("Enter the input folder path: ").strip()
        output_file = input("Enter the output file path: ").strip()
    else:
        input_folder = "images"
        output_file = "output.png"

    sprite_size = int(input("Enter the output sprite size (1:1, in pixels): "))
    sprites_per_row = int(input("Enter the number of sprites per row in the output sprite sheet: "))

    create_sprite_sheet(input_folder, output_file, sprite_size, sprites_per_row)
