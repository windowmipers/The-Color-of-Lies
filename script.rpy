# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mrs. Mulberry", color="#442399", outlines=[(1,"#000000", 0,0)])
define g = Character("Dr. Greenwood", color="#056E04", outlines=[(1,"#000000", 0,0)])
define cr = Character("Mr. Crime", color="#FF1100", outlines=[(1,"#000000", 0,0)])
define cl = Character("Mr. Clean", color="FFFFFF", outlines=[(1,"#000000", 0,0)])
define sk = Character("Mr. Sky", color="00FFEA", outlines=[(1,"#000000", 0,0)])
define su = Character("Mrs. Sun", color="FAFF00", outlines=[(1,"#000000", 0,0)])
define mc = Character("Mr. Sketch", color="000000")
define mcnarr = Character("Mr. Sketch", color="000000", what_italic=True)
define narrator = Character(what_italic=True)
# The game starts here.

label start:
    play music amogus_normal
    narrator "You are Mr. Sketch, one of the few chosen to take a journey via spaceship to a certain destination.
    You are on this journey with your good friend, Ms. Rose, and a handful of rather rich folk who have paid through the nose to be on this flight."
    narrator "Last night, the spaceship broke down unexpectedly and you've all had to take on the previously automated tasks yourself."
    narrator "You and Ms. Rose got into a heated disagreement about something, and now Ms. Rose is dead."
    scene mainhall
    with Dissolve(.5)
    show cyan_720
    sk "Oh, good. That must be the back-up generator."
    show cyan_720 at left
    show white_720 at right
    cl "You can't investigate a crime scene without a little light."
    mc "That body...is that...?"
    hide cyan_720
    show crime at left
    cr "Don't pretend like you didn't know."
    cl "Hey, that was their friend. Show a little compassion.
    And besides, it was definitely Greenwood."
    hide crime
    show green_720 at left
    g "Me? What?"
    cl "You were back here for a long time, with Rose."
    hide green_720
    show yellow_720 at left
    su "So was I. That doesn't mean anything."
    hide white_720
    show green_720 at right
    g "I wasn't even in the sick bay when it happened. I was looking for Mr. Sky."
    hide yellow_720
    show cyan_720 at left
    sk "I never saw you."
    hide green_720
    show crime at right
    cr "Hear that? I'm calling it. It was the doctor."
    hide cyan_720
    show white_720 at left
    cl "It always is."
    hide crime
    show purple_720 at right
    m "Calm down, all. It's almost teatime."
    cl "How can you think about lunch, Auntie? We have a mystery to solve!"
    hide purple_720
    show green_720 at right
    g "I don't trust you to solve it. You already think it was me."
    cl "Well, who else is there?"
    hide green_720
    show cyan_720 at right
    sk "Mr. Sketch seems pretty neutral."
    mc "Me? Well I suppose, since she was my friend. Yes, I'll investigate."
label red1:
    scene stairs
    with Dissolve(.5)
    show crime
    play music amogus_red fadeout 1
    cr "What do you want?"
    mc "I'm just trying to get an accurate picture of what happened."
    mc "You were supposed to be navigating, right? While Mr. Sky was fixing the GPS."
    cr "That's right. I stepped away for a minute to clear my head."
    cr "I let my brother take the controls. You know him? Mr. Clean? Go bother him."
    mc "Hold on a minute. You were the first one here."
    hide crime
    show red_angy
    cr "Yeah? So what? You think that means I did it?"
    menu:
        "No.":
            mc "No."
            jump red1_cont
        "Prove you didn't.":
            mc "Prove you didn't."
            jump red1_cont
label red1_cont:
    hide red_angy
    show crime
    cr "I sounded the alarm. Is that not proof enough?
    If you want more proof, talk to Mulberry. She saw the whole thing go down."
label purple1:
    scene library
    with Dissolve(.5)
    show purple_720
    play music amogus_purple fadeout 1
    mc "Mrs. Mulberry, right?"
    m "Who's asking?"
    mc "I'm Mr. Sketch, remember? I...was just introduced."
    mc "Also I've been on this ship with you for like a month."
    hide purple_720
    show purple_snoot
    m "Yes, yes. Forgive me. I don't care."
    mc "Mr. Crime says you saw everything."
    m "Suppose I did? Actually, suppose I didn't? Mr. Crime is my nephew; I've known him since he was a boy. He's fond of half-truths."
    menu:
        "Could you tell me what you saw?":
            mc "Could you tell me what you saw?"
            jump purple_c1_1
        "Where were you?":
            mc "Where were you?"
            jump purple_c1_2
label purple_c1_1:
    m "Why should I?"
    mc "Because someone died..."
    hide purple_snoot
    show purple_720
    m "Why should I care that Ms. Rose died?"
    jump purple1_end
