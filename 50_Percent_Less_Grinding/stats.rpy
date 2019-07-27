init -100 python:
    def InitMenu(exoticLocation):
        global _game_menu_screen
        global show_button_game_menu
        
        _game_menu_screen = "save_screen"
        show_button_game_menu = True
        storySystem.setExoticLocation(exoticLocation)
        mainMenuActionExecute = None
        renpy.scene()
        renpy.show("background"+exoticLocation)
        renpy.free_memory()


    def StressMap():
        
        
        
        
        
        
        
        
        
        
        
        loc = storySystem.getExoticLocation()
        if loc == "NY":
            x = 2138*resFactor
            y = 1096*resFactor
            t_x = 2138*resFactor
            t_y = 1096*resFactor
        elif loc == "NO":
            x = 2377*resFactor
            y = 217*resFactor
            t_x = 2377*resFactor
            t_y = 217*resFactor
        elif loc == "E":
            x = 860*resFactor
            y = 931*resFactor
            t_x = 860*resFactor
            t_y = 931*resFactor
        elif loc == "A":
            x = 469*resFactor
            y = 1181*resFactor
            t_x = 469*resFactor
            t_y = 1181*resFactor
        elif loc == "I":
            x = 971*resFactor
            y = 468*resFactor
            t_x = 971*resFactor
            t_y = 468*resFactor
        elif loc == "T":
            x = 736*resFactor
            y = 1171*resFactor
            t_x = 736*resFactor
            t_y = 1171*resFactor
        elif loc == "P":
            x = 2375*resFactor
            y = 266*resFactor
            t_x = 2375*resFactor
            t_y = 266*resFactor
        else:
            return
        
        
        stressImageName = "MainMenu" + loc + "_low"
        stressValue = statistics.get_stat_value("stress")
        if stressValue >=10:
            stressImageName = "MainMenu" + loc +"_med"
        if stressValue >=20:
            stressImageName = "MainMenu" + loc + "_high"
        stress_tooltip = TextTooltip(float(t_x/gW), float(t_y/gH), ("Current Stress\n" + str(stressValue)))
        ui.imagebutton(stressImageName, stressImageName, xpos=float(x/gW), ypos=float(y/gH), 
            hovered = stress_tooltip.show,
            unhovered = stress_tooltip.hide,
            action = [stress_tooltip.hide, Return()])

    class StatisticsContainer:
        
        def __init__(self):
            self._m1_stats__dse_stats = dict()
            self._m1_stats__dse_stats_type = dict()
            self._m1_stats__dse_stats_type_key = dict()
            self._m1_stats__dream = "Dream of Family"
            self.dreamDescr = dict()            
            self.relDescr = dict()            
        
        def initialize(self):
            self.addStat(
                "Athletics type", 
                Statistics("Athletics", "General Physical Skill", 50, 100),
                Statistics("Grace", "Fine Coordination", 50, 100),
                Statistics("Climbing", "Ability to Ascend", 50, 100),
                Statistics("Leaping", "Ability to Jump", 50, 100),
                Statistics("Strength", "Raw Muscle", 50, 100),
                Statistics("Riding", "Comfort on Horseback", 50, 100)
                )
            
            self.addStat(
                "Charm type", 
                Statistics("Charm", "Simple Charisma", 50, 100),
                Statistics("Deception", "Ability to Mislead", 50, 100),
                Statistics("Diplomacy", "Skill at Alliance-Making", 50, 100),
                Statistics("Flirting", "Skill at Winks and Smiles", 50, 100),
                Statistics("Negotiation", "Skill at Deal-Making", 50, 100),
                Statistics("Animal Handling", "Skill with Animals", 50, 100)
                )
            
            self.addStat(
                "Dream type", 
                Statistics("Dream of Family", "Devotion to Parents' Memory", 0, 100),
                Statistics("Dream of Ahmose", "Connection to the Prince", 0, 100),
                Statistics("Dream of Nigel", "Connection to the Professor", 0, 100),
                Statistics("Dream of Felix", "Connection to the Boy Who Came Home", 0, 100),
                Statistics("Dream of Roland", "Connection to the Spy", 0, 100),
                Statistics("Dream of Sterling", "Connection to the Rogue", 0, 100),
                Statistics("Conscience", "Awareness of Consequences", 50, 100),
                Statistics("Courage", "Control over Fear", 50, 100),
                Statistics("Patience", "Willingness to Wait", 50, 100),
                Statistics("Resolve", "Determination to Proceed", 50, 100),
                Statistics("Hope", "Faith in Tomorrow", 50, 100),
                
                Statistics("Dream of College", "", 0, 100),
                Statistics("Dream of Change", "", 0, 100),
                Statistics("Dream of Completion", "", 0, 100),
                Statistics("Dream of Christmas", "", 0, 100),
                Statistics("Dream of Egypt", "", 0, 100),
                Statistics("Dream of Australia", "", 0, 100),
                Statistics("Dream of India", "", 0, 100),
                Statistics("Dream of Peru", "", 0, 100),
                Statistics("Dream of New Orleans", "", 0, 100),
                Statistics("Dream of Turkey", "", 0, 100),
                Statistics("Dream of Anna's World Tour", "", 0, 100),
                Statistics("Dream of Blood and Art", "", 0, 100),
                Statistics("Dream of Butlers", "", 0, 100),
                Statistics("Dream of Cappadocia", "", 0, 100),
                Statistics("Dream of the Grimoire", "", 0, 100),
                Statistics("Dream of the Third Eye", "", 0, 100),
                Statistics("Dream of a Royal Family", "", 0, 100),
                Statistics("Dream of the Hunt", "", 0, 100),
                Statistics("Dream of a Big Movie Star", "", 0, 100),
                Statistics("Dream of Football", "", 0, 100),
                Statistics("Dream of the Albino Alligator", "", 0, 100),
                Statistics("Dream of the Great Game", "", 0, 100),
                Statistics("Dream of Flight and Film", "", 0, 100),
                Statistics("Dream of the Crossroads", "", 0, 100),
                Statistics("Dream of a Beautiful City", "", 0, 100),
                Statistics("Dream of the Spear", "", 0, 100),
                Statistics("Dream of the Stolen Scholar", "", 0, 100),
                Statistics("Dream of the Platypus", "", 0, 100),
                Statistics("Dream of the Golden Scarab", "", 0, 100),
                Statistics("Dream of the Serpent Empire", "", 0, 100),
                Statistics("Dream of the Devourers", "", 0, 100),
                Statistics("Dream of the Dead Bakers", "", 0, 100),
                Statistics("Dream of the Ancient Mystery", "", 0, 100)
                )
            
            self.addStat(
                "Knowledge type", 
                Statistics("Knowledge", "Formal Learning", 50, 100),
                Statistics("Problem Solving", "Knowledge of Problems and Solutions", 50, 100),
                Statistics("Language", "Knowledge of Different Tongues", 50, 100),
                Statistics("Cryptography", "Knowledge of Codes", 50, 100),
                Statistics("Repair", "Knowledge of Machines", 50, 100),
                Statistics("Deduction", "Knowledge of Investigation", 50, 100)
                )
            
            
            self.addStat(
                "Relationship type", 
                Statistics("Relationship with Ahmose", "Friendship with the Prince", 0, 100),
                Statistics("Relationship with Nigel", "Friendship with the Professor", 0, 100),
                Statistics("Relationship with Felix",  "Friendship with the Boy Who Came Home", 0, 100),
                Statistics("Relationship with Roland",  "Friendship with the Mystery Man", 0, 100),
                Statistics("Relationship with Sterling",  "Friendship with the Rogue", 0, 100),
                Statistics("Relationship with Aunt Evelyn",  "Relationship with Auntie", 0, 100),
                Statistics("Relationship with Anna",  "Relationship with the Best Friend", 0, 100),
                Statistics("Listen", "Hearing What People Say", 50, 100),
                Statistics("Empathy", "Feeling People's Pain", 50, 100),
                Statistics("Self Knowledge", "Capacity for Introspection", 50, 100),
                Statistics("Tolerance", "Enduring Irritation", 50, 100),
                Statistics("Poise", "Self-Possession and Style", 50, 100),
                )
            
            self.addStat(
                "Stress type", 
                Statistics("Stress", "Weight of the World", 0, 100),
                Statistics("Awareness", "Skill at Reading People", 50, 100),
                Statistics("Fisticuffs", "Skill at Brawling", 50, 100),
                Statistics("Moxie", "Skill at Grinning and Putdowns", 50, 100),
                Statistics("Dodge", "Skill at Evasion", 50, 100),
                Statistics("Escape Artistry", "Skill at Getting Out", 50, 100)
                )
            
            self.addStat(
                "Wits type", 
                Statistics("Wits", "Craft and Cunning", 50, 100),
                Statistics("Magic Tricks", "Pulling Rabbits from Hats", 50, 100),
                Statistics("Occult Lore", "Esoteric Knowledge", 50, 100),
                Statistics("Stealth", "Skill at Sneaking", 50, 100),
                Statistics("Poker", "Skill at Gamesmanship", 50, 100),
                Statistics("Perception", "Skill at Seeing, Hearing, etc.", 50, 100)
                )
            
            self.dreamDescr["family"] = ("Well, hello, journal.  I'm Scheherazade Keating, and I'll be your writer today!  Call me Sadie.\n\n" + 
                    "I'm a freshman at NYU this year, studying archaeology.  I have some good professors, and I love the subject, but there's this odd sense of déjà vu.  Even ten years after my parents left it's strange to be around the department without them.  One of my classes is in Mom's old lecture hall, and Aunt Evelyn's pretty sure Dad actually punched Professor Blake in the face once, before I was even born.  That should do wonders for my grade in his class.\n\n" +  
                    "Still, I wouldn't do this any other way.  I'm Henry and Morgana Keating's daughter.  If I'm going to learn from their examples, I might as well start where they started.\n\n" + 
                    "I'm still living with Aunt Evelyn while I'm in New York.  She hates it when I travel, so I figure I might as well try to make her happy in the times I'm here.  If she hadn't been here for me when I was a kid, I don't think I'd be any kind of human being now.  Besides, if I left her alone, she would probably turn the place into a speakeasy, and that would make the butler sad.\n\n" + 
                    "More soon!  For now, I've got to get ready for the next trip!")
            
            self.dreamDescr["nigel"] = ("It's funny, but I can't stop thinking about Mom's old diaries.  They go all the way back to when she first met Dad (or, as she called him at the time, “that crazy man,” “the debauched refugee from the stagnant backwaters of Theosophy,” “the wild-eyed lunatic,” and “he of the well-formed calves”).  What stands out to me now are the parts where she finally admitted she was falling for him.\n\n" + 
                    "“I cannot help but think it a sign of some higher favor that I have been placed before a man to whom I need not defend my interests, nor the ability of my womanly mind to pursue them.  Even were the dangerous edges of his character less appealing than they are – or, indeed, as unappealing as convention and common sense would argue that they ought to be – the fact that he regards me as a peer and an expert in our shared domain would be enough to make my heart swell.”\n\n" + 
                    "Is it strange that I find that familiar?  I can talk to Nigel for hours about the history of Egyptian linen, and it's better than flirting with any boy I knew in high school.  And I think that being with me makes him happy as well.\n\n" + 
                    "Wow.")
            
            self.dreamDescr["felix"] = ("When I was a kid, I always assumed that Felix would be here for me forever.  I think I even needed him to be.  I had lost my parents, and the idea of losing other people I cared about just filled me with dread, because it seemed so possible.\n\n" + 
                    "And then Felix had to go to another school, and his family moved, and it was terrible.  I've never told him this, and I never will, but Aunt Evelyn could barely coax me out of my room for a week after he left, maybe more.  And then I tried to convince Evelyn to help me (and Anna) go to his new school.  Honestly, I was a brat about it, but losing him was like losing part of myself.\n\n" + 
                    "I don't know why that's coming back to me now.  He's working at the university, and I mean to make sure he'll be able to study here and become the man he wants to be.  I have a plan.  He's not going anywhere.\n\n" + 
                    "Dear journal, I really don't want to lose him again.")
            
            self.dreamDescr["roland"]   = ("Dear journal, Roland continues to baffle me.\n\n" + 
                    "No, not baffle.  Let's be honest here – I'm scared for him.  I've seen what his life demands of him, and even what it demands of the people around him.  At the rate he's going, I'm not sure he's going to come out of the year in one piece, but it's not my place to tell him to stop.\n\n" + 
                    "I guess all I can do is try to help him through, and hope he'll do the same for me.")
            
            self.dreamDescr["sterling"] = ("Dear journal, I don't think I've ever known a man who made my life as complicated as quickly as Sterling Evans.  Secret patrons and strange clues and little double-crosses that always seem to turn out okay, these are the things that Sterling Evans brings.\n\n" + 
                    "And it's not his fault, exactly.  I know that.  I think I know that.  I'm pretty sure.\n\n" + 
                    "I'm in so far over my head.\n\n" + 
                    "But that's the thing about Sterling.  Most of the time, he makes being in over your head seem so much more interesting than the alternatives – as long as we're both underwater together.")
            
            self.dreamDescr["ahmose"] = ("Ahmose Ankh.  Stuffy, undead, uncompromising.\n\n" + 
                    "My dear journal, I can't begin to tell you how happy I am to have met him.  I read what I wrote before, “not just fascinating.  He's honorable!” and I just cringe.  I look at it now, and there's this girl from New York trying to pretend that meeting a thirty-six hundred year old boy was just more of the same old lah-de-dah.  In real life, let me tell you, there was a lot more pacing in circles in the dead of night and smothering panic attacks.\n\n" + 
                    "Now, there are fewer of those scenes, and most of them are about trying to keep him safe.  He's such a good person – dignified, caring, and endlessly patient with all the nonsense with which he's been subjected (even by certain blondes who might now regret certain early arguments).\n\n" + 
                    "Every time I think of him, I find myself smiling.")
            
            self.relDescr["sadie"] = ("Well, journal, things are changing.  Oh, I'm still the wandering star of the archaeology class, I'm still running around the world.  I hope I'm still doing work that would make Mom and Dad proud.\n\n"
                    "What's different now is that I feel like maybe Mom and Dad would have been proud anyway.  Maybe there's more to life than judging myself by what they did.  They're still inspirational, and if they're out there I'll find them, but maybe it's okay to let go.  Just a little.\n\n" +
                    "Or maybe that's just the way I'm feeling for a guy making me crazy.  I'm not sure I can tell the difference anymore.\n\n" + 
                    "Maybe that's okay too.")
            
            self.relDescr["nigel"] = ("Professor Nigel Hemsworth is the best teacher I have this year, dear journal.  There's also something about him that reminds me of Buster Keaton – the baby face, the clumsiness that works out so well it has to be planned.  I don't know.\n\n"+
                    "He's the youngest professor the department has had in ages.  Maybe ever.  And, mathematically, it'll be hard to beat him, even with all the credits I earned in high school.  Darn it.\n\n" + 
                    "But, anyway, he's brilliant, and he knows what it's like to be young and motivated.  He doesn't have the kind of field experience I do, but Dad always said anyone can get experience.  A good heart is harder to come by.\n\n" + 
                    "And that, Professor Hemsworth has in spades.")
            
            self.relDescr["felix"] = ("There was a time, when I was a kid, when Felix Weber was my best friend.  Anna insisted on playing with dolls and talking about dresses, bless her heart, but Felix would climb trees with me.\n\n"+  
                        "Then he went one way, and I went another, and now it's years later and all of a sudden he's someone who needs to shave, who has a job to support his mother and sisters.\n\n" +
                        "He's also a mechanical genius, and a self-taught pilot, and he's the man who lugs around all the equipment the archaeology department can't be bothered to deal with on its own.  If there's any justice in the world, he'll get a job with the Ford Motor Company and be filthy rich in five years or less – and he'd deserve it, because there isn't a nicer man alive.\n\n" + 
                        "And you can tell, just from talking to him for five minutes, that he's still up for climbing trees.")
            
            self.relDescr["roland"] = ("Roland (Smith, if that's his real name) is a smirking, secretive Briton of a man.  He's never been anything other than charming – and that's a quality that Aunt Evelyn has always warned me to be wary of in men.  He's not a wolf; I'd know how to deal with that.  He's… well, he's Roland.\n\n" + 
                        "But being Roland also seems to mean being brave, and caring about people, and having a sense of duty and courtesy that seems internally consistent, if occasionally hard to anticipate.  I may occasionally feel uneasy trusting him, but so far he's never made me regret it.\n\n" + 
                        "I just wish it was easier to make him trust me.")
            
            self.relDescr["sterling"] = ("Sterling Evans: treasure-hunter, man-of-action, grifter and secret romantic.  I think.\n\n" + 
                        "What I'm sure he is is fun.  I've been in wildly unsafe surroundings or surrounded by enemies with far too many people in my life, and I don't think I've ever met anyone as good as Sterling at making a girl crack a smile as the roof is caving in.\n\n" + 
                        "That's probably not the way I should put it to Aunt Evelyn.\n\n" + 
                        "That's probably not even the way I should put it to you, dear journal, but it is what it is.  He's not the safest friend to have, maybe, but I'm glad I know him all the same.")
            
            self.relDescr["ahmose"] = ("I know a prince.  An Egyptian prince.  From, heavens, I don't know?  The Fourteenth Dynasty?\n\n" + 
                        "This is not something that even my rather unusual upbringing really adequately prepared me for.  Dad would be over the moon!\n\n" + 
                        "But the striking thing is how normal he seems.  Well, no.  Accommodating?  Modern, in an ancient sort of way?  I think what I mean to say is that he's much more willing to try to understand the world in which he finds himself than I would ever have expected, but at the same time he's staying remarkably true to the set of ethics with which he was raised.\n\n" + 
                        "He's not just fascinating.  He's honorable.  I like him!\n\n" + 
                        "It almost makes me revisit my assumptions about monarchy.  [[To say nothing of magic, dear journal.]")
            
            self.relDescr["anna"] = ("Dear journal, have I not told you yet about Anna?  Bad Sadie!\n\n" + 
                        "She's my best friend.  Heck, for most of high school, she was my only friend.  We were both a bit too eccentric for the other girls – me with the archaeological obsessions, and Anna with the fear of horses and the gift for gambling and the tendency to laugh at just the strangest times.  I remember when Norma Howard tried to frame me for pickpocketing: Anna, no more than two thirds her weight, jumped on her back, wrapped her arms around her throat, and just rode her around campus screaming, “Justice!  Justice!”\n\n" + 
                        "She's the sister I never had.  That's all there is to it.")
            
            self.relDescr["aunt evelyn"] = ("And then there's Aunt Evelyn.\n\n"+
                        "I'll tell you, dear journal, my parents never did anything better for me than leaving me with Mom's sister Evelyn when they left on their last trip.  I include giving birth to me in that.  I was alone and scared and waiting for another terrible shoe to drop, and thanks to Evelyn it never did.\n\n" + 
                        "She raised me as her own, while always insisting Mom and Dad would come back, and she never once allowed me to go to bed feeling like I wasn't loved and like the world wasn't basically a good place.  She's eccentric, she's temperamental, she says that Prohibition saved drinking by taking it away from stinky men in saloons and giving it to women of refinement and long lists of friends, and I love her more than anything.\n\n" + 
                        "That said, she can be an incredible pain in the you-know-where.  And I'm not entirely sure that she'd be able to feed herself without the aid of Bigglesworth, the finest butler alive.  But, really, we all have our quirks.")
        
        
        def dreamNote(self, dream, txt):
            if dream.lower().startswith("dream of "):
                k = dream.lower().replace("dream of ", "")
                if k in self.dreamDescr:
                    self.dreamDescr[k] = (self.dreamDescr[k] + "\n\n" + txt)
        
        def relationshipNote(self, relationship, txt):
            if relationship.lower().startswith("relationship with "):
                k = relationship.lower().replace("relationship with ", "")
                if k in self.relDescr:
                    self.relDescr[k] = (self.relDescr[k] + "\n\n" + txt)
        
        def wrap(self, container, max):
            for k, v in container._m1_stats__dse_stats_type_key.iteritems():           
                self._m1_stats__dse_stats_type_key[k] = v
            
            for k, v in container._m1_stats__dse_stats.iteritems():           
                stat = Statistics(v.name, "", v.default, max)
                stat.setValue(v.var)
                self._m1_stats__dse_stats[k] = stat
            
            for k1, v1 in container._m1_stats__dse_stats_type.iteritems():
                list = []
                for l in v1:
                    list.append(l)
                self._m1_stats__dse_stats_type[k1] = list
        
        def addStat(self, type, *argstatistics):
            list = []
            
            for stat in argstatistics:
                list.append(stat.name.lower())
                self._m1_stats__dse_stats[stat.name.lower()] = stat
                self._m1_stats__dse_stats_type_key[stat.name.lower()] = type
            
            self._m1_stats__dse_stats_type[type.lower()] = list
        
        def get_type_by_skill(self, skillName):
            if self._m1_stats__dse_stats_type_key.has_key(skillName.lower()):
                return self._m1_stats__dse_stats_type_key[skillName.lower()]
        
        def is_type_exists(self, name):
            return self._m1_stats__dse_stats_type.has_key(name.lower())
        
        def get_type_atributes(self, name):
            if self._m1_stats__dse_stats_type.has_key(name.lower()):
                return self._m1_stats__dse_stats_type[name.lower()]
        
        def get_stat_value(self, name):
            if self._m1_stats__dse_stats.has_key(name.lower()):
                return self._m1_stats__dse_stats[name.lower()].var
        
        def get_stat(self, name):
            if self._m1_stats__dse_stats.has_key(name.lower()):
                return self._m1_stats__dse_stats[name.lower()]
        
        def get_skill_level(self, name):
            return self.get_stat_value(name) // 10
        
        def get_possible_cards_number(self):
            return 10 + self.get_skill_level(self._m1_stats__dream)
        
        def get_dream(self):
            return self._m1_stats__dream
        
        def set_stat_value(self, name, val):
            if self._m1_stats__dse_stats.has_key(name.lower()):
                self._m1_stats__dse_stats[name.lower()].setValue(val)
        
        def add_stat_value(self, name, val, enableAchievement=True):
            if self._m1_stats__dse_stats.has_key(name.lower()):
                self._m1_stats__dse_stats[name.lower()].addValue(val, enableAchievement)
        
        def add_stat_value_to_all(self, val, enableAchievement=True):
            for st in self._m1_stats__dse_stats.values():
                st.addValue(val, enableAchievement)
        
        def change_dream(self, dream):
            if self._m1_stats__dream != dream:
                self._m1_stats__dream = dream
                self.set_stat_value("Dream of Family", 0)
                self.set_stat_value("Dream of Ahmose", 0)
                self.set_stat_value("Dream of Nigel", 0)
                self.set_stat_value("Dream of Felix", 0)
                self.set_stat_value("Dream of Roland", 0)
                self.set_stat_value("Dream of Sterling", 0)

    class Statistics:
        def __init__(self, name, description, default, max):
            self.name = name
            self.description = description
            self.default = default
            self.var = default
            self.max = max
        
        
        def setValue(self, newValue, enableAchievement=True):
            if newValue > self.max:
                self.var = self.max
            elif newValue < 0:
                self.var = 0
            else:
                self.var = newValue
            
            if enableAchievement and self.var == 100 and not self.name.startswith('Dream') and not self.name.startswith('Relationship'): 
                steamApi.SetAchievement('ACH_SKILL_' + str.replace(self.name.upper(), " ", "_") + '_100')
        
        
        def addValue(self, newValue, enableAchievement=True):
            totalV = self.var + newValue
            self.setValue(totalV, enableAchievement)

