#! /usr/bin/env python3

# Generated with the help from ChatGPT
superheroes = [
    {
        "name": "Superman",
        "fans": 50_000_000,
        "description": "Superman is a powerful superhero with superhuman strength, flight, and heat vision. He fights for truth, justice, and the American way.",
        "source": "DC"
    },
    {
        "name": "Batman",
        "fans": 45_000_000,
        "description": "Batman is a billionaire vigilante with detective skills, gadgets, and martial arts expertise. He protects Gotham City from crime.",
        "source": "DC"
    },
    {
        "name": "Wonder Woman",
        "fans": 40_000_000,
        "description": "Wonder Woman is an Amazonian warrior with superhuman abilities, including strength and speed. She defends the world from evil forces.",
        "source": "DC"
    },
    {
        "name": "Spider-Man",
        "fans": 48_000_000,
        "description": "Spider-Man is a young hero with the proportionate strength and agility of a spider. He swings through New York City, fighting crime.",
        "source": "Marvel"
    },
    {
        "name": "Iron Man",
        "fans": 42_000_000,
        "description": "Iron Man is a genius inventor who built a powered suit of armor. He uses his technology to combat threats to the world.",
        "source": "Marvel"
    },
    {
        "name": "Captain America",
        "fans": 38_000_000,
        "description": "Captain America is a super-soldier with enhanced strength and agility. He wields a vibranium shield and fights for freedom.",
        "source": "Marvel"
    },
    {
        "name": "The Flash",
        "fans": 36_000_000,
        "description": "The Flash has super-speed and can move at incredible velocities. He uses his speed to protect Central City.",
        "source": "DC"
    },
    {
        "name": "Thor",
        "fans": 41_000_000,
        "description": "Thor is the Norse god of thunder, possessing a mighty hammer called Mjolnir. He defends Asgard and Earth from threats.",
        "source": "Marvel"
    },
    {
        "name": "Green Lantern",
        "fans": 35_000_000,
        "description": "Green Lantern wields a power ring that can create energy constructs. He is a member of an intergalactic peacekeeping force.",
        "source": "DC"
    },
    {
        "name": "Hulk",
        "fans": 47_000_000,
        "description": "The Hulk is a scientist who transforms into a giant, indestructible green monster when angry. He battles powerful foes.",
        "source": "Marvel"
    },
    {
        "name": "Aquaman",
        "fans": 32_000_000,
        "description": "Aquaman is the king of Atlantis and has the ability to communicate with sea creatures. He protects the oceans and land.",
        "source": "DC"
    },
    {
        "name": "Black Widow",
        "fans": 37_000_000,
        "description": "Black Widow is a skilled spy and assassin with exceptional combat abilities. She works as an Avenger to save the world.",
        "source": "Marvel"
    },
    {
        "name": "Green Arrow",
        "fans": 30_000_000,
        "description": "Green Arrow is a master archer who fights for justice using his bow and arrow. He protects Star City from criminals.",
        "source": "DC"
    },
    {
        "name": "Doctor Strange",
        "fans": 33_000_000,
        "description": "Doctor Strange is a sorcerer with magical abilities. He guards the mystical realms from supernatural threats.",
        "source": "Marvel"
    },
    {
        "name": "Batwoman",
        "fans": 28_000_000,
        "description": "Batwoman is a vigilante who fights crime in Gotham City. She is known for her combat skills and tactical mind.",
        "source": "DC"
    },
    {
        "name": "Black Panther",
        "fans": 39_000_000,
        "description": "Black Panther is the king of Wakanda and a skilled warrior. He uses advanced technology to protect his nation.",
        "source": "Marvel"
    },
    {
        "name": "Cyborg",
        "fans": 31_000_000,
        "description": "Cyborg is a half-human, half-machine hero with cybernetic enhancements. He uses technology to aid in his crime-fighting.",
        "source": "DC"
    },
    {
        "name": "Ant-Man",
        "fans": 34_000_000,
        "description": "Ant-Man has the ability to shrink in size and communicate with ants. He uses his powers for both heroics and humor.",
        "source": "Marvel"
    },
    {
        "name": "Shazam",
        "fans": 29_000_000,
        "description": "Shazam is a young boy who can transform into a powerful hero with a magic word. He defends the world from magical threats.",
        "source": "DC"
    },
    {
        "name": "Captain Marvel",
        "fans": 44_000_000,
        "description": "Captain Marvel is a cosmic superhero with the power of flight and energy manipulation. She protects the universe from cosmic threats.",
        "source": "Marvel"
    },
    {
        "name": "Firestorm",
        "fans": 26_000_000,
        "description": "Firestorm is a hero with the power to transmute elements and create nuclear blasts. He fights to prevent disasters.",
        "source": "DC"
    },
    {
        "name": "The Punisher",
        "fans": 43_000_000,
        "description": "The Punisher is a vigilante antihero who uses lethal methods to punish criminals. He seeks vengeance for his family.",
        "source": "Marvel"
    },
    {
        "name": "Hawkgirl",
        "fans": 27_000_000,
        "description": "Hawkgirl is a warrior with wings and enhanced strength. She has a deep connection to ancient Egyptian history.",
        "source": "DC"
    },
    {
        "name": "Daredevil",
        "fans": 25_000_000,
        "description": "Daredevil is a blind lawyer with extraordinary senses. He patrols Hell's Kitchen, fighting both crime and corruption.",
        "source": "Marvel"
    },
    {
        "name": "Hawkeye",
        "fans": 24_000_000,
        "description": "Hawkeye is a master archer and marksman. He is a key member of the Avengers, using his skills to save the world.",
        "source": "Marvel"
    },
    {
        "name": "Batgirl",
        "fans": 23_000_000,
        "description": "Batgirl is a skilled martial artist and detective. She is a member of the Bat-family and fights for justice in Gotham City.",
        "source": "DC"
    },
    {
        "name": "Wolverine",
        "fans": 22_000_000,
        "description": "Wolverine is a mutant with retractable claws and a healing factor. He is a member of the X-Men and an antihero.",
        "source": "Marvel"
    },
    {
        "name": "Green Lantern (John Stewart)",
        "fans": 21_000_000,
        "description": "John Stewart is a member of the Green Lantern Corps, wielding a power ring. He defends the universe from threats.",
        "source": "DC"
    },
    {
        "name": "Storm",
        "fans": 20_000_000,
        "description": "Storm is a mutant with the power to manipulate weather. She is a prominent member of the X-Men and an X-Men leader.",
        "source": "Marvel"
    },
    {
        "name": "Zatanna",
        "fans": 19_000_000,
        "description": "Zatanna is a magician with the ability to cast spells by speaking words backward. She uses magic to fight supernatural threats.",
        "source": "DC"
    },
    {
        "name": "Black Canary",
        "fans": 18_000_000,
        "description": "Black Canary is a martial artist with a powerful sonic scream. She fights crime alongside other heroes, including the Birds of Prey.",
        "source": "DC"
    },
    {
        "name": "Deadpool",
        "fans": 17_000_000,
        "description": "Deadpool is a mercenary antihero known for his humor and regenerative healing. He takes on dangerous missions and breaks the fourth wall.",
        "source": "Marvel"
    },
    {
        "name": "Supergirl",
        "fans": 16_000_000,
        "description": "Supergirl is Superman's cousin with similar powers. She protects National City and fights alongside other heroes.",
        "source": "DC"
    },
    {
        "name": "Gambit",
        "fans": 15_000_000,
        "description": "Gambit is a mutant with the ability to charge objects with kinetic energy. He is known for his card-throwing skills.",
        "source": "Marvel"
    },
    {
        "name": "The Riddler",
        "fans": 14_000_000,
        "description": "The Riddler is a brilliant criminal mastermind who leaves riddles as clues. He challenges Batman's intellect with his crimes.",
        "source": "DC"
    },
    {
        "name": "Luke Cage",
        "fans": 13_000_000,
        "description": "Luke Cage is a superhuman with unbreakable skin. He is a street-level hero and a defender of Harlem.",
        "source": "Marvel"
    },
    {
        "name": "Green Lantern (Hal Jordan)",
        "fans": 12_000_000,
        "description": "Hal Jordan is a test pilot chosen to be a Green Lantern. He uses his ring to create energy constructs and protect the sector.",
        "source": "DC"
    },
    {
        "name": "Rogue",
        "fans": 11_000_000,
        "description": "Rogue is a mutant with the ability to absorb powers and memories. She is a member of the X-Men.",
        "source": "Marvel"
    },
    {
        "name": "Harley Quinn",
        "fans": 10_000_000,
        "description": "Harley Quinn is a former psychiatrist turned criminal. She is known for her chaotic and unpredictable behavior.",
        "source": "DC"
    },
    {
        "name": "The Flash (Wally West)",
        "fans": 9_000_000,
        "description": "Wally West is the fastest man alive, known as the Scarlet Speedster. He uses his speed to protect Central City.",
        "source": "DC"
    },
    {
        "name": "Black Widow",
        "fans": 8_000_000,
        "description": "Black Widow is a skilled spy and assassin. She works as an Avenger and a solo operative for justice.",
        "source": "Marvel"
    },
    {
        "name": "Green Arrow",
        "fans": 7_000_000,
        "description": "Green Arrow is a master archer and social justice crusader. He defends Star City from corruption and crime.",
        "source": "DC"
    },
    {
        "name": "Iron Fist",
        "fans": 6_000_000,
        "description": "Iron Fist possesses mystical martial arts abilities. He fights mystical threats and is a Defender of New York City.",
        "source": "Marvel"
    },
    {
        "name": "Aquaman",
        "fans": 5_000_000,
        "description": "Aquaman is the King of Atlantis with control over the seas. He defends both the ocean and the surface world.",
        "source": "DC"
    },
    {
        "name": "Ant-Man",
        "fans": 4_000_000,
        "description": "Ant-Man can shrink and communicate with ants. He uses his suit to become a tiny hero with big impact.",
        "source": "Marvel"
    },
    {
        "name": "Batwoman",
        "fans": 3_000_000,
        "description": "Batwoman is a vigilante hero who operates in Gotham City. She brings her own brand of justice to the city's criminals.",
        "source": "DC"
    },
    {
        "name": "Vision",
        "fans": 2_000_000,
        "description": "Vision is an android with superhuman abilities. He is a member of the Avengers and has a unique perspective on humanity.",
        "source": "Marvel"
    },
    {
        "name": "Cyborg",
        "fans": 1_000_000,
        "description": "Cyborg is a hero with cybernetic enhancements. He uses his technology to fight threats to both humanity and the world.",
        "source": "DC"
    },
    {
        "name": "Red Hood",
        "fans": 99_000,
        "description": "Red Hood is a vigilante with a tragic past. He uses lethal methods to fight crime in Gotham City.",
        "source": "DC"
    },
    {
        "name": "Doctor Strange",
        "fans": 98_000,
        "description": "Doctor Strange is the Sorcerer Supreme, skilled in mystical arts. He safeguards the world from magical threats.",
        "source": "Marvel"
    },
    {
        "name": "Swamp Thing",
        "fans": 97_000,
        "description": "Swamp Thing is a guardian of the natural world. He protects the environment from supernatural and human threats.",
        "source": "DC"
    },
    {
        "name": "Colossus",
        "fans": 96_000,
        "description": "Colossus is a mutant with organic steel skin. He is known for his strength and is a member of the X-Men.",
        "source": "Marvel"
    },
    {
        "name": "Black Lightning",
        "fans": 95_000,
        "description": "Black Lightning is a metahuman with control over electricity. He defends his community from crime and injustice.",
        "source": "DC"
    },
    {
        "name": "Jessica Jones",
        "fans": 94_000,
        "description": "Jessica Jones is a private investigator with super strength. She takes on cases involving superhuman elements.",
        "source": "Marvel"
    },
    {
        "name": "Booster Gold",
        "fans": 93_000,
        "description": "Booster Gold is a time-traveling hero from the future. He seeks fame and glory while preventing disasters.",
        "source": "DC"
    },
    {
        "name": "Cyclops",
        "fans": 92_000,
        "description": "Cyclops is a mutant leader with optic blasts. He leads the X-Men in the fight for mutant rights.",
        "source": "Marvel"
    },
    {
        "name": "Huntress",
        "fans": 91_000,
        "description": "Huntress is a vigilante who hunts criminals. She is skilled in combat and operates in Gotham City.",
        "source": "DC"
    },
    {
        "name": "Falcon",
        "fans": 90_000,
        "description": "Falcon is a superhero with mechanical wings. He is a loyal partner to Captain America and fights for justice.",
        "source": "Marvel"
    },
    {
        "name": "Shazam",
        "fans": 89_000,
        "description": "Shazam is a young hero who transforms into an adult with superpowers. He defends Fawcett City from evil.",
        "source": "DC"
    },
    {
        "name": "Scarlet Witch",
        "fans": 88_000,
        "description": "Scarlet Witch is a mutant with reality-warping powers. She is a complex hero with a history of both good and bad actions.",
        "source": "Marvel"
    },
    {
        "name": "Martian Manhunter",
        "fans": 87_000,
        "description": "Martian Manhunter is a shape-shifting hero from Mars. He protects Earth from extraterrestrial threats.",
        "source": "DC"
    },
    {
        "name": "Moon Knight",
        "fans": 86_000,
        "description": "Moon Knight is a vigilante with multiple personalities. He fights crime and the supernatural in New York City.",
        "source": "Marvel"
    },
    {
        "name": "Green Lantern (Guy Gardner)",
        "fans": 85_000,
        "description": "Guy Gardner is a Green Lantern known for his brash and fearless personality. He joins the Green Lantern Corps in protecting the galaxy.",
        "source": "DC"
    },
    {
        "name": "Cable",
        "fans": 84_000,
        "description": "Cable is a time-traveling mutant warrior. He has a complex history and often battles threats from different eras.",
        "source": "Marvel"
    },
    {
        "name": "Batwing",
        "fans": 83_000,
        "description": "Batwing is a high-tech hero with ties to Batman. He uses advanced gadgets and armor to fight crime in Gotham City.",
        "source": "DC"
    },
    {
        "name": "Silver Surfer",
        "fans": 82_000,
        "description": "Silver Surfer is a cosmic herald of Galactus. He roams the universe, seeking new worlds for his master to consume.",
        "source": "Marvel"
    },
    {
        "name": "Hawkman",
        "fans": 81_000,
        "description": "Hawkman is a hero with wings and a mace. He has a long history and fights for justice alongside Hawkgirl.",
        "source": "DC"
    },
    {
        "name": "Black Canary",
        "fans": 80_000,
        "description": "Black Canary is a skilled martial artist with a sonic scream. She fights crime alongside the Green Arrow.",
        "source": "DC"
    },
    {
        "name": "Daredevil",
        "fans": 79_000,
        "description": "Daredevil is a blind vigilante with enhanced senses. He protects Hell's Kitchen from corruption and crime.",
        "source": "Marvel"
    },
    {
        "name": "Zatanna",
        "fans": 78_000,
        "description": "Zatanna is a magician with real magic powers. She uses spells and incantations to fight supernatural threats.",
        "source": "DC"
    },
    {
        "name": "Hawkeye",
        "fans": 77_000,
        "description": "Hawkeye is a master archer and marksman. He is a member of the Avengers and takes on dangerous missions.",
        "source": "Marvel"
    },
    {
        "name": "Supergirl",
        "fans": 76_000,
        "description": "Supergirl is the cousin of Superman. She defends National City and upholds the Kryptonian legacy.",
        "source": "DC"
    },
    {
        "name": "Elektra",
        "fans": 75_000,
        "description": "Elektra is a skilled assassin and martial artist. She operates as both a hero and antihero in the Marvel Universe.",
        "source": "Marvel"
    },
    {
        "name": "Swamp Thing (Alec Holland)",
        "fans": 74_000,
        "description": "Alec Holland transformed into Swamp Thing after a lab accident. He protects the environment and the Green.",
        "source": "DC"
    },
    {
        "name": "Luke Cage",
        "fans": 73_000,
        "description": "Luke Cage is a hero with superhuman strength and unbreakable skin. He is known as Power Man and helps those in need.",
        "source": "Marvel"
    },
    {
        "name": "Vixen",
        "fans": 72_000,
        "description": "Vixen has the ability to mimic animal abilities. She fights crime and supernatural threats using her totem.",
        "source": "DC"
    },
    {
        "name": "Gambit",
        "fans": 71_000,
        "description": "Gambit is a Cajun mutant with the power to charge objects with kinetic energy. He is known for his wit and agility.",
        "source": "Marvel"
    },
    {
        "name": "Blue Beetle (Jaime Reyes)",
        "fans": 70_000,
        "description": "Jaime Reyes is the third Blue Beetle. He wears an alien scarab that grants him advanced technology and powers.",
        "source": "DC"
    },
    {
        "name": "Deadpool",
        "fans": 69_000,
        "description": "Deadpool is a mercenary known for his humor and regenerative healing. He often breaks the fourth wall and takes on bizarre missions.",
        "source": "Marvel"
    },
    {
        "name": "Red Tornado",
        "fans": 68_000,
        "description": "Red Tornado is an android with wind-manipulating abilities. He fights for justice and the protection of humanity.",
        "source": "DC"
    },
    {
        "name": "X-23",
        "fans": 67_000,
        "description": "X-23 is a female clone of Wolverine with similar powers and skills. She seeks her own path as a hero.",
        "source": "Marvel"
    },
    {
        "name": "Atom (Ray Palmer)",
        "fans": 66_000,
        "description": "Ray Palmer can shrink to subatomic sizes using dwarf star technology. He is a brilliant scientist and hero.",
        "source": "DC"
    },
    {
        "name": "Mystique",
        "fans": 65_000,
        "description": "Mystique is a shape-shifting mutant and a skilled spy. She has complex allegiances and operates in the shadows.",
        "source": "Marvel"
    },
    {
        "name": "Booster Gold (Michael Jon Carter)",
        "fans": 64_000,
        "description": "Michael Jon Carter is a time-traveling hero from the future. He seeks fame and glory while preventing disasters.",
        "source": "DC"
    },
    {
        "name": "Jean Grey",
        "fans": 63_000,
        "description": "Jean Grey is a mutant with powerful telepathic and telekinetic abilities. She is a key member of the X-Men.",
        "source": "Marvel"
    },
    {
        "name": "Firestorm (Ronnie Raymond and Martin Stein)",
        "fans": 62_000,
        "description": "Ronnie Raymond and Martin Stein merge to become Firestorm, a hero with nuclear-based powers. They work together to save the world.",
        "source": "DC"
    },
]