label purple_c1_2:
    m "Why does it matter?"
    mc "You're a suspect."
    hide purple_snoot
    show purple_720
    m "I'm a suspect? Ludicrous."
    jump purple1_end
label purple1_end:
    m "Talk to Mrs. Sun. She admitted she was there."
    m "In fact, we walked there together. Lovely jacket she had on."
label yellow1:
    scene lounge
    with Dissolve(.5)
    show yellow_720
    play music amogus_yellow fadeout 1
    mc "Mrs. Sun?"
    su "Ah, Mr. Sketch! Am I next? What can I do for you?"
    mc "You said you were back here, with Ms. Rose?"
    su "I was. I thought it would be best to make sure we had security and electricity, since my husband was handling oxygen and navigation."
    mc "You were fixing the lights? But the lights went out."
    su "Whoever killed Ms. Rose yanked the wires right out of the wall!
    And after I did all that work to fix it."
    menu:
        "How did you know how to fix the lights?":
            mc "How did you know how to fix the lights?"
            hide yellow_720
            show yellow_closed
            su "I'm an engineer! That's how I met Mr. Sky, actually."
            jump yellow1_end
        "How hard would it be to yank the wires out of the wall?":
            mc "How hard would it be to yank the wires out of the wall?"
            su "Not hard at all. Though it would take guts. You've got a pretty decent chance of getting electrocuted."
            jump yellow1_end
label yellow1_end:
    hide yellow_closed
    show yellow_720
    mc "Did you see anything while you were fixing the lights?"
    su "Nothing of note."
    mc "Well, thank you for your time."
    su "I can't stand a dreary mood. Hey—why do cows wear bells?"
    mc "What?"
    hide yellow_720
    show yellow_closed
    su "Because their horns don't work!"
    mc "..."
label green1:
    scene parlor
    with Dissolve(.5)
    show green_720
    play music amogus_green fadeout 1
    g "It wasn't me."
    menu:
        "Okay...":
            mc "Okay..."
            jump green1_c1_1
        "Then who was it?":
            mc "Then who was it?"
            jump green1_c1_2
label green1_c1_1:
    hide green_720
    show green_lewk
    g "You have to clear my name with Mr. Clean.
    They're going to throw me out!"
    jump green1_end
label green1_c1_2:
    hide green_720
    show green_lewk
    g "I don't know. Maybe it was Mr. Sky. I never could find him."
    jump green1_end
label green1_end:
    hide green_lewk
    show green_720
    mc "I'm just trying to figure out what happened."
    g "I'm the only one here who doesn't have connections to any of the others."
    mc "Not anymore. Ms. Rose was my only friend. I don't have a side."
    g "We could be on the same side."
    mc "Not before I find out what happened. What were you doing?"
    hide green_720
    show green_lewk
    g "I was in the sick bay. I was running samples. I'm a doctor, you know."
    mc "Did anyone see you in there?"
    g "Yeah, a lot of people. Mr. Crime came through, Mrs. Sun, uh… Could you see? From the cafeteria?"
    mc "I must have missed it."
label cyan1:
    scene dining
    with Dissolve(.5)
    show cyan_720
    play music amogus_cyan fadeout 1
    mc "Mr. Sky?"
    sk "Mr. Sketch. I'm afraid I don't have anything useful to tell you."
    menu:
        "You never know. Did you see anything?":
            mc "You never know. Did you see anything?"
            jump cyan1_c1_1
        "Is there anything you can tell me about the other people on the ship?":
            mc "Is there anything you can tell me about the other people on the ship?"
            jump cyan1_c1_2
label cyan1_c1_1:
    sk "I wasn't back there."
    mc "You still could have seen something."
    sk "I...don't know. I saw a lot of things.
    There were a lot of wires I had to fix and I don't know why..."
    hide cyan_720
    show cyan_surprise
    sk "It didn't look like an accident. It was like someone went around and yanked out wires by the handful."
    menu:
        "What do you think happened?":
            mc "What do you think happened?"
            jump cyan1_c2_1
        "What makes you think that?":
            mc "What makes you think that?"
            jump cyan1_c2_2
label cyan1_c1_2:
    sk "I really don't know what to say. The only crewmate I know very well is my wife, Mrs. Sun."
    mc "We've been on this ship a while, though. You have to know the other crew members at least a little. What do you think happened?"
    sk "I couldn't say. I saw a lot of things."
    mc "Did you see anything?"
    sk "I was moving around a lot and I was focused on the wires. I'm not the most observant."
    jump yellow2
label cyan1_c2_1:
    hide cyan_surprise
    show cyan_720
    sk "I couldn't say. I saw a lot of things."
    sk "I was moving around a lot and I was focused on the wires. I'm not the most observant."
    jump yellow2
label cyan1_c2_2:
    sk "It just isn't natural; I checked the plans for this ship before we left."
    sk "It would take some kind of superhuman strength to rip the panels off the wall and mess with the wiring."
    jump yellow2
