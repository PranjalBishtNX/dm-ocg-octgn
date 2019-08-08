# ------------------------------------------------------------------------------
# Constant and Variables Values
# ------------------------------------------------------------------------------
import re
import itertools

shields = []
playerside = None
sideflip = None
diesides = 20
shieldMarker = ('Shield', 'a4ba770e-3a38-4494-b729-ef5c89f561b7')
waitingCard = []  # Cards waiting for targets. Please replace this with FUNCTIONS waiting for targets later. If a card calls 2 functions both will happen again otherwise
waitingCard1 = []
waitingCard2 = []
functionlistglobal = []
# Start of Automation code

cardScripts = {
	# ON PLAY EFFECTS

	'Alshia, Spirit of Novas': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Akashic Second, Electro-Spirit': {'onPlay': ['draw(me.Deck, True)']},
	'Aures, Spirit Knight': {'onPlay': ['mana(me.Deck)']},
	'Aqua Bouncer': {'onPlay': ['bounce()']},
	'Aqua Deformer': {'onPlay': ['fromMana(2, "ALL", "ALL", "ALL", True, False, True)']},
	'Aqua Hulcus': {'onPlay': ['draw(me.Deck, True)']},
	'Aqua Hulk': {'onPlay': ['draw(me.Deck, True)']},
	'Aqua Sniper': {'onPlay': ['bounce(2)']},
	'Aqua Surfer': {'onPlay': ['bounce()']},
	'Armored Decimator Valkaizer': {'onPlay': [' kill(4000)']},
	'Artisan Picora': {'onPlay': ['fromMana(1,"ALL","ALL","ALL",False,True)']},
	'Astral Warper': {'onPlay': ['draw(me.Deck, True, 3)']},
	'Baban Ban Ban, Earth\'s Blessing': {'onPlay': ['massMana(me.Deck, True)']},
	'Ballom, Master of Death': {'onPlay': ['destroyAll(table, True, "ALL", "Darkness", True)']},
	'Bega, Vizier of Shadow': {'onPlay': ['shields(me.Deck)', 'targetDiscard(True)']},
	'Belix, the Explorer': {'onPlay': ['fromMana(1,"Spell")']},
	'Bronze-Arm Tribe': {'onPlay': ['mana(me.Deck)']},
	'Bronze Chain Sickle': {'onPlay': ['mana(me.Deck)']},
	'Buinbe, Airspace Guardian': {'onPlay': ['draw(me.Deck, True)']},
	'Chaos Worm': {'onPlay': [' kill()']},
	'Chief De Baula, Machine King of Mystic Light': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Cobalt Hulcus, Aqua Savage': {'onPlay': ['draw(me.Deck, True)']},
	'Corile': {'onPlay': ['bounce(1, True, True)']},
	'Craze Valkyrie, the Drastic': {'onPlay': ['tapCreature(2)']},
	'Crimson Maru, the Untamed Flame': {'onPlay': [' kill(4000)']},
	'Cyber N World': {'onPlay': [' semiReset()']},
	'Dacity Dragoon, Explosive Beast': {'onPlay': [' kill(3000)']},
	'Dandy Eggplant': {'onPlay': ['fromDeck()']},
	'Dark Hydra, Evil Planet Lord': {'onPlay': ['fromGrave()']},
	'Death Mendosa, Death Dragonic Baron': {'onPlay': ['kill("ALL","Untap")']},
	'Emperor Himiko': {'onPlay': ['draw(me.Deck, True)']},
	'Emperor Marco': {'onPlay': ['draw(me.Deck, False, 3)']},
	'Estol, Vizier of Aqua': {'onPlay': ['shields(me.Deck)']},
	'Evolution Totem': {'onPlay': [' search(me.Deck, 1, "Evolution Creature")']},
	'Factory Shell Q': {'onPlay': [' search(me.Deck, 1, "ALL", "ALL", "Survivor")']},
	'Fighter Dual Fang': {'onPlay': [' mana(me.Deck,2)']},
	'Fist Dragoon': {'onPlay': ['kill(2000)']},
	'Flameburn Dragon': {'onPlay': ['kill(4000)']},
	'Fonch, the Oracle': {'onPlay': [' tapCreature()']},
	'Forest Sword, Great Hero': {'onPlay': ['mana(me.Deck)']},
	'Fortress Shell': {'onPlay': [' destroyMana(2)']},
	'Forbos, Sanctum Guardian Q': {'onPlay': [' search(me.Deck, 1, "Spell")']},
	'Funky Wizard': {'onPlay': [' draw(me.Deck, True)']},
	'Gajirabute, Vile Centurion': {'onPlay': ['burnShieldKill(1)']},
	'Galek, the Shadow Warrior': {'onPlay': ['targetDiscard(True)']},
	'Gardner, the Invoked': {'onPlay': ['gear("mana")']},
	'Gigargon': {'onPlay': [' search(me.piles["Graveyard"], 2, "Creature")']},
	'Gigabalza': {'onPlay': ['targetDiscard(True)']},
	'Grave Worm Q': {'onPlay': ['search(me.piles["Graveyard"], 1, "ALL", "ALL", "Survivor")']},
	'Gunes Valkyrie, Holy Vizier': {'onPlay': ['tapCreature()']},
	'Gylus, Larval Lord': {'onPlay': ['targetDiscard(True)']},
	'Gyulcas, Sage of the East Wind': {'onPlay': [' search(me.Deck, 1, "Cross Gear")']},
	'Hawkeye Lunatron': {'onPlay': ['search(me.Deck, 1, "ALL", "ALL", "ALL", False)']},
	'Honenbe, Skeletal Guardian': {
		'onPlay': ['mill(me.Deck, 3, True)', 'search(me.piles["Graveyard"], 1, "Creature")']},
	'Hormone, Maxim Bronze': {'onPlay': ['mana(me.Deck)']},
	'Hot Spring Crimson Meow': {'onPlay': ['draw(me.Deck, True)']},
	'Hulk Crawler': {'onPlay': ['draw(me.Deck, True)']},
	'Hurlosaur': {'onPlay': [' kill(1000)']},
	'Iron Arm Tribe': {'onPlay': ['mana(me.Deck)']},
	'Izana Keeza': {'onPlay': [' kill(2000)']},
	'Jasmine, Mist Faerie': {'onPlay': ['suicide("Jasmine, Mist Faerie", mana, me.Deck)']},
	'Jelly, Dazzling Electro-Princess': {'onPlay': ['draw(me.Deck, True)']},
	'Jenny, the Dismantling Puppet': {'onPlay': [' targetDiscard()']},
	'Jenny, the Suicide Doll': {'onPlay': ['suicide("Jenny, the Suicide Doll", targetDiscard, True)']},
	'Jet R.E, Brave Vizier': {'onPlay': ['shields(me.Deck)']},
	'King Ripped-Hide': {'onPlay': ['draw(me.Deck, True, 2)']},
	'Kolon, the Oracle': {'onPlay': ['tapCreature()']},
	'Lena, Vizier of Brilliance': {'onPlay': ['fromMana(1,"Spell")']},
	'Lugias, The Explorer': {'onPlay': ['tapCreature()']},
	'Locomotiver': {'onPlay': ['targetDiscard(True)']},
	'Magris, Vizier of Magnetism': {'onPlay': ['draw(me.Deck, True)']},
	'Masked Horror, Shadow of Scorn': {'onPlay': ['targetDiscard(True)']},
	'Meteosaur': {'onPlay': ['kill(2000)']},
	'Miele, Vizier of Lightning': {'onPlay': ['tapCreature()']},
	'Moors, the Dirty Digger Puppet': {'onPlay': [' search(me.piles["Graveyard"])']},
	'Muramasa\'s Socket': {'onPlay': [' kill(1000)']},
	'Murian': {'onPlay': ['suicide("Murian", draw, me.Deck)']},
	'Nam=Daeddo, Bronze Style': {'onPlay': ['mana(me.Deck, preCondition=manaArmsCheck("Nature",3))']},
	'Niofa, Horned Protector': {'onPlay': ['search(me.Deck, 1, "ALL", "Nature")']},
	'Ochappi, Pure Hearted Faerie': {'onPlay': ['fromGrave()']},
	'Pakurio': {'onPlay': [' targetDiscard(False,"shields")']},
	'Phal Eega, Dawn Guardian': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Phal Pierro, Apocalyptic Guardian': {'onPlay': ['suicide("Phal Pierro, Apocalyptic Guardian", fromGrave, )']},
	'Phal Reeze, Apocalyptic Sage': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Piara Heart': {'onPlay': [' kill(1000)']},
	'Pointa, the Aqua Shadow': {'onPlay': ['targetDiscard(True)']},
	'Prometheus, Splash Axe': {'onPlay': ['mana(me.Deck, 2, False, True)']},
	'Qurian': {'onPlay': ['draw(me.Deck, True)']},
	'Raiden, Lightfang Ninja': {'onPlay': ['tapCreature()']},
	'Rayla, Truth Enforcer': {'onPlay': ['search(me.Deck, 1, "Spell")']},
	'Rom, Vizier of Tendrils': {'onPlay': ['tapCreature()']},
	'Rothus, the Traveler': {'onPlay': ['sacrifice()']},
	'Romanesk, the Dragon Wizard': {'onPlay': [' mana(me.Deck, 4)']},
	'Rumbling Terahorn': {'onPlay': ['search(me.Deck, 1, "Creature")']},
	'Ryokudou, the Principle Defender': {'onPlay': ['mana(me.Deck,2)', 'fromMana()']},
	'Sarvarti, Thunder Spirit Knight': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Scissor Scarab': {'onPlay': ['search(1,"ALL","ALL","Giant Insect")']},
	'Shtra': {'onPlay': [' fromMana(1, "ALL", "ALL", "ALL", True, False, True)']},
	'Self-Destructing Gil Poser': {'onPlay': ['suicide("Self-Destructing Gil Poser", kill, 2000)']},
	'Sir Navaal, Thunder Mecha Knight': {'onPlay': ['fromMana(1,"Spell")']},
	'Sir Virginia, Mystic Light Insect': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Skysword, the Savage Vizier': {'onPlay': ['mana(me.Deck)', 'shields(me.deck)']},
	'Solidskin Fish': {'onPlay': ['fromMana()']},
	'Spiritual Star Dragon': {'onPlay': ['fromDeck()']},
	'Splash Zebrafish': {'onPlay': ['fromMana()']},
	'Syforce, Aurora Elemental': {'onPlay': ['fromMana(1,"Spell")']},
	'Terradragon Zalberg': {'onPlay': [' destroyMana(2)']},
	'Thorny Mandra': {'onPlay': [' fromGrave()']},
	'Thrash Crawler': {'onPlay': [' fromMana()']},
	'Titan Giant': {'onPlay': ['mana (me.Deck, 2, True)']},
	'Torpedo Cluster': {'onPlay': [' fromMana()']},
	'Triple Mouth, Decaying Savage': {'onPlay': ['mana(me.Deck)', 'targetDiscard(True)']},
	'Unicorn Fish': {'onPlay': ['bounce()']},
	'Velyrika Dragon': {'onPlay': ['search(me.Deck, 1, "ALL", "ALL", "Armored Dragon")']},
	'Viblo Blade, Hulcus Range': {'onPlay': ['draw(me.Deck, True)']},
	'Walmiel, Electro-Sage': {'onPlay': ['tapCreature()']},
	'Whispering Totem': {'onPlay': ['fromDeck()']},
	'Wind Axe, the Warrior Savage': {'onPlay': [' mana(me.Deck)']},
	'Zardia, Spirit of Bloody Winds': {'onPlay': [' shields(me.Deck)']},
	'Zemechis, the Explorer': {'onPlay': [' gear("kill")']},
	# ON CAST EFFECTS

	'Abduction Charger': {'onPlay': [' bounce(2)']},
	'Apocalypse Day': {'onPlay': [' destroyAll(table, len([card for card in table if isCreature(card)])>5)']},
	'Big Beast Cannon': {'onPlay': ['kill(7000)']},
	'Blizzard of Spears': {'onPlay': [' destroyAll(table, True, 4000)']},
	'Bomber Doll': {'onPlay': ['kill(2000)']},
	'Bone Dance Charger': {'onPlay': ['mill(me.Deck, 2)']},
	'Boomerang Comet': {'onPlay': ['fromMana()', 'toMana(card)']},
	'Brain Cyclone': {'onPlay': ['draw(me.Deck, False, 1)']},
	'Brain Serum': {'onPlay': [' draw(me.Deck, False, 2)']},
	'Burst Shot': {'onPlay': [' destroyAll(table, True, 2000)']},
	'Cannonball Sling': {'onPlay': ['kill(2000)'],
						 'onMetaMorph': ['kill(6000)']},
	'Chains of Sacrifice': {'onPlay': ['kill("ALL","ALL","ALL",2)', 'sacrifice()']},
	'Clone Factory': {'onPlay': [' fromMana(2)']},
	'Cloned Nightmare': {'onPlay': [' clonedDiscard()']},
	'Corpse Charger': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Crimson Hammer': {'onPlay': ['kill(2000)']},
	'Cyber Brain': {'onPlay': ['draw(me.Deck, False, 3)']},
	'Crystal Memory': {'onPlay': ['search(me.Deck, 1, "ALL", "ALL", "ALL", False)']},
	'Darkflame Drive': {'onPlay': ['kill("ALL","Untap")']},
	'Dark Reversal': {'onPlay': ['search(me.piles["Graveyard"], 1, "Creature")']},
	'Death Chaser': {'onPlay': ['kill("ALL","Untap")']},
	'Death Gate, Gate of Hell': {'onPlay': ['kill("ALL","Untap")', 'fromGrave()']},
	'Death Smoke': {'onPlay': ['kill("ALL","Untap")']},
	'Decopin Crash': {'onPlay': ['kill(4000)']},
	'Devil Hand': {'onPlay': ['kill()', 'mill(me.Deck, 3, True)']},
	'Devil Smoke': {'onPlay': ['kill("ALL","Untap")']},
	'Dimension Gate': {'onPlay': ['search(me.Deck, 1, "Creature")']},
	'Dracobarrier': {'onPlay': ['tapCreature()']},
	'Drill Bowgun': {'onPlay': ['gear("kill")']},
	'Enchanted Soil': {'onPlay': ['fromGrave()']},
	'Energy Stream': {'onPlay': ['draw(me.Deck, False, 2)']},
	'Eureka Charger': {'onPlay': ['draw(me.Deck)']},
	'Eureka Program': {'onPlay': ['eurekaProgram(True)']},
	'Faerie Crystal': {'onPlay': ['mana(me.Deck, postAction="ManaIfCiv", postArgs=["Zero"] )']},
	'Faerie Life': {'onPlay': ['mana(me.Deck)']},
	'Faerie Miracle': {'onPlay': ['mana(me.Deck, postAction="mana(me.Deck)", postCondition="manaArmsCheck()")']},
	'Faerie Shower': {'onPlay': ['lookAtTopCards(2,"card","hand","mana", False)']},
	'Flame-Absorbing Palm': {'onPlay': ['kill(2000)']},
	'Fire Crystal Bomb': {'onPlay': ['kill(5000)']},
	'Flame Lance Trap': {'onPlay': ['kill(5000)']},
	'Flood Valve': {'onPlay': ['fromMana()']},
	'Gardening Drive': {'onPlay': ['mana(me.Deck)']},
	'Gatling Cyclone': {'onPlay': [' kill(2000)']},
	'Geo Bronze Magic': {'onPlay': ['mana(me.Deck, postAction="DrawIfCiv", postArgs=["Fire", "Light"])']},
	'Ghost Clutch': {'onPlay': ['targetDiscard(True)']},
	'Ghost Touch': {'onPlay': ['targetDiscard(True)']},
	'Goren Cannon': {'onPlay': ['kill(3000)']},
	'Goromaru Communication': {'onPlay': ['search(me.Deck, 1, "Creature")']},
	'Hell Chariot': {'onPlay': ['kill("ALL","Untap")']},
	'Hide and Seek': {
		'onPlay': ['bounce(1, True, condition = \'not re.search("Evolution", card.Type)\')', 'targetDiscard(True)']},
	'Hogan Blaster': {'onPlay': ['drama(True, "creature or spell", "battlezone", "top")']},
	'Holy Awe': {'onPlay': ['tapCreature(1,True)']},
	'Hopeless Vortex': {'onPlay': ['kill()']},
	'Hyperspatial Storm Hole': {'onPlay': ['kill(5000)']},
	'Hyperspatial Bolshack Hole': {'onPlay': ['kill(5000)']},
	'Hyperspatial Kutt Hole': {'onPlay': ['kill(5000)']},
	'Hyperspatial Guard Hole': {'onPlay': ['sendToShields()']},
	'Hyperspatial Vice Hole': {'onPlay': [' targetDiscard()']},
	'Hyperspatial Shiny Hole': {'onPlay': ['tapCreature()']},
	'Hyperspatial Energy Hole': {'onPlay': ['draw(me.Deck, False, 1)']},
	'Hyperspatial Faerie Hole': {'onPlay': ['mana(me.Deck)']},
	'Hyperspatial Revive Hole': {'onPlay': ['search(me.piles["Graveyard"], 1, "Creature")']},
	'Infernal Smash': {'onPlay': ['kill()']},
	'Intense Vacuuming Twist': {
		'onPlay': ['lookAtTopCards(5, "card", "hand", "bottom", True, "BOUNCE", ["Fire", "Nature"])', 'bounce(1,False, False, "True", True)']},
	'Invincible Abyss': {'onPlay': ['destroyAll([card for card in table if card.owner != me], True)']},
	'Invincible Aura': {'onPlay': ['shields(me.Deck, 3, True)']},
	'Invincible Technology': {'onPlay': ['search(me.Deck,len(me.Deck)']},
	'Lifeplan Charger': {'onPlay': ['lookAtTopCards(5, "Creature")']},
	'Lightning Charger': {'onPlay': ['tapCreature()']},
	'Like a Rolling Storm': {'onPlay': ['mill(me.Deck, 3, True)', 'search(me.piles["Graveyard"], 1, "Creature")']},
	'Lionic Phantom Dragon\'s Flame': {'onPlay': [' kill(2000)']},
	'Living Lithograph': {'onPlay': ['mana(me.Deck)']},
	'Logic Cube': {'onPlay': ['search(me.Deck, 1, "Spell")']},
	'Logic Sphere': {'onPlay': ['fromMana(1, "Spell")']},
	'Lost Soul': {'onPlay': ['discardAll()']},
	'Mana Crisis': {'onPlay': ['destroyMana()']},
	'Martial Law': {'onPlay': ['gear("kill")']},
	'Magic Shot - Arcadia Egg': {'onPlay': ['kill("ALL","Untap")']},
	'Magic Shot - Chain Spark': {'onPlay': ['tapCreature()']},
	'Magic Shot - Open Brain': {'onPlay': ['draw(me.Deck, False, 2)']},
	'Magic Shot - Panda Full Life': {'onPlay': ['mana(me.Deck)']},
	'Magic Shot - Soul Catcher': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Magic Shot - Sword Launcher': {'onPlay': [' kill(3000)']},
	'Mana Bonanza': {'onPlay': ['massMana(me.Deck, False)']},
	'Miraculous Rebirth': {'onPlay': ['kill(5000)', 'fromDeck()']},
	'Miraculous Snare': {'onPlay': ['sendToShields()']},
	'Moonlight Flash': {'onPlay': ['tapCreature(2)']},
	'Morbid Medicine': {'onPlay': ['search(me.piles["Graveyard"], 2, "Creature")']},
	'Mystery Cube': {'onPlay': ['drama()']},
	'Mystic Dreamscape': {'onPlay': ['fromMana(3)']},
	'Mystic Inscription': {'onPlay': ['shields(me.Deck)']},
	'Natural Snare': {'onPlay': ['sendToMana()']},
	'Persistent Prison of Gaia': {
		'onPlay': ['bounce(1, True, condition = \'not re.search("Evolution", card.Type)\')', 'targetDiscard(True)']},
	'Phantom Dragon\'s Flame': {'onPlay': [' kill(2000)']},
	'Phantasm Clutch': {'onPlay': ['kill("ALL","Tap")']},
	'Pixie Cocoon': {'onPlay': ['fromMana(1, "Creature")', 'toMana(card)']},
	'Pixie Life': {'onPlay': ['mana(me.Deck, 1, False, False)', 'fromMana(1, "ALL", "Zero")']},
	'Primal Scream': {'onPlay': ['mill(me.Deck, 4, True)', 'search(me.piles["Graveyard"], 1, "Creature")']},
	'Punish Hold': {'onPlay': ['tapCreature(2)']},
	'Purgatory Force': {'onPlay': ['search(me.piles["Graveyard"], 2, "Creature")']},
	'Reap and Sow': {'onPlay': ['mana(me.Deck)', 'destroyMana()']},
	'Reaper Hand': {'onPlay': ['kill()']},
	'Reflecting Ray': {'onPlay': ['tapCreature()']},
	'Reverse Cyclone': {'onPlay': ['tapCreature()']},
	'Riptide Charger': {'onPlay': [' bounce()']},
	'Skeleton Vice': {'onPlay': ['targetDiscard(True, "grave", 2)']},
	'Samurai Decapitation Sword': {'onPlay': [' kill(5000)']},
	'Screw Rocket': {'onPlay': ['gear("kill")']},
	'Seventh Tower': {'onPlay': ['mana(me.Deck)'],
					  'onMetamorph': ['mana(me.Deck,3)']},
	'Searing Wave': {'onPlay': ['burnShieldKill(1, True, 3000, "ALL", False)']},
	'Solar Grace': {'onPlay': ['tapCreature()']},
	'Solar Ray': {'onPlay': ['tapCreature()']},
	'Solar Trap': {'onPlay': ['tapCreature()']},
	'Spastic Missile': {'onPlay': [' kill(3000)']},
	'Spiral Drive': {'onPlay': ['bounce()']},
	'Spiral Gate': {'onPlay': ['bounce()']},
	'Spiral Lance': {'onPlay': ['gear("bounce")']},
	'Stronghold of Lightning and Flame': {'onPlay': ['kill(3000)', 'tapCreature()']},
	'Super Burst Shot': {'onPlay': [' destroyAll([card for card in table if card.owner != me], True, 2000)']},
	'Super Infernal Gate Smash': {'onPlay': ['kill()']},
	'Super Spark': {'onPlay': ['tapCreature(1,True)']},
	'Teleportation': {'onPlay': ['bounce(2)']},
	'Ten-Ton Crunch': {'onPlay': ['kill(3000)']},
	'Terror Pit': {'onPlay': ['kill("All")']},
	'The Strong Spiral': {'onPlay': ['bounce()']},
	'The Strong Breath': {'onPlay': ['kill("ALL","Untap")']},
	'Timeless Garden': {'onPlay': ['mana(me.Deck)']},
	'Tornado Flame': {'onPlay': [' kill(4000)']},
	'Transmogrify': {'onPlay': ['killAndSearch(True)']},
	'Triple Brain': {'onPlay': ['draw(me.Deck, False, 3)']},
	'Ultimate Force': {'onPlay': [' mana(me.Deck, 2)']},
	'Vacuum Ray': {'onPlay': ['tapCreature()']},
	'Valiant Spark': {'onPlay': [' tapCreature()'],
					  'onMetamorph': ['tapCreature(1,True)']},
	'Volcanic Arrows': {'onPlay': ['burnShieldKill(1, True, 6000, 1, False)']},
	'Volcano Charger': {'onPlay': ['kill(2000)']},
	'Wave Rifle': {'onPlay': ['gear("bounce")']},
	'White Knight Spark': {'onPlay': ['tapCreature(1,True)']},
	'Wizard Resurrection': {'onPlay': ['mana(me.Deck)', 'fromMana(1,"Spell")']},
	'XENOM, the Reaper Fortress': {'onPlay': [' targetDiscard(True)']},
	'Zombie Carnival': {'onPlay': ['fromGrave()']},
	'Zombie Cyclone': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	# ON DESTROY EFFECTS

	'Akashic First, Electro-Dragon': {'onDestroy': ['toHand(card)']},
	'Akashic Second, Electro-Spirit': {'onPlay': ['draw(me.Deck, True)'],
										'onDestroy': ['toMana(card)']},
	'Aqua Agent': {'onDestroy': ['toHand(card)']},
	'Aqua Knight': {'onDestroy': ['toHand(card)']},
	'Aqua Ranger': {'onDestroy': ['toHand(card)']},
	'Aqua Skydiver': {'onDestroy': [' toHand(card)']},
	'Aqua Soldier': {'onDestroy': ['toHand(card)']},
	'Aqua Warrior': {'onDestroy': [' draw(me.Deck, True, 2)']},
	'Asylum, the Dragon Paladin': {'onDestroy': [' toShields(card)']},
	'Bat Doctor, Shadow of Undeath': {'onDestroy': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Bone Piercer': {'onDestroy': ['fromMana(1, "Creature")']},
	'Cetibols': {'onDestroy': [' draw(me.Deck, True)']},
	'Chillias, the Oracle': {'onDestroy': [' toHand(card)']},
	'Coiling Vines': {'onDestroy': ['toMana(card)']},
	'Crasher Burn': {'onDestroy': ['kill(3000)']},
	'Crystal Jouster': {'onDestroy': ['toHand(card)']},
	'Cubela, the Oracle': {'onDestroy': ['tapCreature()']},
	'Death Monarch, Lord of Demons': {'onDestroy': [
		'SummonFromGrave(len([card for card in me.piles["Graveyard"] if not re.search("Evolution",card.type)]),"Creature", "ALL", "Demon Command")']},
	'Dracodance Totem': {'onDestroy': ['fromMana(1,"ALL","ALL","Dragon")', 'toMana(card)']},
	'Fly Lab, Crafty Demonic Tree': {'onDestroy': ['targetDiscard(True)']},
	'Glider Man': {'onDestroy': ['targetDiscard()']},
	'Hammerhead Cluster': {'onDestroy': ['bounce()']},
	'Jil Warka, Time Guardian': {'onDestroy': [' tapCreature(2)']},
	'Mighty Shouter': {'onDestroy': ['toMana(card)']},
	'Ouks, Vizier of Restoration': {'onDestroy': [' toShields(card)']},
	'Peace Lupia': {'onDestroy': ['tapCreature()']},
	'Peru Pere, Viral Guardian': {'onDestroy': ['toHand(card)']},
	'Pharzi, the Oracle': {'onDestroy': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Propeller Mutant': {'onDestroy': ['targetDiscard(True)']},
	'Proxion, the Oracle': {'onDestroy': ['toHand(card)']},
	'Shaman Broccoli': {'onDestroy': ['toMana(card)']},
	'Shout Corn': {'onDestroy': ['toMana(card)']},
	'Solid Horn': {'onDestroy': ['toMana(card)']},
	'Stubborn Jasper': {'onDestroy': ['toHand(card)']},
	'Red-Eye Scorpion': {'onDestroy': ['toMana(card)']},
	'Worm Gowarski, Masked Insect': {'onDestroy': ['targetDiscard(True)']},

	# ON SHIELD TRIGGER CHECKS - condtion for a card to be shield trigger(functions used here should ALWAYS return a boolean)
	'Awesome! Hot Spring Gallows' : {'onTrigger': ['manaArmsCheck("Water", 3)']},
	'Soul Garde, Storage Dragon Elemental': {'onTrigger': ['manaArmsCheck("Light", 5)']},
	'Sg Spagelia, Dragment Symbol': {'onTrigger': ['manaArmsCheck("Water", 5)']},
	'Zanjides, Tragedy Demon Dragon': {'onTrigger': ['manaArmsCheck("Darkness", 5)']},
	'Mettagils, Passion Dragon': {'onTrigger': ['manaArmsCheck("Fire", 5)']},
	'Traptops, Green Trap Toxickind': {'onTrigger': ['manaArmsCheck("Nature", 5)']},
}


######### Events ##################

def endTurn(args, x=0, y=0):
	mute()
	clearWaitingCard()
	nextPlayer = args.player
	if nextPlayer == None or "":
		# normally passed without green button
		currentPlayers = getPlayers()
		if len(currentPlayers) > 1:
			nextPlayer = currentPlayers[1]
		else:
			nextPlayer = me
	if turnNumber() > 0:
		if nextPlayer == me and len(getPlayers()) > 1:
			whisper("You shall not pass the turn to yourself!")
		elif getActivePlayer() != me:
			whisper("It's not your turn")
		else:
			notify("{} ends their turn.".format(me))
			remoteCall(nextPlayer, 'untapAll', table)
			nextTurn(nextPlayer, True)
	else:
		# The first turn. Can be passed to anyone.
		nextTurn(nextPlayer, True)


def resetGame():
	mute()
	me.setGlobalVariable("shieldCount", "0")


def onTarget(args):
	global functionlistglobal
	numberOfTargets = len([c for c in table if c.targetedBy == me])
	if numberOfTargets == 0:
		return
	if waitingCard1:
		waitingCard1.pop()
		evaluateotherfunctions()
		if waitingCard:
			card = waitingCard.pop()
			endoffunctionality(card)


############################################################ would have to change this alot according to cascading functions, but for now this works.#########

'''
we can add more funcations here with conditions if need be in future, specially for cards with nested functions
 e.g. death gate and intense vacuuming twist. Since these cards only take 1 card as target, additional check here is not required
 for multiple targets of nested function cards, different checks will be required here.
 This will be the main body for handling them.
'''


def evaluatetargetfunction(funct):
	global functionlistglobal
	waitForTgt = eval(funct)
	if waitForTgt:
		waitingCard2.append(funct)
		waitForTarget()


###########################################################################################################################################################################


def askCard2(list, title="Select a card", buttonText="Select",numberToTake=1):  # askCard function was changed. So using the same name but with the new functionality# this is for showing a dialog box with the cards in the incoming list. Careful, all cards will be visible, even if they're facedown.
	dlg = cardDlg(list)
	dlg.title = title

	if numberToTake == 0:
		# if this dialog is opened without any card to take, that means it's for rearranging cards.
		dlg.min, dlg.max = 0, 0
		dlg.text = "Card Order(drag to rearrange):"
		dlg.show()
		return dlg.list
	result = dlg.show()

	if result is None:
		return None
	return result[0]


def askYN(text="Proceed?", c1="Yes", c2="No"):
	# this asks a simple Y N question, but Yes or No can be replaced by other words. Returns 1 if yes, 2 for No and 0 if the box is closed
	choiceList = [c1, c2]
	colorsList = ['#FF0000', '#FF0000']
	choice = askChoice(text, choiceList, colorsList)
	return choice


def removeIfEvo(card):
	# Will remove passed card from the list of tracked evos/baits
	# returns a list of bait cards if evo was removed
	# returns empty list if not found or bait was removed

	evolveDict = eval(me.getGlobalVariable('evolution'))
	resultList = []
	for evo in evolveDict.keys():
		if evo == card._id:
			for cardID in evolveDict[evo]:
				resultList.append(Card(cardID))
			del evolveDict[evo]
			# notify("Evo removed from evo in dict")
			break
		baitList = evolveDict[evo]
		if card._id in baitList:
			baitList.remove(card._id)
			evolveDict[evo] = baitList
			# notify("Bait removed from evo in dict")
			break
	me.setGlobalVariable('evolution', str(evolveDict))
	return resultList


def isBait(card):  # check if card is under and evo(needs to be ignored by most things) This is really inefficient, maybe make a func to get all baits once
	result = False
	evolveDict = eval(me.getGlobalVariable('evolution'))
	for evo in evolveDict.keys():
		baitList = evolveDict[evo]
		if card._id in baitList:
			result = True
			break
	return result


def antiDiscard(card, sourcePlayer):
	# sourcePlayer = the player trying play the discarding effect, not the target player
	# le anti-discard check. Still WIP.
	return False
	if card in antiDiscardDict:
		# do shit
		notify("Anti-Discard triggered")
	else:
		return False


def waitForTarget():
	whisper("Waiting for targets. Please (re)target...")
	whisper("[Esc to cancel]")
	return


def clearWaitingCard():  # clears any pending plays for a card that's waiting to choose targets etc
	if waitingCard:
		card = waitingCard.pop()
		notify("Waiting for target for {} cancelled.".format(card.Name))


def manaArmsCheck(civ='ALL5', num=0):
	if civ == 'ALL5':  # check if you have all 5 civs in mana zone
		manaCards = [card for card in table if isMana(card) and card.owner == me]
		civList = ["Fire", "Nature", "Water", "Light", "Darkness"]
		flags = [False] * 5  # one flag for each corresponding civ [False, False, False, False, False]
		for card in manaCards:
			for i in range(0, 5):
				if not flags[i] and re.search(civList[i], card.Civilization):
					flags[i] = True
			if flags[0] and flags[1] and flags[2] and flags[3] and flags[4]:
				return True
		return False
	else:
		manaCards = [card for card in table if isMana(card) and card.owner == me and re.search(civ, card.Civilization)]
		if len(manaCards) >= num:
			return True

def ifRaceInBattleZone(race):
	cardList = [card for card in table if card.owner == me and isCreature(card) and not isBait(card)]

################ Functions used in the Automation dictionaries.####################

def SummonFromGrave(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL",noEvo=True):  # Temporary Fix for not allowing Evolutions
	mute()
	for i in range(0, count):
		if TypeFilter != "ALL" and noEvo:
			cardsInGroup_Type_Filtered = [card for card in me.piles["Graveyard"] if
										  re.search(TypeFilter, card.Type) and not re.search("Evolution", card.type)]
		else:
			cardsInGroup_Type_Filtered = [card for card in me.piles["Graveyard"]]
		if CivFilter != "ALL":
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered if
												re.search(CivFilter, card.properties['Civilization'])]
		else:
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered]
		if RaceFilter != "ALL":
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered if
													re.search(RaceFilter, card.properties['Race'])]
		else:
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered]
		if len(cardsInGroup_CivTypeandRace_Filtered) == 0: return
		choice = askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose a Card  to Summon from the Graveyard',
						  'Graveyard')
		if type(choice) is not Card: break
		toPlay(choice)