image backgroundSkills:
    "images/Skills/UI_Game_SKILLS_Background.png"
    zoom factor

image knowledgeSkills:
    "images/Skills/Badge_Knowledge.png"
    zoom factor

image knowledgeSkills_h:
    "images/Skills/Badge_Knowledge_hover.png"
    zoom factor

image stressSkills:
    "images/Skills/Badge_Stress.png"
    zoom factor

image stressSkills_h:
    "images/Skills/Badge_Stress_hover.png"
    zoom factor

image athleticsSkills:
    "images/Skills/Badge_Athletics.png"
    zoom factor

image athleticsSkills_h:
    "images/Skills/Badge_Athletics_hover.png"
    zoom factor

image witsSkills:
    "images/Skills/Badge_Wits.png"
    zoom factor

image witsSkills_h:
    "images/Skills/Badge_Wits_hover.png"
    zoom factor

image relationshipSkills:
    "images/Skills/Badge_Relationship.png"
    zoom factor

image relationshipSkills_h:
    "images/Skills/Badge_Relationship_hover.png"
    zoom factor

image charmSkills:
    "images/Skills/Badge_Charm.png"
    zoom factor

image charmSkills_h:
    "images/Skills/Badge_Charm_hover.png"
    zoom factor

image dreamSkills:
    "images/Skills/Badge_Dream.png"
    zoom factor

