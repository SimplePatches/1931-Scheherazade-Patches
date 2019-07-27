



image inspBackground:
    "images/Inspirations/UI_Game_MENU_Background.png"
    zoom factor

image inspDiscard:
    "images/Inspirations/Button_Discard.png"
    zoom (factor * 0.8)

image inspDiscardh:
    "images/Inspirations/Button_Discard_hover.png"
    zoom (factor * 0.8)

image inspDiscardU:
    "images/Inspirations/Button_Discard_Underlay.png"
    zoom (factor * 0.8)

image inspKeep:
    "images/Inspirations/Button_Keep.png"
    zoom (factor * 0.8)

image inspKeeph:
    "images/Inspirations/Button_Keep_hover.png"
    zoom (factor * 0.8)

image inspDone:
    "images/Inspirations/Button_Done.png"
    zoom (factor * 0.8)

image inspDoneh:
    "images/Inspirations/Button_Done_hover.png"
    zoom (factor * 0.8)


init python:
    import random
    class InspEffect:
        def __init__(self, type, min, max):
            self.type = type
            self.min = min
            self.max = max
        
        def clone(self):
            return InspEffect(self.type, self.min, self.max)

    class Inspirations:
        def __init__(self, type, number, name, description, argeffects):
            self.type = type
            self.number = number
            self.name = name
            self.description = description
            self.effectsCount = len(argeffects)
            self.effects = []
            
            for effect in argeffects:
                self.effects.append(effect)
        
        def getDescr(self):
            txt = ""
            for eff in self.effects:
                txt = txt +"+"+ str(eff.min)
                if eff.min != eff.max:
                    txt = txt + "-" + str(eff.max)
                txt = txt + " " + eff.type + "\n"
            return txt
        
        def clone(self):
            renpy.log("clone")
            eff = []
            for effect in self.effects:
                eff.append(effect.clone())
            
            return  Inspirations(self.type, self.number, self.name, self.description, eff)   

    class InspirationContainer:
        
        def __init__(self):
            self.list = []
            self.playerList = []
        
        def addPlayerInspire(self, object):
            renpy.log("add player inspire")
            if isinstance(object, Inspirations):
                
                self.playerList.append(object)
        
        def removePlayerInspire(self, object):
            
            if isinstance(object, Inspirations):
                self.playerList.remove(object)
        
        
        def addInspire(self,object):
            if object == False:
                return
            else:
                self.list.append(object)
            return
        
        def getSpecificInspireByMaxNumber(self, type, number):
            inspList = []
            for Inspirations in self.list:
                
                if Inspirations.type.lower() == type.lower() and Inspirations.number <= number and Inspirations.number >= (number - 2):
                    inspList.append(Inspirations)
            if len(inspList) > 0:
                return random.choice(inspList).clone()
        
        def getSpecificInspire(self, type, number):
            for Inspirations in self.list:
                if Inspirations.type.lower() == type.lower() and Inspirations.number == number:
                    
                    return Inspirations.clone()
        
        
        def getRandomInspireByType(self, type):
            inspList = []
            for Inspirations in self.list:
                if Inspirations.type.lower() == type.lower():
                    inspList.append(Inspirations)
            if len(inspList) > 0:
                return random.choice(inspList).clone()
        
        def getRandomInspire(self):
            return random.choice(self.list).clone()
        
        def initialize(self):
            
            self.addInspire(Inspirations(
                "Athletics",
                0,
                "Lucky Bumbling",
                "Athletics",
                [InspEffect("General", 50, 50),
                InspEffect("Strength", 5, 5),
                InspEffect("Leaping", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Athletics", 
                1,
                "Playful Challenge",
                "Athletics", 
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Athletics", 
                2,
                "Pent-Up Energy",
                "Athletics", 
                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 4, 4), 
                InspEffect("Strength", 3, 3)] 
            ))
            
            
            self.addInspire(Inspirations(   
                "Athletics", 
                3,
                "Competitive Spark",
                "Athletics", 
                [InspEffect("General", 50, 50), 
                InspEffect("Moxie", 4, 4)] 
            ))
            
            
            self.addInspire(Inspirations(
                "Athletics", 
                4,
                "Frustration to Burn",
                "Athletics", 
                [InspEffect("General", 50, 50),
                InspEffect("Strength", 6, 6), 
                InspEffect("Athletics Type", 5, 5), 
                InspEffect("Fisticuffs", 5, 5)] 
            ))
            
            
            self.addInspire(Inspirations(
                "Athletics", 
                5,
                "Athlete's Discipline",
                "Athletics", 
                [InspEffect("Grace", 6, 6), 
                InspEffect("General", 50, 50), 
                InspEffect("Resolve", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Athletics", 
                6,
                "Hunger for Challenges",
                "Athletics", 
                [InspEffect("General", 50, 50),
                InspEffect("Athletics Type", 7, 7), 
                InspEffect("Escape Artistry", 5, 5), 
                InspEffect("Courage", 5, 5), 
                InspEffect("Fisticuffs", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Athletics", 
                7,
                "Overcoming Pain",
                "Athletics", 
                [InspEffect("Resolve", 7, 7), 
                InspEffect("Strength", 1, 20), 
                InspEffect("General", 50, 50), 
                InspEffect("Fisticuffs", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Athletics", 
                8,
                "Dad's Example",
                "Athletics", 
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 1, 25), 
                InspEffect("Moxie", 7, 7), 
                InspEffect("Self Knowledge", 7, 7), 
                InspEffect("Athletics Type", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Athletics", 
                9,
                "Will to Dominate",
                "Athletics", 
                [InspEffect("Strength", 8, 8), 
                InspEffect("Moxie", 1, 20), 
                InspEffect("Fisticuffs", 7, 7), 
                InspEffect("General", 50, 50)] 
            ))
            
            self.addInspire(Inspirations(     
                "Athletics", 
                10,
                "In the Zone",
                "Athletics", 
                [InspEffect("General", 50, 50), 
                InspEffect("Athletics Type", 12, 12), 
                InspEffect("Poise", 7, 7), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("Problem Solving", 5, 5)] 
            ))
            
            
            
            
            self.addInspire(Inspirations(
                "Grace",
                0,
                "Improvisational Flailing Around",
                "Athletics",
                [InspEffect("General", 50, 50),
                InspEffect("Grace", 4, 4),
                InspEffect("Athletics Type", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                1,
                "Natural Flexibility",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                2,
                "Ballet Teacher's Advice",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 3, 3), 
                InspEffect("Poise", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                3,
                "Survivor of Many Handstands",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 6, 6), 
                InspEffect("Strength", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                4,
                "Juggler's Training",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 6, 6), 
                InspEffect("Magic Tricks", 5, 5), 
                InspEffect("Resolve", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                5,
                "Showing Off",
                "Athletics", 

                [InspEffect("General", 50, 50), 
                InspEffect("Poise", 1, 15), 
                InspEffect("Flirting", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                6,
                "Physical Memory",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 6, 6), 
                InspEffect("Poise", 5, 5), 
                InspEffect("Athletics Type", 4, 4), 
                InspEffect("Dodge", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                7,
                "Magician's Artistry",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 7, 7), 
                InspEffect("Magic Tricks", 5, 5), 
                InspEffect("Deception", 5, 5), 
                InspEffect("Poise", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                8,
                "Gymnast's Concentration",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 7, 7), 
                InspEffect("Resolve", 1, 25), 
                InspEffect("Escape Artist", 5, 5), 
                InspEffect("Dodge", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                9,
                "Love of Movement",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 8, 8), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("Poise", 7, 7), 
                InspEffect("Athletics Type", 6, 6)] 
            ))
            
            self.addInspire(Inspirations(
                "Grace", 
                10,
                "Grace under Pressure",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Grace", 12, 12), 
                InspEffect("Courage", 9, 9), 
                InspEffect("Escape Artist", 7, 7), 
                InspEffect("Athletics Type", 10, 10), 
                InspEffect("Poise", 5, 5)] 
            ))
            
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Climbing",
                0,
                "Monkey-Like Grip",
                "Athletics",
                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 4, 4),
                InspEffect("Strength", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                1,
                "A Good Hold",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 1, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                2,
                "Enjoying the View",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 4, 4), 
                InspEffect("Resolve", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                3,
                "Better There than Here",
                "Athletics", 
  
                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 6, 6), 
                InspEffect("Resolve", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                4,
                "Contempt for Gravity",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 1, 15), 
                InspEffect("Courage", 5, 5), 
                InspEffect("Grace", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                5,
                "There's a Handhold!",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 7, 7), 
                InspEffect("Problem Solving", 5, 5), 
                InspEffect("Patience", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                6,
                "Beating Your Best Time",
                "Athletics", 

                [InspEffect("Climbing", 7, 7), 
                InspEffect("Resolve", 6, 6), 
                InspEffect("Leaping", 5, 5), 
                InspEffect("General", 50, 50)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                7,
                "Bracing Breeze",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 1, 20), 
                InspEffect("Grace", 6, 6), 
                InspEffect("Athletics Type", 5, 5), 
                InspEffect("Hope", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                8,
                "Aching Fingers",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Climbing", 1, 25), 
                InspEffect("Strength", 6, 6), 
                InspEffect("Courage", 6, 6), 
                InspEffect("Moxie", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                9,
                "Superb Equipment",
                "Athletics", 

                [InspEffect("Climbing", 9, 9), 
                InspEffect("Stealth", 7, 7), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("General", 50, 50)] 
            ))
            
            self.addInspire(Inspirations(
                "Climbing", 
                10,
                "Because It's There",
                "Athletics", 

                [InspEffect("Climbing", 10, 19), 
                InspEffect("Resolve", 1, 30), 
                InspEffect("Courage", 1, 30), 
                InspEffect("Moxie", 1, 25), 
                InspEffect("General", 50, 50)] 
            ))
            
            
            
            
            self.addInspire(Inspirations(
                "Leaping",
                0,
                "Overly Excited",
                "Athletics",
                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 4, 4),
                InspEffect("Hope", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                1,
                "Spring in Your Step",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 1, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                2,
                "Wind at Your Back",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 4, 4), 
                InspEffect("Moxie", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(    
                "Leaping", 
                3,
                "Good Traction",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 6, 6), 
                InspEffect("Grace", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                4,
                "Years of Jumping",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 7, 7), 
                InspEffect("Dodge", 1, 15), 
                InspEffect("Stealth", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(       
                "Leaping", 
                5,
                "New Shoes",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 7, 7), 
                InspEffect("Grace", 5, 5), 
                InspEffect("Athletics Type", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                6,
                "This Time for Sure",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 1, 15), 
                InspEffect("Resolve", 7, 7), 
                InspEffect("Courage", 5, 5), 
                InspEffect("Dodge", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                7,
                "Wolves at Your Heels",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 1, 20), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("Stealth", 6, 6), 
                InspEffect("Athletics Type", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                8,
                "Almost Like Flying",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 7, 7), 
                InspEffect("Dodge", 1, 20), 
                InspEffect("Moxie", 1, 20), 
                InspEffect("Grace", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                9,
                "You Can Make It!",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 9, 9), 
                InspEffect("Stealth", 7, 7), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("Strength", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Leaping", 
                10,
                "Touching the Sky",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Leaping", 10, 10), 
                InspEffect("Self Knowledge", 1, 25), 
                InspEffect("Grace", 7, 7), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("Escape Artist", 7, 7)] 
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Strength",
                0,
                "Can of Spinach",
                "Athletics",
                [InspEffect("General", 50, 50),
                InspEffect("Strength", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                1,
                "A Good Breakfast",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                2,
                "Long Night's Sleep",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Athletics Type", 4, 4), 
                InspEffect("Resolve", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                3,
                "Testing Yourself",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 6, 6), 
                InspEffect("Self Knowledge", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                4,
                "Simple Irritation",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 6, 6), 
                InspEffect("Fisticuffs", 5, 5), 
                InspEffect("Athletics Type", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                5,
                "You've Trained for This",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 7, 7), 
                InspEffect("Climbing", 5, 5), 
                InspEffect("Leaping", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                6,
                "Motivating Anger",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 7, 7), 
                InspEffect("Climbing", 5, 5), 
                InspEffect("Fisticuffs", 5, 5), 
                InspEffect("Moxie", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                7,
                "Flush of Adrenaline",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 1, 20), 
                InspEffect("Climbing", 1, 15), 
                InspEffect("Leaping", 1, 15), 
                InspEffect("Athletics Type", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                8,
                "Athlete's Will",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 1, 25), 
                InspEffect("Resolve", 7, 7), 
                InspEffect("Courage", 7, 7), 
                InspEffect("Athletics Type", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                9,
                "Desperate Urgency",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 9, 9), 
                InspEffect("Climbing", 1, 25), 
                InspEffect("Fisticuffs", 1, 25), 
                InspEffect("Dodge", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Strength", 
                10,
                "Untapped Reserves",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Strength", 10, 10), 
                InspEffect("Athletics Type", 10, 10), 
                InspEffect("Fisticuffs", 7, 7), 
                InspEffect("Dodge", 7, 7), 
                InspEffect("Resolve", 5, 5)] 
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Riding",
                0,
                "Clinging for Dear Life",
                "Athletics",
                [InspEffect("General", 50, 50),
                InspEffect("Riding", 4, 4),
                InspEffect("Strength", 4, 4)]
            ))
            
            self.addInspire(Inspirations( 
                "Riding", 
                1,
                "Good Day for Riding",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                2,
                "Smooth Path So Far",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 4, 4), 
                InspEffect("Grace", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                3,
                "Comfortable Seat",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 6, 6), 
                InspEffect("Poise", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                4,
                "Years at the Reins",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 1, 15), 
                InspEffect("Grace", 5, 5), 
                InspEffect("Poise", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                5,
                "Gentle Ride",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 7, 7), 
                InspEffect("Poise", 1, 15), 
                InspEffect("Animal Handling", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                6,
                "Love of Speed",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 7, 7), 
                InspEffect("Jumping", 5, 5), 
                InspEffect("Dodge", 5, 5), 
                InspEffect("Athletics Type", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                7,
                "Challenging Course Ahead",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 7, 7), 
                InspEffect("Resolve", 6, 6), 
                InspEffect("Problem Solving", 6, 6), 
                InspEffect("Animal Handling", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                8,
                "Win the Race",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 1, 25), 
                InspEffect("Moxie", 1, 20), 
                InspEffect("Leaping", 6, 6), 
                InspEffect("Grace", 6, 6)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                9,
                "The Perfect Horse",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 9, 9), 
                InspEffect("Animal Handling", 7, 7), 
                InspEffect("Dodging", 1, 20), 
                InspEffect("Poise", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Riding", 
                10,
                "Exhilarating Partnership",
                "Athletics", 

                [InspEffect("General", 50, 50),
                InspEffect("Riding", 10, 10), 
                InspEffect("Animal Handling", 9, 9), 
                InspEffect("Grace", 7, 7), 
                InspEffect("Poise", 7, 7), 
                InspEffect("Dodging", 5, 5)] 
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Charm",
                0,
                "Goofy Appeal",
                "Charm",
                [InspEffect("General", 50, 50),
                InspEffect("Charm Type", 3, 3),
                InspEffect("Poise", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                1,
                "Recalling a Funny Story",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                2,
                "Nice Card from Evelyn",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 3, 3), 
                InspEffect("Self Knowledge", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                3,
                "A Smile in a Crowd",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 5, 5), 
                InspEffect("Patience", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                4,
                "Reread a Favorite Novel",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 6, 6), 
                InspEffect("Tolerance", 4, 4), 
                InspEffect("Occult Lore", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                5,
                "A Bridge to Sell",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 7, 7), 
                InspEffect("Negotiation", 6, 6), 
                InspEffect("Poker", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                6,
                "Sincere Admiration",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7), 
                InspEffect("Charm Type", 6, 6), 
                InspEffect("Empathy", 5, 5), 
                InspEffect("Listen", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                7,
                "The Company of Friends",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 7, 7), 
                InspEffect("Diplomacy", 7, 7), 
                InspEffect("Courage", 6, 6), 
                InspEffect("Charm Type", 6, 6)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                8,
                "Work's Going Well",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 7, 7), 
                InspEffect("Tolerance", 7, 7), 
                InspEffect("Resolve", 6, 6), 
                InspEffect("Diplomacy", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                9,
                "Joy of Being Alive",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 9, 9), 
                InspEffect("Animal Handling", 7, 7), 
                InspEffect("Hope", 7, 7), 
                InspEffect("Patience", 1, 20)] 
            ))
            
            self.addInspire(Inspirations(
                "Charm", 
                10,
                "Natural Glow",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 10, 10), 
                InspEffect("Poise", 8, 8), 
                InspEffect("Deception", 1, 25), 
                InspEffect("Charm Type", 10, 10), 
                InspEffect("Hope", 5, 5)] 
            ))
            
            
            
            self.addInspire(Inspirations(
                "Deception",
                0,
                "Innocent Face",
                "Charm",
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 4, 4),
                InspEffect("Poker", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                1,
                "Convincing Smile",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                2,
                "Everybody Does It",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 4, 4), 
                InspEffect("Moxie", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                3,
                "A Really Fun Lie",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 6, 6), 
                InspEffect("Flirting", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                4,
                "Ready-Made Sob Story",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 7, 7), 
                InspEffect("Empathy", 5, 5), 
                InspEffect("Diplomacy", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                5,
                "Family of Bridge-Sellers",
                
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 7, 7), 
                InspEffect("Negotiation", 6, 6), 
                InspEffect("Poise", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                6,
                "For a Good Cause",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 7, 7), 
                InspEffect("Resolve", 7, 7), 
                InspEffect("Charm Type", 6, 6), 
                InspEffect("Conscience", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                7,
                "Just One Chance",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 1, 20), 
                InspEffect("Resolve", 7, 7), 
                InspEffect("Hope", 7, 7), 
                InspEffect("Courage", 6, 6)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                8,
                "A Deserving Mark",
                "Charm", 

                [InspEffect("General", 50, 50),
                InspEffect("Deception", 7, 7), 
                InspEffect("Moxie", 7, 7), 
                InspEffect("Awareness", 7, 7), 
                InspEffect("Poker", 1, 15)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                9,
                "Kissed the Blarney Stone",
                "Charm", 

                [InspEffect("General", 50, 50),
                InspEffect("Deception", 8, 8), 
                InspEffect("Flirting", 7, 7), 
                InspEffect("Negotiation", 7, 7), 
                InspEffect("Charm Type", 10, 10)] 
            ))
            
            self.addInspire(Inspirations(
                "Deception", 
                10,
                "Puppet Master",
                "Charm", 

                [InspEffect("General", 50, 50),
                InspEffect("Deception", 10, 10), 
                InspEffect("Negotiation", 8, 8), 
                InspEffect("Awareness", 7, 7), 
                InspEffect("Diplomacy", 7, 7), 
                InspEffect("Moxie", 7, 7)] 
            ))
            
            
            
            self.addInspire(Inspirations(
                "Diplomacy",
                0,
                "Generally Amiable Nature",
                "Charm",
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 4, 4),
                InspEffect("Awareness", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",
                1,
                "Seeing Both Sides",
                "Charm", 
               [InspEffect("General", 50, 50),
               InspEffect("Diplomacy", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",
                2,
                "Current on the Issues",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 5, 5),               
                InspEffect("Problem Solving", 4, 4)]
            ))
            
            self.addInspire(Inspirations(   
                "Diplomacy",                
                3,                
                "Creative Approach",               
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 6, 6),                
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(    
                "Diplomacy",               
                4,
                "Glimpse of Middle Ground",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),       
                InspEffect("Awareness", 5, 5),  
                InspEffect("Negotiation", 4, 4)]   
            ))
            
            self.addInspire(Inspirations(  
                "Diplomacy",              
                5,
                "Convincing Threats",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),
                InspEffect("Resolve", 5, 5),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",               
                6,
                "What Would Solomon Do?",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),            
                InspEffect("Problem Solving", 6, 6),               
                InspEffect("Poker", 5, 5),          
                InspEffect("Resolve", 4, 4)]                     
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",               
                7,    
                "Unexpected Leverage",          
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 1, 20),           
                InspEffect("Awareness", 7, 7),          
                InspEffect("Poise", 1, 15),           
                InspEffect("Negotiation", 1, 15)]
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",                
                8,
                "A Handy Bribe",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),        
                InspEffect("Negotiation", 7, 7),       
                InspEffect("Deception", 7, 7),
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",              
                9,
                "Moment of Insight",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 9, 9),
                InspEffect("Awareness", 7, 7),
                InspEffect("Negotiation", 1, 20),
                InspEffect("Empathy", 7, 7)]      
            ))
            
            self.addInspire(Inspirations(
                "Diplomacy",              
                10,
                "Silver Tongue",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 10, 10),   
                InspEffect("Flirting", 8, 8), 
                InspEffect("Charm Type", 12, 12),
                InspEffect("Negotiation", 7, 7),
                InspEffect("Deception", 5, 5)]
            ))
            
            
            
            self.addInspire(Inspirations(
                "Flirting",
                0,
                "Adorable When Flummoxed",
                "Charm",
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 4, 4),
                InspEffect("Negotiation", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Flirting",
                1,
                "A Ready Laugh",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 5, 5)]        
            ))
            
            self.addInspire(Inspirations(
                "Flirting",               
                2,
                "Come-Hither Eyes",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 4, 4),               
                InspEffect("Moxie", 1, 15)]
            ))
            
            self.addInspire(Inspirations(      
                "Flirting",                
                3,                
                "Roguish Grin",               
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 6, 6),                
                InspEffect("Deception", 1, 15)]
            ))
            
            self.addInspire(Inspirations(
                "Flirting",               
                4,
                "Jane Austen's My Guide",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),       
                InspEffect("Diplomacy", 5, 5),  
                InspEffect("Charm Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Flirting",              
                5,
                "Easy Banter",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),
                InspEffect("Awareness", 5, 5),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Flirting",               
                6,
                "Well-Timed Wink",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 1, 15),            
                InspEffect("Moxie", 6, 6),               
                InspEffect("Poise", 5, 5),          
                InspEffect("Charm Type", 7, 7)]                     
            ))
            
            self.addInspire(Inspirations(
                "Flirting",              
                7,    
                "A Gentle Touch",          
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 1, 20),           
                InspEffect("Empathy", 7, 7),          
                InspEffect("Courage", 5, 5),           
                InspEffect("Resolve", 4, 4)]              
            ))
            
            self.addInspire(Inspirations(
                "Flirting",              
                8,
                "Double Entendres Aplenty",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),        
                InspEffect("Language", 1, 20),       
                InspEffect("Listen", 7, 7),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Flirting",             
                9,
                "Thrill of the Chase",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 9, 9),
                InspEffect("Hope", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("Charm Type", 10, 10)]      
            ))
            
            self.addInspire(Inspirations(
                "Flirting",            
                10,
                "Jaw-Dropping Spark",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 10, 10),   
                InspEffect("Problem Solving", 8, 8), 
                InspEffect("Charm Type", 12, 12),
                InspEffect("Hope", 7, 7),
                InspEffect("Moxie", 5, 5)]
            ))
            
            
            
            self.addInspire(Inspirations(
                "Negotiation",
                0,
                "Obstinate Ways",
                "Charm",
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 4, 4),
                InspEffect("Resolve", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                1,
                "Good Sales Pitch",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 5, 5)]  
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",                
                2,
                "Firm Handshake",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 4, 4),               
                InspEffect("Poise", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                3,                
                "Eye for Weakness",               
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 6, 6),                
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(    
                "Negotiation",
                4,
                "Something Worth Selling",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 7, 7),       
                InspEffect("Resolve", 4, 4),  
                InspEffect("Poise", 3, 3)]   
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                5,
                "Huckster's Patter",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 7, 7),
                InspEffect("Deception", 5, 5),
                InspEffect("Flirting", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                6,
                "Flashback to Debate Team",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 1, 15),            
                InspEffect("Problem Solving", 5, 5),               
                InspEffect("Listen", 5, 5),          
                InspEffect("Deduction", 5, 5)]                      
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                7,    
                "Mutual Respect",          
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 7, 7),           
                InspEffect("Diplomacy", 7, 7),          
                InspEffect("Empathy", 5, 5),           
                InspEffect("Charm Type", 10, 10)]
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                8,
                "You Can Walk Away",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 7, 7),        
                InspEffect("Poise", 7, 7),       
                InspEffect("Moxie", 6, 6),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                9,
                "Predator's Instinct",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 9, 9),
                InspEffect("Moxie", 7, 7),
                InspEffect("Courage", 7, 7),
                InspEffect("Resolve", 6, 6)]      
            ))
            
            self.addInspire(Inspirations(
                "Negotiation",
                10,
                "The Angle",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 10, 10),   
                InspEffect("Deduction", 8, 8), 
                InspEffect("Awareness", 7, 7),
                InspEffect("Moxie", 1, 20),
                InspEffect("Diplomacy", 1, 25)]
            ))
            
            
            self.addInspire(Inspirations(
                "Animal Handling",
                0,
                "Blissfully Unafraid of Fangs",
                "Charm",
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 4, 4),
                InspEffect("Fisticuffs", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                1,
                "It's Sooo Furry",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                2,
                "Gentle Demeanor",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 5, 5),               
                InspEffect("Riding", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                3,                
                "Simple Trust",               
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 6, 6),                
                InspEffect("Conscience", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                4,
                "Pack Leader",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 6, 6),       
                InspEffect("Courage", 5, 5),  
                InspEffect("Poise", 4, 4)]  
                            
            ))
            
            self.addInspire(Inspirations(       
                "Animal Handling",
                5,
                "Raised by Dogs",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 7, 7),
                InspEffect("Moxie", 5, 5),
                InspEffect("Courage", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                6,
                "Obvious Body Language",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 7, 7),            
                InspEffect("Awareness", 6, 6),               
                InspEffect("Riding", 5, 5),          
                InspEffect("Flirting", 4, 4)]                    
            ))
            
            self.addInspire(Inspirations(       
                "Animal Handling",
                7,    
                "Aunt Evelyn's Animal Advice",          
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 1, 25),           
                InspEffect("Conscience", 7, 7),          
                InspEffect("Charm Type", 7, 7),           
                InspEffect("Riding", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                8,
                "Reassuring Manner",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 7, 7),        
                InspEffect("Riding", 7, 7),       
                InspEffect("Charm Type", 7, 7),
                InspEffect("Empathy", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                9,
                "Treats",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 9, 9),
                InspEffect("Negotiation", 7, 7),
                InspEffect("Riding", 7, 7),
                InspEffect("Poise", 6, 6)]    
            ))
            
            self.addInspire(Inspirations(
                "Animal Handling",
                10,
                "Tips from a Whisperer",
                "Charm", 
                [InspEffect("General", 50, 50),
                InspEffect("Animal Handling", 10, 10),   
                InspEffect("Riding", 9, 9), 
                InspEffect("Courage", 7, 7),
                InspEffect("Empathy", 7, 7),
                InspEffect("Poise", 5, 5)]
            ))
            
            
            
            self.addInspire(Inspirations(
                "Dream of Family",
                0,
                "Faded Memories",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 4, 4),
                InspEffect("Hope", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                1,
                "Mother's Lullabyes",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Dream Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                2,
                "Hard Work Pays",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 4, 4),               
                InspEffect("Self Knowledge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                3,                
                "Childhood Games",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 6, 6),                
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations( 
                "Dream of Family",
                4,
                "Archaeologist from Early Days",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),       
                InspEffect("Deduction", 5, 5),  
                InspEffect("Occult Lore", 4, 4)]   
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                5,
                "Old Scars Itch",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),
                InspEffect("Self Knowledge", 5, 5),
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                6,
                "High School Flashback",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 7, 7),            
                InspEffect("Resolve", 6, 6),               
                InspEffect("Tolerance", 5, 5),          
                InspEffect("Self Knowledge", 3, 3)]                     
            ))
            
            self.addInspire(Inspirations(   
                "Dream of Family",
                7,    
                "All According to Plan",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),           
                InspEffect("Patience", 6, 6),          
                InspEffect("Moxie", 5, 5),           
                InspEffect("Hope", 4, 4)]    
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                8,
                "Special Training",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 1, 25),        
                InspEffect("Problem Solving", 7, 7),       
                InspEffect("Deduction", 7, 7),
                InspEffect("Magic Tricks", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                9,
                "The Keating Luck",
                "Dream", 

                [InspEffect("Problem Solving", 9, 9),
                InspEffect("Hope", 7, 7),
                InspEffect("Poise", 1, 20),
                InspEffect("General", 50, 50)]    
            ))
            
            self.addInspire(Inspirations(
                "Dream of Family",
                10,
                "View of the Future",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 10, 10),   
                InspEffect("Hope", 9, 9), 
                InspEffect("Dream Type", 15, 15),
                InspEffect("Patience", 7, 7),
                InspEffect("Self Knowledge", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Conscience",
                0,
                "Faint Qualm",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 4, 4),
                InspEffect("Awareness", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                1,
                "Aesop's Lessons",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                2,
                "Sunday School Flashback",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 5, 5),               
                InspEffect("Tolerance", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                3,                
                "Basic Humanity",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 6, 6),                
                InspEffect("Empathy", 5, 5)]
            ))
            
            self.addInspire(Inspirations(      
                "Conscience",
                4,
                "Lessons from Fitzgerald",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 6, 6),       
                InspEffect("Self Knowledge", 5, 5),  
                InspEffect("Dream Type", 7, 7)]        
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                5,
                "The Howard Carter Example",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 7, 7),
                InspEffect("Deduction", 5, 5),
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                6,
                "Legal Scholarship",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 6, 6),            
                InspEffect("Diplomacy", 6, 6),               
                InspEffect("Awareness", 5, 5),          
                InspEffect("Tolerance", 4, 4)]                   
            ))
            
            self.addInspire(Inspirations(    
                "Conscience",
                7,    
                "A Strong Sermon",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 7, 7),           
                InspEffect("Self Knowledge", 6, 6),          
                InspEffect("Empathy", 6, 6),           
                InspEffect("Hope", 5, 5)]                  
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                8,
                "Code of Honor",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 7, 7),        
                InspEffect("Self Knowledge", 7, 7),       
                InspEffect("Courage", 7, 7),
                InspEffect("Resolve", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Conscience",
                9,
                "Sleep of the Just",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 9, 9),
                InspEffect("Courage", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("Moxie", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(   
                "Conscience",
                10,
                "Moral Clarity",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 10, 10),   
                InspEffect("Self Knowledge", 8, 8), 
                InspEffect("Resolve", 7, 7),
                InspEffect("Dream Type", 10, 10),
                InspEffect("Animal Handling", 6, 6)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Courage",
                0,
                "Poor Impulse Control",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Courage", 4, 4),
                InspEffect("Leaping", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                1,
                "Lucky Coin",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                2,
                "Deep, Calming Breath",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 4, 4),               
                InspEffect("Resolve", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                3,                
                "Reputation to Maintain",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Courage", 6, 6),                
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                4,
                "Adrenaline Rush",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 6, 6),       
                InspEffect("Strength", 5, 5),  
                InspEffect("Leaping", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                5,
                "Can't Fail!",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 6, 6),
                InspEffect("Resolve", 5, 5),
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                6,
                "Unleash the Pep Talk",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),            
                InspEffect("Resolve", 6, 6),               
                InspEffect("Hope", 5, 5),          
                InspEffect("Moxie", 4, 4)]                    
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                7,    
                "Survived Worse!",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),           
                InspEffect("Patience", 6, 6),          
                InspEffect("Self Knowledge", 5, 5),           
                InspEffect("Hope", 5, 5)]
            ))
            
            self.addInspire(Inspirations(   
                "Courage",
                8,
                "Energizing Anger",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),        
                InspEffect("Strength", 7, 7),       
                InspEffect("Fisticuffs", 7, 7),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                9,
                "No Time to Think!",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 9, 9),
                InspEffect("Resolve", 7, 7),
                InspEffect("Leaping", 7, 7),
                InspEffect("Climbing", 7, 7)]      
            ))
            
            self.addInspire(Inspirations(
                "Courage",
                10,
                "Fire of Heroism",
                "Dream", 

                [InspEffect("Courage", 10, 10),   
                InspEffect("Fisticuffs", 7, 7), 
                InspEffect("Grace", 7, 7),
                InspEffect("Dream Type", 10, 10),
                InspEffect("General", 50, 50)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Patience",
                0,
                "Satisfying Yawn",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Patience", 4, 4),
                InspEffect("Tolerance", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                1,
                "Counting to a Thousand",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                2,
                "Magazine to Read",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 4, 4),               
                InspEffect("Magic Tricks", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                3,                
                "Interesting Things to See",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Patience", 6, 6),                
                InspEffect("Dream Type", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                4,
                "Letter to Write",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 6, 6),       
                InspEffect("Diplomacy", 5, 5),  
                InspEffect("Self Knowledge", 4, 4)] 
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                5,
                "Elevator Music",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 7, 7),
                InspEffect("Hope", 5, 5),
                InspEffect("Flirting", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                6,
                "Simple Stationary Exercises",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 7, 7),            
                InspEffect("Leaping", 5, 5),               
                InspEffect("Climbing", 5, 5),          
                InspEffect("Dodging", 3, 3)]                    
            ))
            
            self.addInspire(Inspirations(   
                "Patience",
                7,    
                "Moment of Tranquility",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Patience", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Deduction", 6, 6),           
                InspEffect("Repair", 4, 4)]             
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                8,
                "New Meditation Technique",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 7, 7),        
                InspEffect("Poise", 7, 7),       
                InspEffect("Escape Artistry", 7, 7),
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Patience",
                9,
                "Deep Thinking",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 9, 9),
                InspEffect("Deduction", 7, 7),
                InspEffect("Awareness", 7, 7),
                InspEffect("Self Knowledge", 1, 25)]   
            ))
            
            self.addInspire(Inspirations(  
                "Patience",
                10,
                "Perfect Serenity",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 10, 10),   
                InspEffect("Self Knowledge", 8, 8), 
                InspEffect("Poise", 7, 7),
                InspEffect("Dream Type", 10, 10),
                InspEffect("Grace", 1, 25)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Resolve",
                0,
                "Simple Inertia",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 4, 4),
                InspEffect("Poise", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                1,
                "Moment of Spite",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 4, 4)]          
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                2,
                "Inspiring Sight",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 5, 5),               
                InspEffect("Hope", 3, 3)]
            ))
            
            self.addInspire(Inspirations(   
                "Resolve",
                3,                
                "Remembered Speech",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 5, 5),                
                InspEffect("Dream Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                4,
                "Streak of Stubbornness",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 6, 6),       
                InspEffect("Courage", 5, 5),  
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                5,
                "Expectations of Friends",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),
                InspEffect("Self Knowledge", 5, 5),
                InspEffect("Dream Type", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                6,
                "The Plan After A",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),            
                InspEffect("Problem Solving", 6, 6),               
                InspEffect("Courage", 5, 5),          
                InspEffect("Awareness", 3, 3)]                    
            ))
            
            self.addInspire(Inspirations(  
                "Resolve",
                7,    
                "A Well-Defined Goal",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),           
                InspEffect("Courage", 6, 6),          
                InspEffect("Climbing", 5, 5),           
                InspEffect("Leaping", 5, 5)]             
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                8,
                "Excitement in Adversity",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 1, 25),        
                InspEffect("Courage", 7, 7),       
                InspEffect("Moxie", 7, 7),
                InspEffect("Fisticuffs", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                9,
                "Heroic Examples",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 9, 9),
                InspEffect("Courage", 7, 7),
                InspEffect("Strength", 7, 7),
                InspEffect("Problem Solving", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Resolve",
                10,
                "Iron Will",
                "Dream", 

                [InspEffect("Resolve", 10, 10),   
                InspEffect("Courage", 9, 9), 
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Poise", 7, 7),
                InspEffect("General", 50, 50)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Hope",
                0,
                "No Point Worrying",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 4, 4),
                InspEffect("Animal Handling", 4, 4)]
            ))
            
            self.addInspire(Inspirations( 
                "Hope",
                1,
                "Sun After the Rain",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                2,
                "Beautiful Morning",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 4, 4),               
                InspEffect("Tolerance", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                3,                
                "Whistling a Happy Tune",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 6, 6),                
                InspEffect("Diplomacy", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                4,
                "Sense of Progress",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 6, 6),       
                InspEffect("Resolve", 5, 5),  
                InspEffect("Dream Type", 5, 5)]   
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                5,
                "Letter from a Friend",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 7, 7),
                InspEffect("Empathy", 5, 5),
                InspEffect("Dream Type", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                6,
                "Remembered Advice",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 7, 7),            
                InspEffect("Resolve", 6, 6),               
                InspEffect("Diplomacy", 5, 5),          
                InspEffect("Negotiation", 3, 3)]                  
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                7,    
                "End Almost in Sight",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 7, 7),           
                InspEffect("Resolve", 7, 7),          
                InspEffect("Dream Type", 7, 7),           
                InspEffect("Courage", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                8,
                "Optimistic Temperament",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 7, 7),        
                InspEffect("Diplomacy", 7, 7),       
                InspEffect("Animal Handling", 6, 6),
                InspEffect("Tolerance", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                9,
                "Good Friends Abound",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 8, 8),
                InspEffect("Resolve", 7, 7),
                InspEffect("Dream Type", 10, 10),
                InspEffect("Courage", 1, 25)]    
            ))
            
            self.addInspire(Inspirations(
                "Hope",
                10,
                "Reassuring Experience",
                "Dream", 

                [InspEffect("Hope", 10, 10),   
                InspEffect("Self Knowledge", 9, 9), 
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("General", 50, 50)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Dream of College",
                0,
                "All Grown Up",
                "Dream",
                [InspEffect("General", 90, 90)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Change",
                0,
                "Life's Getting Interesting",
                "Dream",
                [InspEffect("General", 80, 80)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Completion",
                0,
                "The Final Stretch",
                "Dream",
                [InspEffect("General", 70, 70)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Christmas",
                0,
                "Warm Christmas Memories",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Egypt",
                0,
                "Egyptian Dreams",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Australia",
                0,
                "Australian Dreams",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of India",
                0,
                "Indian Dreams",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Peru",
                0,
                "Peruvian Dreams",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of New Orleans",
                0,
                "New Orleans Dreams",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Turkey",
                0,
                "Turkish Dreams",
                "Dream",
                [InspEffect("General", 50, 50)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Anna's World Tour",
                0,
                "World Tourist",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Deduction", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Blood and Art",
                0,
                "Finder of the Lost",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Empathy", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Butlers",
                0,
                "Well Cared For",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Leaping", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Cappadocia",
                0,
                "Up from the Dark",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Perception", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Grimoire",
                0,
                "The King's Book",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Magic Tricks", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Third Eye",
                0,
                "Rescuer of Carpenters",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Poise", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of a Royal Family",
                0,
                "Queen of Horses",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Riding", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Hunt",
                0,
                "Fox and Headwear Capturer",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Moxie", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of a Big Movie Star",
                0,
                "Drake Darling's Strange Career",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Deception", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Football",
                0,
                "Taking out the Trash",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Listen", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Albino Alligator",
                0,
                "Friend to the Alligators",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Animal Handling", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Great Game",
                0,
                "Great Game Player",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Dodge", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of Flight and Film",
                0,
                "Looking from Great Heights",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Climbing", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Crossroads",
                0,
                "Quickfinger Girl",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Resolve", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of a Beautiful City",
                0,
                "Lions of the Library",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Hope", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Spear",
                0,
                "The Spear in the Cave",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Moxie", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Stolen Scholar",
                0,
                "Tello's Gratitude",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Diplomacy", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Platypus",
                0,
                "Diamond in the Light",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Courage", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Golden Scarab",
                0,
                "Taste o'the Golden Scarab",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Leaping", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Serpent Empire",
                0,
                "Fallen City Survivor",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Occult Lore", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Devourers",
                0,
                "The Devourers' Bane",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Repair", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Dead Bakers",
                0,
                "Marc Antony's Messenger",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Cryptography", 10, 10)]
                ))
            
            
            self.addInspire(Inspirations(
                "Dream of the Ancient Mystery",
                0,
                "Finder of Strange Tombs",
                "Dream",
                [InspEffect("General", 60, 70),
                InspEffect("Problem Solving", 10, 10)]
                ))                 
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                0,
                "From Past to Future",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 4, 4),
                InspEffect("Resolve", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                1,
                "Tender Word",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                2,
                "Kheper Shuts Up",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),               
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                3,                
                "See Him More",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 6, 6),                
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                4,
                "Cracking His Reserve",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),       
                InspEffect("Flirting", 5, 5),  
                InspEffect("Dream Type", 7, 7)]  
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                5,
                "Arguing with Style",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Negotiation", 7, 7),
                InspEffect("Problem Solving", 6, 6),
                InspEffect("Self Knowledge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(     
                "Dream of Ahmose",
                6,
                "Learn About Him",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),            
                InspEffect("Empathy", 7, 7),               
                InspEffect("Occult Lore", 5, 5),          
                InspEffect("Listen", 5, 5)]                      
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                7,    
                "Making Him Laugh",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),           
                InspEffect("Flirting", 7, 7),          
                InspEffect("Awareness", 6, 6),           
                InspEffect("Dream Type", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                8,
                "Debate the World",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),        
                InspEffect("Listen", 7, 7),       
                InspEffect("Self Knowledge", 7, 7),
                InspEffect("Conscience", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                9,
                "Saving His Life",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 9, 9),
                InspEffect("Courage", 7, 7),
                InspEffect("Self Knowledge", 7, 7),
                InspEffect("Hope", 7, 7)]     
            ))
            
            self.addInspire(Inspirations(
                "Dream of Ahmose",
                10,
                "Happy Ending with Ahmose",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 10, 10),   
                InspEffect("Hope", 9, 9), 
                InspEffect("Flirting", 9, 9),
                InspEffect("Dream Type", 10, 10),
                InspEffect("Self Knowledge", 7, 7)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                0,
                "Something New to Learn",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 4, 4),
                InspEffect("Poise", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                1,
                "Simple Admiration",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                2,
                "Mutual Respect",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),               
                InspEffect("Flirting", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                3,                
                "Interesting Archaeology Talk",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Listen", 5, 5),                
                InspEffect("Occult Lore", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                4,
                "Companionship in the Tombs",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),       
                InspEffect("Resolve", 5, 5),  
                InspEffect("Perception", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                5,
                "Loosening the Boy Up",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),
                InspEffect("Moxie", 5, 5),
                InspEffect("Dream Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                6,
                "Professional Coordination",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),            
                InspEffect("Resolve", 6, 6),               
                InspEffect("Escape Artistry", 6, 6),          
                InspEffect("Perception", 5, 5)]                    
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                7,    
                "Surprising Wit",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),           
                InspEffect("Poise", 7, 7),          
                InspEffect("Listen", 6, 6),           
                InspEffect("Courage", 5, 5)]                   
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                8,
                "Conversations into the Night",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),        
                InspEffect("Language", 7, 7),       
                InspEffect("Hope", 7, 7),
                InspEffect("Dream Type", 8, 8)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Nigel",
                9,
                "Thrill of the Dig",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 9, 9),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Occult Lore", 7, 7),
                InspEffect("Flirting", 6, 6)]     
            ))
            
            self.addInspire(Inspirations(     
                "Dream of Nigel",
                10,
                "Happy Ending with Nigel",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 10, 10),   
                InspEffect("Resolve", 9, 9), 
                InspEffect("Flirting", 9, 9),
                InspEffect("Dream Type", 12, 12),
                InspEffect("Self Knowledge", 7, 7)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                0,
                "Head in the Clouds",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 4, 4),
                InspEffect("Self Knowledge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                1,
                "Easy Companionship",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                2,
                "Flirty Banter",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 5, 5),               
                InspEffect("Awareness", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                3,                
                "A Hand to Hold",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Courage", 5, 5),                
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                4,
                "Keep the Motor Running",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 6, 6),       
                InspEffect("Flirting", 5, 5),  
                InspEffect("Problem Solving", 3, 3)]  
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                5,
                "Trust",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),
                InspEffect("Hope", 6, 6),
                InspEffect("Self Knowledge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                6,
                "Rapport of Many Years",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),            
                InspEffect("Courage", 7, 7),               
                InspEffect("Dream Type", 5, 5),          
                InspEffect("Empathy", 3, 3)]                   
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                7,    
                "Mutual Support",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),           
                InspEffect("Tolerance", 7, 7),          
                InspEffect("Courage", 5, 5),           
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                8,
                "Years of Laughter",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),        
                InspEffect("Moxie", 7, 7),       
                InspEffect("Dream Type", 8, 8),
                InspEffect("Awareness", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                9,
                "Deep Friendship",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 9, 9),
                InspEffect("Flirting", 8, 8),
                InspEffect("Hope", 7, 7),
                InspEffect("Empathy", 7, 7)]     
            ))
            
            self.addInspire(Inspirations(
                "Dream of Felix",
                10,
                "Happy Ending with Felix",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 10, 10),   
                InspEffect("Self Knowledge", 9, 9), 
                InspEffect("Hope", 8, 8),
                InspEffect("Dream Type", 10, 10),
                InspEffect("Empathy", 8, 8)]
            ))
            
            
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                0,
                "Light in the Shadows",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 4, 4),
                InspEffect("Courage", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                1,
                "Never Quiet",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                2,
                "Droll and Cultured",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),               
                InspEffect("Flirting", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                3,                
                "Globe-Trotting Ways",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 5, 5),                
                InspEffect("Dream Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(  
                "Dream of Roland",
                4,
                "Seeing the Big Picture",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 6, 6),       
                InspEffect("Awareness", 5, 5),  
                InspEffect("Problem Solving", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                5,
                "Whiff of Danger",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),
                InspEffect("Courage", 6, 6),
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                6,
                "Always Seducing, Always Seduced",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),            
                InspEffect("Deception", 7, 7),               
                InspEffect("Poise", 5, 5),          
                InspEffect("Awareness", 3, 3)]                   
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                7,    
                "Steadfast at Useful Moments",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),           
                InspEffect("Courage", 7, 7),          
                InspEffect("Poise", 5, 5),           
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                8,
                "The Greater Good",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),        
                InspEffect("Dream Type", 8, 8),       
                InspEffect("Courage", 7, 7),
                InspEffect("Moxie", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                9,
                "Adventurous Heart",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 9, 9),
                InspEffect("Flirting", 8, 8),
                InspEffect("Hope", 7, 7),
                InspEffect("Dodging", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Dream of Roland",
                10,
                "Happy Ending with Roland",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 10, 10),   
                InspEffect("Resolve", 9, 9), 
                InspEffect("Courage", 8, 8),
                InspEffect("Dream Type", 12, 12),
                InspEffect("Deception", 7, 7)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                0,
                "Tested Appeal",
                "Dream",
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 4, 4),
                InspEffect("Tolerance", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                1,
                "Always a New Challenge",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                2,
                "Sparks Flying",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 4, 4),               
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                3,                
                "Wits Always About You",               
                "Dream", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 5, 5),                
                InspEffect("Wits Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                4,
                "Moments of Wonder",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 6, 6),       
                InspEffect("Hope", 5, 5),  
                InspEffect("Conscience", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                5,
                "True Equals",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 7, 7),
                InspEffect("Flirting", 6, 6),
                InspEffect("Listen", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                6,
                "Gentle Cut and Parry",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 7, 7),            
                InspEffect("Flirting", 7, 7),               
                InspEffect("Dream Type", 5, 5),          
                InspEffect("Self Knowledge", 3, 3)]                  
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                7,    
                "Spurring One Another Forward",          
                "Dream", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Flirting", 5, 5),           
                InspEffect("Moxie", 5, 5)]                
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                8,
                "Reckless Adventure",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),        
                InspEffect("Courage", 7, 7),       
                InspEffect("Leaping", 7, 7),
                InspEffect("Perception", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                9,
                "Better Together than Apart",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 9, 9),
                InspEffect("Courage", 8, 8),
                InspEffect("Hope", 7, 7),
                InspEffect("Dream Type", 10, 10)] 
            ))
            
            self.addInspire(Inspirations(
                "Dream of Sterling",
                10,
                "Happy Ending with Sterling",
                "Dream", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 10, 10),   
                InspEffect("Flirting", 9, 9), 
                InspEffect("Courage", 8, 8),
                InspEffect("Dream Type", 12, 12),
                InspEffect("Poise", 7, 7)]
            ))
            
            
            
            self.addInspire(Inspirations(
                "Knowledge",
                0,
                "Childhood with Ruddy",
                "Knowledge",
                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 4, 4),
                InspEffect("Problem Solving", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                1,
                "Overheard Conversation",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                2,
                "Note in the Margins",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 4, 4),               
                InspEffect("Perception", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                3,                
                "Half-Remembered Lecture",               
                "Knowledge", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Language", 6, 6),                
                InspEffect("Knowledge Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                4,
                "Recent Journal Article",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Repair", 5, 5),  
                InspEffect("Occult Lore", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                5,
                "Debated the Subject",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),
                InspEffect("Problem Solving", 6, 6),
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                6,
                "Jane-of-All-Trades",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),            
                InspEffect("Deduction", 7, 7),               
                InspEffect("Moxie", 5, 5),          
                InspEffect("Knowledge Type", 5, 5)]                     
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                7,    
                "Noted Expert's a Friend",          
                "Knowledge", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),           
                InspEffect("Language", 7, 7),          
                InspEffect("Knowledge Type", 8, 8),           
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                8,
                "Mom and Dad's Research",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),        
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Occult Lore", 7, 7),
                InspEffect("Problem Solving", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                9,
                "Notes Close at Hand",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 8, 8),
                InspEffect("Language", 7, 7),
                InspEffect("Knowledge Type", 10, 10),
                InspEffect("Repair", 7, 7)]     
            ))
            
            self.addInspire(Inspirations(
                "Knowledge",
                10,
                "Mind Like a Trap",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 10, 10),   
                InspEffect("Cryptography", 8, 8), 
                InspEffect("Language", 7, 7),
                InspEffect("Repair", 7, 7),
                InspEffect("Deduction", 1, 25)]
            ))
            
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Problem Solving",
                0,
                "Gut Check",
                "Knowledge",
                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 4, 4),
                InspEffect("Resolve", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                1,
                "A Coin to Flip",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                2,
                "Helpful Insight",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 4, 4),               
                InspEffect("Repair", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                3,                
                "Radio Drama Precedent",               
                "Knowledge", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 6, 6),                
                InspEffect("Knowledge Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                4,
                "Hare-Brained Scheme",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),       
                InspEffect("Deception", 5, 5),  
                InspEffect("Moxie", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                5,
                "Relevant to Hobbies",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Magic Tricks", 6, 6),
                InspEffect("Cryptography", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                6,
                "Scheherazade's Plan 27",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),            
                InspEffect("Escape Artistry", 7, 7),               
                InspEffect("Deception", 6, 6),          
                InspEffect("Poise", 4, 4)]                
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                7,    
                "Reckless Experimentation",          
                "Knowledge", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),           
                InspEffect("Courage", 7, 7),          
                InspEffect("Deduction", 7, 7),           
                InspEffect("Moxie", 6, 6)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                8,
                "Lucky Break",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),        
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Escape Artistry", 7, 7),
                InspEffect("Repair", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                9,
                "Astonishing Foresight",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 8, 8),
                InspEffect("Knowledge Type", 10, 10),
                InspEffect("Language", 7, 7),
                InspEffect("Magic Tricks", 7, 7)] 
            ))
            
            self.addInspire(Inspirations(
                "Problem Solving",
                10,
                "Bolt from the Blue",
                "Knowledge", 

                [InspEffect("Problem Solving", 10, 10),   
                InspEffect("Deduction", 9, 9), 
                InspEffect("Awareness", 7, 7),
                InspEffect("Cryptography", 7, 7),
                InspEffect("General", 50, 50)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Language",
                0,
                "Good Ear",
                "Knowledge",
                [InspEffect("General", 50, 50),
                InspEffect("Language", 4, 4),
                InspEffect("Listen", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                1,
                "That Sounds Familiar",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                2,
                "Did Some Reading Earlier",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 5, 5),         
                InspEffect("Knowledge Type", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                3,                
                "Handy Phrase Book",               
                "Knowledge", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Language", 6, 6),                
                InspEffect("Diplomacy", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                4,
                "Know a Native Speaker",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 6, 6),       
                InspEffect("Listen", 5, 5),  
                InspEffect("Awareness", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Language",
                5,
                "Took a Semester",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 7, 7),
                InspEffect("Awareness", 5, 5),
                InspEffect("Negotiation", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                6,
                "Learning as You Go",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 7, 7),            
                InspEffect("Deduction", 6, 6),               
                InspEffect("Awareness", 5, 5),          
                InspEffect("Cryptography", 3, 3)]              
            ))
            
            self.addInspire(Inspirations(
                "Language",
                7,    
                "Linguistic Insight",          
                "Knowledge", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Language", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Awareness", 5, 5),           
                InspEffect("Diplomacy", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                8,
                "Travel Dictionary",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 7, 7),        
                InspEffect("Problem Solving", 7, 7),       
                InspEffect("Negotiation", 7, 7),
                InspEffect("Awareness", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Language",
                9,
                "Heard That Before",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 8, 8),
                InspEffect("Deduction", 7, 7),
                InspEffect("Listen", 7, 7),
                InspEffect("Awareness", 6, 6)] 
            ))
            
            self.addInspire(Inspirations(
                "Language",
                10,
                "Extensive Study",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 10, 10),   
                InspEffect("Listen", 8, 8), 
                InspEffect("Cryptography", 7, 7),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Knowledge Type", 10, 10)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Cryptography",
                0,
                "Mind for Puzzles",
                "Knowledge",
                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 4, 4),
                InspEffect("Problem Solving", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                1,
                "Lots of Scratch Paper",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                2,
                "Surprisingly Simple Pattern",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 5, 5),               
                InspEffect("Deduction", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                3,                
                "Flash of Cryptographic Inspiration",           
                "Knowledge", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 6, 6),                
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                4,
                "Partial Clue",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 6, 6),       
                InspEffect("Deduction", 6, 6),  
                InspEffect("Perception", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                5,
                "New System to Try",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),
                InspEffect("Problem Solving", 6, 6),
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                6,
                "Familiar Sequence",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),            
                InspEffect("Deduction", 7, 7),               
                InspEffect("Knowledge Type", 5, 5),          
                InspEffect("Occult Lore", 3, 3)]                   
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                7,    
                "Zimmerman Telegram Story",    
                "Knowledge", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Deduction", 6, 6),           
                InspEffect("Knowledge Type", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                8,
                "Student of Al-Kindi",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 1, 25),        
                InspEffect("Language", 7, 7),       
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Deduction", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                9,
                "Stories from Room 40",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 8, 8),
                InspEffect("Resolve", 7, 7),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Knowledge Type", 10, 10)]  
            ))
            
            self.addInspire(Inspirations(
                "Cryptography",
                10,
                "The Key",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 10, 10),   
                InspEffect("Deduction", 8, 8), 
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Occult Lore", 7, 7),
                InspEffect("Language", 1, 25)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Repair",
                0,
                "Can't Get Much Worse",
                "Knowledge",
                [InspEffect("General", 50, 50),
                InspEffect("Repair", 4, 4),
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                1,
                "Simple Machine",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                2,
                "Leverage",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 4, 4),               
                InspEffect("Strength", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                3,                
                "Steady Hands",               
                "Knowledge", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Repair", 6, 6),                
                InspEffect("Grace", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                4,
                "Easy Access",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 7, 7),       
                InspEffect("Perception", 5, 5),  
                InspEffect("Deduction", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                5,
                "Good Wrench",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 7, 7),
                InspEffect("Fisticuffs", 6, 6),
                InspEffect("Strength", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                6,
                "Mechanical Insight",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 7, 7),            
                InspEffect("Deduction", 7, 7),               
                InspEffect("Knowledge Type", 5, 5),          
                InspEffect("Problem Solving", 3, 3)]                    
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                7,    
                "Confusing Diagram",          
                "Knowledge", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Repair", 1, 20),           
                InspEffect("Problem Solving", 1, 15),          
                InspEffect("Language", 5, 5),           
                InspEffect("Cryptography", 5, 5)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                8,
                "You've Seen This Before",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 1, 25),        
                InspEffect("Poise", 7, 7),       
                InspEffect("Deduction", 7, 7),
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                9,
                "Clean Diagram",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 9, 9),
                InspEffect("Knowledge Type", 10, 10),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Escape Artistry", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Repair",
                10,
                "Every Tool You Need",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 10, 10),   
                InspEffect("Escape Artistry", 8, 8), 
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Magic Tricks", 7, 7),
                InspEffect("Climbing", 6, 6)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Deduction",
                0,
                "Wild Hunch",
                "Knowledge",
                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 4, 4),
                InspEffect("Escape Artistry", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                1,
                "Something's out of Place",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                2,
                "Channel Sherlock Holmes",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 4, 4),               
                InspEffect("Knowledge Type", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                3,                
                "Inquisitive Nature",               
                "Knowledge", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 5, 5),                
                InspEffect("Occult Lore", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                4,
                "Uncontaminated Scene",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 6, 6),       
                InspEffect("Perception", 5, 5),  
                InspEffect("Awareness", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                5,
                "Student of Human Nature",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 7, 7),
                InspEffect("Empathy", 5, 5),
                InspEffect("Knowledge Type", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                6,
                "Knack for Visualization",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 7, 7),            
                InspEffect("Perception", 6, 6),               
                InspEffect("Repair", 5, 5),          
                InspEffect("Problem Solving", 3, 3)]                    
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                7,    
                "Gift for Puzzle-Solving",          
                "Knowledge", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Knowledge Type", 9, 9),           
                InspEffect("Cryptography", 5, 5)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                8,
                "Major Clue",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 7, 7),        
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Awareness", 7, 7),
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                9,
                "The Impossible Is Eliminated",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 8, 8),
                InspEffect("Cryptography", 7, 7),
                InspEffect("Problem solving", 7, 7),
                InspEffect("Poker", 7, 7)]   
            ))
            
            self.addInspire(Inspirations(
                "Deduction",
                10,
                "Keen Deductive Powers",
                "Knowledge", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 10, 10),   
                InspEffect("Knowledge Type", 12, 12), 
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Cryptography", 7, 7),
                InspEffect("Escape Artistry", 6, 6)]
            ))
            
            
            
            
            
            self.addInspire(Inspirations(
                "Listen",
                0,
                "Hard to Tune Out",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Listen", 4, 4),
                InspEffect("Perception", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                1,
                "Faint Curiosity",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 5, 5)]    
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                2,
                "Tantalizing Murmur",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 4, 4),               
                InspEffect("Courage", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                3,                
                "Unsettling Groan",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Listen", 6, 6),                
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                4,
                "Significant Sigh",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 7, 7),       
                InspEffect("Empathy", 5, 5),  
                InspEffect("Awareness", 3, 3)] 
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                5,
                "Catch of Breath",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 7, 7),
                InspEffect("Awareness", 6, 6),
                InspEffect("Dodge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                6,
                "Sincere Interest",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 7, 7),            
                InspEffect("Empathy", 7, 7),               
                InspEffect("Diplomacy", 5, 5),          
                InspEffect("Relationship Type", 5, 5)]                     
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                7,    
                "Meaningful Pause",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Listen", 1, 20),           
                InspEffect("Flirting", 7, 7),          
                InspEffect("Deduction", 7, 7),           
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                8,
                "Threatening Rumble",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 1, 25),        
                InspEffect("Dodge", 7, 7),       
                InspEffect("Climbing", 7, 7),
                InspEffect("Leaping", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                9,
                "Portentous Silence",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 8, 8),
                InspEffect("Perception", 7, 7),
                InspEffect("Awareness", 7, 7),
                InspEffect("Stealth", 7, 7)]  
            ))
            
            self.addInspire(Inspirations(
                "Listen",
                10,
                "Ears of a Bat",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 10, 10),   
                InspEffect("Awareness", 8, 8), 
                InspEffect("Perception", 7, 7),
                InspEffect("Language", 7, 7),
                InspEffect("Relationship Type", 10, 10)]
            ))
            
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Empathy",
                0,
                "A Good Heart",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 4, 4),
                InspEffect("Diplomacy", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                1,
                "Twinge of Concern",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                2,
                "Wouldn't Want to Be Him",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 4, 4),               
                InspEffect("Stealth", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                3,                
                "That Could Be You",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 6, 6),                
                InspEffect("Deduction", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                4,
                "Trying to See Good",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 6, 6),       
                InspEffect("Tolerance", 5, 5),  
                InspEffect("Patience", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                5,
                "Feeling Your Pain",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 7, 7),
                InspEffect("Diplomacy", 5, 5),
                InspEffect("Self Knowledge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                6,
                "We've All Been There",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 7, 7),            
                InspEffect("Self Knowledge", 7, 7),               
                InspEffect("Negotiation", 5, 5),          
                InspEffect("Relationship Type", 7, 7)]                  
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                7,    
                "Fellow Feeling",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 1, 20),           
                InspEffect("Conscience", 7, 7),          
                InspEffect("Listen", 6, 6),           
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                8,
                "Brotherly Love",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 7, 7),        
                InspEffect("Tolerance", 1, 20),       
                InspEffect("Conscience", 7, 7),
                InspEffect("Listen", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                9,
                "An Abiding Bond",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 1, 30),
                InspEffect("Courage", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("Relationship Type", 10, 10)]   
            ))
            
            self.addInspire(Inspirations(
                "Empathy",
                10,
                "Some Kinda Saint",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 10, 10),   
                InspEffect("Tolerance", 1, 30), 
                InspEffect("Hope", 7, 7),
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Diplomacy", 7, 7)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                0,
                "Honesty's Its Own Reward", 
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 4, 4),
                InspEffect("Tolerance", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                1,
                "Always Been This Way",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                2,
                "Pavlovian Response Index",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 4, 4),               
                InspEffect("Awareness", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                3,                
                "Questioning Mood",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 6, 6),                
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                4,
                "Tickled by Doubt",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 6, 6),       
                InspEffect("Conscience", 5, 5),  
                InspEffect("Awareness", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                5,
                "Moment of Introspection",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 7, 7),
                InspEffect("Poise", 6, 6),
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                6,
                "Family Trait",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 1, 15),            
                InspEffect("Resolve", 6, 6),               
                InspEffect("Courage", 5, 5),          
                InspEffect("Moxie", 3, 3)]                   
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                7,    
                "Quirk of Your Upbringing",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 1, 20),           
                InspEffect("Moxie", 7, 7),          
                InspEffect("Deduction", 5, 5),           
                InspEffect("Magic Tricks", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                8,
                "What Jung Said",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 7, 7),        
                InspEffect("Occult Lore", 1, 20),       
                InspEffect("Empathy", 6, 6),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                9,
                "Rare Epiphany",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 8, 8),
                InspEffect("Deduction", 7, 7),
                InspEffect("Awareness", 7, 7),
                InspEffect("Relationship Type", 10, 10)]     
            ))
            
            self.addInspire(Inspirations(
                "Self Knowledge",
                10,
                "True to Yourself",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 10, 10),   
                InspEffect("Moxie", 8, 8), 
                InspEffect("Magic Tricks", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("Courage", 1, 20)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Tolerance",
                0,
                "Protective Veil of Obliviousness", 
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 4, 4),
                InspEffect("Poise", 4, 4)]
                ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                1,
                "Just Hold It In",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                2,
                "No Time for Outrage",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 5, 5),               
                InspEffect("Patience", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                3,                
                "Nobody's Business",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 5, 5),                
                InspEffect("Resolve", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                4,
                "Grit Teeth, Hold Nose",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 1, 15),       
                InspEffect("Resolve", 5, 5),  
                InspEffect("Courage", 3, 3)] 
                            
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                5,
                "Not One to Judge",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 7, 7),
                InspEffect("Self Knowledge", 6, 6),
                InspEffect("Conscience", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                6,
                "Got a Job to Do",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 7, 7),            
                InspEffect("Resolve", 7, 7),               
                InspEffect("Awareness", 5, 5),          
                InspEffect("Poise", 3, 3)]               
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                7,    
                "Seen Worse",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 1, 20),           
                InspEffect("Diplomacy", 7, 7),          
                InspEffect("Self Knowledge", 7, 7),           
                InspEffect("Relationship Type", 7, 7)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                8,
                "Not So Bad",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 1, 25),        
                InspEffect("Diplomacy", 7, 7),       
                InspEffect("Empathy", 7, 7),
                InspEffect("Hope", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                9,
                "Actually Kinda Interesting",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 9, 9),
                InspEffect("Perception", 7, 7),
                InspEffect("Relationship Type", 10, 10),
                InspEffect("Courage", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Tolerance",
                10,
                "A Learning Experience",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 10, 10),   
                InspEffect("Self Knowledge", 1, 25), 
                InspEffect("Awareness", 7, 7),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Deduction", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Poise",
                0,
                "Unusual Childhood",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),
                InspEffect("Dodge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                1,
                "Hard to Rattle",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                2,
                "Extra Coffee",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),               
                InspEffect("Resolve", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                3,                
                "Dancer's Posture",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 6, 6),                
                InspEffect("Grace", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                4,
                "Ready for Anything",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 1, 15),       
                InspEffect("Resolve", 5, 5),  
                InspEffect("Problem Solving", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                5,
                "Confident Smile",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 7, 7),
                InspEffect("Negotiation", 6, 6),
                InspEffect("Diplomacy", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                6,
                "Unshakable Nerves",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 7, 7),            
                InspEffect("Courage", 7, 7),               
                InspEffect("Fisticuffs", 5, 5),          
                InspEffect("Poker", 4, 4)]                  
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                7,    
                "Nepalese Breathing Exercises",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 1, 20),           
                InspEffect("Patience", 7, 7),          
                InspEffect("Awareness", 7, 7),           
                InspEffect("Climbing", 5, 5)]            
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                8,
                "Keating Pride",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 1, 25),        
                InspEffect("Moxie", 7, 7),       
                InspEffect("Resolve", 7, 7),
                InspEffect("Courage", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                9,
                "Aristocratic Bearing",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 8, 8),
                InspEffect("Diplomacy", 7, 7),
                InspEffect("Deception", 7, 7),
                InspEffect("Negotiation", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Poise",
                10,
                "Preternatural Calm",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 10, 10),   
                InspEffect("Awareness", 8, 8), 
                InspEffect("Poker", 7, 7),
                InspEffect("Patience", 7, 7),
                InspEffect("Climbing", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                0,
                "The Past Is Close",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 4, 4),
                InspEffect("Conscience", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                1,
                "Nagging Voice of Caution", 
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                2,
                "Attendance to Duty",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 4, 4),               
                InspEffect("Conscience", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                3,                
                "Princely Rectitude",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 6, 6),                
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                4,
                "Whispers of the Past",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 7, 7),       
                InspEffect("Problem Solving", 5, 5),  
                InspEffect("Listen", 4, 4)] 
                            
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                5,
                "Kheper's Leash",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Language", 7, 7),
                InspEffect("Courage", 6, 6),
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                6,
                "Unhesitating Backup",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),            
                InspEffect("Poise", 7, 7),               
                InspEffect("Resolve", 5, 5),          
                InspEffect("Relationship Type", 7, 7)]                    
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                7,    
                "Magical Thinking",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 1, 20),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Awareness", 7, 7),           
                InspEffect("Self Knowledge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                8,
                "Distant Perspective",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 7, 7),        
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Conscience", 7, 7),
                InspEffect("Resolve", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                9,
                "Royal Counsel",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 9, 9),
                InspEffect("Self Knowledge", 7, 7),
                InspEffect("Relationship Type", 10, 10),
                InspEffect("Deduction", 7, 7)]   
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Ahmose",
                10,
                "Eternal Friendship",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Hope", 10, 10),   
                InspEffect("Resolve", 8, 8), 
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Diplomacy", 7, 7),
                InspEffect("Self Knowledge", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                0,
                "Classroom Give and Take",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 4, 4),
                InspEffect("Diplomacy", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                1,
                "On Alert",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                2,
                "Diplomatic Entreaty",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 4, 4),               
                InspEffect("Awareness", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                3,                
                "Extra Eyes in the Field",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Perception", 6, 6),                
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                4,
                "Enthusiastic Talker",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Language", 5, 5),  
                InspEffect("Listen", 4, 4)]   
                            
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                5,
                "Handy Resource",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Language", 7, 7),
                InspEffect("Occult Lore", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                6,
                "Courage in Impossible Moments", 
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),            
                InspEffect("Resolve", 7, 7),               
                InspEffect("Problem Solving", 1, 15),          
                InspEffect("Relationship Type", 6, 6)]                  
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                7,    
                "Respect of a Peer",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 7, 7),           
                InspEffect("Resolve", 7, 7),          
                InspEffect("Diplomacy", 7, 7),           
                InspEffect("Flirting", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                8,
                "Deep Conversation",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Listen", 7, 7),        
                InspEffect("Occult Lore", 7, 7),       
                InspEffect("Relationship Type", 9, 9),
                InspEffect("Flirting", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                9,
                "Efficient Collaboration",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 9, 9),
                InspEffect("Perception", 7, 7),
                InspEffect("Deduction", 7, 7),
                InspEffect("Cryptography", 7, 7)]      
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Nigel",
                10,
                "Professional Partnership",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 10, 10),   
                InspEffect("Problem Solving", 8, 8), 
                InspEffect("Diplomacy", 7, 7),
                InspEffect("Language", 5, 5),
                InspEffect("Relationship Type", 12, 12)]
            ))
            
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                0,
                "A Friendly Face",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 4, 4),
                InspEffect("Charm Type", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                1,
                "Fixer-Upper",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                2,
                "Gentle Soul",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Conscience", 4, 4),
                InspEffect("Listen", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                3,                
                "Stealth Tickle",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 5, 5),                
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                4,
                "Steady Hands",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 6, 6),       
                InspEffect("Repair", 5, 5),  
                InspEffect("Grace", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                5,
                "Steadfast Support",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 7, 7),
                InspEffect("Courage", 5, 5),
                InspEffect("Relationship Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                6,
                "Mechanical Marvel",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Repair", 7, 7),            
                InspEffect("Problem Solving", 7, 7),               
                InspEffect("Deduction", 5, 5),          
                InspEffect("Moxie", 5, 5)]                
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                7,    
                "Steady at the Wheel",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 7, 7),           
                InspEffect("Grace", 7, 7),          
                InspEffect("Courage", 7, 7),           
                InspEffect("Dodge", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                8,
                "Good Nature",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),        
                InspEffect("Relationship Type", 9, 9),       
                InspEffect("Flirting", 7, 7),
                InspEffect("Empathy", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                9,
                "Right Good Laugh",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 9, 9),
                InspEffect("Flirting", 7, 7),
                InspEffect("Magic Tricks", 7, 7),
                InspEffect("Relationship Type", 10, 10)]  
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Felix",
                10,
                "Indispensable Partnership",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 10, 10),   
                InspEffect("Problem Solving", 7, 7), 
                InspEffect("Hope", 7, 7),
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Empathy", 5, 5)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                0,
                "Intrigue",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),
                InspEffect("Tolerance", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                1,
                "Interesting Story",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                2,
                "Smooth under Fire",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 4, 4),               
                InspEffect("Dodge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                3,                
                "Stirred, not Shaken",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),                
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                4,
                "Clever Lies Are Fun",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),       
                InspEffect("Listen", 5, 5),  
                InspEffect("Deception", 3, 3)]  
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                5,
                "Dangerous Dance",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),
                InspEffect("Courage", 6, 6),
                InspEffect("Fisticuffs", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                6,
                "Verbal Jousting",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),            
                InspEffect("Negotiation", 7, 7),               
                InspEffect("Moxie", 5, 5),          
                InspEffect("Relationship Type", 6, 6)]           
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                7,    
                "The Art of Misleading",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Deception", 7, 7),           
                InspEffect("Moxie", 7, 7),          
                InspEffect("Magic Tricks", 7, 7),           
                InspEffect("Stealth", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                8,
                "Two Steps Ahead",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),        
                InspEffect("Moxie", 7, 7),       
                InspEffect("Dodge", 7, 7),
                InspEffect("Relationship Type", 8, 8)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                9,
                "English Steel",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 9, 9),
                InspEffect("Diplomacy", 7, 7),
                InspEffect("Courage", 7, 7),
                InspEffect("Fisticuffs", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Roland",
                10,
                "Partners in Shadows",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 10, 10),   
                InspEffect("Stealth", 8, 8), 
                InspEffect("Deception", 7, 7),
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Cryptography", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                0,
                "The Big Tease",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 4, 4),
                InspEffect("Courage", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                1,
                "Competitive Spur",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                2,
                "Ready Wit",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 5, 5),               
                InspEffect("Flirting", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                3,                
                "Fast on His Feet",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 6, 6),                
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                4,
                "Brave unto Madness",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),       
                InspEffect("Resolve", 5, 5),  
                InspEffect("Fisticuffs", 3, 3)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                5,
                "Hint of Vulnerability",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 7, 7),
                InspEffect("Relationship Type", 6, 6),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                6,
                "Plan Later, Act Now",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),            
                InspEffect("Courage", 7, 7),               
                InspEffect("Leaping", 5, 5),          
                InspEffect("Dodge", 3, 3)]                 
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                7,    
                "Discerning Eye",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Perception", 7, 7),           
                InspEffect("Deduction", 7, 7),          
                InspEffect("Awareness", 7, 7),           
                InspEffect("Hope", 5, 5)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                8,
                "Trickster's Humor",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Flirting", 7, 7),        
                InspEffect("Moxie", 7, 7),       
                InspEffect("Courage", 7, 7),
                InspEffect("Relationship Type", 9, 9)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                9,
                "Madman's Luck",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 9, 9),
                InspEffect("Courage", 7, 7),
                InspEffect("Moxie", 7, 7),
                InspEffect("General", 50, 50)]    
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Sterling",
                10,
                "Exhilarating Partnership",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 10, 10),   
                InspEffect("Courage", 8, 8), 
                InspEffect("Flirting", 7, 7),
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Dodge", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                0,
                "Bedrock of the Family",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 4, 4),
                InspEffect("Conscience", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                1,
                "Well-Timed Nag",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                2,
                "Curious Eccentricity",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 4, 4),               
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                3,                
                "Word of Encouragement",               
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 6, 6),                
                InspEffect("Courage", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                4,
                "Tie to the Past",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 7, 7),       
                InspEffect("Poise", 5, 5),  
                InspEffect("Relationship Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                5,
                "Worldly Insight",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Tolerance", 7, 7),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                6,
                "Life-Long Support",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Relationship Type", 7, 7),            
                InspEffect("Self Knowledge", 7, 7),               
                InspEffect("Empathy", 5, 5),          
                InspEffect("Hope", 5, 5)]                 
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                7,    
                "Joie de Vivre",          
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Hope", 7, 7),           
                InspEffect("Moxie", 7, 7),          
                InspEffect("Grace", 7, 7),           
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                8,
                "Unique Insight",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 1, 25),        
                InspEffect("Cryptography", 7, 7),       
                InspEffect("Deduction", 7, 7),
                InspEffect("Awareness", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                9,
                "Own Personal Anchor",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Resolve", 9, 9),
                InspEffect("Courage", 7, 7),
                InspEffect("Moxie", 7, 7),
                InspEffect("Relationship Type", 10, 10)]    
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Aunt Evelyn",
                10,
                "Unconditional Love",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Empathy", 10, 10),   
                InspEffect("Self Knowledge", 8, 8), 
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Courage", 7, 7),
                InspEffect("Patience", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                0,
                "Friends Forever",
                "Relationship",
                [InspEffect("General", 50, 50),
                InspEffect("Listen", 4, 4),
                InspEffect("Patience", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                1,
                "Onto Your Tricks",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Relationship Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                2,
                "'I Think You're Overreacting'",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Patience", 4, 4),
                InspEffect("Tolerance", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                3,                
                "Remembering What You Forget",           
                "Relationship", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 6, 6),                
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                4,
                "Good Conversation",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Diplomacy", 7, 7),       
                InspEffect("Relationship Type", 5, 5),  
                InspEffect("Hope", 5, 5)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                5,
                "Good Instincts",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 7, 7),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Cryptography", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                6,
                "Outside Perspective",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 7, 7),            
                InspEffect("Resolve", 7, 7),               
                InspEffect("Awareness", 6, 6),          
                InspEffect("Hope", 3, 3)]                
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                7,    
                "You Can Count On Me",   
                "Relationship", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Self Knowledge", 7, 7),           
                InspEffect("Resolve", 7, 7),          
                InspEffect("Empathy", 7, 7),           
                InspEffect("Relationship Type", 7, 7)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                8,
                "Braver Than You'd Think",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 7, 7),        
                InspEffect("Resolve", 7, 7),       
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Poise", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                9,
                "Trusted Advice",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 8, 8),
                InspEffect("Conscience", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("Hope", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Relationship with Anna",
                10,
                "Faithful Friend",
                "Relationship", 

                [InspEffect("General", 50, 50),
                InspEffect("Courage", 10, 10),   
                InspEffect("Diplomacy", 8, 8), 
                InspEffect("Resolve", 7, 7),
                InspEffect("Relationship Type", 12, 12),
                InspEffect("Problem Solving", 5, 5)]
            ))
            
            
            
            
            
            self.addInspire(Inspirations(
                "Stress",
                0,
                "High Tolerance for Stress",
                "Stress",
                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 4, 4),
                InspEffect("Stress Type", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                1,
                "Constructive Twitchiness",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                2,
                "Startled into Action",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 4, 4),               
                InspEffect("Leaping", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                3,                
                "Time to Double-Check",               
                "Stress", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 6, 6),                
                InspEffect("Deduction", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                4,
                "Friends Close, Enemies Closer",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),       
                InspEffect("Awareness", 5, 5),  
                InspEffect("Stress Type", 5, 5)] 
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                5,
                "Hyper-Alert",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),
                InspEffect("Dodge", 6, 6),
                InspEffect("Escape Artistry", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                6,
                "Keep It Steady",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 7, 7),            
                InspEffect("Poise", 7, 7),               
                InspEffect("Dodge", 5, 5),          
                InspEffect("Grace", 3, 3)]                   
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                7,    
                "The Going Gets Tough",          
                "Stress", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),           
                InspEffect("Stress Type", 8, 8),          
                InspEffect("Fisticuffs", 7, 7),           
                InspEffect("Escape Artistry", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                8,
                "Nerves of Steel",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Stress Type", 10, 10),        
                InspEffect("Courage", 7, 7),       
                InspEffect("Escape Artistry", 7, 7),
                InspEffect("Poise", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                9,
                "Utterly Unflappable",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Poise", 9, 9),
                InspEffect("Stress Type", 11, 11),
                InspEffect("Moxie", 7, 7),
                InspEffect("Resolve", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Stress",
                10,
                "Driven to Succeed",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 10, 10),   
                InspEffect("Resolve", 1, 25), 
                InspEffect("Courage", 7, 7),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Fisticuffs", 5, 5)]
            ))
            
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Awareness",
                0,
                "Generally Paying Attention",
                "Stress",
                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 4, 4),
                InspEffect("Listen", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                1,
                "A Strange Movement",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                2,
                "Fleeting Glimpse",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 4, 4),               
                InspEffect("Perception", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                3,                
                "Telling Facial Tick",               
                "Stress", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Poker", 7, 7),                
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                4,
                "Subtle Sign",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),       
                InspEffect("Diplomacy", 5, 5),  
                InspEffect("Negotiation", 3, 3)]  
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                5,
                "Significant Mannerism",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),
                InspEffect("Negotiation", 6, 6),
                InspEffect("Poker", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                6,
                "Pattern of Activity",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),            
                InspEffect("Deduction", 7, 7),               
                InspEffect("Diplomacy", 5, 5),          
                InspEffect("Empathy", 4, 4)]                   
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                7,    
                "Looking for Something Specific",        
                "Stress", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 1, 20),           
                InspEffect("Perception", 7, 7),          
                InspEffect("Deduction", 7, 7),           
                InspEffect("Problem Solving", 5, 5)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                8,
                "Giveaway",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 7, 7),        
                InspEffect("Poker", 7, 7),       
                InspEffect("Negotiation", 7, 7),
                InspEffect("Deduction", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                9,
                "Eye for Detail",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 9, 9),
                InspEffect("Perception", 7, 7),
                InspEffect("Deduction", 7, 7),
                InspEffect("Diplomacy", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Awareness",
                10,
                "Total Awareness",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Awareness", 10, 10),   
                InspEffect("Stress Type", 12, 12), 
                InspEffect("Negotiation", 7, 7),
                InspEffect("Empathy", 7, 7),
                InspEffect("Deduction", 1, 15)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                0,
                "Wild Flailing",
                "Stress",
                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 4, 4),
                InspEffect("Strength", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                1,
                "Underestimated",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                2,
                "Quick Kick",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 4, 4),               
                InspEffect("Dodge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                3,                
                "'But I'm a Girl!'",               
                "Stress", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 6, 6),                
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                4,
                "First Punch",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 6, 6),       
                InspEffect("Moxie", 5, 5),  
                InspEffect("Negotiation", 3, 3)]  
                            
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                5,
                "Light on Your Feet",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 7, 7),
                InspEffect("Dodge", 7, 7),
                InspEffect("Grace", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                6,
                "Fearless in the Ring",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 1, 15),            
                InspEffect("Courage", 7, 7),               
                InspEffect("Strength", 5, 5),          
                InspEffect("Moxie", 5, 5)]               
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                7,    
                "Strong Left Hook",          
                "Stress", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 7, 7),           
                InspEffect("Stress Type", 7, 7),          
                InspEffect("Strength", 5, 5),           
                InspEffect("Courage", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                8,
                "Terrifying Glare",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 1, 25),        
                InspEffect("Moxie", 7, 7),       
                InspEffect("Negotiation", 7, 7),
                InspEffect("Diplomacy", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                9,
                "He's Wide Open!",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 9, 9),
                InspEffect("Courage", 7, 7),
                InspEffect("Moxie", 7, 7),
                InspEffect("Resolve", 7, 7)]  
            ))
            
            self.addInspire(Inspirations(
                "Fisticuffs",
                10,
                "Artist of Pugilism",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Fisticuffs", 10, 10),   
                InspEffect("Dodge", 8, 8), 
                InspEffect("Grace", 7, 7),
                InspEffect("Strength", 7, 7),
                InspEffect("Courage", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Moxie",
                0,
                "Policy of Shamelessness",
                "Stress",
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 4, 4),
                InspEffect("Deception", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                1,
                "Kid's Got Spunk",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                2,
                "Nothin' to Lose",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 5, 5),               
                InspEffect("Resolve", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                3,                
                "Sensing Some Give",               
                "Stress", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 6, 6),                
                InspEffect("Negotiation", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                4,
                "Boo to Common Sense!",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 6, 6),       
                InspEffect("Courage", 5, 5),  
                InspEffect("Stress Type", 5, 5)]
                            
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                5,
                "'Hmph!' of the Ages",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),
                InspEffect("Resolve", 7, 7),
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                6,
                "Pure Relentlessness",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 1, 15),            
                InspEffect("Resolve", 7, 7),               
                InspEffect("Problem Solving", 5, 5),          
                InspEffect("Escape Artistry", 3, 3)]                    
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                7,    
                "Fast Talking",          
                "Stress", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),           
                InspEffect("Deception", 7, 7),          
                InspEffect("Negotiation", 6, 6),           
                InspEffect("Diplomacy", 5, 5)]               
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                8,
                "Not Beaten Yet",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 7, 7),        
                InspEffect("Resolve", 1, 20),       
                InspEffect("Courage", 7, 7),
                InspEffect("Escape Artistry", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                9,
                "Master-Class Lip",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 8, 8),
                InspEffect("Negotiation", 7, 7),
                InspEffect("Poker", 7, 7),
                InspEffect("Fisticuffs", 7, 7)]   
            ))
            
            self.addInspire(Inspirations(
                "Moxie",
                10,
                "No Taking No",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Moxie", 10, 10),   
                InspEffect("Courage", 9, 9), 
                InspEffect("Resolve", 7, 7),
                InspEffect("Stress Type", 12, 12),
                InspEffect("Escape Artistry", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Dodge",
                0,
                "Natural Twitchiness",
                "Stress",
                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 4, 4),
                InspEffect("Leaping", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                1,
                "Well-Timed Goosebumps",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                2,
                "Lucky Stumble",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 4, 4),               
                InspEffect("Climbing", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                3,                
                "Close to the Ground",    
                "Stress", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 6, 6),                
                InspEffect("Stealth", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                4,
                "Dive!",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 7, 7),       
                InspEffect("Leaping", 5, 5),  
                InspEffect("Escape Artistry", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                5,
                "Burst of Speed",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 7, 7),
                InspEffect("Leaping", 6, 6),
                InspEffect("Grace", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                6,
                "Handy Distraction",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 7, 7),            
                InspEffect("Stealth", 7, 7),               
                InspEffect("Escape Artistry", 5, 5),          
                InspEffect("Deception", 3, 3)]                      
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                7,    
                "Feint and Sidestep",          
                "Stress", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 1, 20),           
                InspEffect("Fisticuffs", 7, 7),          
                InspEffect("Grace", 5, 5),           
                InspEffect("Stealth", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                8,
                "Saw It Coming",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 8, 8),        
                InspEffect("Awareness", 7, 7),       
                InspEffect("Grace", 7, 7),
                InspEffect("Moxie", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                9,
                "Advanced Evasive Tactics",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 8, 8),
                InspEffect("Stealth", 7, 7),
                InspEffect("Leaping", 7, 7),
                InspEffect("Climbing", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Dodge",
                10,
                "Uncanny Quickness",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Dodge", 10, 10),   
                InspEffect("Awareness", 8, 8), 
                InspEffect("Stress Type", 12, 12),
                InspEffect("Poise", 7, 7),
                InspEffect("Fisticuffs", 6, 6)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                0,
                "Flexibility",
                "Stress",
                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 4, 4),
                InspEffect("Grace", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                1,
                "Dumb Luck",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                2,
                "Naturally Wriggly",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 4, 4),               
                InspEffect("Dodge", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                3,                
                "Deft Fingers",               
                "Stress", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 6, 6),                
                InspEffect("Repair", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                4,
                "Calmness in Tight Quarters",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 6, 6),       
                InspEffect("Poise", 5, 5),  
                InspEffect("Courage", 3, 3)] 
                            
            ))
            self.addInspire(Inspirations(
                "Escape Artistry",
                5,
                "Saw Hardeen's Act",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 7, 7),
                InspEffect("Awareness", 6, 6),
                InspEffect("Grace", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                6,
                "Room to Move",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 1, 15),            
                InspEffect("Grace", 7, 7),               
                InspEffect("Dodge", 5, 5),          
                InspEffect("Stress Type", 6, 6)]                   
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                7,    
                "Insight into the Trick",          
                "Stress", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Deduction", 7, 7),           
                InspEffect("Magic Tricks", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                8,
                "Student of Masters",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 1, 25),        
                InspEffect("Grace", 7, 7),       
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Magic Tricks", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                9,
                "Hidden Tools",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 9, 9),
                InspEffect("Stress Type", 10, 10),
                InspEffect("Magic Tricks", 7, 7),
                InspEffect("Repair", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Escape Artistry",
                10,
                "Escapologist",
                "Stress", 

                [InspEffect("General", 50, 50),
                InspEffect("Escape Artistry", 10, 10),   
                InspEffect("Magic Tricks", 8, 8), 
                InspEffect("Climbing", 7, 7),
                InspEffect("Grace", 7, 7),
                InspEffect("Strength", 5, 5)]
            ))
            
            
            
            
            self.addInspire(Inspirations(
                "Wits",
                0,
                "Natural Trickiness",
                "Wits",
                [InspEffect("General", 50, 50),
                InspEffect("Wits Type", 3, 3),
                InspEffect("Problem Solving", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                1,
                "Glimmer of Understanding",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Wits Type", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                2,
                "'I See the Trick!'",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 4, 4),               
                InspEffect("Magic Tricks", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                3,                
                "Low Cunning",               
                "Wits", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Problem Solving", 6, 6),                
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                4,
                "Quick on the Draw",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 7, 7),       
                InspEffect("Dodge", 5, 5),  
                InspEffect("Fisticuffs", 3, 3)]   
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                5,
                "New York's Early Lessons",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 7, 7),
                InspEffect("Moxie", 6, 6),
                InspEffect("Stealth", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                6,
                "Well Prepared",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 7, 7),            
                InspEffect("Wits Type", 7, 7),               
                InspEffect("Escape Artistry", 5, 5),          
                InspEffect("Repair", 3, 3)]                      
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                7,    
                "Tipped Off",          
                "Wits", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 7, 7),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Awareness", 7, 7),           
                InspEffect("Perception", 5, 5)]
                                           
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                8,
                "Student of the Unexpected",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 7, 7),        
                InspEffect("Occult Lore", 7, 7),       
                InspEffect("Dodge", 7, 7),
                InspEffect("Deduction", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Wits",
                9,
                "Lightning-Fast Mind",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Deduction", 8, 8),
                InspEffect("Problem Solving", 7, 7),
                InspEffect("Awareness", 7, 7),
                InspEffect("Wits Type", 10, 10)]      
            ))
            
            self.addInspire(Inspirations(      
                "Wits",
                10,
                "Trickster",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 10, 10),   
                InspEffect("Wits Type", 14, 14), 
                InspEffect("Deception", 7, 7),
                InspEffect("Occult Lore", 7, 7),
                InspEffect("Moxie", 5, 5)]
            ))
            
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                0,
                "Flair for the Dramatic",
                "Wits",
                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 4, 4),
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                1,
                "Cheap Trick",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                2,
                "Deck of Special Cards",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 5, 5),               
                InspEffect("Poker", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                3,                
                "Something Up Your Sleeve",               
                "Wits", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 6, 6),                
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                4,
                "Mentalist's Patter",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 6, 6),       
                InspEffect("Diplomacy", 5, 5),  
                InspEffect("Negotiation", 3, 3)]   
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                5,
                "Useful Distraction",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 7, 7),
                InspEffect("Dodge", 6, 6),
                InspEffect("Fisticuffs", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                6,
                "Attention to Detail",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 1, 15),            
                InspEffect("Perception", 7, 7),               
                InspEffect("Deduction", 5, 5),          
                InspEffect("Wits Type", 5, 5)]                    
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                7,    
                "New Spin, Classic Trick",          
                "Wits", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 1, 20),           
                InspEffect("Problem Solving", 7, 7),          
                InspEffect("Escape Artistry", 7, 7),           
                InspEffect("Occult Lore", 5, 5)]             
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                8,
                "Easy Audience",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 7, 7),        
                InspEffect("Deception", 7, 7),       
                InspEffect("Awareness", 7, 7),
                InspEffect("Flirting", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                9,
                "Knack for Misdirection",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 9, 9),
                InspEffect("Stealth", 7, 7),
                InspEffect("Dodge", 7, 7),
                InspEffect("Fisticuffs", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Magic Tricks",
                10,
                "Master Magician",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Magic Tricks", 10, 10),   
                InspEffect("Escape Artistry", 8, 8), 
                InspEffect("Grace", 7, 7),
                InspEffect("Stealth", 7, 7),
                InspEffect("Deception", 5, 5)]
            ))
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Occult Lore",
                0,
                "Love of the Spooky",
                "Wits",
                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 4, 4),
                InspEffect("Magic Tricks", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                1,
                "Whisper Once Heard",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 5, 5)]      
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                2,
                "What the Astrologer Said",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 4, 4),               
                InspEffect("Hope", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                3,                
                "As the Theosophists Say...",               
                "Wits", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 6, 6),                
                InspEffect("Moxie", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                4,
                "Strange Things", 
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 6, 6),       
                InspEffect("Deduction", 5, 5),  
                InspEffect("Wits Type", 5, 5)]  
                            
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                5,
                "A Story from Marrakech",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 7, 7),
                InspEffect("Awareness", 5, 5),
                InspEffect("Deception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                6,
                "Lore from Witch Trials",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 7, 7),            
                InspEffect("Magic Tricks", 7, 7),               
                InspEffect("Empathy", 5, 5),          
                InspEffect("Conscience", 3, 3)]                     
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                7,    
                "Studies of Ancient Religion",          
                "Wits", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 7, 7),           
                InspEffect("Resolve", 7, 7),          
                InspEffect("Deduction", 5, 5),           
                InspEffect("Wits Type", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                8,
                "Dreams from Beyond",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 7, 7),        
                InspEffect("Courage", 7, 7),       
                InspEffect("Awareness", 7, 7),
                InspEffect("Perception", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                9,
                "The Mad Egyptian's Words",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 9, 9),
                InspEffect("Resolve", 7, 7),
                InspEffect("Perception", 7, 7),
                InspEffect("Dodge", 7, 7)]      
            ))
            
            self.addInspire(Inspirations(
                "Occult Lore",
                10,
                "Seeker of Esoteric Truth",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Occult Lore", 10, 10),   
                InspEffect("Problem Solving", 8, 8), 
                InspEffect("Wits Type", 10, 10),
                InspEffect("Deception", 7, 7),
                InspEffect("Awareness", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Stealth",
                0,
                "Library-Trained for Quiet",
                "Wits",
                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 4, 4),
                InspEffect("Wits Type", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                1,
                "Soft-Soled Shoes",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                2,
                "Dark Clothes",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 5, 5),               
                InspEffect("Magic Tricks", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                3,                
                "Poor Lighting",               
                "Wits", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 6, 6),                
                InspEffect("Dodge", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                4,
                "Convenient Background Noises",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 6, 6),       
                InspEffect("Dodge", 5, 5),  
                InspEffect("Deception", 3, 3)]   
                            
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                5,
                "Distracted Sentries",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 7, 7),
                InspEffect("Dodge", 6, 6),
                InspEffect("Magic Tricks", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                6,
                "Gift for Silence",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 7, 7),            
                InspEffect("Grace", 7, 7),               
                InspEffect("Listen", 5, 5),          
                InspEffect("Magic Tricks", 3, 3)]                  
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                7,    
                "Shadows Seek You Out",          
                "Wits", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 1, 20),           
                InspEffect("Dodge", 7, 7),          
                InspEffect("Magic Tricks", 7, 7),           
                InspEffect("Deception", 5, 5)]    
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                8,
                "Skilled Curfew-Breaker",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 7, 7),        
                InspEffect("Deception", 1, 20),       
                InspEffect("Negotiation", 7, 7),
                InspEffect("Magic Tricks", 6, 6)]
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                9,
                "Improbable Ninjutsu Training",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 9, 9),
                InspEffect("Wits Type", 9, 9),
                InspEffect("Grace", 7, 7),
                InspEffect("Dodge", 7, 7)]    
            ))
            
            self.addInspire(Inspirations(
                "Stealth",
                10,
                "Arch-Phantom",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Stealth", 1, 30),   
                InspEffect("Dodge", 9, 9), 
                InspEffect("Grace", 7, 7),
                InspEffect("Climbing", 7, 7),
                InspEffect("Leaping", 5, 5)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Poker",
                0,
                "Taste for Gambling",
                "Wits",
                [InspEffect("General", 50, 50),
                InspEffect("Courage", 4, 4),
                InspEffect("Moxie", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                1,
                "Aces and Eights",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                2,
                "Wild Card",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 4, 4),               
                InspEffect("Deception", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                3,                
                "Inconsistent Tell",               
                "Wits", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Poker", 6, 6),                
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                4,
                "Sunglasses Hide Your Eyes",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 6, 6),       
                InspEffect("Deception", 5, 5),  
                InspEffect("Perception", 3, 3)]  
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                5,
                "Knack for the Bluff",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 7, 7),
                InspEffect("Deception", 6, 6),
                InspEffect("Poise", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                6,
                "Pass for a Novice",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 1, 15),            
                InspEffect("Deception", 7, 7),               
                InspEffect("Moxie", 5, 5),          
                InspEffect("Wits Type", 5, 5)]                      
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                7,    
                "Perfect Tell",          
                "Wits", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Poker", 1, 20),           
                InspEffect("Awareness", 7, 7),          
                InspEffect("Magic Tricks", 7, 7),           
                InspEffect("Deception", 5, 5)]         
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                8,
                "You Make the Rules",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 7, 7),        
                InspEffect("Problem Solving", 7, 7),       
                InspEffect("Deception", 7, 7),
                InspEffect("Wits Type", 9, 9)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                9,
                "Stacked Deck",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 9, 9),
                InspEffect("Magic Tricks", 7, 7),
                InspEffect("Deception", 7, 7),
                InspEffect("Negotiation", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Poker",
                10,
                "Queen of the Cards",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Poker", 1, 30),   
                InspEffect("Magic Tricks", 8, 8), 
                InspEffect("Awareness", 7, 7),
                InspEffect("Poise", 7, 7),
                InspEffect("Wits Type", 10, 10)]
            ))
            
            
            
            
            
            
            
            self.addInspire(Inspirations(
                "Perception",
                0,
                "Good Eyes, Good Ears",
                "Wits",
                [InspEffect("General", 50, 50),
                InspEffect("Perception", 4, 4),
                InspEffect("Knowledge Type", 3, 3)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                1,
                "Squint",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                2,
                "Otherwise Quiet Day",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 4, 4),               
                InspEffect("Listen", 4, 4)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                3,                
                "Hard to Miss",               
                "Wits", 
               
                [InspEffect("General", 50, 50),
                InspEffect("Perception", 6, 6),                
                InspEffect("Awareness", 5, 5)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                4,
                "Unobstructed View",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 6, 6),       
                InspEffect("Listen", 5, 5),  
                InspEffect("Awareness", 3, 3)]   
                            
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                5,
                "Unusually Alert",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 1, 15),
                InspEffect("Awareness", 1, 15),
                InspEffect("Listen", 1, 15)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                6,
                "Arresting Detail",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 7, 7),            
                InspEffect("Deduction", 7, 7),               
                InspEffect("Awareness", 5, 5),          
                InspEffect("Cryptography", 3, 3)]                     
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                7,    
                "Elementary, My Dear",      
                "Wits", 
           
                [InspEffect("General", 50, 50),
                InspEffect("Perception", 7, 7),           
                InspEffect("Awareness", 7, 7),          
                InspEffect("Deduction", 7, 7),           
                InspEffect("Wits Type", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                8,
                "Totally Attentive",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 1, 25),        
                InspEffect("Dodge", 7, 7),       
                InspEffect("Awareness", 7, 7),
                InspEffect("Magic Tricks", 7, 7)]
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                9,
                "Impossible to Ignore",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 8, 8),
                InspEffect("Awareness", 7, 7),
                InspEffect("Deduction", 7, 7),
                InspEffect("Problem Solving", 7, 7)]   
            ))
            
            self.addInspire(Inspirations(
                "Perception",
                10,
                "Perfect Sentry",
                "Wits", 

                [InspEffect("General", 50, 50),
                InspEffect("Perception", 10, 10),   
                InspEffect("Awareness", 9, 9), 
                InspEffect("Listen", 7, 7),
                InspEffect("Dodge", 7, 7),
                InspEffect("Wits Type", 10, 10)]
            ))

    class InspDescr:       
        def __init__(self, type, number):
            self.type = type
            self.number = number

    class InspUIContainer:
        def __init__(self, inspirations, index, type, position):
            self.inspirations = inspirations
            self.index = index
            self.type = type
            self.position = position 
        
        def clone(self):
            return InspUIContainer(self.inspirations, self.index, self.type, self.position)















    def awardInspirations(inspList):
        global _game_menu_screen
        global show_button_game_menu
        fresult = []
        list = []
        if inspList is not None:
            for inspire in inspList:
                if inspire is not None:
                    list.append(inspire)
        else:
            return fresult
        
        if len(list) == 0:
            return fresult
        
        statMaxInsp =  statistics.get_possible_cards_number()
        currInspCount = len(inspireList.playerList)
        
        maxInsp =  statMaxInsp
        
        renpy.log("max inspirations " + str(maxInsp))
        
        
        if len(list) + len(inspireList.playerList) <=  maxInsp:
            renpy.log("directly add inspirations")
            for insp in list:
                inspireList.addPlayerInspire(insp)
                fresult.append(insp)
            return fresult
        
        _game_menu_screen = None
        show_button_game_menu = False  
        
        inspirations = []
        inspIndex = 0  
        for insp in inspireList.playerList:
            if inspIndex < 20:
                inspType = get_inspType(insp)
                inspPos = get_card_position(inspIndex)
                inspirations.append(InspUIContainer(insp, inspIndex, inspType, inspPos ))
                inspIndex = inspIndex + 1
        
        
        additionalCount = maxInsp - inspIndex
        if additionalCount > 0:
            for i in range(additionalCount):
                inspPos = get_card_position(inspIndex)
                inspirations.append(InspUIContainer(None, inspIndex, None, inspPos ))
                inspIndex = inspIndex + 1
        
        
        removedCard = None
        addCard = None
        
        while True:
            
            tip = ui.frame(xpadding = 0, ypadding = 0, xmargin = 0, ymargin = 0, background = "inspBackground")
            ui.fixed()
            
            cW = 399.0 * resFactor    
            cH = 544.0 * resFactor    
            cHL = 390.0 * resFactor    
            cWL = 281.0 * resFactor    
            sW = 60 * resFactor *factor
            cZ = float(cW/(281.0 * resFactor))
            
            
            for i in range(maxInsp):
                cardBackPos = get_card_position(i)
                ui.add("obstacleCardSlot", xpos=cardBackPos[0], ypos=cardBackPos[1])
            
            validInspCount = 0    
            
            for inspUI in inspirations:
                if inspUI.inspirations is None and addCard is not None:
                    fresult.append(addCard)
                    inspUI.inspirations = addCard
                    inspUI.type = get_inspType(addCard)
                    inspireList.addPlayerInspire(addCard)
                    addCard = None
            
            
            
            ui.text("Inspiration Maximum: " + str(statMaxInsp), xpos= 0.02, ypos = 0.27)
            ui.text("Current Inspirations: " + str(len(inspireList.playerList)), xpos= 0.02, ypos = 0.304) 
            
            
            for inspUI in inspirations:
                if inspUI.inspirations is not None:
                    validInspCount = validInspCount + 1
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    tX = 0.05
                    tY = 0.35
                    
                    
                    tt = InspTooltip(tX, tY, inspUI.inspirations)
                    
                    
                    ui.imagebutton(
                        "obstacleCard_"+inspUI.type, 
                        "obstacleCard_"+inspUI.type, 
                        hovered = tt.show,
                        unhovered = tt.hide,
                        xpos = inspUI.position[0], 
                        ypos = inspUI.position[1],
                        action = SetVariable("inspVar", None)                        
                        )
                    
                    ui.imagebutton(
                        "inspDiscard", 
                        "inspDiscardh", 
                        hovered = tt.show,
                        unhovered = tt.hide,
                        xpos = (inspUI.position[0] + float(105.0 * resFactor/gW)), 
                        ypos = inspUI.position[1],
                        action = ui.returns((inspUI.index, inspUI, inspUI.inspirations))
                        )
            
            
            
            
            
            
            if removedCard is not None:
                inspOffset = get_cardOutOffset(removedCard.type)
                ui.add(("insp_" + removedCard.type), xpos=(removedCard.position[0]+inspOffset[0]), ypos=(removedCard.position[1]+inspOffset[1]))
                removedCard = None
            
            N = len(list)
            if N > 0:
                
                startX = (gW - ((cW * N) + (sW * (N - 1))))* 0.5
                startY = 600 * resFactor * factor
                
                cIndex = 0
                for insp in list:
                    inspType = get_inspType(insp)
                    xP = (startX + cIndex* (cW + sW)) * factor
                    
                    
                    tt = InspTooltip(0.05, 0.35, insp)
                    
                    transform = ui.transform()
                    ui.imagebutton(
                        ("obstacleCard_"+inspType), 
                        ("obstacleCard_"+inspType), 
                        hovered = tt.show,
                        unhovered = tt.hide,
                        xpos = int(xP), 
                        ypos = int(startY),
                        action = SetVariable("inspVar", None))  
                    transform.zoom = cZ
                    transform.update()
                    
                    if validInspCount < maxInsp:
                        ui.imagebutton(
                            "inspKeep", 
                            "inspKeeph", 
                            hovered = tt.show,
                            unhovered = tt.hide,
                            xpos = int(xP), 
                            ypos = int(startY + (470 * resFactor *factor)),
                            action = ui.returns((cIndex + 50, None, insp)))
                    else:
                        ui.imagebutton(
                            "inspKeep", 
                            "inspKeeph", 
                            xpos = int(xP), 
                            ypos = int(startY + (470 * resFactor *factor)))
                    
                    cIndex = cIndex + 1
            
            ui.close()
            
            ui.frame(xalign = 0.5, yalign = 0.67, background=None)
            ui.imagebutton("inspDone", "inspDoneh", action = Return((100, None, None)))
            
            
            result, inspUI, insp = ui.interact()
            
            if result < 20:
                removedCard = inspUI.clone()
                inspireList.removePlayerInspire(inspUI.inspirations)
                if inspUI.inspirations in fresult:
                    fresult.remove(inspUI.inspirations)
                inspUI.inspirations = None
            elif result < 100:
                addCard = insp
                list.remove(insp)
            if result == 100:
                _game_menu_screen = "save_screen"
                show_button_game_menu = True
                
                return fresult
