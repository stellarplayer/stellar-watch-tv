# 从A.M3U读取文本,导出A1,A2...An.M3U.
import io
import os
class m3uParse:
    m3uList = []

    def __init__(self):
        print("----")
    # 生成文件
    def make_m3u_file(self, name, link):
        obj = open(name, mode="w+", encoding="utf8")
        obj.write("#EXTM3U\n#EXTINF:-1,")
        obj.write(name + "\n")
        obj.write(link)
        obj.close


    # 获取文件名,并去除非法字符
    def get_item_name(self, extinf):
        name = extinf.split(",", 1)[1]
        name = name.replace(" ", "")
        name = name.replace(":", ".")
        name = name.replace("/", ".")
        name = name.replace("\\", ".")
        name = name.replace("|", ".")
        name = name.replace("?", ".")
        name = name.replace("*", ".")
        name = name.replace("<", ".")
        name = name.replace(">", ".")
        return name


    # 处理输入的文本文件
    def m3u_dump(self, m3u_file):
        item_name = ""
        item_link = ""
        lines = m3u_file.readlines()
        for line in lines:
            line = line.rstrip("\r\n")
            if line.startswith("#EXTINF"):
                item_name = self.get_item_name(line)
            if line.startswith("http"):
                item_link = line
                ##print(item_name, item_link);
                self.m3uList.append({"weishi": item_name, "link": item_link})



    def openFile(self, m3u_file_name):
        m3u_file_obj = open(m3u_file_name, "r", encoding="utf8")
        self.m3u_dump(m3u_file_obj)
        m3u_file_obj.close()

        ##for key in self.m3uList:
        ##    print (key)
        return self.m3uList

    def getListName(self):
        tkeys = [i['weishi'] for i in self.m3uList]
        tmp2 = [{'weishi': tkeys[i], 'weishi1': tkeys[i + 1]} for i in range(0, len(tkeys), 2)]
        return tmp2


if __name__ == "__main__":
    test = m3uParse()
    tmp = test.openFile("weishi.m3u")
    ##for key in tmp:
     ##   print(key)
    print("------------------------------------")
    tkeys = [i['weishi'] for i in tmp]
    tmp2 = [{'weishi':tkeys[i], 'weishi1':tkeys[i + 1]} for i in range(0, len(tkeys), 2)]
    print(tmp2)