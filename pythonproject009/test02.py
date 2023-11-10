# Object 
class IoTThailand :
    #data
    wow = 100

    #contruter ไม่ใช่ member แต่จะทำงานทุกครั้งที่สร้าง object
    def __init__( self , woo , wee , wea) :#paramiter 3 = woo wee wea
        self.woo = woo
        self.wee = wee
        self.wea = wea

    #Method
    def showdata(self) :
        print ( self.wow * 20) 
    
    #destsuctor
    def __del___ (self):
        print ("Good morning Teacher....")
    
ob1 = IoTThailand( 10 , 20 , 10 )
ob2 = IoTThailand( 10 , 20 , 30 )
ob3 = IoTThailand( 5 , 20 , 10 )
ob4 = IoTThailand( 10 , 20 , 10 )

print (ob1.wea + ob2.wea)
ob3.showdata()