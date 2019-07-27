label endinterview1:

    scene storyNY

    stop music fadeout 1.0
    play music [ "sound/GypsyGirl.ogg", "sound/DinnerforTwoShallwe.ogg", "sound/WhenYouWantItRightway.ogg"] fadeout 1.0 fadein 1.0

    $ s = Character('Sadie')
    $ n = Character('Professor Hemsworth')
    $ l = Character('Lana Lone')
    $ k = Character('Kheper')

    if statistics.get_stat_value("Relationship with Anna") == 100:
        $ steamApi.SetAchievement('ACH_REL_ANNA_100')

    if statistics.get_stat_value("Relationship with Aunt Evelyn") == 100:
        $ steamApi.SetAchievement('ACH_REL_EVELYN_100')

    if statistics.get_stat_value("Relationship with Ahmose") == 100:
        $ steamApi.SetAchievement('ACH_REL_AHMOSE_100')

    if statistics.get_stat_value("Relationship with Felix") == 100:
        $ steamApi.SetAchievement('ACH_REL_FELIX_100')

    if statistics.get_stat_value("Relationship with Nigel") == 100:
        $ steamApi.SetAchievement('ACH_REL_NIGEL_100')

    if statistics.get_stat_value("Relationship with Roland") == 100:
        $ steamApi.SetAchievement('ACH_REL_ROLAND_100')

    if statistics.get_stat_value("Relationship with Sterling") == 100:
        $ steamApi.SetAchievement('ACH_REL_STERLING_100')

    if statistics.get_stat_value("Athletics") == 100 and statistics.get_stat_value("Grace") == 100 and statistics.get_stat_value("Climbing") == 100 and statistics.get_stat_value("Leaping") == 100 and statistics.get_stat_value("Strength") == 100 and statistics.get_stat_value("Riding") == 100:
        $ steamApi.SetAchievement('ACH_ATHLETICS_BLOCK')

    if statistics.get_stat_value("Charm") == 100 and statistics.get_stat_value("Deception") == 100 and statistics.get_stat_value("Diplomacy") == 100 and statistics.get_stat_value("Flirting") == 100 and statistics.get_stat_value("Negotiation") == 100 and statistics.get_stat_value("Animal Handling") == 100:
        $ steamApi.SetAchievement('ACH_CHARM_BLOCK')

    if statistics.get_stat_value("Knowledge") == 100 and statistics.get_stat_value("Problem Solving") == 100 and statistics.get_stat_value("Language") == 100 and statistics.get_stat_value("Cryptography") == 100 and statistics.get_stat_value("Repair") == 100 and statistics.get_stat_value("Deduction") == 100:
        $ steamApi.SetAchievement('ACH_KNOWLEDGE_BLOCK')

    if statistics.get_stat_value("Stress") == 100 and statistics.get_stat_value("Awareness") == 100 and statistics.get_stat_value("Moxie") == 100 and statistics.get_stat_value("Fisticuffs") == 100 and statistics.get_stat_value("Dodge") == 100 and statistics.get_stat_value("Escape Artistry") == 100:
        $ steamApi.SetAchievement('ACH_STRESS_BLOCK')

    if statistics.get_stat_value("Wits") == 100 and statistics.get_stat_value("Magic Tricks") == 100 and statistics.get_stat_value("Occult Lore") == 100 and statistics.get_stat_value("Stealth") == 100 and statistics.get_stat_value("Poker") == 100 and statistics.get_stat_value("Perception") == 100:
        $ steamApi.SetAchievement('ACH_WITS_BLOCK')

    if statistics.get_stat_value("Dream of Family") == 100:
        $ steamApi.SetAchievement('ACH_DREAM_FAMILY_100')

        if statistics.get_stat_value("Relationship with Ahmose") == 100 and statistics.get_stat_value("Relationship with Felix") == 100 and statistics.get_stat_value("Relationship with Nigel") == 100 and statistics.get_stat_value("Relationship with Roland") == 100 and statistics.get_stat_value("Relationship with Sterling") == 100:
            $ steamApi.SetAchievement('ACH_HEARTBREAKER_COMPLETED')

    if statistics.get_stat_value("Relationship with Ahmose") == 100 and statistics.get_stat_value("Relationship with Anna") == 100 and statistics.get_stat_value("Relationship with Evelyn") == 100 and statistics.get_stat_value("Relationship with Felix") == 100 and statistics.get_stat_value("Relationship with Nigel") == 100 and statistics.get_stat_value("Relationship with Roland") == 100 and statistics.get_stat_value("Relationship with Sterling") == 100:
        $ steamApi.SetAchievement('ACH_REL_MASTER')

    if drivenMainOnly:
        $ steamApi.SetAchievement('ACH_DRIVEN_COMPLETED')

    if zulcounter == 7:
        $ steamApi.SetAchievement('ACH_MAXIMUMZUL_COMPLETED')

    if loreleicounter == 6:
        $ steamApi.SetAchievement('ACH_MAXIMUMLORE_COMPLETED')

    if johnnycounter == 2:
        $ steamApi.SetAchievement('ACH_MAXIMUMJOHNNY_COMPLETED')

        if zulcounter == 7 and loreleicounter == 6:
            $ steamApi.SetAchievement('ACH_THREEWEIRDOS_COMPLETED')

    if newyorkcounter == 13:
        $ steamApi.SetAchievement('ACH_ADV_NY_ALL')

        if egyptcounter == 7 and australiacounter == 8 and indiacounter == 8 and perucounter == 7 and neworleanscounter == 8 and turkeycounter == 7:
            $ steamApi.SetAchievement('ACH_ADV_ALL')

    if gameeasy:
        $ steamApi.SetAchievement('ACH_COMPLETED_EASY')
    elif gamenormal:
        $ steamApi.SetAchievement('ACH_COMPLETED_NORMAL')
    else:
        $ steamApi.SetAchievement('ACH_COMPLETED_HARD')

    show sadie ny proud:
        journal_left
    "{i}It's a beautiful June day as Sadie walks to Professor Hemsworth's office, intent on retrieving a few books for some 'easy reading' now that the term is over. Her exams are done, her work complete, and she's looking forward to a nice, quiet summer as she opens the door... {/i}"

    show sadie ny panicked:
        journal_left_zoominout
    show gossipgirl exuberant:
        journal_center
    "{i}...and is violently tackled by a young woman smelling like an exquisite blend of Jean Pateau's Joy and Canadian whiskey.{/i}"

    l "Hey, Sadie. How you doin', kid? Lana Lone, New York Tribune. Can I ask you a few questions?"

    s "Abuh-wha-huh?"

    show nigel ny excited:
        journal_right
    n "Ah, Sadie, good to see you. I have those books you were asking about, and your timing couldn't be better. Miss Lone was just here asking about you for her article, and I had just finished telling her that she'd be best getting things straight from the horse's mouth, as it were. "

    show sadie ny surprised:
        journal_left
    s "From the... wait, {i}you're{/i} Lana Lone? The society page writer? Wow, I just know you from singing show tunes on top of my aunt's piano at parties - I had no idea!"

    show sadie ny curious:
        journal_left
    s "But what article?"

    l "Yes, I'm writing a feature piece on you for next week's issue... 'The Nighttime Tales of Scheherazade Keating!' Or maybe, 'Lady of One Thousand and One Discoveries!' Gotta nail down a title. I talked to your aunt earlier and she told me she'd break me in half if I went with 'Debutante of the Dunes.'"

    show sadie ny blush:
        journal_left
    s "...Why are you writing an article about me?"

    l "Come on! Surely you must realize that, in the past year, you've made more archaeological breakthroughs - as a student - than most scholars make in their entire lives! Hundreds of artifacts, dozens of cities, countless pieces of history uncovered!"

    if gamehard:

        l "From what I hear, you went out of your way to take on every challenge the world could throw at you. You faced down difficulties lesser sorts - like yours truly - would've just packed up and hid from."

    l "Even if we ignore the Keating legacy, your name is already front and center on the entire archaeological world. You are THE thing right now, Miss Keating, and that makes you news."

    show sadie ny pensive:
        journal_left
    show nigel ny cheerful:
        journal_right

    n "Hey, don't look at me! I just told her you were a good student and a credit to your parents' legacy. And, er, perhaps some details about the occasional dig or exploit here or there."

    if nigelromance:
        show sadie ny weary:
            journal_left
        s "{i}I really hope that's all you told her, bucko, or I'm not going to hear the end of it.{/i}"

    show nigel ny dryly:
        journal_right
    n "But she is right, you know. You might only have finished your first year of university, but you've already made more world-changing discoveries than most people make in a lifetime. It's something to be proud of."

    show sadie ny blush:
        journal_left
    s "Well, I... I mean, I didn't do it for the fame. Preserving the past and helping people learn from it in the future is why I got into this in the first place. I didn't do it to make my name or anything..."

    l "Uh huh. Pull the other one. Anyway, why don't you have a seat in that chair over there, and we can get started. Professor Hemsworth, you're welcome to sit in and add anything you can think of."

    show sadie ny disgusted:
        journal_left
    "{i}So before Sadie has a chance to blink, she finds herself seated and trapped, Lana fixing an eager and hungry glance at her while pulling out her pencil and notebook. Sadie looks wildly at Professor Hemsworth for help, but he only smiles in amused encouragement.{/i}"

    if didnothinginegypt:

        jump endinterview3

    l "All right. Let's start with Egypt, then..."