label yellow2:
    scene stairs
    with Dissolve(.5)
    show yellow_720
    play music amogus_yellow fadeout 1
    su "Hey! I saw you talking with Mr. Sky."
    mc "Yes...?"
    hide yellow_720
    show yellow_closed
    su "Did you know he's my husband?"
    menu:
        "So he said.":
            mc "So he said."
            jump yellow2_end
        "Is that relevant to my investigation?":
            mc "Is that relevant to my investigation?"
            jump yellow2_end
label yellow2_end:
    hide yellow_closed
    show yellow_720
    su "He's under a lot of stress right now.
    I would appreciate it if you kept that in mind."
    mc "We're all under a lot of stress right now."
    su "I know exactly what will lighten the mood."
    mc "...what?"
    su "What do you call a snail on a ship?"
    hide yellow_720
    show yellow_closed
    su "A snailor!"
    hide yellow_closed
    show yellow_720
    mc "While I have you here, did you see Dr. Greenwood while you were fixing the wires?"
    su "I saw him when I passed through the sick bay. I don't think I noticed him while I was working on the electricity.
    But then again, I was really focused."
label white1:
    scene mainhall
    with Dissolve(.5)
    show white_720
    play music amogus_white fadeout 1
    cl "Well? Have you figured it out yet?"
    menu:
        "It's only been 10 minutes.":
            mc "It's only been 10 minutes."
            jump white1_cont
        "Did you see anything?":
            mc "Did you see anything?"
            jump white1_cont
label white1_cont:
    hide white_720
    show white_frown
    cl "I was in the cockpit the entire time.
    Someone had to make sure we were going in the right direction."
    menu:
        "How very considerate.":
            mc "How very considerate."
            jump white1_c2_1
        "Wasn't Mr. Crime in there with you?":
            mc "Wasn't Mr. Crime in there with you?"
            jump white1_c2_2
label white1_c2_1:
    hide white_frown
    show white_720
    cl "Wasn't it?"
    jump white1_end
label white1_c2_2:
    hide white_frown
    show white_720
    cl "At the start. We've both done a lot of sailing.
    That's not exactly the same as piloting a ship like this one, but close enough."
    jump white1_end
label white1_end:
    mc "Why did Mr. Crime leave?"
    cl "He wanted to take a walk. My brother tends to get antsy.
    He has since we were kids."
    mc "Did anyone else come in while Mr. Crime was out?"
    cl "Only Mr. Sky. He wanted to make sure that the GPS was back on so he could go work on the electricity."
    menu:
        "Did you get bored, in there by yourself?":
            mc "Did you get bored, in there by yourself?"
            hide white_720
            show white_frown
            cl "Are you suggesting I left? I was very focused on getting us back on course. The time flew by."
            jump red2
        "When was that?":
            mc "When was that?"
            hide white_720
            show white_frown
            cl "I wasn't too focused on the time. I just know it was after my brother left, and before he sounded the alarm."
            jump red2
label red2:
    scene parlor
    with Dissolve(.5)
    show crime
    play music amogus_red fadeout 1
    cr "Ugh, you again."
    mc "I'm not looking for a fight."
    hide crime
    show red_angy
    cr "And I am?"
    hide red_angy
    show crime
    mc "Where did you go on your walk?"
    cr "I just made a circle.
    I went through the cafeteria, through the sick bay and the breaker room, and I was almost to the storage area when I heard a sound."
    menu:
        "Did you see anyone?":
            mc "Did you see anyone?"
            jump red2_c1_1
        "Did you see Ms. Rose?":
            mc "Did you see Ms. Rose?"
            jump red2_c1_2
label red2_c1_1:
    cr "Just the doctor. And Mrs. Sun."
    jump red2_cont
label red2_c1_2:
    cr "Not until it was too late."
    jump red2_cont
label red2_cont:
    menu:
        "What did you hear?":
            mc "What did you hear?"
            jump red2_c2_1
        "Did you see Dr. Greenwood in the sick bay?":
            mc "Did you see Dr. Greenwood in the sick bay?"
            jump red2_c2_2
label red2_c2_1:
    cr "A scream, and a thump.
    It would be weird if I didn't find a body after that."
    menu:
        "What did you do then?":
            mc "What did you do then?"
            jump red2_c2_1_1
        "Did anyone see you by the storage area?":
            mc "Did anyone see you by the storage area?"
            jump red2_c2_1_2
label red2_c2_1_1:
    cr "I ran back, obviously. Then I sounded the alarm."
    mc "How did you know how to sound the alarm?"
    hide crime
    show red_angy
    cr "You're kidding, right? I'm not that oblivious. I know how to report a murder."
    mc "Just checking."
    jump green2
label red2_c2_1_2:
    cr "No. I didn't see anyone between there and the breaker room either."
    jump green2
