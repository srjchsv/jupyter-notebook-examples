import bz2
import os 
from PIL import Image
import tarfile


def compress_images(source_dir, target_dir):
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for filename in os.listdir(source_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename + '.bz2')

                with open(source_file, 'rb') as file:
                    data = file.read()
                    compressed_data = bz2.compress(data)

                with open(target_file, 'wb') as file:
                    file.write(compressed_data)


def get_total_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if not os.path.islink(filepath):  # Skip symbolic links
                total_size += os.path.getsize(filepath)
    return total_size


def calc_compression_difference(source, **compressed):
    for kind, compressed_size in compressed.items():
        print(f"{kind} size: {compressed_size}")
        compression_difference = source - compressed_size
        print(f"compression difference: {round(compression_difference / source * 100,2)}%")
        print()

def compress_directory(source_dir, output_file):
    with tarfile.open(output_file, 'w:bz2') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def convert_png_to_jpeg(source_dir):
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        with Image.open(source_file) as img:
            rgb_im = img.convert("RGB")
            os.remove(source_file)
            rgb_im.save(source_file.replace(".png", ".jpeg"), "JPEG")