def drama(shuffle=True, type='creature', targetZone='battlezone', failZone='mana', conditional=True):
	# drama = getting creatures from top of deck for free
	mute()
	if shuffle:
		me.Deck.shuffle()
		notify("{} shuffles their deck.".format(me))
	card = me.Deck.top()
	card.isFaceUp = True
	notify("Top card is {}".format(card))
	played = False  # Flag for resolving after shuffle, unused rn
	if type == 'creature':
		success = re.search("Creature", card.Type)
	elif type == 'creature or spell':
		success = re.search("Creature", card.Type) or re.search("Spell", card.Type)
	if success:
		if conditional:
			choice = askYN("Put {} into {}?\n\n {}".format(card.Name, targetZone, card.Rules))
			# more conditions for non-bz?
			if choice == 1:
				toPlay(card)
				played = True
				return
		else:
			toPlay(card)
			played = True
			return
	if failZone == 'mana':
		toMana(card)
	elif failZone == 'hand':
		toHand(card)
	else:
		notify("{} puts {} back on top of deck".format(me, card))
		card.isFaceUp = False


def lookAtTopCards(num, cardType='card', targetZone='hand', remainingZone='bottom', reveal=True, specialaction='NONE', specialaction_civs = []):
	mute()
	notify("{} looks at the top {} cards of their deck".format(me, num))
	cardList = [card for card in me.Deck.top(num)]
	choice = askCard2(cardList, 'Choose a card to put into {}'.format(targetZone))
	if type(choice) is Card:
		if not 'NONE' in specialaction:
			card_for_special_action = choice
		if cardType == 'card' or re.search(cardType, choice.Type):
			# use switch instead, when more zones are added here
			if targetZone == 'mana':
				toMana(choice)
			else:
				# to hand is default rn
				toHand(choice, show=reveal)
		else:
			notify("Please select a {}! Action cancelled.".format(cardType))
			return
	else:
		notify("Nothing selected! Action cancelled.")
		return
	cardList = [card for card in me.Deck.top(num - 1)]
	# will it always be 1 card that goes into target zone? Account for more in later upgrades
	if len(cardList) > 1 and remainingZone == 'bottom':
		cardList = askCard2(cardList, 'Rearrange the remaining cards to put to {}'.format(remainingZone), 'OK', 0)
	for card in cardList:
		if remainingZone == 'mana':
			toMana(card)
		else:
			card.moveToBottom(me.Deck)
			notify("{} moved a card to the bottom of their deck.".format(me))
	if specialaction == "BOUNCE":
		for civs in specialaction_civs:
			if re.search(civs, card_for_special_action.properties['Civilization']):
				waitingCard2.append(card_for_special_action.properties['Civilization'])



