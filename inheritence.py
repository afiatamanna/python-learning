class Person:
    def __init__(self,firstname,lastname,emotion,health,status):
        self.firstname = firstname
        self.lastname = lastname
        self.emotion = emotion
        self.health = health
        self.status= status
    def introduce(self):
        print("Hi!! {} {}".format(self.firstname, self.lastname))
    def emot(self):
        #emotion= random.randomrange(1,3)
        if self.emotion==1:
            print("happy {}".format(self.firstname))
        elif self.emotion== 2:
            print("nutral {}".format(self.firstname))
        elif self.emotion==3:
            print("sad {}".format(self.firstname))
        else:
            print("null")
    def health_status(self):
        #self.health = (self.health - 20)
        if self.health==100:
            print("{} is well".format(self.firstname) )
        elif self.health>= 80:
            print("{} is not enough well".format(self.firstname))
        elif self.health>= 60:
            print("{} is not  well".format(self.firstname))
        elif self.health >= 40:
            print("{} is sick".format(self.firstname))
        else:
            print("{} needs to go hospital".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 1,95, status=True)
Rey = Person("Rey", "Jones", 2,88, status=False)
Lee = Person("Lee", "Williams",3, 72, status=True)

Lee.introduce()
Maria.introduce()
Rey.introduce()


Maria.emot()
Lee.emot()
Rey.emot()

Maria.health_status()
Lee.health_status()
Rey.health_status()


class Enemy(Person):
    def __init__(self,weapon,firstname,lastname,health,status):
        super().__init__(self,firstname,lastname,health,status)
        self.weapon = weapon

    def hurt(self,other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stcik':
            other.health -=5
        print(other.health)

    def insult(self,other):
        if other.health >= 70:
            print("{} is weak and tired".format(other.firstname))
        else:
            print("Strong")


    def steal(self,other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))

        if  other.status== True:
            other.status== False



Alex= Enemy('rock', 'Alex', 'Wayne', 75, status = False)

Alex.hurt(Maria)
Alex.steal(Rey)
Alex.insult(Lee)

