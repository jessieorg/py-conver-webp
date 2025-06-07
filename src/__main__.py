from utils.UtilsTools import run_task
import os
from .tinypng import __compress_file__
from PIL import Image
import sys


def __canver_webp__(path: str, quality: int = 100) -> tuple[int, str]:
    if not os.path.exists(path):
        msg = f"文件不存在: {path}"
        return 1, msg
    try:
        img = Image.open(path)
        webp_path = os.path.splitext(path)[0] + ".webp"
        img.save(webp_path, "WEBP", quality=quality)
        msg = f"转换成功: {webp_path}"
        return 0, msg
    except Exception as e:
        msg = f"转换失败: {e}"
        return 2, msg


def main():
    # 从命令行参数获取文件路径
    if len(sys.argv) < 2:
        print("请在命令行中指定要处理的文件路径，例如：python -m src /path/to/file.png")
        return
    file_path = sys.argv[1]
    quality = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    _=run_task("压缩png ", __compress_file__, file_path)
    _=run_task("转换webp ", __canver_webp__, file_path, quality)


if __name__ == "__main__":
    main();