def targetDiscard(randomDiscard=False, targetZone='grave', count=1):
	mute()
	currentPlayers = getPlayers()
	playerList = []
	cardList = []
	for player in currentPlayers:
		playerList.append(player.name)
	choicePlayer = askChoice("Pick a player:", playerList)
	if choicePlayer < 1: return
	targetPlayer = currentPlayers[choicePlayer - 1]
	cardList = [card for card in targetPlayer.hand]
	if randomDiscard:
		remoteCall(targetPlayer, 'randomDiscard', targetPlayer.hand)
		return

	cardChoice = cardDlg(cardList)
	cardChoice.title = 'Choose a Card to discard'
	cardChoice.text = "{}'s hand".format(targetPlayer)
	cardChoice = cardChoice.show()[0]

	if type(cardChoice) is not Card:
		notify("{} - Error".format(type(cardChoice)))
		return

	if targetZone == 'shields':
		whisper("Setting {} as shield.".format(cardChoice))
		remoteCall(targetPlayer, 'toShields', cardChoice)
	elif targetZone == 'grave':
		# do anti-discard check here
		if not remoteCall(targetPlayer, 'antiDiscard', [cardChoice, me]):
			# anti discard will return false if no antiDiscard is available. Remotecalling because...idk might do some things in antiDiscard later.
			# Maybe change it to normal call later, and remoteCall from only inside anti-disc.
			# still WIP
			remoteCall(targetPlayer, 'toDiscard', cardChoice)