label red2_c2_2:
    cr "I saw him in there. I don't know what he was doing, though.
    He was just staring at some tubes."
    mc "Staring at some tubes?"
    cr "Yeah. Wasn't he supposed to be running samples or something?"
    jump green2
label green2:
    scene library
    with Dissolve(.5)
    show green_720
    play music amogus_green fadeout 1
    g "It wasn't me."
    menu:
        "You already said that.":
            mc "You already said that."
            jump green2_c1_1
        "Did you ever run the samples, like you were supposed to?":
            mc "Did you ever run the samples, like you were supposed to?"
            jump green2_c1_2
label green2_c1_1:
    hide green_720
    show green_lewk
    g "Do they all think it was me?"
    menu:
        "Nobody is accusing anyone.":
            mc "Nobody is accusing anyone."
            jump green2_c1_1_1
        "You are acting fairly guilty.":
            mc "You are acting fairly guilty."
            jump green2_c1_1_2
label green2_c1_1_1:
    hide green_lewk
    show green_720
    g "But they all must think it's me."
    mc "Normally, I wouldn't assume, but I am conducting a murder investigation. You're hiding something."
    hide green_720
    show green_lewk
    g "*visibly sweating* What? That's ridiculous. Can I get a lawyer?"
    mc "Sir, we are on a spaceship."
    jump cyan2
label green2_c1_1_2:
    g "I can't help it!
    I'm the only one who doesn't know anyone else on this ship."
    mc "Normally, I wouldn't assume, but I am conducting a murder investigation. You're hiding something."
    hide green_720
    show green_lewk
    g "*visibly sweating* What? That's ridiculous. Can I get a lawyer?"
    mc "Sir, we are on a spaceship."
    jump cyan2
label green2_c1_2:
    g "I tried, I swear. I don't know how to use the equipment.
    It must be different on this ship."
    menu:
        "It's pretty standard stuff.":
            mc "It's pretty standard stuff."
            jump green2_end
        "What makes it different?":
            mc "What makes it different?"
            jump green2_end
label green2_end:
    g "Nothing. I'm sure it was nothing. I'll check it again."
    mc "I can't clear you if you didn't do what you were supposed to.
    What were you doing instead?"
    hide green_720
    show green_lewk
    g "I told you, I was trying to find Mr. Sky!
    I ran into him just as the alarm was sounded."
    mc "Weren't the lights out?"
label cyan2:
    scene lounge
    with Dissolve(.5)
    show cyan_720
    play music amogus_cyan fadeout 1
    sk "Can I help you?"
    mc "Dr. Green says he ran into you when the lights went out."
    sk "I wasn't paying attention. He could have seen me as the lights went out."
    menu:
        "Where did he see you?":
            mc "Where did he see you?"
            jump cyan2_cont
        "Why were you so distracted?":
            mc "Why were you so distracted?"
            jump cyan2_cont
label cyan2_cont:
    sk "I was on my way to the breaker room.
    I wanted to make sure the power stayed on."
    mc "Didn't you know your wife was already fixing the wires?"
    hide cyan_720
    show cyan_surprise
    sk "I...didn't. That's not usually her specialty."
    mc "What do you mean?"
    sk "Mrs. Sun is a chemical engineer. I would have thought she would want to run samples or check on the oxygen.
    Instead, she volunteered me for oxygen and let Dr. Greenwood take the samples."
    sk "She does have a passable knowledge of systems and mechanics, so maybe she thought security was more important."
    menu:
        "Is that out of character?":
            mc "Is that out of character?"
            hide cyan_surprise
            show cyan_720
            sk "I really couldn't say."
            jump cyan2_end
        "Mr. Clean says you stopped by the cockpit?":
            mc "Mr. Clean says you stopped by the cockpit?"
            hide cyan_surprise
            show cyan_720
            sk "I thought making sure we were heading in the right direction was the most important thing to fix, after oxygen.
            If we got too off-course, we would run out of supplies."
            jump cyan2_end
label cyan2_end:
    mc "You seem a little spacey. Are you alright?"
    sk "I've just got a lot on my mind. You know that jacket Mrs. Sun is wearing?"
    mc "The one over her shoulder?"
    hide cyan_720
    show cyan_surprise
    sk "Exactly. I gave that jacket to her last month. Why isn't she wearing it?"
label yellow3:
    scene mainhall
    with Dissolve(.5)
    show yellow_720
    play music amogus_yellow fadeout 1
    su "Hey! How do billboards talk?"
    mc "What?"
    hide yellow_720
    show yellow_closed
    su "Sign language :D"
    mc "Uhh..."
    hide yellow_closed
    show yellow_720
    su "So how's my husband?"
    mc "If it's not too bold of me to ask, why don't you check in on him yourself?"
    su "He's very busy. I don't want to bother him."
    mc "He's a little confused."
    su "About what?"
    menu:
        "Why were you in the breaker room?":
            mc "Why were you in the breaker room?"
            su "It seemed like the most important problem to address."
            jump yellow3_cont
        "Why aren't you wearing your coat?":
            mc "Why aren't you wearing your coat?"
            hide yellow_720
            show yellow_closed
            su "I got pretty warm fixing all those wires."
            hide yellow_closed
            show yellow_720
            jump yellow3_cont