label endinterview2:


    if secondlibalexandria:

        l "Now, let's get started with the really juicy stuff... the lost library of Alexandria. According to you, you and your Bedouin guide were actually able to find the secondary annex to the Library of Alexandria, and were able to recover scrolls from said library?"

        show sadie ny calm:
            journal_left
        s "That's right... we were exploring the ruins when, unfortunately, we triggered a trap and the whole place came down. Luckily, my friend Rashad was able to grab a few of the scrolls, which we handed in to the authorities."

        l "And what scrolls they were! Scholars have confirmed their authenticity and are dispatching teams to the site you described to see what other artifacts can be gleaned from the remains. Truly exciting!"
        l "(slyly) Speaking of sending teams to sites, isn't there another place you'd like to lead them to?"

        show sadie ny surprised:
            journal_left
        s "Huh?"

        l "Rumor has it that you also gave out the location of the lost tomb of Alexander the Great... but that research teams still haven't found a trace of it."

        show sadie ny blush:
            journal_left
        s "Oh, that."

        show sadie ny calm:
            journal_left
        s "I only found the burial chamber thanks to Rashad's help... I was lost in the catacombs beneath Fort Qaitbey when I ran into him, and he guided me there."
        s "Unfortunately, I could never trace my way back there exactly, not with all the tunnels down there. All I could do was tell the authorities that it was down there, somewhere, and that they'd have to search for it. I guess they haven't found it."

        show sadie ny curious:
            journal_left
        s "But you know, maybe it's for the best. Like Rashad told me, it is a resting place for the dead. Part of me wants it to be found so that it can be preserved and shared with the world, but... another part would like Alexander, or whoever's buried there, to rest easy."

        l "A talent for archaeology AND a sentimental side! This is going to be golden!"

    if egyptiandiscovery:

        l "The other big news from Egypt is, of course, the exhibit of Egyptian artifacts uncovered by Professors Hemsworth and Blake, the one that's opening tonight. It's an open secret to everyone that you claim the credit of a large portion of this exhibit, Miss Keating."

        show sadie ny cheerful:
            journal_left
        s "If I do have any credit, I can thank Professor Hemsworth here."

        show nigel ny excited:
            journal_right
        n "Don't be modest, Sadie. I was just telling Miss Lone about how we accidentally fell into that gold chamber."

        l "Haha, you could say that that was when you 'fell' for each other!"

        if nigelromance:

            show nigel ny nervous:
                journal_right
            show sadie ny blush:
                journal_left
            s "...Uh, sure, right. (coughs)."

            n "{i}(Adjusts his collar) My, this office is rather warm.{/i}"

        l "I've heard rumors that the path from Egypt to this New York exhibit wasn't exactly smooth, though. Could you tell me a bit about that?"

        if recoverartifactsegypt:

            show sadie ny curious:
                journal_left
            s "Well, there was that gang in Egypt that stole all the artifacts off the airfield tarmac..."

            l "Really? How did you recover them?"

            show sadie ny laughing:
                journal_left
            s "Would you believe we followed them to a museum and engaged in some old-fashioned fisticuffs?"

            l "(writing madly) Oh goodness, this is gold!"


        if bigdaddydefeated:

            show sadie ny triumphant:
                journal_left
            s "Does a crazed New Orleans gangster grabbing some of our artifacts for his private collection count as a bump in the road?"

            l "Big Daddy Dan! It was all over the news in New Orleans. You were the one who brought Big Daddy down! How did you do it?"

            show sadie ny cheerful:
                journal_left

            if nigelromance:

                s "Well, I had help from someone very important. (Shares a radiant smile with Nigel)"
            else:

                s "Well, I didn't bring him down by myself, you know. Professor Hemsworth helped. A little. (Winks at him)"

            show sadie ny flirtatious:
                journal_left
            s "We did it with two nice costumes, a helpful chef, and one idiot's giant ego."

            l "Brilliant!"

        show sadie ny calm:
            journal_left
        s "Really, archaeology never really 'goes smoothly.' Even the most routine dig has its ups and downs, its surprises. It's just part of the terrain."

        l "You two really do seem to make a brilliant team, though, if you don't mind me saying."

        show nigel ny cheerful:
            journal_right
        show sadie ny cheerful:
            journal_left

        if nigelromance:

            n "I'd say we most certainly are."

            s "And we hope we continue to be."
        else:


            'Nigel and Sadie' "Why, thank you!"


    if rolandegypt:

        l "I'd like to talk about the discovery you made in Professor Blake's dig. He was excavating a pyramid and unearthed an elaborate burial chamber along with four canopic jars, but you uncovered something even more impressive... a scroll referring to someone called the Lost King?"

        show sadie ny surprised:
            journal_left
        s "{i}Yes, of course... that was the scroll that Roland saved for me when we came out of the pyramid, the one he made a copy of.{/i}"
        if sawbernarddie:
            show sadie ny sad:
                journal_left
            s "{i}That was the first time I ever met Bernard.{/i}"
        if rolandromance:
            show sadie ny blush:
                journal_left
            s "{i}Roland... even then, he was looking out for me, trying to make me smile in his own way.{/i}"

        show sadie ny cheerful:
            journal_left
        s "That's right, Miss Lone. I, ah, found the scroll separate from Professor Blake's dig and handed it in to Professor Hemsworth here. It's a very interesting piece... it speaks of a forgotten king who worked from the shadows to protect his kingdom, and no one would ever remember him. Very sad, really."

        l "But now, thanks to you and the museum it's now housed in, thousands of people will remember him. You're doing great work!"

        show sadie ny blush:
            journal_left
        s "Thank you..."

    if metzulinegypt:

        l "Let's talk about your discoveries at the pyramid of... um... Ahmose-whatsis, the one where your team recovered the sarcophagus and other artifacts..."

        hide nigel
        show kheper bragging:
            journal_right
        k "Ooh, ooh! I think she's talking about us!"

        show sadie ny weary:
            journal_left
        s "{i}Psst!{/i} Keep your voice down!"
        hide kheper
        show nigel ny curious:
            journal_right

        l "I'm sorry?"

        show sadie ny cheerful:
            journal_left
        s "Oh, nothing."

        l "I understand there was some drama on site, something to do with the theft of some artifacts by someone called the Pirate of the Sand Seas...."

        show sadie ny surprised:
            journal_left
        s "{i}Wow, she's really well connected. I wonder if there's anything she doesn't know?{/i}"

        if ahmoseromance:
            show sadie ny cheerful:
                journal_left
            s "{i}Well, I imagine she doesn't know I'm dating a mummy... that sort of thing tends not to get out. I hope.{/i}"

        show sadie ny calm:
            journal_left
        s "Yes, well, that's true... he took an artifact of great importance, but we were able to return the rest of our findings to the museum here in New York. We found quite a lot of very unique artifacts, some very valuable. The... man who was buried there was a nobleman."

        l "Fascinating! Was this a particularly interesting or important dig for you?"

        if ahmoseromance:
            show sadie ny blush:
                journal_left
            s "Yes... probably one of the most important digs I've ever been on, really. I... met someone very special there, so this expedition will always have a special place in my heart."

            hide nigel
            show kheper pleased:
                journal_right
            k "Awwwwwwwwwwwwwwww...I know you worship me, but what about Ahmose?"
            hide kheper
            show nigel ny curious:
                journal_right
        else:

            show sadie ny proud:
                journal_left
            s "Every dig is important and interesting! But yes, it definitely was, not least because I made a new friend there."

        l "And yet another feather in the cap of Sadie Keating, I'll bet!"

    if lotustomb:

        l "Now, moving on... Professor Blake has recently gained a permit for excavation of a previously undiscovered tomb related to a nobleman's daughter out in the Egyptian desert, but a little bird told me that you had some hand in this?"

        show sadie ny surprised:
            journal_left
        s "What? Oh, yes..."

        show sadie ny pensive:
            journal_left
        s "{i}That's right... Sterling and I already went out to that tomb while Blake was still twittering about permits.{/i}"

        if sterlingromance:
            show sadie ny sad:
                journal_left
            s "{i}Sterling... I hope he's okay...{/i}"

        show sadie ny calm:
            journal_left
        s "Well, I, er, certainly can't claim credit from Professor Blake, but I did uncover a tablet with a distinctive lotus motif which gave directions to a tomb that would only be revealed at noon. But, um, of course, Professor Blake was the driving force behind the whole thing..."

        l "Nonsense! I think you're just being modest. And even if your name isn't on the project right now, it will be once I get done with this article, or my name's not Lana Lone!"

    if sekhmetherb:

        l "Now, there's one story that's been making the rounds in diplomatic circles for ages. I'm almost embarrassed to ask, since it doesn't seem... well, archaeological, but what's the scoop with all these stories of a plague, and you finding the three thousand year old cure?"

        show sadie ny cheerful:
            journal_left

        s "Oh, right! Honestly, that was dumb luck as much as anything else. My friend Felix and I got separated from the rest of the Professor's class, and we came upon this really interesting little community kind of en route to the Valley of the Kings."

        if felixromance:

            s "{i}And Felix dragged me off away from the crowds and got me dancing. I bet I could've kissed him then...{/i}"

        show sadie ny sad:
            journal_left

        s "But almost immediately there was an outbreak of... I don't know, some kind of virus."

        show sadie ny calm:
            journal_left

        s "That's really where the dumb luck comes in. I've had an interest in Sekhmet and some of the other Egyptian goddesses whose roles extend past simple fertility cult stuff... well, for ages. And some of the old Sekhmet traditions actually turned out to suggest medicinal applications to the local plant life."

        show nigel ny dryly:
            journal_right

        n "That's not just dumb luck, Sadie. You may have saved lives with some very creative scholarship - I'd honestly recommend you and Felix for medals if I knew who gave them out."

        show sadie ny cheerful:
            journal_left

        s "Awwwww."

        l "I love this. You two are gold!"



