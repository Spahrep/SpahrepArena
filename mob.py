import random

class Mob :
    def __init__(self,mID,mHp,mAtt,mDef,mAttRng):
        self.mID = mID
        self.mHP = mHp
        self.mAtt = mAtt
        self.mDef = mDef
        self.mAttRng = mAttRng

        
    def __str__(self):
        
        return f"Mob: HP={self.mHP}, Att={self.mAtt}, Def={self.mDef}"

    def getAttack(self):
        return max(0,round(self.mAtt * (1+random.uniform(0,self.mAttRng))))

myMob = Mob(111111,100,10,13,0.25)


print(myMob)
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