label yellow3_cont:
    mc "You were in there for a long time."
    su "There was a lot of damage. From what I've seen, there's the most destruction in there out of anywhere else on the ship."
    menu:
        "Did you see anyone while you were in there?":
            mc "Did you see anyone while you were in there?"
            su "Mr. Crime came through. Ms. Rose was in the next room, and Mrs. Mulberry was somewhere nearby.
            I walked to the breaker room with her."
            jump purple2
        "That's awfully close to the murder scene.":
            mc "That's awfully close to the murder scene."
            su "It is. I wish I had stayed so I could have seen what happened to poor Ms. Rose."
            mc "Where did you go?"
            su "Back to the sick bay. You know, I don't think Dr. Greenwood ran any of his tests."
            jump purple2
label purple2:
    scene dining
    with Dissolve(.5)
    show purple_720
    play music amogus_purple fadeout 1
    mc "You were standing by the sick bay, weren't you?"
    m "I was in the area."
    mc "Did you see Mr. Crime come through?"
    m "Yeah, I saw him. He came through and spoke briefly with Ms. Rose."
    mc "Whoa! Actual useful information! Why didn't you tell me this before?"
    hide purple_720
    show purple_snoot
    m "You think I would care? It's none of my business who my nephews choose to mingle with. What are you, some kind of snoop?"
    mc "Ma'am, please, it's a murder investigation."
    m "That doesn't stop you from being a busybody. Get out of here!"
label red3:
    scene parlor
    with Dissolve(.5)
    show crime
    play music amogus_tense_theme fadeout 1
    cr "You again?"
    menu:
        "You lied to me. You said you didn't see Ms. Rose before she died.":
            mc "You lied to me. You said you didn't see Ms. Rose before she died."
            jump red3_c1_1
        "Why did you leave the cockpit?":
            mc "Why did you leave the cockpit?"
            jump red3_c1_2
label red3_c1_1:
    cr "Okay, yeah, I did lie. But I didn't kill her!"
    mc "What happened?"
    cr "I just said hi. It would have been weird not to. She was right there."
    mc "Mrs. Mulberry says you were 'mingling.'"
    cr "She says that about everything. She says I'm mingling with the dentist when I go to get my teeth cleaned."
    jump green3
label red3_c1_2:
    cr "I wanted to take a walk. Is there a problem with that?"
    mc "I mean, someone did die..."
    hide crime
    show red_angy
    cr "You wanna go, Sketch? I have no problem fighting someone in space!"
    show red_angy at left
    show white_720 at right
    cl "Calm down. You're not helping your case."
    hide red_angy
    show crime at left
    cr "I didn't do it, alright? Just ask my brother here. I like to fight, but I would never kill someone."
    jump green3
label green3:
    scene stairs
    with Dissolve(.5)
    show green_720
    mc "Mr. Greenwood! Please stop trying to run away from me. I just want to talk."
    g "That's the scariest sentence you could have used!"
    mc "I've talked to a lot of our companions, and I'm starting to think you never ran those samples."
    hide green_720
    show green_lewk
    g "I didn't, okay? I'm not actually a doctor.
    I needed a way onto this ship and that was the easiest way to get on."
    menu:
        "What if there had been an actual emergency?":
            mc "What if there had been an actual emergency?"
            g "Then someone would have died. Whatever."
            jump green3_end
        "What were you planning to do with the samples?":
            mc "What were you planning to do with the samples?"
            g "That's why I was looking for Mr. Sky.
            He seems smart; he might have been able to help me."
            jump green3_end
label green3_end:
    mc "You're sticking to your story, that you didn't do it?"
    g "Why would I have done it? You're the one who fought with her!"
    hide green_lewk
    show green_720
    mc "..."
    g "Sorry. I'm just under a lot of stress."
    mc "Aren't we all..."
label cyan3:
    scene lounge
    with Dissolve(.5)
    show cyan_720
    sk "You're back."
    mc "Just one more question. Why haven't you spoken with your wife this whole time?"
    hide cyan_720
    show cyan_surprise
    sk "..."
    mc "I know it's a personal question, but I feel like I'm close to figuring this out."
    sk "I..."
    show cyan_surprise at left
    show yellow_720 at right
    su "What's going on?"
    hide cyan_surprise
    show cyan_720 at left
    mc "Would you mind..."
    sk "I'll be going."
    su "What? Why?"
    sk "I'm sorry. I just need some fresh air."
    hide cyan_720
    show yellow_720 at center
    su "Sorry. That was awkward."
    menu:
        "What happened?":
            mc "What happened?"
            su "I don't know. It's just been like that recently."
            jump cyan3_end
        "Awkward is my middle name.":
            mc "Awkward is my middle name."
            su "How unfortunate."
            jump cyan3_end