image dreamSkills_h:
    "images/Skills/Badge_Dream_hover.png"
    zoom factor

image AhmosePhotoSkills:
    "images/Skills/Photo_Ahmose.png"
    zoom factor

image FelixPhotoSkills:
    "images/Skills/Photo_Felix.png"
    zoom factor

image NigelPhotoSkills:
    "images/Skills/Photo_Nigel.png"
    zoom factor

image RolandPhotoSkills:
    "images/Skills/Photo_Roland.png"
    zoom factor

image SadiePhotoSkills:
    "images/Skills/Photo_Sadie.png"
    zoom factor

image SterlingPhotoSkills:
    "images/Skills/Photo_Sterling.png"
    zoom factor

image AnnaPhotoSkills:
    "images/Skills/Photo_Anna.png"
    zoom factor

image Aunt EvelynPhotoSkills:
    "images/Skills/Photo_Evelyn.png"
    zoom factor

init 1 python:
    style.skills_list = Style(style.default)
    style.skills_list.size = int(38 *resFactor * factor)
    style.skills_list.font = "georgia.ttf"
    style.skills_list.color = "#ffffff"


    style.skills_list_btn = Style(style.default)
    style.skills_list_btn_text = Style(style.text)
    style.skills_list_btn_text.size = int(38 *resFactor * factor)
    style.skills_list_btn_text.font = "georgia.ttf"
    style.skills_list_btn_text.color = "#FFFFFF"
    style.skills_list_btn_text.hover_color = "#ffd700"




    style.skills_header = Style(style.default)
    style.skills_header.size = int(65 *resFactor * factor)
    style.skills_header.font = "pristina.ttf"
    style.skills_header.color = "#000000"

    style.skills_cg = Style(style.default)
    style.skills_cg.size = int(48 *resFactor * factor)
    style.skills_cg.font = "pristina.ttf"
    style.skills_cg.color = "#624700"

    style.skills_cb = Style(style.default)
    style.skills_cb.size = int(48 *resFactor * factor)
    style.skills_cb.font = "pristina.ttf"
    style.skills_cb.color = "#000000"

    style.skills_cgb = Style(style.default)
    style.skills_cgb_text = Style(style.text)
    style.skills_cgb_text.size = int(48 *resFactor * factor)
    style.skills_cgb_text.font = "pristina.ttf"
    style.skills_cgb_text.color = "#624700"
    style.skills_cgb_text.hover_color = "#bFAb2b"
    style.skills_cgb_text.selected_color = "#624700"
    style.skills_cgb_text.selected_hover_color = "#bFAb2b"

    def skills_get_dream_text(rel):
        k = ""
        if rel is not None:
            k = rel.lower()
        
        if rel is None or rel.lower() == "family" or rel.lower() == "sadie":
            k = "family"
        
        if k in statistics.dreamDescr:
            return statistics.dreamDescr[k]
        else:
            return ""

    def skills_get_rel_text(rel):
        k = ""
        if rel is not None:
            k = rel.lower()
        
        if rel is None or rel.lower() == "sadie":
            k = "sadie"
        
        if k in statistics.relDescr:
            return statistics.relDescr[k]
        else:
            return ""

    def skills_get_text(skill):
        txt = (skill.name + "\n\n" + skill.description)
        
        txt = (txt + "\n\nWhere can I learn " + skill.name +"?\n")
        expand_actions = actionFinder.getExpandSkillMenuActions(skill.name.lower())
        if expand_actions is not None:
            for menu_action in expand_actions:
                txt = (txt + menu_action.name + "\n")
        
        txt = (txt + "\nWhere can I be inspired by " + skill.name +"?\n")
        give_actions = actionFinder.getGiveInspirationMenuActions(skill.name.lower())
        if give_actions is not None:
            for menu_action in give_actions:
                txt = (txt + menu_action.name + "\n")
        
        return txt