def discardAll():
	mute()
	currentPlayers = getPlayers()
	playerList = []
	cardList = []
	for player in currentPlayers:
		playerList.append(player.name)
	choicePlayer = askChoice("Pick a player:", playerList)
	if choicePlayer < 1: return
	targetPlayer = currentPlayers[choicePlayer - 1]

	cardList = [card for card in targetPlayer.hand]
	for card in cardList:
		remoteCall(targetPlayer, 'toDiscard', card)


def clonedDiscard():
	mute()
	currentPlayers = getPlayers()
	playerList = []
	for player in currentPlayers:
		playerList.append(player.name)
	choicePlayer = askChoice("Pick a player:", playerList)
	if choicePlayer < 1: return
	targetPlayer = currentPlayers[choicePlayer - 1]
	cardList = [card for card in targetPlayer.hand]

	count = 1
	for player in currentPlayers:
		for card in player.piles["Graveyard"]:
			if re.search(card.Name, "Cloned Nightmare"):
				count += 1
	notify("Cloned Nightmares in graves:{}".format(count - 1))

	if remoteCall(targetPlayer, 'antiDiscard', ['GENERALCHECK', me]):
		return

	for i in range(0, count):
		remoteCall(targetPlayer, 'randomDiscard', targetPlayer.hand)


# do some anti-discard inside dat randomdisc function

def fromMana(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, toGrave=False,ApplyToAllPlayers=False):
	mute()
	if ApplyToAllPlayers == True:
		playerList = players
	else:
		playerList = [players[0]]  # players[0] is the player calling this function, me
	for player in playerList:
		for i in range(0, count):
			if TypeFilter != "ALL":
				cardsInGroup_Type_Filtered = [card for card in table if
											  isMana(card) and card.owner == me and re.search(TypeFilter, card.Type)]
			else:
				cardsInGroup_Type_Filtered = [card for card in table if isMana(card) and card.owner == me]
			if CivFilter != "ALL":
				cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered if
													re.search(CivFilter, card.properties['Civilization'])]
			else:
				cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered]
			if RaceFilter != "ALL":
				cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered if
														re.search(RaceFilter, card.properties['Race'])]
			else:
				cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered]
			if len(cardsInGroup_CivTypeandRace_Filtered) == 0: return
			choice = askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose a Card from the Mana Zone', 'Mana Zone')
			if type(choice) is not Card: break
			if toGrave == True:
				remoteCall(player, "destroy", choice)
			else:
				remoteCall(player, "toHand", [choice, show])


def killAndSearch(play=False, singleSearch=False):
	# looks like this is only used for Transmogrify
	mute()
	cardList = [card for card in table if isCreature(card) and re.search("Creature", card.Type)] #wtfffffffffff is this why 2 redundant conditions
	if len(cardList) == 0: return
	choice = askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	card = choice
	remoteCall(choice.owner, 'destroy', choice)
	if singleSearch:
		return
	else:
		remoteCall(choice.owner, 'loopThroughDeck', [card, play])