label cyan3_end:
    su "Before you go! What do you call a cow with no legs?"
    mc "Oh no..."
    hide yellow_720
    show yellow_closed
    su "Ground beef!"
label white2:
    scene library
    with Dissolve(.5)
    show white_720
    cl "Did you figure it out yet?"
    menu:
        "Piss off.":
            mc "Piss off."
            jump white2_cont
        "I'm close.":
            mc "I'm close."
            jump white2_cont
label white2_cont:
    hide white_720
    show white_frown
    cl "How do we know it wasn't you?"
    mc "Why would it be me?"
    cl "You had a fight with Ms. Rose. She said you weren't acting like yourself."
    menu:
        "You talked to Ms. Rose?":
            mc "You talked to Ms. Rose?"
            jump white2_c2_1
        "It wasn't a big fight. But it wasn't the kind of note I wanted to end our friendship on.":
            mc "It wasn't a big fight. But it wasn't the kind of note I wanted to end our friendship on."
            jump white2_c2_2
label white2_c2_1:
    hide white_frown
    show white_720
    cl "Of course I did. I talked to everyone.
    I had to make sure nothing sketchy was going on."
    mc "Well, great job with that."
    jump purple3
label white2_c2_2:
    hide white_frown
    show white_720
    cl "Right, right. Well, if you need help finding the culprit, talk to Mrs. Mulberry."
    menu:
        "Why are you helping me?":
            mc "Why are you helping me?"
            cl "I don't want to be next."
            jump purple3
        "Why? She's been no help so far.":
            mc "Why? She's been no help so far."
            cl "She's scarily observant. She sees far more than she says."
            jump purple3
label purple3:
    scene dining
    show purple_snoot
    m "Back for more?"
    mc "I'm running out of time. I need you to tell me what you saw."
    m "What makes you think I saw anything?"
    mc "Please, Mrs. Mulberry."
    hide purple_snoot
    show purple_720
    m "I suppose this game has lost most of its appeal. What do you want to know?"
    menu:
        "Tell me about Dr. Greenwood.":
            mc "Tell me about Dr. Greenwood."
            m " He wasn't doing much of anything. I never saw him run a test.
            I don't think he ever even saw me. Anything else?"
            jump purple3_cont
        "Tell me about Mr. Sky.":
            mc "Tell me about Mr. Sky."
            m "I never saw him back here. Anything else?"
            jump purple3_cont
label purple3_cont:
    menu:
        "Tell me about Mr. Crime.":
            mc "Tell me about Mr. Crime."
            m "He came through and talked to Ms. Rose.
            They disappeared into the next room, the room where her body was found.
            But it was a while before the lights went out."
            hide purple_720
            jump meeting
        "Tell me about Mrs. Sun.":
            mc "Tell me about Ms. Sun."
            m "She was in the breaker room the whole time, the room where Ms. Rose's body was found.
            I don't think I ever saw her leave it."
            hide purple_720
            jump meeting
label meeting:
    scene black
    mcnarr "I think I might have it. I just need to see everyone together one more time to figure it out."
    scene mainhall
    play music amogus_suspense2 fadeout 1
    show crime:
        xalign 1.3
        yalign 1.0
    cr "What's going on here?"
    show white_720:
        xalign 1.0
        yalign 1.0
    cl "Did you figure it out?"
    mc "I think I have."
    show yellow_720:
        xalign 0.8
        yalign 1.0
    su "Who was it? Can you tell us now?"
    cr "It was Greenwood, wasn't it? Bet he isn't even a real doctor."
    show green_720:
        xalign 0.3
        yalign 1.0
    g "Exposed..."
    show cyan_720:
        xalign 0.1
        yalign 1.0
    sk "Please, just end the suspense."
    show purple_720:
        xalign -0.2
        yalign 1.0
    m "No, please, extend it!"
    mc "Well..."
    menu:
        "Who is the culprit?"
        "Mr. Crime":
            hide crime
            hide white_720
            hide yellow_720
            hide green_720
            hide cyan_720
            hide purple_720
            jump accuse_red
        "Mrs. Mulberry":
            hide crime
            hide white_720
            hide yellow_720
            hide green_720
            hide cyan_720
            hide purple_720
            jump accuse_purple
        "Mr. Clean":
            hide crime
            hide white_720
            hide yellow_720
            hide green_720
            hide cyan_720
            hide purple_720
            jump accuse_white
        "Mrs. Sun":
            hide crime
            hide white_720
            hide yellow_720
            hide green_720
            hide cyan_720
            hide purple_720
            jump accuse_yellow
        "Mr. Sky":
            hide crime
            hide white_720
            hide yellow_720
            hide green_720
            hide cyan_720
            hide purple_720
            jump accuse_cyan
        "Dr. Greenwood":
            hide crime
            hide white_720
            hide yellow_720
            hide green_720
            hide cyan_720
            hide purple_720
            jump accuse_green

