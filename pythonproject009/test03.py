#คุณสมบัติเด้นของ OOP : Encapsulation (ห่อหุ้ม/ซ่อนไว้)
class MyTestA :
    __data1 = 10 # การซ่อนทำการ __ ไว้วข้างหน้าตัวแปร
    data2 = 20

    # เมื่อ data โดน Encap การกำหนดหรือเอาคำมาใช้
    # ให้ผ่าน Method get เอามาใช้ set 

    def getdata1(self):
        return self.__data1
    
    def setdata1(self , data1):
        self.__data1 = data1
    
    def getdata3(self):
        return self.__data3
    
    def setdata3(self , data3):
        self.__data3 = data3
    
    def __init__( self , data3 ) :
        self.__data3 = data3
    
    def showdata(self) :
        print (f"__data1 = {self.__data1}")
        print (f"__data2 = {self.data2}")
        print (f"__data3 = {self.__data3}")
        print ("-------------------------------")

ob1 = MyTestA(30)
ob1.data2 = 200
# ob1.__data1 = 100
ob1.setdata1(100)
#ob1.__data3 = 999
ob1.setdata3(999)
ob1.showdata()
print (ob1.getdata3())