def loopThroughDeck(card, play=False):
	group = card.owner.Deck
	if len(group) == 0: return
	newCard = group[0]
	newCard.isFaceUp = True
	notify("{} reveals {}".format(card.owner, newCard.Name))
	rnd(1, 1000)
	if re.search("Creature", newCard.Type) and not re.search("Evolution Creature", newCard.Type):
		if play == True:
			remoteCall(newCard.owner, 'toPlay', newCard)
			return
		else:
			remoteCall(newCard.owner, 'moveTo', newCard.owner.hand)
			return
	else:
		remoteCall(newCard.owner, 'toDiscard', newCard)
		remoteCall(newCard.owner, 'loopThroughDeck', [card, play])


def eurekaProgram(ask=True):
	mute()
	cardList = [card for card in table if isCreature(card) and re.search("Creature", card.Type) and card.owner == me]
	cardList = [card for card in cardList if not re.search("Psychic", card.Type)]
	if len(cardList) == 0: return

	choice = askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	originalCost = int(choice.Cost)
	found = False
	destroy(choice)
	notify("Looking for a creature with cost {}...".format(originalCost + 1))

	for card in me.Deck:
		card = me.Deck[0]
		card.isFaceUp = True
		cost = int(card.Cost)
		notify("{} reveals {}".format(me, card))
		rnd(1, 10)
		if (int(card.Cost) - originalCost) == 1:
			if re.search("Creature", card.Type):
				if not re.search("Evo", card.Type):
					if ask:
						yn = askYN("Put {} into the battle zone?\n\n {}".format(card.Name, card.Rules))
						if yn == 1:
							found = True
							toPlay(card, ignoreEffects=True)
							choice = card
					##add card to resolve list
					break
				else:
					if ask:
						yn = askYN("Put {} into the battle zone?\n\n {}".format(card.Name, card.Rules))
						if yn == 1:
							found = True
							toPlay(card, ignoreEffects=True)
							choice = card
							##add card to resolve list
							card.moveToTable(0, 0)
							align()
					break
		card.moveToBottom(me.Deck)
	for card in me.Deck:
		if card.isFaceUp:
			card.isFaceUp = False
	me.Deck.shuffle()
	notify("{} shuffles their deck.".format(me))
	if found:
		## Temporary fix without a proper resolve list
		toPlay(choice, notifymute=True)
	else:
		notify("No card with cost {} found or action cancelled.".format(originalCost + 1))


""""def volgMill(askChoice = True):
	mute()
	if(askChoice)
		currentPlayers = getPlayers()
		playerList = []
		for player in currentPlayers:
			playerList.append(player.name)
		choicePlayer = askChoice("Pick a player:", playerList)
		if choicePlayer < 1: return
		targetPlayer = currentPlayers[choicePlayer-1]
	group = targetPlayer.Deck
	if len(group) == 0: return
	newCard = group[0]
	newCard.isFaceUp = True
	notify("{} reveals {}".format(card.owner,newCard.name))
	rnd(1,1000)
	if re.search("Creature", newCard.Type) and not re.search("Evolution Creature", newCard.Type):
		if play == True:
			remoteCall(newCard.owner,'toPlay',newCard)
			return
		else:
			remoteCall(newCard.owner,'moveTo',newCard.owner.hand)
			return
	else:
		remoteCall(newCard.owner,'toDiscard',newCard)
		remoteCall(newCard.owner,'loopThroughDeck',[card, play])
"""


def search(group, count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, x=0, y=0):
	mute()
	if len(group) == 0: return
	for i in range(0, count):
		cardsInGroup = [card for card in group]
		if TypeFilter != "ALL":
			cardsInGroup_Type_Filtered = [card for card in group if re.search(TypeFilter, card.Type)]
		else:
			cardsInGroup_Type_Filtered = [card for card in group]
		if CivFilter != "ALL":
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered if
												re.search(CivFilter, card.properties['Civilization'])]
		else:
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered]
		if RaceFilter != "ALL":
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered if
													re.search(RaceFilter, card.properties['Race'])]
		else:
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered]
		while (True):
			choice = askCard2(cardsInGroup, 'Search card to take to hand (1 at a time)')
			if type(choice) is not Card:
				group.shuffle()
				notify("{} finishes searching his/her {}.".format(me, group.name))
				return
			if choice in cardsInGroup_CivTypeandRace_Filtered:
				toHand(choice, show)
				break
	group.shuffle()
	notify("{} finishes searching his/her {}.".format(me, group.name))


def kill(powerFilter='ALL', tapFilter='ALL', civFilter='ALL', count=1, targetOwn=False):
	mute()
	if powerFilter == 'ALL':	powerFilter = float('inf')
	if targetOwn:
		cardList = [card for card in table if isCreature(card) and int(card.Power.strip(' +')) <= powerFilter]
	else:
		cardList = [card for card in table if
					isCreature(card) and not card.owner == me and int(card.Power.strip(' +')) <= powerFilter]
	if tapFilter != 'ALL':
		if tapFilter == 'Untap':
			cardList = [card for card in cardList if card.orientation == Rot0]
		if tapFilter == 'Tap':
			cardList = [card for card in cardList if card.orientation == Rot90]
	if civFilter != "ALL":
		cardList = [card for card in cardList if re.search(civFilter, card.Civilization)]
	if len(cardList) == 0:
		whisper("No valid targets on the table.")
		return

	targets = [c for c in table if c.targetedBy == me and isCreature(c)]
	if len(targets) != count:
		whisper("Wrong number of targets!")
		return True  # return true activates the cardStack/waiting for targets mechanism
	killList = []
	for i in range(0, count):
		if (targets[i] in cardList):
			choice = targets[i]
			killList.append(choice)
		else:
			whisper("Invalid target(s)! Waiting for targets...")
			return True

	for card in killList:
		remoteCall(card.owner, "destroy", card)


def destroyAll(group, condition=False, powerFilter='ALL', civFilter="ALL", AllExceptFiltered=False):
	mute()
	if powerFilter == 'ALL':
		powerfilter = float('inf')
	if condition == False:
		return
	cardlist = []
	if civFilter == "ALL":
		cardList = [card for card in group if isCreature(card) and int(card.Power.strip(' +')) <= powerFilter]
	else:
		if AllExceptFiltered:
			cardList = [card for card in group if isCreature(card) and int(card.Power.strip(' +')) <= powerFilter 
			and not re.search(civFilter, card.properties['Civilization'])]
		else:
			cardList = [card for card in group if
						isCreature(card) and int(card.Power.strip(' +')) <= powerFilter 
						and re.search(civFilter, card.properties['Civilization'])]
	if len(cardList) == 0:
		return
	for card in cardList:
		cardToBeSaved = card
		if cardToBeSaved.owner == me:
			possibleSavers = [card for card in table if
							  cardToBeSaved != card and isCreature(card) and card.owner == me and re.search("Saver",
																											card.rules) and (
										  re.search(cardToBeSaved.properties['Race'], card.rules) or re.search(
									  "Saver: All Races", card.rules))]
			if len(possibleSavers) > 0:
				if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
						cardToBeSaved.Name)):
					choice = askCard2(possibleSavers, 'Choose Saver to destroy')
					if type(choice) is Card:
						toDiscard(choice)
						cardList.remove(choice)
						cardList = [card for card in cardList]
						notify(
							"{} destroys {} to prevent {}'s destruction.".format(me, choice.name, cardToBeSaved.name))
						continue

			toDiscard(cardToBeSaved)
			card = cardToBeSaved  # fix for onDestroy effect, as toDiscard somehow changes card
			if cardScripts.get(card.Name, {}).get('onDestroy', {}):
				functionDict = cardScripts.get(card.Name).get('onDestroy')
				for function in functionDict:
					eval(function)
		else:
			remoteCall(cardToBeSaved.owner, "destroy", cardToBeSaved)


def destroyMana(count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isMana(card) and not card.owner == me]
		if len(cardList) == 0:
			return
		choice = askCard2(cardList, 'Choose a Mana Card to destroy')
		if type(choice) is not Card:
			return
		remoteCall(choice.owner, "destroy", choice)


def burnShieldKill(count=1, targetOwnSh=False, powerFilter='ALL', killCount=0,
				   targetOwnCr=False):  # Mainly for destroying shields. Kill is optional.
	mute()
	targets = [c for c in table if c.targetedBy == me]
	targetSh = []
	targetCr = []
	for c in targets:
		if isShield(c):
			targetSh.append(c)
		elif isCreature(c):
			targetCr.append(c)

	if killCount == "ALL" or killCount > 0:
		if powerFilter == 'ALL': powerFilter = float('inf')
		validKillTargets = [c for c in table if isCreature(c) and int(c.Power.strip(' +')) <= powerFilter]
		if not targetOwnCr:
			validKillTargets = [c for c in validKillTargets if not c.owner == me]
			targetCr = [c for c in targetCr if not c.owner == me]
		if killCount == "ALL":
			targetCr = validKillTargets
			killCount = len(targetCr)
		else:
			killCount = min(killCount, len(validKillTargets))

	myShields = len([c for c in table if isShield(c) and c.owner == me])
	oppShields = len([c for c in table if isShield(c) and c.owner != me])

	if targetOwnSh:
		targetSh = [c for c in targetSh if c.owner == me]
		count = min(count, myShields)
	else:
		targetSh = [c for c in targetSh if c.owner != me]
		count = min(count, oppShields)

	if count == 0 and killCount == 0:  # No shields left to burn, nothing to kill
		whisper("No valid targets.")
		return

	if len(targetSh) != count or len(targetCr) != killCount:
		whisper("Invalid shields and/or creatures targeted.")
		return True  # =>will wait for target

	for shield in targetSh:
		remoteCall(shield.owner, "destroy", [shield, 0, 0, True])
	for card in targetCr:
		remoteCall(card.owner, "destroy", card)


def fromDeck():
	mute()
	notify("{} looks at their Deck.".format(me))
	me.Deck.lookAt(-1)


def fromGrave():
	mute()
	notify("{} looks at their Graveyard.".format(me))
	me.piles['Graveyard'].lookAt(-1)


def lookAtCards(count=1, isTop=True):
	mute()
	if isTop == False:
		notify("{} looks at {} cards from bottom of their deck.".format(me, count))
	notify("{} looks at {} cards from top of their deck.".format(me, count))
	me.Deck.lookAt(count, isTop)


def sacrifice(power=float('inf'), count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if
					isCreature(card) and card.owner == me and re.search("Creature", card.Type)]
		cardList = [card for card in cardList if int(card.Power.strip(' +')) <= power]
		if len(cardList) == 0:
			return
		choice = askCard2(cardList, 'Choose a Creature to destroy')
		if type(choice) is not Card:
			return
		destroy(choice)