label accuse_red:
    mc "I've looked at all the evidence and it has to be Mr. Crime."
    show yellow_720
    su "*gasp* No!"
    show yellow_720 at left
    show red_angy at right
    cr "I have never been so offended!"
    hide red_angy
    show crime at right
    mc "With a name like that, how could you not be the murderer?"
    hide crime
    show red_angy at right
    cr "Am I really supposed to defend against this? Seriously?"
    hide red_angy
    show crime at right
    hide yellow_720
    show white_720 at left
    cl "He can't help it. It's his name!"
    hide crime
    show cyan_720 at right
    sk "Is this supposed to be a real trial?"
    mc "You're right. I suppose I'll lay out my evidence."
    mc "Here it is: Mr. Crime was in the breaker room with Ms. Rose moments before the murder,
        then supposedly 'finished his walk' where there was conveniently nobody around to see him."
    mc "During that time, he clearly waited until enough time had passed to avoid suspicion before sounding the alarm."
    hide white_720
    show crime at left
    cr "I came back when I heard a scream!"
    mc "A likely story!"
    hide cyan_720
    show green_720 at right
    g "I think I might faint."
    hide crime
    show purple_720 at left
    m "This is so exciting!"
    hide green_720
    show white_720 at right
    cl "Mrs. Mulberry, that's your nephew! And Mr. Sketch, you can't do this."
    mc "You all have appointed me as your detective. This is my final decision."
    python:
        accused = "Mr. Crime"
    jump wrong_ending
label accuse_purple:
    mc "I've looked at all the evidence and it has to be Mrs. Mulberry."
    show yellow_720
    su "*gasp* No!"
    show yellow_720 at left
    show purple_720 at right
    m "I guess that's fair."
    mc "For all the trouble you've caused me, you deserve to go down."
    hide yellow_720
    show crime at left
    cr "Whoa there, I can admit that she's annoying, but there's still a killer here. You can't just get rid of Mrs. Mulberry for kicks."
    mc "Okay, fine. I've also decided she's the most likely suspect because she was back there the entire time. And she was withholding information."
    hide purple_720
    show cyan_720 at right
    sk "Is this supposed to be a real trial?"
    mc "You're right. I suppose I'll lay out my evidence."
    mc "Here it is: Mrs. Mulberry supposedly saw everything, and yet, nobody saw her."
    mc "She slipped out when no one was watching and murdered Ms. Rose, then slipped back into her hiding place."
    hide crime
    show purple_720 at left
    m "How exciting! What was my motive?"
    mc "Boredom."
    hide purple_720
    show purple_snoot at left
    m "I suppose I would commit murder out of boredom."
    hide cyan_720
    show crime at right
    cr "Mrs. Mulberry, you aren't going to fight for yourself?"
    hide purple_snoot
    show green_720 at left
    g "I might faint."
    hide crime
    show white_720 at right
    cl "Mr. Sketch, that isn't evidence."
    mc "You all have appointed me as your detective. This is my final decision."
    python:
        accused = "Mrs. Mulberry"
    jump wrong_ending
label accuse_white:
    mc "I've looked at all the evidence and it has to be Mr. Clean."
    show yellow_720
    su "*gasp* No!"
    show yellow_720 at left
    show white_720 at right
    cl "But sir, I was in the cockpit the whole time."
    mc "But you're undeniably suspicious. Anyone who smokes a pencil is a criminal in my book."
    cl "I...have no defense."
    hide yellow_720
    show cyan_720 at left
    sk "Isn't this supposed to be a real trial?"
    mc "You're right. I suppose I'll lay out my evidence."
    mc "Here it is: No one was around to see Mr. Clean in the cockpit."
    mc "After Mr. Sky checked the GPS, Mr. Clean could easily have slipped out and murdered Ms. Rose using the back passages Mr. Crime reported empty."
    cl "Alright, but what was my motive?"
    mc "It was a crime of passion!"
    cl "What??"
    hide cyan_720
    show green_720 at left
    g "I might faint."
    hide green_720
    show purple_720 at left
    m "This is so exciting!"
    cl "Mr. Sketch, that isn't evidence."
    mc "You all have appointed me as your detective. This is my final decision."
    python:
        accused = "Mr. Clean"
    jump wrong_ending