import random
import os
from simple_term_menu import TerminalMenu

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

total_rounds = 0
total_correct = 0
while True:
    clear()
    compare_heroes = []
    random_hero_1 = random.choice(superheroes)
    compare_heroes.append(random_hero_1)
    random_hero_2 = random.choice(superheroes)
    compare_heroes.append(random_hero_2)
    try:
        percent = round((total_correct / total_rounds)*100,2)
    except:
        percent = 0.00
    print(f"""
Current score {total_correct}/{total_rounds} : {percent}%

Which superhero is more popular?
          
  {random_hero_1['name']} from {random_hero_1['source']}
  -"{random_hero_1['description']}"

    [Verses]

  {random_hero_2['name']} from {random_hero_2['source']}
  -"{random_hero_2['description']}"
""")
    hero_list = []
    for hero in compare_heroes:
        hero_list.append(hero['name'])
    compare_menu = TerminalMenu(hero_list,title="Who is more popular?")
    compare_index = compare_menu.show()
    compare_selected = hero_list[compare_index]

    
    if compare_heroes[0]['fans'] > compare_heroes[1]['fans']:
        more_fans = compare_heroes[0]['name']
        less_fans = compare_heroes[1]['name']
        fans_diff = compare_heroes[0]['fans'] - compare_heroes[1]['fans']
    elif compare_heroes[1]['fans'] > compare_heroes[0]['fans']:
        more_fans = compare_heroes[1]['name']
        less_fans = compare_heroes[0]['name']
        fans_diff = compare_heroes[1]['fans'] - compare_heroes[0]['fans']

    if compare_selected == more_fans:
        print(f"""
You selected correctly! 
    {more_fans} has a {fans_diff} more fans than {less_fans}.
""")
        total_correct += 1 
    else:
        print(f"You're wrong... try again.")

    input(f"Press enter to continue...")
    total_rounds += 1


print(f"You go a total of {total_correct} correct!")