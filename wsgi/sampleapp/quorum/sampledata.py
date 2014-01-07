TOPICS_DATA=(
		('General Purpose','cast'),
		('Products','cchip'),
		('Telecommunication','ctech'),
		('Pharmaceutical','czoo'),
		('Graphics','csun'),
		('Business','cbio'),
		('Gaming','cgame'),
		('Only Visible to Other Recruiter or JobSeeker','cbot'),
		('Science','cst'),
		)

#User(username,email,first_name,last_name,EMPLOYER/JOBSEEKER)
USERS_DATA=(
		("suhailvs","suhailvs@gmail.com","Suhail","VS","e"),
		("jani","suhailvs0@gmail.com","Jani","Hashmi","e"),
		("sumesh","suhailvs1@gmail.com","Sumesh","Jacob","j"),
		("sumee","suhspams@gmail.com","Sumee","vs","j"),
		("anoop","suhfiles@gmail.com","Anoop","T","j"),
		("lidercs","lidercs@gmail.com","Lider Consultancy Services","","e"),
		('Accenture','accenture@gmail.com',"Accenture Consultancy Services",'','e'),		
		("cognizent","cognizent@gmail.com","Cognizent Consultancy Services","","e"),
		('capsone','capsone@gmail.com',"Capsone Software Services",'','e'),		
		('gomathi','gomathi@gmail.com',"gomathi",'','j'),		
		("niveda","niveda@gmail.com","niveda","","j"),
		('satheesh','satheesh@gmail.com',"satheesh",'','j'),		
		('karthik','karthik@gmail.com',"karthik",'','j'),		
		("naveen","naveen@gmail.com","naveen","","j"),
		('sami','sami@gmail.com',"sami",'','j'),	
	)

#Question(user, topic, question)
QUESTIONS_DATA=(
		("suhailvs",9,
			"""
			I was attending my philosophy class and in the middle 
			of student presentations, I found myself mentally 
			wondering off and thinking about light. 
			After a few minutes of trying to piece together 
			how the sun works I came to ask a question I could 
			not answer myself. Why does each individual photon 
			have such a low amount of energy? I am hit by photons 
			all day and I find it amazing that I am not vaporized. 
			Am I simply too physically big for the photons to harm 
			me much, or perhaps the Earth's magnetic field filters 
			out enough harmful causes such as gammy rays?
			"""),#1

		("suhailvs",7, 
			"""
			Is anyone eagerly anticipating the unveiling 
			of the new xbox 720 today? This could almost be in the 
			'News' section making a much needed diversion 
			from gay marriage debates and broken britian.
			"""),#2		
		("jani",9, 
			"""
			The ordinary adult never bothers his head about 
			the problems of space and time. These are things he 
			has thought of as a child. But I developed so slowly 
			that I began to wonder about space and time only when 
			I was already grown up. Consequently, I probed more 
			deeply into the problem than an ordinary child would have.
			"""),#3
		("jani",9,
			"""
			Is the world near to its end?"""),#4
		("jani",9,
			"""
			Does red light block infrared?
			How to mask infrared vision"""),#5
		("suhailvs",7, 
			"""
		Is gravity part of physics?
		I'm have to complete a science assignment and I want to do it on gravity but I want to make sure gravity is part of physics, physical world, thanks."""),
		("anoop",7, 
			"""
My sister expressed interest in playing D&D, and I'm interested in DMing, so I decided to try and run The Caves of Chaos from the D&D Next playtest packet. 
Reading through the materials, I became worried that my sister's elf rogue wouldn't last very long by herself. 
None of her friends are interested in D&D, so I've been toying with the idea of including other party members, 
either controlled by me or by her (The way Jason and Marcus play in FoxTrot).

This adventure isn't the most serious thing in the world, obviously...just some Summer break fun. 
But do you guys see any reasons not to do this? Or, do you have any suggestions on how to run the adventure?
	"""),#7
		("suhailvs",9,
"""
What is the proof, without leaving the Earth, and involving only basic physics, that the earth rotates around its axis?
By basic physics I mean the physics that the early physicists must've used to deduce that it rotates, not relativity.
"""
			),#8
		("anoop",1,
"""
Mr A has almost one year of experience with us now. He joined as a 'fresher' (unexperienced).
The problem is he does not have his concepts clear, so we have asked him to take part in various training courses on Saturday and sometimes on Sunday. He demonstrates a lack of interest in the suggested training and does not attend this training regularly. The training is being provided by our senior managers and we are investing our time and money into this employee that way.

We expect him to work hard so that he comes to a level where he can start giving results. He is not ready for complex tasks. He is argumentative with his manager and tries to prove he is right when told his work is incorrect.

Is there an alternative to firing this worker? What might the consequences be if he is fired for the remainder of the staff?
"""
			),#9
)