label endinterview3:



    l "Moving on a bit, I'd like to talk a bit about things you got up to in Australia. It sounds like things were quite exciting there too!"

    if aushieroglyphs:

        l "The biggest news of all, of course, and in my opinion the biggest discovery of your career, of the entire year, of the entire decade, would be the revelation of Egyptian hieroglyphs in Australia. Scholars everywhere are still buzzing over this. Please, tell me how on earth you uncovered them?"

        hide nigel
        show kheper wry:
            journal_right
        k "Well, you see, when a man and a woman and another woman decide they really really want to commit art fraud for the greater good, they..."
        hide kheper
        "{i}The rest of his sentence is muffled as Sadie stuffs him neatly back into a pocket, leaving Lana Lone none the wiser.{/i}"
        show nigel ny curious:
            journal_right

        show sadie ny cheerful:
            journal_left
        s "Well, uh, I happened to discover it thanks to some friends I made in the native Aboriginal community. The amount of knowledge and history they've kept alive has been astounding, including the knowledge of Egyptians somehow making their way to Australia thousands of years ago."

        l "But how?"

        s "Ah, now that I can't answer... I'm afraid I'm an archaeologist, not an engineer or transit expert!"

        l "The ramifications of this are astounding... to learn that Egyptians were capable of intercontinental travel! What else could they be capable of?"

        if ahmoseromance:
            hide nigel
            show kheper wry:
                journal_right
            k "(muffled) What indeed? Let me tell you, a man like Ahmose can MMMPH! (squeaks as Sadie squeezes him back into the pocket)"
            hide kheper
            show nigel ny curious:
                journal_right
        else:
            show sadie ny laughing:
                journal_left
            s "Oh, I'm sure there are limits. I can't imagine they'd, oh, find a way to translate any language or animate the dead or anything like that."
            "{i}An indignant mumble is heard from her pocket, but no one else hears it.{/i}"

        l "Your name is going to go down in the history books, you realize? Scheherazade Keating, the woman who discovered Egyptians in Australia. Glorious!"
        l "Now, around the same time, there was a bit of another important discovery going on, or at least so everyone thought. Can you weigh in on the controversy surrounding Dr. Pavier, Steven Deveny, and the fake grinding bowl they claimed to discover?"

        show sadie ny nervous:
            journal_left
        s "{i}Controversy? Oh dear. No wonder Steven was annoyed. Well, the least I can do is stick up for him...{/i}"

        show sadie ny determined:
            journal_left
        s "As far as I'm concerned, I have the utmost respect for Dr. Pavier, and while Steven and I have had our differences, I have no reason to think he would ever falsify a discovery or not verify an artifact's authenticity. I believe their explanation about someone stealing the original artifact and replacing it with a copy."

        l "But who would do such a thing, and why?"

        show sadie ny weary:
            journal_left
        s "{i}Help me out here, Nardu...{/i}"

        show sadie ny calm:
            journal_left
        s "It was a priceless artifact, so perhaps just regular art thieves. Or perhaps... someone felt the original belonged with the native people rather than a museum."

        if ahmoseromance:
            s "{i}An answer Ahmose would be proud of, I hope.{/i}"

        s "In any event, I stand with Mr. Deveny and Dr. Pavier. I hope their next exhibition goes a bit more smoothly."

        l "Gracious to rivals as well! You are a wonder..."

    if secondtotem:

        l "Now, Professor Elizabeth Eora has recently unveiled a new Aboriginal totem at the Sydney University Museum, and she took special care to mention you as a vital contributor. Can you tell us a bit about what happened there?"

        show sadie ny sad:
            journal_left
        s "{i}Well, it's not like I found the totem... that was all Sterling. His way of saying sorry, I suppose, for all the other mess.{/i}"

        if sterlingromance:
            s "{i}How many times has he tried to make things up to me? Even now, when he's... no, I can't think about that right now.{/i}"

        show sadie ny calm:
            journal_left
        s "I'm afraid I can't take credit. The totem was shipped to us by an anonymous donor. All I did was come along for the expedition and discover where the totem was originally situated."

        l "Well, that's still pretty nifty, considering you got to explore a sunken galleon and an old burial ground."
        l "And you certainly CAN take credit for the arrest of Kate Leigh, right? My sources in Australia are very specific on that point."

        show sadie ny laughing:
            journal_left
        s "Well, far be it for me to argue with your sources!"

        l "Have you ever considered going into law enforcement?"

        show sadie ny teasing:
            journal_left
        s "Believe it or not, you're not the first person to ask."

        if sterlingromance:
            s "{i}If nothing else, it would certainly make my relationship with Sterling a bit more dramatic!{/i}"

        l "Well, I for one prefer having you as an archaeologist if it means we keep on getting fantastic finds!"

    if homelessart:

        l "I understand some congratulations are in order for solving a mystery that had haunted an Australian scholar for months."

        show sadie ny confused:
            journal_left
        s "Oh?"

        l "Returning the Aboriginal art pieces to Dr. Pavier's colleague?"

        show sadie ny laughing:
            journal_left
        s "Oh, yes, of course! Well, it's the least I could do."

        l "You're too modest! It was a great find and certainly won you some reputation among the Australian intelligentsia."

        show sadie ny calm:
            journal_left
        s "The truth is, I mostly just stumbled upon it. I only got involved because I was trying to help this one homeless man... one thing led to another, and we found this hiding spot with all these Aboriginal art pieces."

        l "Some of them broken, I gather? Horrible. Still, excellent work in recovering them!"


    if cyriactheimposter:

        l "Is it true that you and the Professor both unmasked a fake Dr. Pavier?"

        show nigel ny dryly:
            journal_right
        n "Again, 'both' is a bit of an exaggeration. I'd say Sadie did most of the unmasking while I ran around and attempted to appear useful."

        if nigelromance:
            show sadie ny sad:
                journal_left
            s "Nigel, you know you're worth a lot more than just that."
        else:

            show sadie ny teasing:
                journal_left
            s "Oh come on, Nigel, you know you're not that bad."

        l "Oh, 'Nigel,' eh?"

        show nigel ny cheerful:
            journal_right
        n "But yes, we did manage to stop an imposter from taking over his identity."

        show sadie ny weary:
            journal_left
        s "{i}I'm not sure Pavier's staff would do the same.{/i}"

    if cadmancottage:

        l "So what's this about you discovering the lost treasures of John Cadman and preserving a heritage house?"

        show sadie ny laughing:
            journal_left
        s "Oh, it's a long story. Short version is that Kate Leigh's crew were going to knock down his old house, but we were able to figure out the clues Cadman had left and found a safe full of money and jewels and other valuables."

        show sadie ny calm:
            journal_left
        s "The residents were able to use that money to preserve the house and set it up as a heritage site that takes in low-income people in the area."

        l "Hmm, who is this 'we'? You didn't discover this alone?"

        show sadie ny cheerful:
            journal_left
        s "No... I had the help of a very old, dear friend of mine."

        if felixromance:
            s "{i}And hopefully he'll be more than that.{/i}"

        l "Ooh, old dear friends sell lots of papers. Tell me more?"

        show sadie ny determined:
            journal_left
        s "He's very passionate about the plight of the unemployed and poor, both here and abroad. In fact, we'd been talking about displaced Sydney residents when the whole Cadman thing went down, so it really all tied in."

        if felixromance:
            show sadie ny sad:
                journal_left
            s "He's... a very good man."

        l "Better and better!"

    if metzulinplatypus:

        l "One question before moving on... what's all this about a platypus painting and a treasure hunt?"

        show sadie ny nervous:
            journal_left
        s "Uh... no comment."





