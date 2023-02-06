import os
import datetime

# Settings
pc_name = "uname"    # 电脑用户名
qq = "1234567890"   # 要删除文件的QQ号
remove_time = 30    # 删除距今remove_time天前的文件


def remove_qq_pics(filepath, ctime):
    if not os.path.exists(filepath):
        print("Wrong path, check your settings.")
        return
    cur_point = ''
    total_size = 0
    total_num = 0
    for root, dirs, files in os.walk(filepath):
        # $%()0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_`{}~
        for file in files:
            if cur_point != file[0]:
                cur_point = file[0]
                print("▋", end='')
            timestamp = os.path.getctime(os.path.join(root, file))
            file_create_time = datetime.datetime.fromtimestamp(timestamp)
            delta = ctime - file_create_time
            # print(delta.days, os.path.join(root, file))
            if delta.days > remove_time:
                # print(delta.days, os.path.join(root, file))
                file_size = os.path.getsize(os.path.join(root, file))
                total_size += file_size/1024.0
                total_num += 1
                # print("Removing:", os.path.join(root, file))
                os.remove(os.path.join(root, file))
    print("\nAll done. {} pictures deleted, freeing {:.2f}M of storage.".format(
        total_num, total_size/1024.0))


path = f"C:\\Users\\{pc_name}\\Documents\\Tencent Files\\{qq}\\Image\\Group2"
current_time = datetime.datetime.now()

remove_qq_pics(path, current_time)