#Answer(user,question,answer)
ANSWERS_DATA=(
		("sumesh",1,
			"""
			Slightly off topic, but in 'Profiles of the future', when talking about the possibility of invisibility, 
			Arthur C Clarke says 'An invisible man wouldn't just be blind, he would be dead'. 
			At first I misinterpreted this as saying any 'inivisibility potion' would kill you.
			But what it is saying is that normal light would disrupt the processes going on in your cells too much, so its a good thing you've got a fairly opaque skin to keep it out.
		"""),
		("sumesh",1,
			"""
			Individual photons are very small and don't have much energy. If you put a lot of them together in one place you can hurt somebody - 
			by simply supplying enough power to melt an object (ask any spy on a table underneath a laser beam). 
			There is another very odd feature of photons. Although lots of them can provide a lot of energy and heat an object, it takes an individual photon of enough energy to break a chemical bond. 
			So while a single high-energy ultraviolet photon can break a molecule in your skin and cause damage, a billion lower energy visible photons hitting the same point can't break that single bond. 
			Even though they together carry much more energy, it is the energy that is delivered in a single photon that matters in chemistry.
			Fortunately the Earth's atmosphere shields us from the photons with enough energy to break most chemical bonds.
			"""),
		("sumesh",1,
			"""
			I have a somewhat non-physics answer for you. 
			If you allow me to broaden your question a bit to "why doesn't light kill or otherwise make all life on 
			Earth impossible" the answer is that the Earth is in what we call "the habitable zone".

			If the Sun produced so much light or light at such high energies that it would kill you, 
			it also would heat the planet so much that liquid water would not be possible. 
			In this case, it's probably reasonable to argue via the "anthropic principle" 
			that we live on a planet in the habitable zone because otherwise we wouldn't exist to ask such questions. 
			Note of course too that we've defined the habitable zone based on our own life parameters 
			so there is a bit of a circular definition here.
			"""),			
		("anoop",1,
			"""
			This question is more interesting than I thought at first. 
			I like it. There are several different parts to an answer to this question; 
			I'll just contribute a couple that have something in common:
			our bodies (and everything else, it has nothing to do with bodies)
			also emit photons about as fast as they absorb them.

			On the macroscopic/thermal scale, 
			we have black-body radiation. Via black-body radiation, 
			all matter emits a continuous spectrum of radiation. 
			The distribution of this spectrum depends primarily on 
			the temperature of the object. This is why objects placed 
			in a fire appear to glow red, whether they be wood or metal or rocks. 
			Our bodies also emit radiation this way, but at our temperature, 
			this spectrum is in the infrared range, so it isn't visible 
			(to humans snakes can see body heat). Since everything absorbs 
			and emits photons this way, there's an equilibrium where we 
			receive as much thermal energy as we lose, although that's only 
			in an environment where everything is at equilibrium. 
			Hot things like the sun and incandescent lights can throw this 
			off, which is why it feels hot to go outside... or to 
			be under a heat lamp. Anyway, don't worry about filling 
			up on too many photons, they leave you just as fast.

			On the microscopic scale, we have the hard-to-spell
			phenomenon of fluorescence. When a high-energy photon 
			is absorbed by an atom, some of its energy can be 
			reemitted as a lower-energy photon. Of course, 
			this doesn't happen every time, and I don't know if it 
			happens much in our bodies. It depends on the material's 
			properties. That's where we get fluorescent lights and 
			pigments and laundry detergents detergent manufacturers 
			actually include fluorescent pigments in their products 
			so that clothes emit more visible light than they 
			physically should by absorbing UV light and reemitting 
			it in the visible range. Anyway, while I'm not sure if 
			that principle in particular saves you from atomization, 
			it's worth remembering that not every photon that hits you 
			stays there.

			So in conclusion, even though the energy that light 
			brings to our bodies (and the earth) is substantial 
			(imagine if there were no sun radiation is important!), 
			we're not going to fill up on photons to bursting. We're 
			at equilibrium.
			"""),
		("anoop",2,
			"""
			lol society. I'm also happy with my Nokia 3310.
			TBH I'd like to see whats new with the xbox but 
			expect it'll be at least 2 years before I get one. 
			I cant beleive we'll be at the point whereby we 
			look at our old 360s with the sort of disdain usually 
			reserved for a PS1 or original Xbox.
			Xbox 360 - appearing at a car boot near you! 
			"""),
		("anoop",3,
			"""
			I thought that Einstein said it wonderfully!
			None the less, as we grow older we find ourselves 
			having to focus on day to day problems and don't 
			have the time or energy to just wonder about stuff.

			On the other hand children don't have the knowledge 
			nor the skills to really dig in to the things they 
			have time to wonder about.

			Einstein notes that he had the ability to 
			wonder AND the tools to unravel that which he wondered about.

			I'm thinking that my version is far less understandable 
			than his.
			"""),	
		("jani",7,
			"""
A rogue could perhaps play solo. But only if she devoted herself to stealth and avoided all out combat at all costs.

D&D is a very much a party based game. And it's best played with a table full of friends, each with their own character. But at the same time, occasionally circumstances require something less than that ideal. There are two options.

    Go with a single PC per player and find a playstyle that works for this party composition
    Let the limited number of players play a whole party full of PCs.

In your case, especially in a new system, I'd highly recommend the first. The character your sister want's to play is ideal for this style of gameplay as stealth is key.

Some things I would change/instigate:

    less tactical gameplay, stealth roles are going to a major part of play.
    Make sure situations are there where she can quietly and quickly take down the baddies (Don't put in guards with 20 HP, make sure she can take a guy out before he even sees her).
    Make sure there are places where if she makes good tactical choices she can route a small group of enemies
    Provide a lot of healing potions.
    Design encounters to success is not based on completing combat. Give her clear non-combat objectives.
    Rogues are pretty good at sniping, so if she is coming up on a fight in the open, giving her plenty of opportunities to pick people off before they see her is an excellent choice as well.
    Advantage should be gained and used wherever possible. If she is attacking without advantage she will get slaughtered and quickly. The key to making quick work of bad guys is isolation and dealing her sneak attack which needs advantage to function.

Caves of Chaos might not be the best adventure unless you add enough story so as to provide the require non-combat objectives. There is at least one adventure that necessitates the rescue of prisoners, this would be a good one. 
But things like cleaning out a Kobold nest should probably be written (and the flavor/story is pretty much up to you as the DM) in such a way that the objective isn't Kobold death, but Kobold cooperation or migration. 
She can't kill all the Kobolds, but she can certainly get to their leader and threaten him.
	"""),
	("sumesh",7,
		"""
I've run plenty of solo adventures before, both with sidekick characters and with the player on their own.

There are several key factors I've found when running solo adventures that make them more enjoyable

    Pander to what the player likes as much as possible; that isn't to say you make everything a cakewalk - far from it. What you need to do is find what the player enjoys about the game and give them more of it. 
    For new players this can be difficult and you'll have to give them tasters of different aspects of the game (fighting, sneaking, investigation, diplomacy, etc) New players may well not actually chose a character
     particularly suited to the role they enjoy as well, so bare this in mind.
    Single character I'd advise for solo games just keep the player with a single character - it helps them make the focus about them rather than the player juggling between characters - this can be very confusing for new players.
    Personality. Inject your NPCs with personality, even if it's just a familiar war-cry or a amusing habit; these help the NPCs come to life around the solo player without showboating the NPCs too much. It also makes them feel more of a team.
    Showboating - this is a big thing to avoid; the player's character is the focus of the story. If there is a decision to make about something make sure the NPCs ask the player what they think, give the NPCs personality and quirks but don't drive the story through them. 
    There is a big temptation for GMs to get a favourite NPC especially in solo games and make everything about that NPC. Try to avoid this - don't make an NPC do all the work. 
    For example if the player likes sneaking and a fight erupts, feel free to skim over the details of the NPCs combat details so it runs faster (and is less dull to the player) and they can get back to sneaking.
    Feedback - this is the crucial aspect of solo play, see how they enjoyed things - especially in the first few games. Keep the danger factor light for the character at first perhaps; @waxeagle has some excellent suggestions in his post about this.
    Number of NPCS - This has been mentioned elsewhere but I'll add my thoughts too; keep the number of party NPCs low, ideally it should only be one other NPC - the more NPCs you have the less they should talk. Give one a vow of silence or something to help perhaps.
    This is partly to keep the focus on the player and what they can achieve (the more NPCs, the more THEY can do) and also because the more NPCs you have the more the NPCs would naturally be talking to each other which makes 
    things look a bit weird when a) you do this and b) they don't do this when they should.
    Ideally any conversation should be directed through the player - keep them involved.
    I've generally found support and tanking roles are ideal for NPC sidekicks, like healers.
    If you do run several NPCs remember to prefix their speech with who is talking "Bob says this" or work on accents/slang so it's very obvious who is talking. Such as: "Ach! Me axe kannie get thru the steel door lassie, it don't have tha power!" Yep, it's the dwarf again.
	"""),
	("sumee",7,
		"""
I have done a lot of one-on-one roleplaying similar to what you are describing,
 and I think there are several different approaches. 
 You can use some of these simultaneously or (with a bit of work) switch between them throughout a long campaign, but each is pretty much a stand alone technique that at least for me has made solo games work well.

Run Solo With a Tailored Campaign

You can carefully tailor the campaign to emphasize the character's strengths, avoid things that are impossible for the character, and hit their weaknesses only to present a challenge to be overcome creatively. 
Actually, I think that this is a good suggestion for just about any campaign no matter the party size,
 but it becomes both much easier and much more important when running solo with a standard character.

Done well, this is sufficient to let any character be the star of the story without a party. Think about many of the action movies with one clear hero that handles all the action 
by himself/herself or any of the similar video games where you play a single hero without backup. 
The tombraider series does this well.

Make the character powerful

A single 3rd level character will often be more powerful (though also more narrow) then three first level characters. So, 
if you want to play solo you can often take an adventure designed for a party of first level characters and run it with a 3rd or 4th level character. This doesn't quite always work, 
there are times when you really need a second set of hands, but it works a lot of the time, especially if the character either is of a highly versatile class or dips into a second class for breadth. 
It doesn't hurt to let them be on the high side of the wealth by level 
recommendations to make sure they are equipped for a wide array of possibilities.

Provide a party of henchmen

Done right, there is nothing wrong providing NPC party members. The problem is that when you have a full party to start with, it is very hard to do it right. 
There is a temptation for the DM to identify with the NPC party member and make it a DMPC and even start dipping into "Mary Sue" territory with reality warping around the DMPC to make them seem awesome. 
Even if the DM is scrupulous in avoiding that tempetation, there will be a tendency (at least in some groups) to assume that that NPC has special insight and give what they say too much weight.

But those problems are greatly reduced and the benefits of NPC party members are greatly enhanced when you have a very small group of PCs. The key is to make sure the limelight is on the player. 
This doesn't mean that the NPCs shouldn't be fully fleshed out characters with their own feelings and opinions, but it does mean that the PCs should be the ones calling the shots and getting most of the glory. 
This can actually be easier if the NPCs are fully developped characters, as long as they have a reason to defer to the PCs.

Dragon Age (the video game) did this very well. You wind up with a whole group of followers, each one is well fleshed out (at least if you bother to find out about them) and provoked enough they will leave or even attack you. 
But each one also has a reason that they follow you, obey you, and defer to your judgment. 
Zevran is alive because you spared him and he sees himself as owing you fealty. Leilana believes (perhaps rightly?) that she was ordered by her deity to obey you. Allistair is (at least at the start) explicitly hesitant to make decisions and somewhat submissive. 
They are all every bit as powerful as your character and arguably more experienced, but they each have a reason that they will defer to your character and obey (most) orders.

Its not necessary, but this is more believable and easier if the PCs are mechanically more powerful than the NPCs. This makes it hard for the NPCs to outshine the PCs except when the NPCs particular class skills are needed. If you want there can be something story wise or even mechanical, 
beyond just being higher level, about the PC that makes them the natural leader. Perhaps they were marked by fate itself, chosen by one of the pantheon, of a particular lineage (remember that in the late middle ages your lineage mattered a lot).

Let the players have multiple characters

I have heard of this working, but I have never seen it work in a solo campaign. I think it would work well on a tactically oriented game but less well if you want serious character development.

I have seen it work well with multiple players but normally when there was a reason that there characters would rarely be in the same place at the same time. (In a Vampire: The Masquerade game I have seen players each have a Vampire and also each have a ghoul or just servant that was active during the day...)
If your sister wants to do hack and slash this could be perfect for her, but if she wants to deal with the motivations of her character this could be a distraction.
		"""),
	("suhailvs",7,
		"""
Note: in this answer, when counting players, I'm not considering the GM a player. I know it's not accurate, but I do this for the sake of simplicity.

Playing with only one player has its advantages and disadvantages. Mainly, it's less social and the party is weaker and less balanced.

What is great about having only one player is that he always has the spotlight and don't have to compete for your attention. 
This allows you to make much more personal games, which allow you to explore the character in depth and let he have his own personal relations with the NPCs
 (friends, enemies, lovers,...). This stuff can be very interesting on a 1 on 1 game, but can bore the rest of players in a game of 3+ players.

So, my advice is: make the game very personal. It's all about the PC, let her pursue her goals, and create a good interaction based on her character and 
her background story. Don't be too strict with death, I think in this kind of games GM must try not to kill the hero, because as there is only a character, 
it would make more difficult to continue the story.

About the balance problem, she should pick a class without serious weaknesses and you should prepare adventure that are adapted to her character 
in abilities (ie: if she's a warrior, don't make magic necessary) and in difficulty.
		"""),
	("sumee",8,
"""
The Foucault pendulum is a great experiment which does demonstrate that the Earth is rotating, but it was only introduced in 1851. 
The Earth had been known to rotate for several centuries before that, probably stimulated by Copernicus and Galileo pushing the 
heliocentric model of the solar system during the 16th century.

A couple of decades before Faucalt's pendulum, the Coriolis effect was discovered. This effects (among other similarly large systems) hurricanes, 
causing them to rotate clockwise/anti clockwise depending on whether they're in the southern/northern hemisphere. 
It is an apparent force that appears in any rotating frame of reference (like a spinning planet). This again won't have helped early 'spinning-Earth' believers.

Early evidence that the Earth rotates was almost certainly the observation of the sun, planets and stars moving across the sky and then, 
with the help of telescopes, of the other planets also rotating. Of course this requires you to trust that the Earth is not the centre of the universe and so doesn't "prove" the 
Earth is spinning in the same way as observation of Foucault's pendulum or the Coriolis effect.

The idea of a "proof" in physics is a difficult one. A theory such as the 'spinning-Earth' will at first simply be presented to explain anomalous observations that current theories can't 
(such as why do the other planets and the sun move independently of the background stars if everything rotates together around the Earth?). 
It then gets tested by experiments inspired or predicted by the theory (if the Earth is spinning, what should we expect to observe?). If everything holds up, it's accepted as fact. 
Eventually, some bright spark realises he/she can demonstrate that the Earth is rotating with a clever little experiment 
(Foucault's pendulum/Coriolis effect/launching a rocket into space) and it is added to the mountain of evidence already accumulated on the subject.
"""),
("anoop",8,
"""
An indirect indication that the Earth rotates is the fact that the rotation varies over time. First of all, the orientation of the Earth's axis changes: 
long-term effects like precession and slow variations in the axial tilt, as well as small short-term variations like nutation. Precession was already known in the Ancient world (Hipparchus, Ptolemy,...) 
and the change in axial tilt was recognized by people like Fracastoro (in 1538). See the wiki pages for historic background.

The Earth's period of rotation also changes. 
First of all, the rotation is slowing down, caused by the tidal interaction between the Earth and the Moon: the length of the day increases by about 
2 milliseconds per century. Edmond Halley was the first to notice that the orbital period of the Moon had changed compared with ancient records, and the 
effect was explained in the 18th and 19th century.

semiannual period with an amplitude of 0.29 milliseconds, 10day fluctuations of the order of 0.1 milliseconds, fluctuations due to El Nio events, etc 
(see wikipedia, and also this post). Large earthquakes can also change the rotation period by a few microseconds, but these effects prove difficult to measure (see this article on the 2011 Japan earthquake)
not only over thousands of years but even on a daily basis, when the causes of these variations can be traced back to events on Earth or its orbit. 
"""),
("jani",8,
"""
The Sagnac effect can detect absolute rotation. This is used, for example, in the ring laser gyros used on modern aircraft as navigational devices. 
Not only is it possible to use this effect to prove that the earth rotates, its precision for detecting variations in the rotation is starting to become 
competitive with the most precise techniques: see http://www.wettzell.ifag.de/LKREISEL/G/LaserGyros.html
"""),
('sumesh',8,
"""
Measuring the geometry of the earth, we find that it has an equatorial bulge. We make no assumptions about the cause of the bulge,
 though it suggests already that the earth is rotating as @Mike has described.

We measure the acceleration due to gravity at the poles and on the equator. Most of the difference we find is accounted for by the bulge, but there is a 0.3% discrepancy. The acceleration due to gravity is smaller on the equator than we expect. This discrepancy is nicely explained by assuming the earth is rotating. In fact, making this assumption we can make a rough calculation of the period of the earth.

We could go so far as to carefully measure the acceleration due to gravity along different lines of latitude and thus find the acceleration due to gravity as a function of latitude. We would find that these measurements were well described by a model in which the oblate earth were rotating with a period of about a day.

"""
	),
('sumesh',9,
"""
OK, let go through this point by point:

    Mr A is almost one year experience now. He joined as fresher.

So this person has come in with no experience.

    The problem is he is not having his concepts clear, so we have asked him to go under various trainings

OK, but how much training was given up front? Depending on what you do I would expect some ramp up time on technologies AND the code base AND the business domain. Even an experienced developer can take 6 months+ before becoming productive if the area is complicated.

    on Saturday and even sometime on Sunday

How many hours is this person doing normally? if they're on the backfoot as they aren't seen to be coping (as sounds like the case), they'll likely be putting in all hours to try to keep up, and you want them to use their rest/family time for more?

    But he is not taking interest in trainings too. he is not coming for training regularly

Have you discussed this with him? maybe he has kids to look after (maybe he slept in after pulling several long weeks)?

    The training is being provided by our senior managers and we are investing our time and money in that.

hmm, this sounds like being sent to your head teacher for punishment, doubt I'd be interested myself.

    We are expecting him to work hard so that he come to certain level by which he can start producing results

So, you need to prioritise his training over production work. make sure he is up to speed on the important things he needs (in office time).

You then need to get him one of your senior engineers as a mentor. Your new-be should be working as an extension to this senior, so he gets a change to see the codebase, find out the gotchas, and have his work reviewed as he works. Pick someone with an easy going nature, who's high velocity (but not on the critical path), with enough knowledge to pick up tasks anywhere in the code (and ensure they work over a wide area).

I would write off the forced training done, look to spend 6 months doing this. You should be able to judge if it's a benefit within 2-3 months. During this time talk to your senior, find out what they think, and judge from there, maybe the guy isn't up to it, but you only get results if you invest in your staff.
"""
	),
("jani",9,
"""
Unless it was specified in the contract, I don't think you should expect someone to work on a weekend, we all need our rest and to spend some time with our families, friends and even just slouching on the couch doing nothing. People are not machines.

If he needs further training it needs to be provided for him during the working week.

That said, if you are unhappy with the performance you need to have a talk with this person explaining clearly the expectations, current results and also consequences of failing to meet the expectations from now on.

After that, if this person cannot meet the expectations until an agreed time (you need to make it as clear as possible), you should fire him.

I am really against keeping people at work when they don't fit, just because management feels bad. It is not fair for the company, other workers who are meeting expectations and the discussed employee.
"""),
("sumee",9,
"""
Completing tasks is typically dependent on three conditions being met:

    Resources are available to meet the demands
    There is sufficient knowledge to perform the task
    Your employee is motivated to 'work hard'

It seems that your employee does have enough resources to complete the task (i.e. is not bogged down with several other tasks). While it may not be an issue in your specific case it could be that the technology infrastructure slows them down or there are delays in their work that you are not aware of. If they do not meet the deadlines they have agreed, can they explain the delays?

You mention that you have 'offered' training at the weekend (with an implicit expectation that they do so), and you have also made it clear to them that this comes with a cost attached to it.

Training for the most part should only be during work hours, especially when it is essentially mandatory (and even more so for a junior member of the team). Also, training is subjective - what works amazingly well for one person might not sink in at all for others: if the training is not in line with the way they learn best they will become bored of it quickly, and what incentive is there for coming into training in your personal time when it doesn't click or have a quickly demonstrable gain?

Motivationally-speaking, there seems to be negative reinforcement rather than positive when discussing timelines and project delays with this employee (which would naturally result in them becoming defensive and arguing with managers). Working in a buddy system can be a good way to monitor their work and also engage them more in the daily tasks through collaborative teamwork.

Ultimately if the only solution you present to someone who is challenged by their work is to come in, unpaid, on their precious weekends then a serious review of your training practices is needed.
"""),
("suhailvs",9,
"""
Shall we fire him ?

That's your decision, not anyone else's, and it sounds like you're not taking it lightly, which is a good thing.

    is there any alternative -last option before firing him?

You should ensure

    he understands explicitly that he is performing badly;
    he has an opportunity to discuss; and
    he has the opportunity to show he can improve, with appropriate support.

I'd emphasize point 1 because from your post it isn't clear that you have told him explicitly and in detail how his performance isn't good enough; you've only said you've asked him to take extra time to undergo training and are expecting him to work hard. You need to make your expectations very clear, and also how near or far he is to meeting them.

In the UK where I work there are legal hoops that have to be jumped through. Essentially you give the person a series of warnings about their bad performance, together with appropriate training, and if after three warnings the employee has not improved, you can fire them. This isn't the place to advise on legal issues (although you should have your legal position clear). The point I wanted to make was that some time ago I was very struck by an entrepreneur saying how he had wished he could just have fired several unproductive employees, but was forced to go through the process of giving them warnings. He said at the end of the process, he did fire some of them, but some of them were retained, improved their performance and several years on are good performers. So he was glad he had gone through the procedures of formal warnings.

    We feel bad firing somebody

It shouldn't feel good. Bear in mind, however, that there if you fire Mr A and hire Ms B, Ms B might be just as deserving of the position in human terms as Mr A. Moreover Mr A may go onto find something he is better at, or go onto improve his performance in general, which is better for him in the long run.

    How will our decision affect other coworkers?

Some time ago I was a manager and I expected good performance. I imagined that my reports would be upset about that, but I was pleasantly surprised to find that after I stopped being a manager I am still friends with many of them.

More recently I have had the experience of working in a team where one team member was performing badly, and very little was done about it. As someone who performed well I found that very demoralizing. I have talked with friends and colleagues who say the same thing: if a team member is performing badly, it is demotivating for those who want to do well. On the other hand, if one of my colleagues were fired, I'd want to know that they'd had a clear warning about their performance and been given a chance to fix whatever was broken.
"""),
("Accenture",9,
"""
I'm not going to make a judgement call that the manager of the team MUST make. But here's the premises for how to make that sort of decision.
When to Fire

The bottom line is, if after a "reasonable" amount of time, feedback and resources are available to learn, if the person can't come up to speed in the same time frame that most of his collegues can, then he should be fired.

For most jobs, there's a known length of time for a learning curve. In my experience, a year is on the long side - valid in some extremely complex jobs, environments and organizations, but 3-6 months is often the norm for many engineering positions working with standard technology in a standard way with a typical culture.

Another big catch is that many companies may have a probation period - if there's serious issues with a new hire, don't let it lag past the probation period - it's there specifically give you the option to get rid of a bad hiring choice without the tremendous overhead of most corporate hiring processes.
What to Do Before Firing

#1 thing - Give feedback

It is no fun. No one likes to say negative stuff. But the most ethical thing (and often required by HR process) is to alert the employee that there is a problem with performance. It makes sense.

Think of the case in point - without feedback, there are two options to the other guy's side of this story. From his point of view:

Option 1 (no feedback) - I've been working hard for this company, doing my thing, getting it right. They came and asked me to take training on Saturdays and Sundays with Senior Management. They must really think I'm a rockstar. I'll continue to crank away, but these optional meetings don't really fit with my family obligations, so I'm grumpy (or will say no). They really should be more considerate of the needs of top performers.

Option 2 (with feedback) - Eesh, I hadn't realized my job was in jeopardy! I thought I was getting it, but my manager just said that I"m missing major concepts and he gave me 3 examples where I created a pretty big mess. I think this weekend training is the only way to catch up, and I hope I don't act like a jerk with senior management. I'll make the time and be thankful for the extra chance.

The difference here is that the guy is aware that he's messing up.

Also...

It's best to give direct guidance on what it will take to correct the situation and how this can be demonstrated and measured. Examples of problems, and what needed to happen better are good. Anything clear and unambiguous. But be careful to say "if you do this, it'll let you keep your job" unless that's true. It's easy to get into that case - for example, being reliably on time to work is a must have in most environments for good job performance. But it's not the ONLY qualification. You have actually do your job as well. Just sitting there, drooling, isn't going to save a job.

In many environments, there's a "probation" cycle of:

    feedback
    plan of action to improve
    execution of better job performance action plan
    yes/no decision

In a big company, this can be very formalized.

In most hard jobs, there's not a very, very clear plan of action. If you have a wrote procedure, then it's pretty clear - which is why safety violations, for example, can involve immediate firing - they are intentionally clear, unambiguous, and specific.

But in knowledge work "think harder" is not meaningful advice. So a plan of action is often worked out jointly. The manager says "I need more of X or less of Y" and the employee says "I could do that this way or that way, but I need A or B". It can't be ultimately the employee's choice, because there are finite demands. But where it's possible, the process of getting from bad to good is something the employee can and should give input on.
Consequences on Staff

I've been through some pretty bad layoffs, and I can honestly say, I think it's harder on the manager than on the staff. Looking into someone's eye and saying "you're not good enough to work here" - is the worst part.

Staff reactions will vary by person and predicament. But in a rightful hiring, they are usually:

    (Most) - phew, the troublemaker is gone, we can get back to work! Most people who like the job and know what good work is (they know, because they do it), will know that this person is not getting the job done. Usually knowing that their bosses won't ask them to pick up the slack and allow the problem to continue is a relief to most. Particularly if they know there was a reasonably fair process.

    (Some) - Oh no!! Am I next??? Those that didn't get why this person was a poor perfomer will ask. Often it helps to out line what you expect "if you X, Y and Z in a reasonable time frame, we're good". Stay out of what the problem person did, stick to your own expectations and clarifying if the other employees are meeting them in your opinion. Back to feedback - good or bad, people need it.

    (A few) - The totalitarian dictators are opressing us! Yeah. There will be a few who hate that anyone was fired. My experience is that they won't raise it to management, they will raise it with peers. The big question is - OK, if he stayed, someone was going to pick up the slack... given that you wanted him to be employeed here, would you have been willing to do your work and his? This isn't as crazy as it sounds. Once and a great while, the answer is "yes" and some interesting discussions can ensue.

Worse yet, is the opposing issue - collect too many non-performers, and you create a retention issue. If you have a now-experienced person who wanders around clueless on concepts, then when new people come, he will be their impression of a standard employee. That's worse for morale than the momentary pain of firing the real problem.
"""),
("lidercs",9,
"""
Look, a job is NOT a social institution. It is not granted on basis of "opportunities out there" It is about doing work, and get salary if done right.

Certainly if you are the owner of the business, you are allowed to throw your money away as you see fit, including burn it in campfire or give out as charity. But if it's not the case, and you are, in your job, responsible for good use of resources, including salary budget, it is your responsibility to either make the guy work up or get rid of him. ASAP.

From the description it seem you already passed the "put on improvement plan" part and it didn't work. So the next logical step is to offer some agreement terms on leaving. And if rejected proceed by regular or special form of termination.

i always consider mutual agreement the best form, if unprofessional conduct applies to the situation the more chances you have to make it work as a better choice for the other party.

As for coworkers, sending off people is certainly not a regular morale boost, but if the guy was actually bad and worked in teal, the coworkers who actually did the job will be happy. As doing others work while they sit back and just get the money is even more drag.

If reasons are not obvious it may be a good idea explaining all the reasons and especially addressing that it's not part of some downsizing, and the vent is tied to personal performance, not to be extrapolated to anyone else. Also good idea to announce that replacement is getting hired (if so), meybe even ask the team;s help to find someone usable.
"""),
("cognizent",9,
"""
I won't get into all the more minor details of your plan to salvage the situation, that's been covered pretty well.

However, I will say that I have managed quite a number of people. I have NEVER been in a situation where I was questioning in my head whether I should fire someone, then tried to make it work and didn't regret it. Trust your gut, don't prolong your misery.

I know where your head is at. You like the person. You think you just need to give them a little more motivation, or training, or something. But trust me, an unmotivated person who is under-performing is not a project worth your time that you could better spend motivating your star players.

Plus, if you know the guy isn't working out you can bet your team does too. It is much more demoralizing for them to be working hard and seeing you coddle (try to save) an under-performer.

Spend your time on your TOP performers, not fixing the underperformers. The ROI is much better.
"""),
("capsone",9,
"""
First thing is that user5377 taking it emotionally. and i think it's not bad idea.

you provide him fully environment then also he is not trying to develop himself then it is his problem. i want to suggest that you should directly talk with Mr.A about his problem.

1)i mean at which point he have problem?
2)What things he can't getting?

if then also he is not ready to learn anything and not cooperate with company then you should do meeting with your manager and discuss about Mr.A all are agree then you can fire Mr.A directly. but don't fire him without discuss his problem with him.

i have my own example. as i am also under the training now a days, i do try to learn task whole day. if i can't get idea, my co-worker help me alot. and also my sir. but my problem is that i need to learn all thing in detail and i need more time to understand thoroughly so, i am trying to learn on weekend also. i am also allocate weekly 45 hours.
"""),
("niveda",9,
"""
I've always thought that a problem is a chance to do your best. From your question it's clear that your employee does not understand that he has problems (i.e. might be fired). Why won't you let him know it and see if he is able to be more productive? In a case it appears that employee was doing his best it means he is not in a good fit for his current position and further explanations would not be required. If his performance will be improved everybody is going to be happy.

The trickiest part here is how to let him know about it. I don't know if this is the best way of doing this but personally I'd send him on leave without salary for 2-4 weeks (depending on company needs) and tell him that when returns he should take some exams (related to work, of course) and the results will affect his position. You can identify if it worth to continue working with this employee depending on exam results.
"""),
("gomathi",9,
"""
If you are unhappy with an employee, and there is no sign of improvement, I would decide to let that person go. I assume that the employee does not have a permanent contract. Therefore, I would discuss his (lack of) performance during the yearly (?) performance meeting, and simply not prolong his contract. This is under the assumption that you warned the employee during the year that his performance needed to improve, although not prolonging a contract can be decided unilaterally by the employer. If this person has a permanent contract, you'll have more problems getting rid of them.

If he/she is not productive, and not making an effort to get up-to-speed, it is better to part ways. In general, this should have no adverse effect on other people, as it is Mr. A's performance that is lacking, not their own.
"""),
("satheesh",9,
"""
But with a permanent contract, it is harder to get rid of someone from a legal standpoint. You need to be able to show a judge that the person was really under performing. With a temporary contract you can simply let the contract expire
you are just going to fire this guy when there are SO many questions to ask this company! 1. It is a startup so i assure you their processes are shit, and probably 90% of their codebase. And their management. They need to look on this employee as a chance to correct wrongs - including letting the situation get this far, and ridic "training on the weekend"
"""),
("karthik",9,
"""
 I would fire the guy after the "improvement plan" route got exhausted. From OPs description it's moot issue, I assume it was, others assume it was not -- but we all are just speculating. The rest you write is even more speculation based on just keyword match on keyword "weekend"
"""),
("naveen",9,
"""
 If you buy a city bike and take it on a mountain trail ride, it won't work. If you try and fix it by adding the oil it still won't work. Translation: if the company is misutilising the employee AND their solution to training is flawed, it isn't an indictment on the employee. In fact, it is an indictment on the company - and they should be able to see that they've done something wrong and remedy it
"""),
("sami",9,
"""	
Or if the city bike turned out suboptimal in the mountains maybe it's time to face the situation and replace it with an actual mountain bike instead of trying to patch it while riding. If the company is not up to the task of training, then it better hire already-trained personnel and do its primary business. And I could write a hundred more speculative IFs in the next hour, each likely as far from the truth as any other.
"""),
)