label endinterview4:

    show sadie ny calm:
        journal_left
    l "Moving around the globe a bit, I'd like to talk about your adventures and discoveries in India."

    if naraka:

        l "I think it's safe to say that the big red-letter discovery for you is, of course, the underground city of Naraka. It's going to take researchers years to fully study its secrets. And its discovery is all thanks to you."

        show sadie ny curious:
            journal_left
        s "{i}Well, not exactly... it was really Sterling who got us moving there in the first place, even if I did solve all the puzzles.{/i}"

        if sterlingromance:
            show sadie ny sad:
                journal_left
            s "{i}That was when Sterling started to act strangely, after that thing with the mirror... I guess he realized then that I was the one Ruddy was looking for. He was... just trying to protect me.{/i}"

            show sadie ny determined:
                journal_left
            s "{i}Well, I wish he wouldn't! I can take care of myself!{/i}"

        show sadie ny calm:
            journal_left
        s "I had a friend of sorts who helped me out... got me pointed in the right direction, you could say. I can't really take full credit."

        l "There's that modesty again. Friend or no, you're still the one who approached Indian archaeologists with the location of the site."
        l "Do you think you'd like to go back there to excavate Naraka?"

        show sadie ny laughing:
            journal_left
        s "Of course! I just have to slot it in between the other ten places I want to revisit!"

        l "Haha! I can imagine!"

    if mosqueemerald:

        l "Now, Professor Hemsworth was just telling me a rather interesting story about some of your adventures around India... I particularly liked the one about finding an emerald and causing a mosque roof to collapse."

        show sadie ny disgusted:
            journal_left
        s "{i}ohnohetoldyouthat{/i}"

        if sterlingromance:
            s "{i}I'm going to kill Sterling when I see him again. Once I stop cuddling with him, that is. Yes, that's it, I will cuddle him to death.{/i}"

        l "What's your stance on destroying one monument to uncover another piece of history?"

        show sadie ny determined:
            journal_left
        s "I don't stand by it, and normally I always try to preserve. In India, things happened too quickly, and I didn't realize what would happen. I feel terrible for the damage, but at least the emerald and the other gems I found are in good hands now."

        l "And you were quite busy, weren't you? Finding secret chambers in Ahmedabad, exploring temples in Wadhwam, finding statue-controlled elevators in Gujarat... the discoveries just keep coming!"

        show sadie ny blush:
            journal_left
        s "I don't think I discovered anything life changing..."

        l "Uh huh. Tell that to the poor undergrads who are going to be working away at your dig sites for the next three years, hon!"

    if sawbernarddie:


        l "What with your interests, I'm surprised you didn't try to examine the temple of Sati Ranakdevi for more discoveries. I can imagine the things they likely have in there would be phenomenal."

        show sadie ny sad:
            journal_left
        s "...No, I think it's best to leave that temple alone. Some things are... better left undisturbed."

        if rolandromance:
            "{i}She says no more on the subject, but winces at the memory of Roland's hand burning through Bernard's last moments.{/i}"

    if codebook:

        l "Okay... so, what's the story behind you turning in a dagger from the Tippoo Sultan? Legend has that treasure was missing."

        show sadie ny proud:
            journal_left
        s "It was. But apparently there were still a few pieces in circulation. I, ah, managed to acquire one through a friend."
        s "{i}Who took it off of a thug working for a spy who was using it to fool us into a trap, but meh, details!{/i}"

        l "That must be some friend!"

        if rolandromance:
            show sadie ny cheerful:
                journal_left
            s "{i}It was very sweet of Roland to hand over the dagger after we'd dealt with Stravinsky. I can't help it if being all honorable and upright gets me all weak in the knees.{/i}"
        else:
            show sadie ny laughing:
                journal_left
            s "Trust me, he's a character, I'll say that much! And he got as good as he gave, believe me."

    if methickok:

        show sadie ny curious:
            journal_left

        l "Oh, hey. Some of my military friends tell me you headed off some kind of mutiny in the jungle?"

        show nigel ny concerned:
            journal_right

        n "She what? You {i}what?{/i}"

        s "Felix didn't tell you?"

        n "No!"

        show sadie ny calm:
            journal_left

        s "Well, he - the Professor's assistant, Felix - really did all the work. There was this crooked officer who was using his position to smuggle opium, and..."

        n "There was a what -?"

        s "Yeah, that's why the British Army had to stop working with us in the field for a while; there was a whole investigation. Felix found proof of Hickok's wrongdoing, so Hickok had him arrested and lined up for summary execution, and I got all huffy about it so they tied me up too."

        n "And you didn't think this was worth mentioning?"

        s "Well, we obviously broke out, and it all ended well. We got to Hickok's commanding officer before he could be assassinated, and... well, the rest is history. Again, it really was more Felix's doing than mine."

        s "He probably didn't tell you because he thought you'd think he was angling for a raise. He's weird that way."

        if felixromance:

            s "{i}And adorable. I probably shouldn't say that out loud.{/i}"

        show nigel ny dryly:
            journal_right

        n "He {i}should{/i} angle for a raise, actually. He's been doing the work of at least four men ever since he signed on."

        n "And that's even without becoming a hero of the British Empire. Good Lord. I knew I liked that fellow."

        l "Oh, this is just superb stuff."




