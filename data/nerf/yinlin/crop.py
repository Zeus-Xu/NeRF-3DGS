from PIL import Image
import os

def crop_images_in_directory(input_dir, output_dir, crop_box):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            img_path = os.path.join(input_dir, filename)
            with Image.open(img_path) as img:
                # 裁剪图片
                cropped_img = img.crop(crop_box)
                # 保存裁剪后的图片
                cropped_img.save(os.path.join(output_dir, filename))
            print(f"Cropped and saved {filename}")

if __name__ == "__main__":
    input_directory = "images_raw"
    output_directory = "images"
    crop_box = (650, 100, 1300, 950)  # 例如: (100, 100, 400, 400)

    crop_images_in_directory(input_directory, output_directory, crop_box)