#usage
#---------

# commet out these lines in file quorum/models
# admin.site.register(Topic)
#open cmd. 
#then goto main directory(ie directory contains manage.py)
#then execute $: python manage.py shell
#you will enter into python shell >>
# >>> import ci
# >>> ci.initd()


# now uncommet these lines in file quorum/models
# admin.site.register(Topic)
#
# now uncommet these in registration/models 
# admin.site.register(Employer), admin.site.register(Jobseeker)

from quorum import models
from django.contrib.auth.models import User
def add_topics(M):
	#topics
	for i in TOPICS_DATA:
		p=M.Topic(creator_id=1,topic=i[0],imgurl=i[1])
		p.save()

def add_users(M):
	for i in USERS_DATA:
		p=User.objects.create_user(username=i[0],email=i[1],
			password='s')#,first_name=i[2],last_name=i[3])
		p.is_active = True
		p.save()		

def add_questions(M):
	#Question(user, topic, question)
	for i in QUESTIONS_DATA:
		usr=User.objects.get(username=i[0])
		tp=M.Topic.objects.get(pk=i[1])
		p=M.Question(user=usr,topic=tp,question=i[2])
		p.save()

def add_answers(M):
	#Answer(user,question,answer)
	for i in ANSWERS_DATA:
		usr=User.objects.get(username=i[0])
		qst=M.Question.objects.get(pk=i[1])
		p=M.Answer(user=usr,question=qst,answer=i[2])
		p.save()
		
def initd():
	add_topics(models)
	add_users(models)
	add_questions(models)
	add_answers(models)