def bounce(count=1, opponentOnly=False, toDeckTop=False, condition='True', check_bounce = False):
	mute()
	if check_bounce == True:
		if not waitingCard2:
			return
	if opponentOnly:
		cardList = [card for card in table if
					isCreature(card) and card.owner != me and not isBait(
						card) and eval(condition)]
	else:
		cardList = [card for card in table if
					isCreature(card) and not isBait(card) and eval(condition)]
	if len(cardList) < 1:
		whisper("No valid targets on the table.")
		return

	# forcing octgn to go to targets function and wait
	targets = [c for c in table if c.targetedBy == me]
	if len(targets) != count:
		return True

	bounceList = []
	for i in range(0, count):
		if (targets[i] in cardList):
			choice = targets[i]
			bounceList.append(choice)
			whisper("{}.".format(choice))
		else:
			whisper("Wrong target(s)!")
			return True

	for card in bounceList:
		if toDeckTop:
			remoteCall(card.owner, "toDeck", card)
		else:
			remoteCall(card.owner, "toHand", card)
	if waitingCard2:
		waitingCard2.pop()

def gear(str):
	mute()
	if str == 'kill':
		cardList = [card for card in table if isGear(card)
					and not card.owner == me]
		if len(cardList) == 0:
			return
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Graveyard')
		if type(choice) is not Card:
			return
		remoteCall(choice.owner, 'destroy', choice)
	elif str == 'bounce':
		cardList = [card for card in table if isGear(card)]
		if len(cardList) == 0:
			return
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Hand')
		if type(choice) is not Card:
			return
		if choice.owner == me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toHand', choice)
	elif str == 'mana':
		cardList = [card for card in table if isGear(card)]
		if len(cardList) == 0:
			return
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Mana')
		if type(choice) is not Card:
			return
		if choice.owner == me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toMana', choice)


def sendToShields(count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isCreature(card) and card.owner != me]
		if len(cardList) == 0: return
		choice = askCard2(cardList, 'Choose a Creature to send to shields')
		if type(choice) is not Card: return
		remoteCall(choice.owner, "toShields", choice)


def sendToMana(count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isCreature(card) and card.owner != me]
		if len(cardList) == 0: return
		choice = askCard2(cardList, 'Choose a Creature to send to mana')
		if type(choice) is not Card: return
		remoteCall(choice.owner, "toMana", choice)


def tapCreature(count=1, targetALL=False, includeOwn=False):
	mute()
	if targetALL:
		if includeOwn == True:
			cardList = [card for card in table if
						isCreature(card) and card.orientation == Rot0 and re.search("Creature", card.Type)]
		else:
			cardList = [card for card in table if
						isCreature(card) and card.orientation == Rot0 and not card.owner == me and re.search("Creature",
																											 card.Type)]
		if len(cardList) == 0:
			return
		for card in cardList:
			remoteCall(card.owner, "tap", card)
	else:
		for i in range(0, count):
			if includeOwn == True:
				cardList = [card for card in table if
							isCreature(card) and card.orientation == Rot0 and re.search("Creature", card.Type)]
			else:
				cardList = [card for card in table if
							isCreature(card) and card.orientation == Rot0 and not card.owner == me and re.search(
								"Creature", card.Type)]
			if len(cardList) == 0:
				return
			choice = askCard2(cardList, 'Choose a Creature to tap')
			if type(choice) is not Card:
				return
			remoteCall(choice.owner, "tap", choice)


def semiReset():
	mute()
	if confirm("Are you sure you want to continue?"):
		currentPlayers = getPlayers()
		for player in currentPlayers:
			cardsInHand = [c for c in player.hand]
			cardsInGrave = [c for c in player.piles['Graveyard']]
			if cardsInHand or cardsInGrave:
				for card in cardsInHand:
					remoteCall(player, 'toDeck', card)
				for card in cardsInGrave:
					remoteCall(player, 'toDeck', card)
			remoteCall(player, 'shuffle', player.deck)
			remoteCall(player, 'draw', [player.deck, False, 5])


def suicide(name, action, arg):
	mute()
	choiceList = ['Yes', 'No']
	colorsList = ['#FF0000', '#FF0000']
	choice = askChoice("Destroy the card to activate effect?", choiceList, colorsList)
	if choice == 0 or choice == 2:
		return
	cardList = [card for card in table if isCreature(card) and card.owner == me and re.search("Creature", card.type)]
	cardList = [card for card in cardList if card.name == name]
	toDiscard(cardList[-1])
	action(arg)


# End of Automation Code

def flip(card, x=0, y=0):
	mute()
	if (re.search("Psychic", card.Type)):
		altName = card.alternateProperty('awakening', 'name')
		if card.alternate is '':
			card.alternate = 'awakening'
			notify("{}'s' {} awakens to {}.".format(me, altName, card))
			align()
			return
		else:
			card.alternate = ''
			notify("{}'s {} reverts to {}.".format(me, altName, card))
			align()
			return
	elif (re.search("Dragheart", card.Type)):
		# draghearts
		old = card.Name
		forms = card.alternates
		if card.alternate is forms[0]:
			card.alternate = forms[1]
			notify("{}'s' {} dragonsolutions to {}.".format(me, old, card))
		elif card.alternate is forms[1]:
			# Is in 2nd form
			if len(forms) == 2:
				# Not 3 sided
				card.alternate = forms[0]
				notify("{}'s {} reverts to {}.".format(me, old, card))
			else:
				# 3 sided card
				card.alternate = forms[2]
				notify("{}'s {} 3D dragonsolutions to {}.".format(me, old, card))
		elif card.alternate is forms[2]:
			card.alternate = forms[0]
			notify("{}'s {} reverts to {}.".format(me, old, card))
		# align()
		# no align for now as these cards have diff. sizes
		return

	else:
		if card.isFaceUp:
			notify("{} flips {} face down.".format(me, card))
			card.isFaceUp = False
		else:
			card.isFaceUp = True
			notify("{} flips {} face up.".format(me, card))


def toHyperspatial(card, x=0, y=0, notifymute=False):
	mute()
	removeIfEvo(card)
	if card.alternate is not '' and re.search("{RELEASE}", card.Rules):
		flip(card)
		return
	else:
		card.moveTo(me.Hyperspatial)
		align()
		if notifymute == False:
			notify("{}'s {} returns to the Hyperspatial Zone.".format(me, card))


def moveCards(args):
	mute()
	clearWaitingCard()  # clear the waitingCard if ANY CARD moved from table
	player = args.player

	fromGroup = args.fromGroups[0]
	toGroup = args.toGroups[0]
	## Old vars are: player, card, fromGroup, toGroup, oldIndex, index, oldX, oldY, x, y, highlights, markers, faceup
	for card in args.cards:
		if player != me:  ##Ignore for cards you don't control
			return
		##When a player moves top card of deck to bottom of deck
		if fromGroup == me.Deck and toGroup == me.Deck:
			if card == me.Deck.bottom():
				notify("{} moves a card in their deck to bottom".format(me))
			elif card == me.Deck.top():
				notify("{} moves a card in their deck to top".format(me))
			else:
				notify("{} moves a card around in their deck".format(me))
			return

		## This updates the evolution dictionary in the event one of the cards involved in an evolution leaves the battlezone.
		if table not in args.fromGroups:  ## we only want cases where a card is being moved from table to another group
			##notify("Ignored")
			return
		evolveDict = eval(me.getGlobalVariable("evolution"))
		for evo in evolveDict.keys():
			if Card(evo) not in table:
				del evolveDict[evo]
			else:
				evolvedList = evolveDict[evo]
				for evolvedCard in evolvedList:
					if Card(evolvedCard) not in table:
						evolvedList.remove(evolvedCard)
				if len(evolvedList) == 0:
					del evolveDict[evo]
				else:
					evolveDict[evo] = evolvedList
		if evolveDict != eval(me.getGlobalVariable("evolution")):
			me.setGlobalVariable("evolution", str(evolveDict))


def isCreature(card):
	mute()
	if card in table and not isShield(
			card) and not card.orientation == Rot180 and not card.orientation == Rot270 and re.search("Creature", card.Type):
		return True
	else:
		return False


def isGod(card):
	mute()
	if card in table and not isShield(
			card) and not card.orientation == Rot180 and not card.orientation == Rot270 and re.search("Creature", card.Type) and re.search(
			"God", card.Race):
		return True
	else:
		return False


def isGear(card):
	mute()
	if card in table and not isShield(
			card) and not card.orientation == Rot180 and not card.orientation == Rot270 and re.search("Cross Gear", card.Type):
		return True
	else:
		return False


def isFortress(card):
	mute()
	if card in table and not isShield(
			card) and not card.orientation == Rot180 and not card.orientation == Rot270 and re.search("Fortress", card.Type) and not re.search(
			"Dragheart", card.Type):
		return True
	else:
		return False


def isMana(card):
	mute()
	if card in table and not isShield(card) and not card.orientation == Rot90 and not card.orientation == Rot0:
		return True
	return False


def isShield(card):
	mute()
	if card in table and not card.isFaceUp:
		return True
	elif card in table and card.markers[shieldMarker] > 0:
		return True
	return False


def isPsychic(card):
	mute()
	if re.search("Psychic", card.Type) or re.search("Dragheart", card.Type):
		return True
	else:
		return False


def metamorph():
	mute()
	cardList = [card for card in table if isMana(card) and card.owner == me]
	if len(cardList) < 7:
		return False
	else:
		return True