label endinterview5:

    l "So, according to my notes, you were next in Peru, is that right?"

    show sadie ny calm:
        journal_left
    s "Yes, that's right."

    if ruddyoldruins:

        l "I gather you were responsible for the re-discovery of Rüdeger Von Prenzwald's old dig site... an ancient Wari temple in the middle of the jungle, no?"

        s "Yes. The Wari were the precursors to the Inca, though not much of their civilization remains."

        l "How did you rediscover it?"

        show sadie ny proud:
            journal_left
        s "Well, as a matter of fact, I'd gotten separated from my aunt during a pleasure cruise down the Amazon... I found a guide who led me to a cliff where we saw some ancient structures built into the cliff face. That was how I gained access and found it."

        l "Incredible! You realize that with the re-opening of this site, historians will be able to learn much more about this ancient tribe! So why was the site abandoned in the first place?"

        show sadie ny sad:
            journal_left
        s "I... I can't really answer that. {i}Ruddy...{/i}"

        l "You were also able to uncover a really interesting chunk of black rock from the site, right?"

        show sadie ny cheerful:
            journal_left
        s "Oh, yes, the obsidian. It actually produces some energy... I was able to power a radio with it. They're currently studying it at the university... they're hoping to have it on display sometime next year."

        l "I imagine some people would be more interested in keeping that gem for personal use rather than turning it in to the authorities."

        show sadie ny injured pride:
            journal_left
        s "Ha ha, yes, imagine that, using it for personal aims. Unthinkable."

    if sadieglyph:

        l "Also, congratulations on the discovery of Sadie's Spider! Dr. Julio Tello has named the most recent geoglyph site after you. Imagine your very own geoglyph!"

        show sadie ny blush:
            journal_left
        s "Well, it wasn't a hugely amazing thing I did... I just happened to be looking out the right window in the aircraft."

        hide nigel
        show kheper pleased:
            journal_right
        k "Well, having a certain someone along for good luck probably didn't hurt!"
        hide kheper
        show nigel ny curious:
            journal_right

        l "What does it feel like to know there's an enormous spider glyph out there with your name on it?"

        show sadie ny nervous:
            journal_left
        s "... kinda creepy, when you put it that way."

        l "(laughs) True, true!"

        if ahmoseromance:
            show sadie ny pensive:
                journal_left
            s "{i}Maybe now all this Ruby Eye business is over, I can take Ahmose there to see the glyphs in person. I think he'd like that...{/i}"

            show sadie ny blush:
                journal_left
            s "{i}Even if I did love being able to share it with him from a distance, it would mean so much more to share it with him in person.{/i}"


    if bolivarblocked:

        l "Tell me a bit about this amazing Peruvian burial vase you found and the site you uncovered. The entire country is buzzing about it!"

        show sadie ny sad:
            journal_left
        s "That I definitely can't take credit for. My... my parents originally found the site."

        l "Oh! A true Keating legacy, then. They left some sort of message for you, then?"

        show sadie ny weary:
            journal_left
        s "No... unfortunately, their fraud of an assistant was the only one who knew where it was. He basically got Nigel and I to go do his dirty work."

        l "That's right! Professor Hemsworth here was part of that discovery. My word, Professor, you make almost as many discoveries as your student!"

        if nigelromance:
            show nigel ny cheerful:
                journal_right
            n "Not at all. We make discoveries {i}together.{/i}"
            show sadie ny cheerful:
                journal_left
            s "{i}Awww, Nigel... you always say such sweet things.{/i}"
            show nigel ny dryly:
                journal_right
        else:
            show nigel ny dryly:
                journal_right
            n "Ah, you see, my trade secret is to follow along behind Miss Keating at all times and bask in her reflected glory."
            show sadie ny teasing:
                journal_left
            s "The truth comes out! You're leeching off my success!"
            n "It seems to have worked so far."
            s "Point."

        l "The burial vase in question is incredible... people say it almost glows. And there were other artifacts discovered. Do you think this could change the way we think about ancient Peruvian culture?"

        show sadie ny excited:
            journal_left
        s "Miss Lone, the wonderful thing about archaeology is that everything we find can change the way we think about a culture. Not just the major finds of gold and gems, but the little things like pottery, tools... things used day to day. My discovery might be rather dramatic, but there are plenty of hardworking archaeologists out there making discoveries just as meaningful."

        n "As one of said boring, hardworking archaeologists, that's very well said, Sadie."

        l "Ooh, you are a treasure! Such politeness!"

    if chavindehuantar:

        l "Tell me a bit about how you helped Dr. Tello discover the lost gems of Chavin de Huantar!"

        show sadie ny blush:
            journal_left
        s "Well... more like I was in the general vicinity of the discovery when it happened."

        l "Miss Keating, isn't it true that Dr. Tello was kidnapped and held ransom for his knowledge of the site, and that you foiled his kidnappers?"

        show sadie ny proud:
            journal_left
        s "Well, I think the credit goes to Dr. Tello's niece, Claudia. Let's just say she's a bit of a spitfire."

        l "So what happened?"

        show sadie ny calm:
            journal_left
        s "We met the kidnappers at Chavin de Huantar, where things got a bit loopy... I managed to help Dr. Tello get away, we all got separated, it was very confusing. The site is like a maze, you see."
        s "As we were running from the kidnappers, we happened to stumble upon a large stone chest filled with sapphires and other jewelry. Apparently they'd taken Dr. Tello thinking he knew where the treasure was."

        l "And now it's in a museum, where it belongs!"
        l "Tell the truth, though... were you not even slightly tempted, maybe just a bit, to keep some of the jewelry for yourself?"

        show sadie ny teasing:
            journal_left
        s "Ask me no questions, and I'll tell you no lies."

        l "Ha ha! I knew it!"

    if choquequirao:

        l "You were part of the team that began excavation on Choquequirao, the city of gold. Now, you made quite a few waves with your early reports, particularly your emphasis on the guardian triad: the puma, the condor and the snake. Why did you focus on that?"

        show sadie ny weary:
            journal_left
        s "{i}I suppose 'Because I met three weird spirits in a temple in the middle of the night' wouldn't exactly win her over.{/i}"

        show sadie ny calm:
            journal_left
        s "The motifs were all over the site, particularly the underground sections. It was clear that these animal symbols were of great religious significance."

        l "While you were part of a larger archaeological group sent to excavate, it seems your name, as usual, is getting top billing for the amazing discoveries that came out of there, particularly the underground lake and catacombs. How do you feel about that?"

        show sadie ny determined:
            journal_left
        s "Firstly, even if I did stumble on those parts, it's thanks to the hard work of the rest of the team that they can be fully uncovered and catalogued. No archaeologist really works alone."
        s "Secondly, I didn't even find the rest of it alone. I had a very dear friend who was with me during the initial visit."

        l "Oh? A dear friend?"

        if felixromance:
            show sadie ny blush:
                journal_left
            s "Very dear."
        else:
            show sadie ny cheerful:
                journal_left
            s "He's an old friend who just returned to New York this year. He's been a great help on these adventures."

        l "Ha ha, I'll bet."

    if rivalperudone:
        l "I'd love to hear a bit more about your discoveries related to Conde de Lemos, particularly the storerooms in his house and mine."

        show sadie ny weary:
            journal_left
        s "To be honest, I don't have the best memory of that particular expedition. It... one of my friends, Anna, was very badly affected by what we uncovered."

        if sterlingromance:
            s "{i}And that was when Sterling tried to say goodbye forever. I don't even want to think about it, not after what happened in Turkey...{/i}"

        l "Oh, can you tell me more?"

        s "Not really, but... let's just say that the Conde de Lemos was an incredibly cruel, vicious and greedy man, and leave it at that."

        l "Researchers are still poring over all the items found in the Conde's house as well as the secret chamber in the Layakakota mine. Apparently there are hundreds of gold pieces in each of them!"
        l "But there's also great interest in the incredibly detailed notes you were able to provide regarding a large Incan sun totem. Could you tell us how you procured these notes and where the totem is?"

        show sadie ny surprised:
            journal_left
        s "Uh..."

        show sadie ny calm:
            journal_left
        s "As far as I could tell, the storeroom in Layakakota used to have that statue in it, but, uh... a previous robber must have gained access and stolen it before we found it. He must have taken notes on it before moving it and forgotten those notes, because, er, they were there when we got there."

        if sterlingromance:
            s "{i}Oh, the little white lies I tell for your sake, Sterling Evans...{/i}"

        l "A shame, but at least the notes are detailed enough to keep researchers busy for years... assuming there was actually such a statue, mind you! Where do you think it would be now?"

        if ruddyexposedinno:
            show sadie ny flirtatious:
                journal_left
            s "Could be anywhere, really... maybe even in a New Orleans villa."

            l "Haha! I suppose anything is possible!"
        else:
            show sadie ny curious:
                journal_left
            s "I honestly don't know."

    if peruvianlake:

        show sadie ny calm:
            journal_left

        l "I understand you had a major discovery at Choquequirao? One that had a bunch of old fuddy-duddies screaming that you were advocating a return to paganism?"

        show sadie ny irritated:
            journal_left

        s "Oh, I remember the screaming. But that wasn't my point at all. Felix, the Professor's assistant, and I really had to think about the culture that produced that complex as we were... finding our way past some of its defenses... and I just thought, and think, that we owe it to the people who came before us, and to ourselves, to really try to understand how they made sense of the world."

        show sadie ny calm:
            journal_left

        s "We're talking about a civilization that thrived for hundreds of years. It wouldn't have lasted as long as it did if it didn't have some insights that really worked."

        s "{i}Of course, they also had puma spirits with bad attitudes.{/i}"

        if felixromance:

            s "{i}Good thing I had Felix there to help me stare the old ghosts down...{/i}"

        l "Kind of a wistful look in your eye for a second there. Anything you're not telling me?"

        show sadie ny cheerful:
            journal_left

        s "Miss Lone, I simply don't know what you mean."





