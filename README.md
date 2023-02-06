# delete_qq_pics

根据文件创建时间删除Windows端QQ群聊缓存图片

删除路径"C:\Users\{}\Documents\Tencent Files\{}\Image\Group2"下的缓存图片（qq的图片缓存机制真的逆天，这里堆了几十G的图片缓存）

## 使用方式

下载.py文件后放在电脑任意位置，修改文件中settings部分后使用python运行该文件

 - pc_name: 电脑用户名，用于定位图片缓存路径

 - qq: QQ号，用于定位图片缓存路径

 - remove_time: 删除缓存时间大于此项天数的图片，如设置为30则删除30天前的图片