def align():
	mute()
	global playerside  ##Stores the Y-axis multiplier to determine which side of the table to align to
	global sideflip  ##Stores the X-axis multiplier to determine if cards align on the left or right half
	if sideflip == 0:  ##the 'disabled' state for alignment so the alignment positioning doesn't have to process each time
		return "BREAK"
	if Table.isTwoSided():
		if playerside == None:  ##script skips this if playerside has already been determined
			if me.isInverted:
				playerside = -1  # inverted (negative) side of the table
			else:
				playerside = 1
		if sideflip == None:  ##script skips this if sideflip has already been determined
			playersort = sorted(getPlayers(), key=lambda
				player: player._id)  ##makes a sorted players list so its consistent between all players
			playercount = [p for p in playersort if
						   me.isInverted == p.isInverted]  ##counts the number of players on your side of the table
			if len(playercount) > 2:  ##since alignment only works with a maximum of two players on each side
				whisper("Cannot align: Too many players on your side of the table.")
				sideflip = 0  ##disables alignment for the rest of the play session
				return "BREAK"
			if playercount[0] == me:  ##if you're the 'first' player on this side, you go on the positive (right) side
				sideflip = 1
			else:
				sideflip = -1
	else:  ##the case where two-sided table is disabled
		whisper("Cannot align: Two-sided table is required for card alignment.")
		sideflip = 0  ##disables alignment for the rest of the play session
		return "BREAK"

	cardorder = [[], [], []]
	evolveDict = eval(me.getGlobalVariable("evolution"))

	for card in table:
		if card.controller == me and not isFortress(card) and not card.anchor and not card._id in list(
				itertools.chain.from_iterable(evolveDict.values())):
			if isShield(card):
				cardorder[1].append(card)
			elif isMana(card):
				cardorder[2].append(card)
			else:  ##collect all creatures
				cardorder[0].append(card)

	temp = []
	bigCards = []
	# notify("CardOrderzero is {}".format(cardorder[0]))
	for card in cardorder[0]:
		# notify("{} Size is {}".format(card, card.size))
		if card.size == "wide" or card.size == "tall":
			# notify("BIG CARD!!! {}".format(card))
			bigCards.append(card)
		else:
			temp.append(card)
	cardorder[0] = temp
	# remove all big cards from normall aligned ones
	xpos = 80
	ypos = 5 + 10 * (max([len(evolveDict[x]) for x in evolveDict]) if len(evolveDict) > 0 else 1)
	for cardtype in cardorder:
		if cardorder.index(cardtype) == 1:
			xpos = 80
			ypos += 93
		elif cardorder.index(cardtype) == 2:
			xpos = 80
			ypos += 93
		for c in cardtype:
			x = sideflip * xpos
			y = playerside * ypos + (44 * playerside - 44)
			if c.position != (x, y):
				c.moveToTable(x, y)
			xpos += 79
	for evolution in evolveDict:
		count = 0
		for evolvedCard in evolveDict[evolution]:
			x, y = Card(evolution).position
			count += 1
			Card(evolvedCard).moveToTable(x, y - 10 * count * playerside)
			Card(evolvedCard).sendToBack()
	# for landscape or large cards
	xpos = 10
	ypos = 5 + 10 * (max([len(evolveDict[x]) for x in evolveDict]) if len(evolveDict) > 0 else 1)
	for c in bigCards:
		xpos += max(c.width, c.height) + 10
		x = -1 * sideflip * xpos
		y = ypos
		if c.position != (x, y):
			c.moveToTable(x, y)


def clear(group, x=0, y=0):
	mute()
	clearWaitingCard()
	for card in group:
		card.target(False)


def setup(group, x=0, y=0):
	mute()
	clearWaitingCard()

	cardsInTable = [c for c in table if c.controller == me and c.owner == me and not isPsychic(c)]
	cardsInHand = [c for c in me.hand if not isPsychic(c)]
	cardsInGrave = [c for c in me.piles['Graveyard'] if not isPsychic(c)]

	psychicsInTable = [c for c in table if c.controller == me and c.owner == me and isPsychic(c)]
	psychicsInHand = [c for c in me.hand if isPsychic(c)]
	psychicsInGrave = [c for c in me.piles['Graveyard'] if isPsychic(c)]

	if cardsInTable or cardsInHand or cardsInGrave or psychicsInTable or psychicsInGrave or psychicsInHand:
		if confirm("Are you sure you want to setup battlezone? Current setup will be lost"):

			for card in cardsInTable:
				card.moveTo(me.Deck)
			for card in cardsInHand:
				card.moveTo(me.Deck)
			for card in cardsInGrave:
				card.moveTo(me.Deck)

			for card in psychicsInTable:
				card.moveTo(me.Hyperspatial)
			for card in psychicsInHand:
				card.moveTo(me.Hyperspatial)
			for card in psychicsInGrave:
				card.moveTo(me.Hyperspatial)
		else:
			return
	if len(me.Deck) < 10:  # We need at least 10 cards to properly setup the game
		whisper("Not enough cards in deck")
		return

	cardsInDeck = [c for c in me.Deck]
	for card in cardsInDeck:
		if isPsychic(card):
			whisper("You cannot have Psychic creatures in your main deck")
			return

	me.setGlobalVariable("shieldCount", "0")
	me.setGlobalVariable("evolution", "{}")
	me.Deck.shuffle()
	rnd(1, 10)
	for card in me.Deck.top(5): toShields(card, notifymute=True)
	for card in me.Deck.top(5): card.moveTo(card.owner.hand)
	align()
	notify("{} sets up their battle zone.".format(me))


def rollDie(group, x=0, y=0):
	mute()
	global diesides
	n = rnd(1, diesides)
	notify("{} rolls {} on a {}-sided die.".format(me, n, diesides))


def untapAll(group=table, x=0, y=0):
	mute()
	clearWaitingCard()
	for card in group:
		if not card.owner == me:
			continue
		if card.orientation == Rot90:
			card.orientation = Rot0
		if card.orientation == Rot270:
			card.orientation = Rot180
	notify("{} untaps all their cards.".format(me))


def tap(card, x=0, y=0):
	mute()
	clearWaitingCard()
	card.orientation ^= Rot90
	if card.orientation & Rot90 == Rot90:
		notify('{} taps {}.'.format(me, card))
	else:
		notify('{} untaps {}.'.format(me, card))


def destroy(card, x=0, y=0, dest=False, ignoreEffects=False):
	mute()
	if isShield(card):
		if dest == True:
			toDiscard(card)
			return
		card.peek()
		rnd(1, 10)
		#check conditonal trigger for cards like Awesome! Hot Spring Gallows or Traptops
		conditionalTrigger = True
		if cardScripts.get(card.Name, {}).get('onTrigger'):
			trigFunctions = cardScripts.get(card.Name).get('onTrigger')
			notify("On trig list is".format(trigFunctions[0]))
			for function in trigFunctions:
				conditionalTrigger = conditionalTrigger and eval(trigFunctions[0])
		if conditionalTrigger and re.search("{SHIELD TRIGGER}", card.Rules):
			if confirm("Activate Shield Trigger for {}?\n\n{}".format(card.Name, card.Rules)):
				rnd(1, 10)
				notify("{} uses {}'s Shield Trigger.".format(me, card.Name))
				card.isFaceUp = True
				toPlay(card, notifymute=True)
				return
		shieldCard = card
		cardsInHandWithStrikeBackAbility = [card for card in me.hand if re.search("Strike Back", card.rules)]
		if len(cardsInHandWithStrikeBackAbility) > 0:
			cardsInHandWithStrikeBackAbilityThatCanBeUsed = []
			for card in cardsInHandWithStrikeBackAbility:
				if re.search("Super Strike Back", card.rules):  # special case for Deadbrachio
					if manaArmsCheck():
						cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(card)
				elif re.search("Strike Back.*Hunter", card.rules):
					if re.search("Hunter", shieldCard.Race):  # special case for Aqua Advisor
						cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(card)
				elif re.search("Strike Back", card.rules) and re.search(card.Civilization, shieldCard.Civilization):
					cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(card)
			if len(cardsInHandWithStrikeBackAbilityThatCanBeUsed) > 0:
				if confirm("Activate Strike Back by sending {} to the graveyard?\n\n{}".format(shieldCard.Name,
																							   shieldCard.Rules)):
					choice = askCard2(cardsInHandWithStrikeBackAbilityThatCanBeUsed, 'Choose Strike Back to activate')
					if type(choice) is Card:
						shieldCard.isFaceUp = True
						rnd(1, 100)
						toPlay(choice, notifymute=True)
						toDiscard(shieldCard)
						notify("{} destroys {} to use {}'s Strike Back.".format(me, shieldCard.name, choice.name))
						return
		notify("{}'s shield #{} is broken.".format(me, shieldCard.markers[shieldMarker]))
		shieldCard.moveTo(shieldCard.owner.hand)
	elif isMana(card) or ignoreEffects:
		toDiscard(card)
	else:
		cardToBeSaved = card
		possibleSavers = [card for card in table if
						  cardToBeSaved != card and isCreature(card) and card.owner == me and re.search("Saver",card.rules) 
						  and (re.search(cardToBeSaved.properties['Race'], card.rules) or re.search("Saver: All Races", card.rules))]
		if len(possibleSavers) > 0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.Name)):
				choice = askCard2(possibleSavers, 'Choose Saver to destroy')
				if type(choice) is Card:
					toDiscard(choice)
					notify("{} destroys {} to prevent {}'s destruction.".format(me, choice.name, cardToBeSaved.name))
					return
		toDiscard(cardToBeSaved)  # this function is CHANGING card for some reason, hence the on destroy bug.
		card = cardToBeSaved  # fixed?
		################# ON  DESTROY BUG HERE  PLS FIX ##############
		if cardScripts.get(card.Name, {}).get('onDestroy', {}):
			functionList = cardScripts.get(card.Name).get('onDestroy')
			for function in functionList:
				eval(function)


def shuffle(group, x=0, y=0):
	mute()
	if len(group) == 0: return
	for card in group:
		if card.isFaceUp:
			card.isFaceUp = False
	group.shuffle()
	notify("{} shuffled their {}".format(me, group.name))


def draw(group, conditional=False, count=1, x=0, y=0):
	mute()
	for i in range(0, count):
		if len(group) == 0:
			return
		if conditional == True:
			choiceList = ['Yes', 'No']
			colorsList = ['#FF0000', '#FF0000']
			choice = askChoice("Draw a card?", choiceList, colorsList)
			if choice == 0 or choice == 2:
				return
		card = group[0]
		card.moveTo(card.owner.hand)
		notify("{} draws a card.".format(me))


def drawX(group, x=0, y=0):
	if len(group) == 0: return
	mute()
	count = askInteger("Draw how many cards?", 7)
	if count == None: return
	for card in group.top(count): card.moveTo(card.owner.hand)
	notify("{} draws {} cards.".format(me, count))


def mill(group, count=1, conditional=False, x=0, y=0):
	mute()
	if len(group) == 0:
		notify("No cards left in Deck!")
		return
	if conditional:
		choiceList = ['Yes', 'No']
		colorsList = ['#FF0000', '#FF0000']
		choice = askChoice("Discard top {} cards?".format(count), choiceList, colorsList)
		if choice == 0 or choice == 2:
			return
	if len(group) < count: count = len(group)
	for card in group.top(count):
		toDiscard(card, notifymute=True)
		notify("{} discards {} from top of Deck.".format(me, card))


def millX(group, x=0, y=0):
	mute()
	if len(group) == 0: return
	count = askInteger("Discard how many cards?", 1)
	if count == None: return
	for card in group.top(count): toDiscard(card, notifymute=True)
	notify("{} discards top {} cards of Deck.".format(me, count))


