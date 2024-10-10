import psutil
import ctypes
# thư viện vẫn là học từ chatgpt ạ..
import sys

# Dừng tiến trình bằng PID
# command : python taskkill_psutil.py name <tên-tiến-trình>
def terminate_process(pid):
    handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
    if handle:
        ctypes.windll.kernel32.TerminateProcess(handle, 0)
        ctypes.windll.kernel32.CloseHandle(handle)

# Dừng tiến trình theo tên
# command : python taskkill_psutil.py PID <PID>
def kill_by_name(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == name.lower():
            terminate_process(proc.info['pid'])

# argv : số lượng tham số truyền vào ( phải đủ 3 )
if len(sys.argv) == 3:
    if sys.argv[1] == 'name':
        # name thì call đấm kiểu nêm và truyền vào tham số là tên chương trình 
        # nói thế cho oai chứ vẫn là tìm PID ứng với tên chương trình rồi ném PID vào hàm kia=)))

        kill_by_name(sys.argv[2])
    elif sys.argv[1] == 'pid':
        # PID thì call xiên kiểu pi ai đi và truyền vào PID
        terminate_process(int(sys.argv[2]))
