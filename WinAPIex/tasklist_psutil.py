import psutil

def list_processes():
    print(f"{'Image Name':30} {'PID':10}")
    print("="*40) # làm màu để trông cái bảng đẹp hơn tí ạ
    # theo em research + học hỏi từ chatgpt, em biết được trong thư viện psutil của python có thể trả về các đối tượng mà mình đang đi tìm
    # cụ thể là PID và name nên em dùng nó 
    # https://psutil.readthedocs.io/en/latest/
    for x in psutil.process_iter(['pid', 'name']):
        try:
            process_name = x.info['name']
            process_pid = x.info['pid']
            print(f"{process_name:<30} {process_pid:<10}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

list_processes()
