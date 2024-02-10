import random

class Mob_Attack :
    def __init__(self,aID,aName,aType,aSubType,aBaseDmgMod,aCritRateMod,aSpMod,aCool,aCritDmgMod,aWeight):
        self.aID = aID
        self.aName = aName
        self.aType = aType
        self.aSubType = aSubType
        self.aBaseDmgMod = aBaseDmgMod
        self.aCritDmgMod = aCritDmgMod
        self.aCritRateMod = aCritRateMod
        self.aSpMod = aSpMod

        self.aCool = aCool
        self.aWeight = aWeight

        
    def __str__(self):
        
        return f"Mob_attack: Name={self.aName} Type={self.aType} SubType={self.aSubType} BaseDmgMod={self.aBaseDmgMod} CritRateMod={self.aCritRateMod}"

    def getAttackValue(self,mobBaseAttack,mobBaseCritRate):
        critRate = self.aCritRateMod * mobBaseCritRate
        roll = random.uniform(0,1)
        attackValue = mobBaseAttack * self.aBaseDmgMod
        #print("BaseAttack: ",mobBaseAttack," BaseDmgMod: ",self.aBaseDmgMod," Attack Value: ",attackValue, " CritRate: ",critRate," Roll: ",roll )
        if(roll <= critRate):
            #print("In Crit. DmgMod: ",self.aCritDmgMod)
            attackValue = attackValue * self.aCritDmgMod
        return round(attackValue)

    def getWeight()
        return self.aWeight

    def getCoolDown()
        return self.aCool

myAttack = Mob_Attack(1,"Power Attack",1,2,2.0,1.25,1.5,20,2)


print(myAttack)
print (myAttack.getAttackValue(50,0.25))
print (myAttack.getAttackValue(50,0.25))
print (myAttack.getAttackValue(50,0.25))
print (myAttack.getAttackValue(10,0.25))
print (myAttack.getAttackValue(10,0.25))
print (myAttack.getAttackValue(10,0.25))
print (myAttack.getAttackValue(10,0.25))
print (myAttack.getAttackValue(10,0.25))