label endinterview6:
    l "Next up... I understand you just came back from Turkey, right?"

    show sadie ny cheerful:
        journal_left
    s "Yes, that's right. Not long ago, actually."

    l "Would you mind telling us about some of the things you did, particularly your finds in regards to Pergamon?"

    s "Such as?"

    if marclettercredit:

        l "Well, first off, let's go into the absolutely amazing news that you were the one to actually find a love letter from Marc Antony to Cleopatra! I mean, this is like the Holy Grail of finds... romance and history and all the wonderful meaty stuff people love. How on earth did you uncover something like that?"

        show sadie ny blush:
            journal_left
        s "Well, it was mostly thanks to my parents, to be honest... they left some clues in their diary and had hidden the letter away so it wouldn't be found and exploited."

        l "How wonderful! A real treasure passed from parent to child. It'll be part of the Cleopatra legend, for sure! I gather there was also some excitement when you recovered it?"

        show sadie ny cheerful:
            journal_left
        s "Let's just say that bullets were exchanged."

        l "Oooh! Thank goodness you are in one piece!"
        l "Why did you decide to leave the letter in Turkey, though? Seems to me it would be most welcome in the Metropolitan Museum's collection, or the German Pergamon museum, or maybe even in an Egyptian museum as part of a Cleopatra exhibit."

        show sadie ny determined:
            journal_left
        s "Yes, but part of being a good archaeologist involves respecting the countries you're digging in. This letter was found in Turkey, and given the... negotiations with certain parties, it seemed clear that it should therefore remain in Turkey."

        l "An interesting perspective! But at least you were able to gain full credit... I understand your name has pride of place on the museum placard."

        show sadie ny blush:
            journal_left
        s "Well, I would have turned it in regardless, but... it's nice to be recognized, I admit."

        l "I can imagine!"

    if perglostscrolls:

        l "I'm really curious about these Lost Scrolls of Pergamon that you found. What was that all about?"

        show sadie ny pensive:
            journal_left
        s "Well, the Pergamon Library was emptied and destroyed thousands of years ago, but there were still caches of scrolls and books hidden away... I stumbled across one of those caches."

        l "You understate the significance of your discovery. Hundreds and thousands of scrolls saved from destruction in Alexandria, right? Tomes and tomes of ancient knowledge, all with the potential to blow the lid open on Pergamon! How did you find them?"

        show sadie ny proud:
            journal_left
        s "Would you believe I tripped over them?"

        l "Haha! No, but it certainly sounds interesting on paper!"

        if wenthomeearly:
            l "Now onto the thing that's really got people buzzing. Biggest find of the century - besides, you know, all your other ones - and a huge excavation organized with Dr. Krause... and yet you come home and leave your big discovery behind. Why?"

            show sadie ny sad:
                journal_left
            s "Well... you see... There's something important I have to do here in New York. Something that made me realize there's more to life than just archaeology."

            l "And it couldn't have waited until after you were done with your find?"

            s "If I'd waited, I don't think I would have had the courage to try. Even now, I... I haven't had the strength to try."

            l "Oooooh.... I think I see where this is going! Best of luck to you on that score, if you know what I mean."
        else:
            l "So after you discovered all that, you're on the cusp of the largest discovery of the century, ready to be there for YOUR dig... and the university calls you back for your examinations?"

            show sadie ny cheerful:
                journal_left
            s "Hey, I don't make the rules. Besides, Dr. Krause will be handling the initial organization, and I'll be joining her as soon as possible. I seem to have become rather busy as of late!"

            l "(laughing) I can imagine!"


    if felldownwellsterling:

        l "What's this about falling down a well and finding the lost city of Iram?"

        show sadie ny excited:
            journal_left
        s "Oh, that? Well, things are still in very early days yet... it's going to take a few months of excavation. But yes, I did fall down an oasis well and found at least what looks like the entrance to Iram."

        l "Just out there in the middle of the desert! Incredible. Did you actually see the city?"

        show sadie ny weary:
            journal_left
        s "Uh, well... yes... sort of... maybe... I don't know."

        show sadie ny cheerful:
            journal_left
        s "But there is definitely a maze down there, and I hope the archaeologists will be able to uncover more down there."

        l "I understand Dr. Von Prenzwald was involved with this particular dig?"

        show sadie ny sad:
            journal_left
        s "...Yes, somewhat. He was... he was there for the initial discovery."

        if sterlingromance:
            s "{i}So was Sterling... he was trying to warn me even then about Ruddy... He really does care about me.{/i}"

        l "I hope the excavators find something!"

    if felldownwellanna:

        l "What's this about falling down a well and finding the lost city of Iram?"

        show sadie ny excited:
            journal_left
        s "Oh, that? Well, things are still in very early days yet... it's going to take a few months of excavation. But yes, I did fall down an oasis well and found at least what looks like the entrance to Iram."

        l "Just out there in the middle of the desert! Incredible. Did you actually see the city?"

        show sadie ny weary:
            journal_left
        s "Uh, well... yes... sort of... maybe... I don't know."

        show sadie ny cheerful:
            journal_left
        s "But there is definitely a maze down there, and I hope the archaeologists will be able to uncover more down there."

        l "I understand Dr. Von Prenzwald was involved with this particular dig?"

        show sadie ny sad:
            journal_left
        s "...Yes, somewhat. He was... he was there for the initial discovery."

        l "I hope the excavators find something!"


    if zularrested:

        l "You also had a role in the arrest of the notorious antiquities thief, Zul al Zan."

        show sadie ny laughing:
            journal_left
        s "More like Dr. Krause figured it out and I just confirmed it, but yes."

        l "The amount of stuff recovered from his house was astonishing! Dr. Krause says that all of it is being returned to museums in their home countries, and that they have you to thank."

        show sadie ny blush:
            journal_left
        s "I just wanted to do the right thing."

        hide nigel
        show kheper wry:
            journal_right
        k "Ooh! Ooh! Is this where you also talk about the Ruby Eye and maybe stealing it for yours- MMPH! (is quickly silenced)"
        hide kheper
        show nigel ny curious:
            journal_right

    if lorelikessterling:

        l "Can you comment on the rumors that you were involved in a major cave-in at a private German dig site in Gobleki?"

        show sadie ny sad:
            journal_left
        s "...No. No, I'm afraid I can't."

        l "Pity. I hear the excavation was on a possible site for the Library of Pergamon or some satellite installation. You wouldn't know anything about that, would you?"

        s "{i}I'd know all sorts of things, but... I think some things are best left to rest.{/i}"

        if sterlingromance:
            s "{i}And Sterling was injured... I still haven't heard from him to see if he's all right. What if he's... no, I can't think like that.{/i}"

        show sadie ny calm:
            journal_left
        s "As I said, no comment."