label accuse_yellow:
    play music amogus_good_end fadeout 1
    mc "I've decided...it's Mrs. Sun."
    show yellow_720
    su "*gasp*"
    show yellow_720 at left
    show cyan_surprise at right
    sk "*gasp* Where's your proof?"
    mc "You're right. Here it is: Mrs. Sun, though in the breaker room, never mentioned seeing Mr. Crime and Ms. Rose go in together, and she never left."
    mc "Mr. Crime didn't see her in the room, so she must have been hiding. Mr. Sky didn't want to admit it, but his wife has been displaying odd behavior lately."
    mc "The final piece of the puzzle was Mrs. Mulberry's testimony, as frustrating as it was to get. Mrs. Sun never left the room, as she claimed."
    mc "If Mrs. Sun never left the room, she must have been the killer."
    hide yellow_720
    show crime at left
    cr "Whoa."
    sk "Is this...is it true?"
    mc "I do have real, concrete evidence for this one. If you'll open up Mrs. Sun's coat, you'll see that it is splattered with blood."
    mc "Mrs. Mulberry saw her wearing it into the breaker room, but by the time we caught up, she had it slung over her shoulder, despite the low temperatures that the ship had fallen to without electricity."
    sk "I can't believe it."
    hide crime
    show yellow_closed at left
    su "Don't worry, dear. I never would have killed you."
    show green_720
    g "I think I might faint."
    hide cyan_surprise
    show purple_720 at right
    m "This is so exciting!"
    hide green_720
    show white_720
    cl "Great job, Mr. Sketch."
    jump good_ending
label accuse_cyan:
    mc "I've looked at all the evidence and it has to be Mr. Sky."
    show yellow_720
    su "*gasp* No!"
    show yellow_720 at left
    show cyan_720 at right
    sk "Okay."
    mc "What?"
    sk "I accept your decision."
    hide yellow_720
    show white_720 at left
    cl "Isn't this supposed to be a trial of sorts? Where is your evidence?"
    mc "You're right. Here it is: Mr. Sky's memory appears to have numerous holes in it."
    mc "It is well within the realm of possibility that he simply murdered Ms. Rose while walking around, looking for wires to fix."
    hide white_720
    show crime at left
    cr "Mr. Sky, are you just going to accept this?"
    sk "Why not."
    hide crime
    show green_720 at left
    g "I think I might faint."
    hide cyan_720
    show purple_720 at right
    m "This is so exciting!"
    hide green_720
    show white_720 at left
    cl "Mr. Sketch, that isn't evidence."
    mc "You all have appointed me as your detective. This is my final decision."
    python:
        accused = "Mr. Sky"
    jump wrong_ending
label accuse_green:
    mc "I've looked at all the evidence and it has to be Dr. Greenwood."
    show yellow_720
    su "*gasp* No!"
    show yellow_720 at left
    show white_720 at right
    cl "I knew it."
    hide yellow_720
    show green_720 at left
    g "No! You were supposed to be on my side!"
    mc "You've been lying about so much—did you really think I would believe that you didn't do it?
    You could have proven your innocence by simply doing your task."
    hide green_720
    show green_lewk at left
    g "I'll admit I lied, but I'm not a murderer!"
    hide white_720
    show cyan_720 at right
    sk "Is this supposed to be a real trial?"
    mc "You're right. I suppose I'll lay out my evidence."
    mc "Here it is: Dr. Greenwood never finished his tasks for the day."
    mc "He waited until there was nobody around to see him,
        then he dashed across the hall, murdered Ms. Rose, and went along back down the corridor, pretending to be looking for Mr. Sky."
    hide green_lewk
    show green_720 at left
    g "What was my motive??"
    mc "It was a crime of passion!"
    hide green_720
    show green_lewk at left
    g "What?!"
    hide cyan_720
    show purple_720 at right
    m "This is so exciting!"
    hide green_lewk
    show white_720 at left
    cl "Mr. Sketch, that isn't evidence."
    mc "You all have appointed me as your detective. This is my final decision."
    python:
        accused = "Dr. Greenwood"
    jump wrong_ending
label wrong_ending:
    scene black
    narrator "After you escort [accused] to the airlock, you can't help but feel like something is missing."
    narrator "It isn't until later, when the lights go out and the air begins to leak from the ship, that you hit upon the answer."
    narrator "It's already too late. Or is it? Play again?"
    jump end
label good_ending:
    scene ending_cool
    narrator "Congratulations! You solved the mystery!"
    narrator "You decided that your other top suspects had to be innocent.
    Dr. Greenwood was too worried about covering his ass to worry about what other people were doing, and Mr. Crime wouldn't be able to solve a puzzle if it only had two pieces."
    narrator "Mr. Sky was hesitant to point out his wife's odd behavior, knowing that it would almost certainly lead to her death."
    narrator "As you hurtle through space with a handful of eccentrics, you have to wonder...Am I really safe?"
    jump end
label end:
    # This ends the game.

    return
