#encoding:utf-8
class usp():
    def usp_1(self):
        leave=[]
        leave_data=[]
        arrive=[]
        arrive_data=[]
        with open(R"C:\Users\Administrator\Desktop\12.txt", "r") as file:
    # 读取文件内容
            lines = file.readlines()
            for line in lines:
        # # 分割字符串
                leave.append(line.split(',')[0])
                leave_data.append(line.split(',')[1])
                arrive.append(line.split(',')[2])
                arrive_data.append(line.split(',')[3])
        return leave,leave_data,arrive,arrive_data
lg=usp()