label endinterview7:

    l "I'm getting near the end of the interview, so I want to look at things a bit closer to home. You've been having a few adventures in America as well, haven't you? Even in New York City itself!"

    show sadie ny cheerful:
        journal_left
    s "Not too much, but a few here and there."

    if bigdaddydefeated:

        l "I wouldn't call overthrowing Big Daddy Dan 'not too much'!"

        show sadie ny flirtatious:
            journal_left
        s "Ah, but that's not a discovery now, is it? And it's in New Orleans, so that's technically not close to home. Besides, Nigel takes most of the credit for that."

        show nigel ny nervous:
            journal_right
        n "Wait, what? I am sorry, I got a bit distracted while you were speaking... there was a particularly gripping chapter on Etruscan burial artifacts that had its hooks in me."

        if nigelromance:
            show sadie ny cheerful:
                journal_left
            s "{i}Oh Nigel, you adorable, wonderful nerd, you.{/i}"

        l "How exciting! I always love a tale of underdogs defeating wicked crime lords, and so do the people. Sells tons of papers!"

    if partybaron:

        l "A little bird tells me that you and a friend managed to stop an assassination while you were in New Orleans."
        l "The investigator in charge of the case said you were a great help. What's it like being a hero?"

        if felixromance:
            show sadie ny pensive:
                journal_left
            s "{i}Poor Felix... he probably deserves just as much credit, but because he's an unknown and I'm not...{/i}"

        show sadie ny triumphant:
            journal_left
        s "I'd say it was a team effort all the way."

        l "Spoken like a true gentlewoman!"

    if dutchbox:

        l "Right on our back doorstep, I hear there was a very important dig near Central Park that uncovered an interesting Dutch book. You were part of that?"

        show sadie ny calm:
            journal_left
        s "That's right. The book was a grimoire, a book of spells. Superstitious nonsense, of course, but still a valuable book in terms of the culture of the Netherlands during the time of Charles V."

        if ahmoseromance:
            hide nigel
            show kheper wry:
                journal_right
            k "Superstitious nonsense, she says. No such thing as magic, she says. Now excuse me while I take my talking scarab and go meet my undead mummy boyfriend, she says."
            show sadie ny weary:
                journal_left
            s "{i}Why did I bring him along again?{/i}"
            hide kheper
            show nigel ny curious:
                journal_right

        l "I heard some vague rumors around town that there was something else connected to the book... something about a box?"

        show sadie ny nervous:
            journal_left
        s "Oh, uh, don't really know anything about that!"
        s "{i}I imagine it won't look good if we go into the whole ripping-pages and keeping-unusual-historical-necklaces ...{/i}"

        l "Pity! But still, imagine finding a magic grimoire in this very city! I imagine your discovery is driving all sorts of people to their local used bookstores to see if they can find their own!"

    if raeks:
        l "You donated a few pieces you'd discovered from all over the world to the museum, but there's one that's stirring up a bit of a rumor mill... the one strange looking statue."
        l "Is it true that you got it from Raeks Karahkwa?"

        show sadie ny panicked:
            journal_left
        s "How do you know... er, I mean, what made you think that?"

        l "Hello? Reporter! It's my job to hear rumors. So, is it true?"

        s "Uhh...."

        show nigel ny dryly:
            journal_right
        n "While I appreciate your enthusiasm, Miss Lone, I'm sure you'll understand that we traffic in fact here, not myth or rumor. The statue was identified as a Pre-Columbian fertility idol, and any further classification will have to wait for further evidence."

        show sadie ny blush:
            journal_left
        s "{i}thankyouthankyouthankyou...{/i}"

        l "Fair enough, I suppose. You can't blame a girl for wanting some adventure to a story!"

    show sadie ny excited:
        journal_left
    s "The truth is, Miss Lone, there are always adventures close to home, we just don't think of them as such. Yes, my life might be very exciting, but that doesn't mean the life that you lead has to be any less filled with excitement and danger..."

    show sadie ny teasing:
        journal_left
    s "... Well, okay, maybe a bit less danger isn't a bad idea."

    show sadie ny determined:
        journal_left
    s "It's so easy to get caught up in the adventures of archaeologists and scientists and all those people that we miss what's going on around us, the people in our lives, the little adventures here and now. Don't you agree?"

    l "Absolutely! I think that's very well said."





