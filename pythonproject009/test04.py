# OOP : interitance สือทอด
# คือ คลาสหนึ่งสือทอดอีกคลาสหนึ่ง (มีแม่ super / มีลูก Sub)
# พอเป็นแม่ลูก แม่มีอะไรลูกมีด้วย

class TestA :
    data1 = 10
    data2 = 20

    def showSAU() :
        print ("Hi......SAU")

class TestB(TestA) :
    data3 = 30
    
    def showWow() :
        print ("Wow Woo Wea")

class TestC(TestA) :
    data4 = 40

class TestD(TestB) :
    data5 = 50

ob1 = TestA()
ob2 = TestB()
ob3 = TestD()


# OOP : Polymorphism ห้องรูป
# คือ การกระทำเดี่ยวกัน แต้วิธีต่างกัน (ต้องเป็นแม่(super) , ลูก(Sub))
# คือ การที่ลูกเอา Method ของแม่มาเขียนใหม่

class TestZ (TestA) :
    data6 = 60

    # Polymorphism : Overiding Method
    def showSAU():
        print ("Hello....SAU")

ob4 = TestZ()