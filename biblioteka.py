


class Gramata:
        def __init__(self,nosaukums,autors,pieejams=True):
            self.nosaukums=nosaukums
            self.autors=autors
            self.pieejams=pieejams
        def pieejamiba(self):
              print(f"Gramatas statuss ir: {self.pieejams} ")
        def mainit(self):
            while True:
                a=int(input("Vēlaties saņemt grāmatu (1) vai nodot atpakaļ (2) ? "))
                print("dasdsada")
                if a ==1 :
                    self.pieejams= not self.pieejams
                    print("Statuss tika pamainits uz nav pieejams")
                    break
                elif a == 2 :
                    self.pieejams = True
                    print("Statuss tika pamainits uz pieejams")
                    break

                else:
                    print("Nepareizi ievadits skaitlis!!!")
                    

#Labi organizets ievads ,bet bija diezgan gruti izprast dažus uzdevumus ,jo pietrūkst zināšanu.
        
''''
def pievienot():
     
    
def dzest():
     


class Parbauda(Gramata):
    def __init__(self,pieejamiba):
        super().__init__(pieejamiba)
'''


        

a=Gramata("Putekli","Laize","Pieejams")

a.pieejamiba()
a.mainit()






















