def sumNumber ():
    pass #ตัวคั่นไม่ให้ Error 

#OOP = Object Oriented Programming
#สร้าง class ใน python
class IotSAU : #ตัวใหญ่หมด เป็น ค่าคงที่ class คือ แม่พิมพ์/ต้นแบบ
    #data/attribute/filed/property member เหมือนตัวแปร
    info1 = 20
    info2 = ""

    #Method member เหมือนฟังก์ชั่น
    def showHi(self):
        print ("Hi....")

    def showInfo(self):
        print (self.info1 , self.info1)
        self.showHi()
# สร้าง odject 
obA = IotSAU()
obB = IotSAU()
obC = IotSAU()

obA.info1 = 100
print ( obA.info1 + obB.info1 ) #120
obB.showInfo()
obA.showInfo()