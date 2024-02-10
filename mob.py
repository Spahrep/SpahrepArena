import random

class Mob :
    def __init__(self,mID,mName,mLevel,mMaxHP,mMinHP,mMaxAtt,mMinAtt,mMaxDef,mMinDef,mMaxSp,mMinSp,mCritRate):
        self.mID = mID
        self.mName = mName
        self.mMaxHP = round(mMinHP +(random.uniform(0,1)*(mMaxHP-mMinHP)),0)
        self.mMinAtt = mMinAtt
        self.mMaxAtt = mMaxAtt
        self.mMinDef = mMinDef
        self.mMaxDef = mMaxDef
        self.mMinSp = mMinSp
        self.mMaxSp = mMaxSp
        self.mCritRate = mCritRate
       # self.mAtt = mMinAtt + (random.uniform(0,1)*(mMaxAtt-mMinAtt))
       # self.mDef = mMinDef + (random.uniform(0,1)*(mMaxDef-mMinDef))
       # self.mSp = mMinSp + (random.uniform(0,1)*(mMaxSp-mMinSp))
       

        
    def __str__(self):
        
        return f"Mob: HP={self.mMaxHP}, Att={self.mMaxAtt}, Def={self.mMaxDef}"

    def getAttack(self):
        return round(self.mMinAtt + (random.uniform(0,1)*(self.mMaxAtt-self.mMinAtt)),0)

    def getDef(self):
        return round(self.mMinDef + (random.uniform(0,1)*(self.mMaxDef-self.mMinDef)))

    def getSp(self):
        return round(self.mMinSp + (random.uniform(0,1)*(self.mMaxSp-self.mMinSp)))

myMob = Mob(1,"Blue Slime",1,10,8,5,2,4,2,10,10)


print(myMob)
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
print("Mob Attack: " + str(myMob.getAttack()))