label endinterview8:
    l "All right, so one last question, but the most important question of all..."

    show sadie ny excited:
        journal_left
    s "Oh! Is it about my archaeological methodology, or my parents, or my future plans?"

    l "None of the above! Do you have a special man in your life?"

    show sadie ny surprised:
        journal_left
    s "...Wait, what?"

    l "Oh come on, dear, this is the New York Tribune! And nothing spices up a story like a little romance."

    show sadie ny weary:
        journal_left
    s "I don't suppose my private life can remain private?"

    l "Haha, not really... we get to you somehow or other. Besides... if there's someone special in your life, doesn't it make sense to celebrate it and shout it to the world, at least a bit?"

    show sadie ny pensive:
        journal_left
    s "I suppose when you put it like that..."

    l "Sooo...?"

    if nigelromance:

        show nigel ny nervous:
            journal_right
        show sadie ny cheerful:
            journal_left
        s "There sure is. He's right here."

        n "Sadie, are you sure it's the right time to..."

        s "Nigel, sometimes it's good to just get things out in the open so people stop pestering you about it."

        show sadie ny blush:
            journal_left

        s "We're not 'official' official yet, of course, not with being teacher and student, but... considering I'm no longer in his class, there's no longer a conflict of interest to consider, let's just say that much."

        l "(happy squeal) Oooh, then all the reports about the two of you were true?"

        show nigel ny cheerful:
            journal_right
        n "Well, not all of them. I can vouch for the fact that I never stormed into the dean's office and demanded that he let her stay in my class or I'd quit. I'm pretty sure I'd remember something like that."

        show sadie ny cheerful:
            journal_left
        s "Aww, so would I."

        l "Wow, well, best wishes to the two of you! It's like a fairytale ending!"

    elif felixromance:
        show sadie ny blush:
            journal_left
        s "Well... there is one boy in particular..."

        l "(hinting) Blond fella? Looks like a young Viking god only a little bit shy?"

        n "Huh. Why do people never say things like that about me?"

        "{i}Sadie flashes Nigel a grin, then concedes the point...{/i}"

        show sadie ny cheerful:
            journal_left
        s "That'd be the one."

        show sadie ny sad:
            journal_left
        s "You can't write about him, though. Not yet. I... we've been friends since childhood, and only recently we found each other again. I promised we would always come back together, no matter what."

        l "Aw, you dear little chipmunk. That's sweet!"

        show sadie ny weary:
            journal_left
        s "But... I have to admit, I've been chickening out about telling him how I feel. I'm not sure a newspaper piece is really..."

        l "Well, what are you waiting for, Christmas? You've got to get out there and tell him! Confess your love! It'll be the most magical, fairytale romance!"

        show sadie ny cheerful:
            journal_left
        s "Thank you for the vote of confidence, Miss Lone!"

        l "Hell, dear, this is why I get drunk. I'm confident in everyone when I'm sauced!"

    elif ahmoseromance:
        show sadie ny blush:
            journal_left
        s "Well... there is one man I met on my travels..."

        l "Ooooooh! Sounds exotic! Is he foreign?"

        show sadie ny blush:
            journal_left
        s "Oh, you have no idea! But yes, he is from another country. He can be a bit... old fashioned at times, but he's always been a perfect gentleman, very protective and supportive, and I... I've grown to care for him. A lot."

        l "Oh wow! Who is this mystery man?"

        s "I... don't think I should reveal that just yet. He's a rather private man."

        hide nigel
        show kheper pleased:
            journal_right
        k "Yeah! He likes to keep things wrapped up. BADUM-BUM-TISH! Thank you, try the veal!"
        hide kheper
        show nigel ny curious:
            journal_right

        l "What is that voice I keep hearing, anyway?"

        show sadie ny weary:
            journal_left
        s "Just the wind, I'm sure."

        show sadie ny cheerful:
            journal_left
        l "Well, we hope we'll see you and your mysterious gentleman around town. It truly sounds like a tale from 'A Thousand and One Arabian Nights'!"

    elif sterlingromance:
        show sadie ny blush:
            journal_left
        s "There is a man I've fallen in love with, actually..."

        l "Details!"

        s "Not sure how many I should give... he's, ah, extremely caring and passionate, but he's a bit of a rogue."

        l "(squeals in joy) Oh, dearie, those are the best kinds. Is he cute?"

        show sadie ny laughing:
            journal_left
        s "Let's just say I have a fondness for ruffled red hair and leave it at that."

        l "Where is he right now?"

        show sadie ny sad:
            journal_left
        s "...in the hospital. He... he was hurt very badly during one of our adventures."

        l "Oh no! So he's a fellow archaeologist, then?"

        s "Something like that."

        l "I hope he gets better soon!"

        show sadie ny calm:
            journal_left
        s "Thank you."

        l "A roguish adventurer captures the heart of society's princess and wounds himself in protecting her... eeee, it's like an epic romance!"

    elif rolandromance:
        show sadie ny blush:
            journal_left
        s "There is someone, actually... he's from Britain."

        l "Ooh, I love British accents. Is he a proper gentleman?"

        show sadie ny cheerful:
            journal_left
        s "In every sense of the word. He's honorable, dashing, true to his word, and always willing to give of himself."

        l "Oh, sounds like a real catch! And handsome?"

        show sadie ny teasing:
            journal_left
        s "Well, not that I'd notice such paltry things as appearance, but... definitely."

        l "And where is this dashing Brit at the moment?"

        show sadie ny sad:
            journal_left
        s "...in Britain, actually."

        l "What? Some devoted English gentleman he turned out to be if he can't even be here with his lady love!"

        s "It's not like that. It's... family, and work, and other things."

        l "(gasps) So it's a star-crossed-lovers sort of thing! Aw, this is magic. This is the sort of thing plays and stories are written about."
    else:

        show sadie ny calm:
            journal_left
        s "To be honest, Miss Lone, I have a lot of people who are special to me, but not in the way you're thinking of. I don't really have time for romance right now."
        s "Right now, the most important thing to me is to focus on my studies and on archaeology. To help bring the past into the present and to help educate people about our history so we know where we've come from.. and where we're going."

        show sadie ny sad:
            journal_left
        s "There's also my friends, my family... my parents. I want to find out what happened to them. That's my goal, and I need to focus on it right now. I have... I have a lot I need to do."

        l "I understand. Sometimes things like career or family take a front seat and romance has to wait for a bit. Just don't wait forever, okay? An amazing young lady like you deserves to have the best love story of all time!"




label endinterview9:
    l "Speaking of stories, your life... goodness, this past year alone has been the story to end all stories! So young and so accomplished, to have discovered so much! What's next for you?"

    show sadie ny laughing:
        journal_left
    s "To be honest, a few weeks' break, I think!"

    l "Haha, I'll bet! Well, I think that's everything, Sadie. I'll be sure to contact you if I have any further questions."

    show sadie ny cheerful:
        journal_left
    s "Or just come say hi at the next party. Heck, Aunt Evelyn'll probably throw one in your honor after the article comes out!"

    l "That's the cunning plan, kiddo."

    hide gossipgirl

    "{i}A few minutes of mutual pleasantries and exchange of info later, and Lana Lone is out the door.{/i}"

    show nigel ny cheerful:
        journal_right
    n "That was less unpleasant than I expected."

    s "No kidding! Where was the merciless grilling, the hot rack, the 'we have ways of making you talk' routine?"

    show nigel ny dryly:
        journal_right
    n "I suppose we didn't see what would happen if we just refused to answer any of her questions..."

    if gamehard:

        n "But, in all seriousness, what she said at the outset was true. Not many people would even try to do what you did this year. You should be proud of what you accomplished - and, more, you should be proud of your ambition. I know I am."

    elif gamenormal:

        n "But, in all seriousness, I'm glad you're getting the attention you deserve. You had a challenging year, and you... well, you excelled. You should be proud of that. I know I am."
    else:


        n "I'm just as happy we didn't, though. You don't have to stand up in front of a firing squad to know you don't want to get shot."

    if nigelromance:
        show sadie ny blush:
            journal_left
        s "So... I suppose I'll likely see you tonight?"

        show nigel ny excited:
            journal_right
        n "You shall indeed. It's funny, I've never looked forward to a gala evening before."

        s "Oh?"

        n "Mind you, I've never had the privilege of going to one with someone I love before."

        s "Oh..."

        show nigel ny cheerful:
            journal_right
        n "I'll see you there, then."

        show sadie ny cheerful:
            journal_left
        s "I can't wait."
    else:

        show sadie ny excited:
            journal_left
        s "Well, I'd best get going. Will I see you at the opening of the Egyptian exhibit, then?"

        show nigel ny excited:
            journal_right
        n "Naturally. I'll look forward to seeing you there."

    show sadie ny calm:
        journal_left

    s "Oh. Before I head out. My aunt wanted me to be sure to thank you for the card. Though she says it isn't necessary."

    show nigel ny concerned:
        journal_right

    n "Oh, it was no trouble. But... well, I wasn't going to ask, and you can ignore me if I'm prying, but are the two of you... better?"

    show sadie ny curious:
        journal_left

    s "I guess. Sort of. Aunt Evelyn talked to her favorite astrologer, who told her to 'expect good news.' So now she's deep in everything's-going-to-turn-out-all-right mode, and it's like Ruddy's just off on another dig somewhere."

    show sadie ny sad:
        journal_left

    s "It's better than having her cry all the time, I guess, but someday the other shoe's going to drop. And I don't know how she's... well. It could be bad."

    show nigel ny dryly:
        journal_right

    n "At the risk of ruining my reputation as a man of rationality, let me point out that there's a possibility you seem to be overlooking."

    show sadie ny curious:
        journal_left

    s "Yes?"

    n "Maybe everything's going to turn out all right."

    show sadie ny calm:
        journal_left

    s "Maybe it will. See you later, Professor Hemsworth."

    show nigel ny cheerful:
        journal_right

    n "See you later, Miss Keating."

    hide nigel


    $ gameCalendar.journal("I dropped by Nigel's office today and found a reporter, Lana Lone, waiting to interview me on all the discoveries I've made over the past year. It really drove home how much I've done, how many things I've uncovered... and how important the people in my life really are.")

    jump startpresent1