screen skills_relationship:
    $ useFinder = False
    $ txt = ""
    if isinstance(skillDream, str):
        if skillDream == "Family":
            $ skillRelationship = "Sadie"
        else:
            $ skillRelationship = skillDream

        $ txt = skills_get_dream_text(skillRelationship)
    elif isinstance(skillDream, Statistics):
        $ useFinder = True
    elif isinstance(skillDream, Inspirations):
        $ txt = (skillDream.name + "\n\n" + skillDream.getDescr())
    else:
        $ txt = skills_get_rel_text(skillRelationship)

    $ imageName = "SadiePhotoSkills"
    if skillRelationship is not None:
        if skillRelationship.startswith("Skill_") == False and skillRelationship.startswith("Insp_") == False:
            $ imageName = (skillRelationship + "PhotoSkills")

    frame xpos (1802*resFactor/gW) ypos (139*resFactor/gH) xpadding 0 ypadding 0 background None:
        imagebutton:
            idle imageName
            hover imageName







    frame xpos (1971*resFactor/gW) ypos (660*resFactor/gH) xpadding 0 ypadding 0 background None xmaximum (1000*resFactor/gW) ymaximum (920*resFactor/gH):
        has side "c r":

            $ adj = ui.adjustment()

            area (int(0 * resFactor *factor), int(0 * resFactor *factor), int(900 *resFactor *factor), int(2000 *resFactor *factor))

        viewport:
            yadjustment adj
            mousewheel True

            has hbox:
                spacing 5

            if useFinder == False:
                text txt style style.skills_cb
            else:
                vbox:
                    text (skillDream.name + ":") style style.skills_header
                    text ("\n" + skillDream.description) style style.skills_cb
                    $ txt = ("\nWhere can I learn " + skillDream.name +"?")
                    text txt style style.skills_cb
                    $ expand_actions = actionFinder.getExpandSkillMenuActions(skillDream.name.lower())
                    if expand_actions is not None:
                        for menu_action in expand_actions:
                            textbutton ("- " + menu_action[1].name) action [ 
                                        SetVariable("mainMenuAction", menu_action[0].actionMenu),
                                        SetVariable("mainMenuActionFeedback", menu_action[0].random_bubble),
                                        Return()] style style.actionfinder_button text_style style.actionfinder_button

                    $ txt = ("\nWhere can I be inspired by " + skillDream.name +"?")
                    text txt style style.skills_cb
                    $ give_actions = actionFinder.getGiveInspirationMenuActions(skillDream.name.lower())
                    if give_actions is not None:
                        for menu_action in give_actions:
                            textbutton ("- " + menu_action[1].name) action [ 
                                        SetVariable("mainMenuAction", menu_action[0].actionMenu),
                                        SetVariable("mainMenuActionFeedback", menu_action[0].random_bubble),
                                        Return()] style style.actionfinder_button text_style style.actionfinder_button

        bar adjustment adj style "vscrollbar" unscrollable "hide"


