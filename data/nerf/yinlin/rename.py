import os

def rename_files_in_directory(directory, prefix=""):
    # 获取目录中的所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # 过滤出图片文件
    image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff"))]
    
    # 排序文件列表，确保按顺序重命名
    image_files.sort()

    # 遍历图片文件并重命名
    for idx, filename in enumerate(image_files):
        new_name = f"{prefix}{idx + 1:04d}{os.path.splitext(filename)[1]}"  # 生成新文件名
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)
        print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    directory = "images"  # 设置要重命名文件的目录
    prefix = ""  # 可选：文件名前缀，例如 "img_"
    rename_files_in_directory(directory, prefix)