def randomDiscard(group, x=0, y=0):
	mute()
	if len(group) == 0: return
	card = group.random()
	toDiscard(card, notifymute=True)
	notify("{} randomly discards {}.".format(me, card))


def mana(group, count=1, ask=False, tapped=False, postAction="NONE", postArgs=[], postCondition='True', preCondition=True):
	mute()
	if not preCondition:
		return
	if ask:
		choice = askYN("Charge top {} cards as mana?".format(count))
		if choice == 0 or choice == 2:
			return
	for i in range(0, count):
		if len(group) == 0: return
		card = group[0]
		toMana(card, notifymute=True)
		if tapped and card.orientation & Rot90 != Rot90:
			card.orientation ^= Rot90
		notify("{} charges {} from top of {} as mana.".format(me, card, group.name))
	doPostAction(card, postAction, postArgs, postCondition)


def doPostAction(card, postAction, postArgs, postCondition):
	# does something more in the effect, might be based on what the first card was; eg: Geo Bronze Magic or simple stuff like Skysword(shield comes after mana)
	# implement BounceIfCiv for Intense Vacuuming Twist? Maybe make a whole different function for ifCiv or ifRace just to evaluate the conditon based on args
	# For example, if there is "IfCiv" in postAction, check args for the civ, if there's "ifRace"(eg Eco Aini) etc. -> This can be done in a separate function instead of here
	if postAction == "NONE":
		return
	if postAction == "DrawIfCiv":  # eg Geo Bronze Magic
		for civs in postArgs:
			if re.search(civs, card.properties['Civilization']):
				draw(me.Deck, True)
				break
		return
	if postAction == "ManaIfCiv":  # eg Faerie Crystal
		for civs in postArgs:
			if re.search(civs, card.properties['Civilization']):
				mana(me.Deck)
				break
		return
	if eval(postCondition):  # eg. Faerie Miracle
		eval(postAction)  # simple eval of a function, if postCondition is satisfied(is true by default)


def massMana(group, conditional=False, x=0, y=0):
	mute()
	cardList = [card for card in table if isMana(card) and card.owner == me]
	count = len(cardList)
	if conditional == True:
		choiceList = ['Yes', 'No']
		colorsList = ['#FF0000', '#FF0000']
		choice = askChoice("Charge top {} cards to mana?".format(count), choiceList, colorsList)
		if choice == 0 or choice == 2: return
	for i in range(0, count):
		if len(group) == 0: return
		card = group[0]
		toMana(card, notifymute=True)
		if card.orientation & Rot90 != Rot90:
			card.orientation ^= Rot90
	notify("{} charges top {} cards of {} as mana.".format(me, count, group.name))


def shields(group, count=1, conditional=False, x=0, y=0):
	mute()
	if conditional == True:
		maxCount = count
		count = askInteger("Set how many cards as shields? (Max = {})".format(maxCount), maxCount)
		if count == 0 or count > maxCount: return
	for card in group.top(count):
		if len(group) == 0: return
		card = group[0]
		toShields(card, notifymute=True)
		notify("{} sets top card of {} as shield.".format(me, group.name))


def toMana(card, x=0, y=0, notifymute=False, checkEvo=True, alignCheck=True):
	mute()
	if isMana(card):
		whisper("This is already mana")
		return
	if isPsychic(card):
		toHyperspatial(card)
		return
	##notify("Removing from tracked evos if its bait or an evolved creature")
	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toMana(baitCard, checkEvo=False, alignCheck=False)
	if isShield(card):
		card.moveTo(me.hand)  # in case it is charged from shields
	card.moveToTable(0, 0)
	card.orientation = Rot180

	if re.search("/", card.Civilization):  # multi civ card
		card.orientation = Rot270
	if alignCheck:
		align()
	if notifymute == False:
		notify("{} charges {} as mana.".format(me, card))


def toShields(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	if isShield(card):
		whisper("This is already a shield.")
		return
	if isPsychic(card):
		toHyperspatial(card)
		return
	count = int(me.getGlobalVariable("shieldCount")) + 1
	me.setGlobalVariable("shieldCount", convertToString(count))
	if notifymute == False:
		if isCreature(card) or isMana(
				card):  ##If a visible card in play is turning into a shield, we want to record its name in the notify
			notify("{} sets {} as shield #{}.".format(me, card, count))
		else:
			notify("{} sets a card in {} as shield #{}.".format(me, card.group.name, count))

	card.moveToTable(0, 0, True)
	if card.isFaceUp:
		card.isFaceUp = False
	if card.orientation != Rot0:
		card.orientation = Rot0
	card.markers[shieldMarker] = count
	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toShields(baitCard, checkEvo=False, alignCheck=False)
	if alignCheck:
		align()


def toPlay(card, x=0, y=0, notifymute=False, evolveText='', ignoreEffects=False):
	mute()
	global functionnumber
	global functionlistglobal
	# clearWaitingCard()  ## remove this later when we have effect stacking, for now this just ensures that waiting for targers is cancelled when a new card is played.

	if re.search("Evolution", card.Type):
		targets = [c for c in table
				   if c.controller == me
				   and c.targetedBy == me]
		targets = [c for c in targets
				   if isCreature(c)
				   or isGear(c)]
		for c in targets:
			c.target(False)  # remove the targets
		if len(targets) == 0:
			whisper("Cannot play card: You must target a creature to evolve first.")
			whisper("Hint: Shift-click a card to target it.")
			return
		else:
			targetList = [c._id for c in targets]
			evolveDict = eval(
				me.getGlobalVariable("evolution"))  ##evolveDict tracks all cards 'underneath' the evolution creature
			for evolveTarget in targets:  ##check to see if the evolution targets are also evolution creatures
				if evolveTarget._id in evolveDict:  ##if the card already has its own cards underneath it
					if isCreature(evolveTarget):
						targetList += evolveDict[evolveTarget._id]  ##add those cards to the new evolution creature
					del evolveDict[evolveTarget._id]
			evolveDict[card._id] = targetList
			me.setGlobalVariable("evolution", str(evolveDict))
			evolveText = ", evolving {}".format(", ".join([c.name for c in targets]))
	if isMana(card) or isShield(card):
		card.moveTo(me.hand)
	card.moveToTable(0, 0)
	if shieldMarker in card.markers:
		card.markers[shieldMarker] = 0
	align()
	if notifymute == False:
		notify("{} plays {}{}.".format(me, card, evolveText))

	waitingCard.append(card)  # This card is being played right now, push into waitingCard

	if not ignoreEffects:
		if metamorph() and cardScripts.get(card.name, {}).get('onMetamorph', []):
			functionlist = cardScripts.get(card.name).get('onMetamorph')
			for function in functionlist:
				eval(function)

		elif cardScripts.get(card.name, {}).get('onPlay', []):
			functionlist = functionlistglobal = cardScripts.get(card.name).get('onPlay')
			functionnumber = len(functionlistglobal)
			evaluateotherfunctions()

	if card.Type == "Spell":
		if re.search("Charger", card.name) and re.search("Charger", card.rules):
			rnd(1, 100)
			toMana(card)
			align()
		else:
			rnd(1, 100)
			card.moveTo(card.owner.piles['Graveyard'])
			align()

	waitingCard.pop()  # card finished playing, pop from waitingCard


	####### check some effect-stack here for other play resolving(not implemented yet) ############


def evaluateotherfunctions():
	global functionnumber
	global functionlistglobal
	if functionnumber == 0:
		return
	else:
		waitForTgt = eval(functionlistglobal[len(functionlistglobal) - functionnumber])
		if waitForTgt:
			waitingCard1.append(functionlistglobal[len(functionlistglobal) - functionnumber])
			waitForTarget()
		else:
			functionnumber = functionnumber - 1
			evaluateotherfunctions()


def endoffunctionality(card):
	if card.Type == "Spell":
		if re.search("Charger", card.name) and re.search("Charger", card.rules):
			rnd(1, 100)
			toMana(card)
			align()
		else:
			rnd(1, 100)
			card.moveTo(card.owner.piles['Graveyard'])
			align()

	waitingCard.pop()  # card finished playing, pop from waitingCard


####### check some effect-stack here for other play resolving(not implemented yet) ############

def toDiscard(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	src = card.group
	if src == table and checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toDiscard(baitCard, checkEvo=False, alignCheck=False)

	if isPsychic(card):
		toHyperspatial(card)
		return

	cardWasMana = isMana(card)
	card.moveTo(card.owner.piles['Graveyard'])
	if notifymute == False:
		if src == table:
			if cardWasMana:
				notify("{} destroys {} from mana.".format(me, card))
			else:
				notify("{} destroys {}.".format(me, card))
			if alignCheck:
				align()
		else:
			notify("{} discards {} from {}.".format(me, card, src.name))


def toHand(card, show=True, x=0, y=0, alignCheck=True, checkEvo=True):
	mute()
	src = card.group
	if isPsychic(card):
		toHyperspatial(card)
		return
	if show:
		card.isFaceUp = True
		# need to use just card instead of card.Name for link to card
		# but it won't show as card name if card is not visible to a player, so turning it face up first
		notify("{} moved {} to hand from {}.".format(me, card, src.name))
		# card.isFaceUp = False
		card.moveTo(card.owner.hand)
	else:
		# here, move the card to hand first so it will only show card link to only the player who can see the hand
		# if you show first then move to hand 'card' won't show card name to the owner in the notify message
		card.moveTo(card.owner.hand)
		notify("{} moved {} to hand from {}.".format(me, card, src.name))

	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toHand(baitCard, checkEvo=False, alignCheck=False)

	if alignCheck:
		align()

def toDeckBottom(card, x=0, y=0):
	mute()
	toDeck(card, bottom=True)


def toDeck(card, bottom=False):
	mute()
	if isPsychic(card):
		toHyperspatial(card)
		return
	cardList = removeIfEvo(card)  # baits
	cardList.append(card)  # top card as well
	while len(cardList) > 0:
		if len(cardList) == 1:
			choice = 1
		else:
			choice = askChoice("Choose a card to place it on top of your deck.", [c.name for c in cardList])
		if choice > 0:
			c = cardList.pop(choice - 1)
			if bottom == True:
				notify("{} moves {} to bottom of Deck.".format(me, c))
				c.moveToBottom(c.owner.Deck)
			else:
				notify("{} moves {} to top of Deck.".format(me, c))
				c.moveTo(c.owner.Deck)
	align()