screen skills_values:
    if stype is not None:
        frame xpos (1145*resFactor/gW) ypos (327*resFactor/gH) xpadding 0 ypadding 0 background None:
            has vbox
            $ attrs = statistics.get_type_atributes(stype)
            for attr in attrs:
                if attr.startswith("dream of") == False and attr.startswith("relationship with") == False:
                    $ st = statistics.get_stat(attr)
                    grid 2 1:
                        xmaximum (1000*resFactor/gW)
                        xfill True
                        textbutton st.name action [SetVariable("skillRelationship", ("Skill_" + st.name)), SetVariable("skillDream", st)] style style.skills_list_btn
                        text str(st.var) style style.skills_list

screen skills tag menu:


    frame xalign 0.5 yalign 0.5 background "backgroundSkills":
        has fixed

        textbutton "Back" xpos 0.94 ypos 0.01 action Return() text_style style.simple_button_text

        imagebutton xpos float(20.0*resFactor/gW) ypos float(65.0*resFactor/gH):
            idle "witsSkills"
            hover "witsSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Wits type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Wits type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Wits type")
                        ]
        imagebutton xpos float(300.0*resFactor/gW) ypos float(40.0*resFactor/gH):
            idle "knowledgeSkills"
            hover "knowledgeSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Knowledge type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Knowledge type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Knowledge type")
                        ]
        imagebutton xpos float(582.0*resFactor/gW) ypos float(65.0*resFactor/gH):
            idle "stressSkills"
            hover "stressSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Stress type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Stress type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Stress type")
                        ]
        imagebutton xpos float(865.0*resFactor/gW) ypos float(59.0*resFactor/gH):
            idle "athleticsSkills"
            hover "athleticsSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Athletics type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Athletics type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Athletics type")
                        ]
        imagebutton xpos float(136.0*resFactor/gW) ypos float(350.0*resFactor/gH):
            idle "relationshipSkills"
            hover "relationshipSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Relationship type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Relationship type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Relationship type")
                        ]
        imagebutton xpos float(460.0*resFactor/gW) ypos float(358.0*resFactor/gH):
            idle "charmSkills"
            hover "charmSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Charm type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Charm type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Charm type")
                        ]
        imagebutton xpos float(782.0*resFactor/gW) ypos float(339.0*resFactor/gH):
            idle "dreamSkills"
            hover "dreamSkills_h"
            hovered [Hide("skills_values"),
                        Show("skills_values", stype="Dream type")]
            unhovered [Hide("skills_values"),
                        Show("skills_values", stype=skillValues)]
            action [
                        SetVariable("skillValues", "Dream type"),
                        Hide("skills_values"),
                        Show("skills_values", stype="Dream type")
                        ]





























        vbox xpos (518*resFactor/gW) ypos (716*resFactor/gH) spacing int(-10*resFactor*factor):
            text "Inspirations:" style style.skills_header
            null height int(35*resFactor*factor)
            for insp in inspireList.playerList:



                textbutton insp.name style style.skills_cgb:
                    hovered [SetVariable("skillRelationship", ("Insp_"+insp.name)), SetVariable("skillDream", insp)]
                    action [Return()]


        vbox xpos (2455*resFactor/gW) ypos (140*resFactor/gH) spacing int(-10*resFactor*factor):
            text "Relationships:" style style.skills_header
            null height int(30*resFactor*factor)
            style_group "rel"
            $ attrs = statistics.get_type_atributes("Relationship type")
            for attr in attrs:
                if attr.startswith("relationship with ") == True:
                    $ st = statistics.get_stat(attr)
                    $ rn = st.name.replace("Relationship with ", "")
                    if st.var > 0 or rn == "Anna" or rn == "Aunt Evelyn":
                        grid 2 1:
                            xmaximum (700*resFactor/gW)
                            xfill True
                            textbutton rn action [SetVariable("skillRelationship", rn), SetVariable("skillDream", None)] style style.skills_cgb
                            text str(st.var) style style.skills_cg



            $ dr = statistics.get_dream().replace("Dream of ", "")
            grid 2 1:
                xmaximum (700*resFactor/gW)
                xfill True
                textbutton ("Dream of " + dr) action [SetVariable("skillDream", dr)] style style.skills_cgb
                text str(statistics.get_stat_value(statistics.get_dream())) style style.skills_cg

        use skills_relationship

