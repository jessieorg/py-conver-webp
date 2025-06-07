import time
import datetime
from typing import Callable



def encode_str(message: str):
    """
    编码字符串
    @param message: 待编码字符串
    """
    # if IS_WIN:
        # str_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # message = message.decode("utf-8").encode("gb2312")
        # message = str_time + " " + message.decode("utf-8")
        # message = str_time + " " + message
    return message

def print_log(message: str):
    """
    打印日志
    @param message: 日志信息
    """
    try:
        str_log = encode_str(message)
        print("[%s][python] %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%m"), str_log))
    except BaseException as e:
        raise Exception(e)

def run_task(task_name: str, fun: Callable[..., tuple[int, str | int | float]], *args: object, **kwargs: object) -> tuple[int, str | int | float]:
    """
    执行任务
    @param task_name: 任务名称
    @param fun: 任务函数
    @param args: 任务函数参数
    @param kwargs: 任务函数参数
    @return: 任务执行状态
    """
    print_log("--- " + task_name)
    start_time = time.time()
    status = 1
    msg = ""
    
    try:
        status, msg = fun(*args, **kwargs)
    except BaseException as e:
        print(e)
        raise Exception(e)
    
    end_time = time.time()
    if isinstance(msg, str) or isinstance(msg, int) or isinstance(msg, float):
        print_log("###耗时:%s %s status:%s msg:%s" % (end_time - start_time, task_name, status, msg))
    else:
        print_log("###耗时:%s %s status:%s msg:%s" % (end_time - start_time, task_name, status, ""))
    
    if status != 0:
        if isinstance(msg, str) or isinstance(msg, int) or isinstance(msg, float):
            message = encode_str("task[%s]执行异常, status:%s, msg:%s" % (task_name, status, msg))
        else:
            message = encode_str("task[%s]执行异常, status:%s, msg:%s" % (task_name, status, ""))
        
        raise Exception(message)
    
    return status, msg
