import os
import subprocess
from utils.UtilsTools import print_log

IS_MAC = os.uname().sysname == "Darwin"

def __get_pngquant_path__():
    """
    获取pngquant路径
    """
    pngquant_path = os.getcwd() + "/tools/pngquant/pngquant.exe"
    if IS_MAC:
        pngquant_path = os.getcwd() + "/tools/pngquant/pngquant"

        cmd = "chmod +x %s" % (pngquant_path)
        os.system(cmd)
    
    return pngquant_path


def __compress_file__(path) -> tuple[int, str]:
    """
    压缩单个文件
    @param path: 文件路径
    """
    if not os.path.exists(path):
        # 文件不存在，返回
        print_log(f"file not exist: {path}")
        return 0, "文件不存在"
    
    stat = os.stat(path)
    org_size = stat.st_size

    min, max = 45, 85
    if org_size > 1 * 1024 * 1024:
        # 大于1M，修改压缩参数
        min, max = 20, 80

    cmd = '"{0}" --force --skip-if-larger --strip --quality={2}-{3} {1} --output {1}'.format(__get_pngquant_path__(), path, min, max)
    result = subprocess.run(cmd, shell=True)
    if result.returncode == 0:
        return 0, "压缩成功"
    else:
        print_log(f"命令执行失败，返回码: {result.returncode}")
        return 0, '压缩失败' 