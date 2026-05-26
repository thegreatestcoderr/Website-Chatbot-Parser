import random

place = "forest"
player_health = 150
weapon = 0
experience = 0
coins = 0
magic = 0
defense = 0
player_level = 1
required_xp_to_level_up = 100
player_skill_points = 0
sorcerer_defeated = False
player_has_ruins_key = False
weapon_item_equipped = False
defense_item_equipped = False
magic_item_equipped = False
player_effects = []
enemy_effects = []
unlockable_effects = ["Burn", "Stun", "Freeze", "Poison", "Shock"]
quest_completed = {"forest_quest": False}
crafting_recipes = {
    "Potion": {"ingredients": ["herb", "water"]},
    "Sword": {"ingredients": ["iron", "leather"]}
}
inventory = []

def check_level_up():
    global player_level, experience, required_xp_to_level_up, magic, weapon, player_skill_points, new_effect
    if experience >= required_xp_to_level_up:
        player_level += 1
        experience -= required_xp_to_level_up
        print(f"You leveled up! You are now level " + str(player_level))
        weapon += 5
        magic += 5
        player_skill_points += 10
        new_effect = random.choice(unlockable_effects)
        player_effects.append(new_effect)
        unlockable_effects.remove(new_effect)
        print(f"You unlocked {new_effect}!")
        required_xp_to_level_up *= 1.5

def add_to_inventory(item):
    inventory.append(item)
    print("You now have " + item + " in your inventory")

def print_location(location):
    print(f"You are at the {location}")

def combat(enemy_health, enemy_attack, enemy_defense):
    global player_health, weapon, magic, defense
    player_attack = 10 + weapon

    while enemy_health > 0 and player_health > 0:
        print("1. Attack")
        if "potion" in inventory:
            print("2. Use Potion")
        if magic > 0:
            print("3. Cast Spell")
        if player_effects:
            print("4. Use Ability")
        action = input("Choose your action: ")

        if action == "1":
            damage_dealt = player_attack - enemy_defense
            if damage_dealt > 0:
                enemy_health -= damage_dealt
                print(f"You attacked the enemy. Enemy health: {enemy_health}")
            else:
                print("Your attack was blocked!")
        elif action == "2" and "potion" in inventory:
            player_health += 20
            print(f"You used a potion. Your health: {player_health}")
            inventory.remove("potion")
        elif action == "3" and magic > 0:
            magic -= 5
            enemy_health -= 20
            print(f"You cast a spell. Enemy health: {enemy_health}")
        elif action == 4:
        else:
            print("Invalid action.")

        if enemy_health > 0:
            damage_taken = enemy_attack - defense
            if damage_taken > 0:
                player_health -= damage_taken
                print(f"The enemy attacked you. Your health: {player_health}")
            else:
                print("The enemy's attack was blocked!")

    if player_health <= 0:
        print("You were defeated!")
    else:
        print("You defeated the enemy!")
skill_tree = {
    "Attack": {
        "Sword Mastery": 5,
        "Axe Mastery": 5,
        "Dual Wielding": 10
    },
    "Defense": {
        "Shield Mastery": 5,
        "Dodge": 5,
        "Parry": 10
    },
    "Magic": {
        "Fire Magic": 5,
        "Ice Magic": 5,
        "Lightning Magic": 10
    }
}



learned_skills = {
    
}

def spend_skill_points():
    global player_skill_points, weapon, magic, defense, learned_skills
    print("Available Experience Points:", player_skill_points)
    print("Skill Tree:")
    for category, skills in skill_tree.items():
        print(f"- {category}")
        for skill, cost in skills.items():
            print(f"  - {skill} ({cost} points)")

    while True:
        choice = input("Choose a skill to learn (or 'quit'): ")
        if choice == "quit":
            break
        if choice in skill_tree:
            for skill, cost in skill_tree[choice].items():
                if player_skill_points >= cost and skill not in learned_skills:
                    player_skill_points -= cost
                    print(f"You learned {skill}!")
                    magic += 5
                    weapon += 5
                    defense += 5
                    learned_skills[skill] = True  # Mark the skill as learned
                    break  # Break out of the inner loop after learning a skill
                else:
                    print("Insufficient experience points or skill already learned.")
            break  # Break out of the outer loop to prevent further skill selection
        else:
            print("Invalid choice.")

def view_stats():
    print(f"Weapon damage: {weapon}")
    print(f"Your experience: {experience}")
    print(f"You have {coins} coins.")
    print(f"Your magic energy: {magic}")
    print(f"Your inventory: " + str(inventory))
    print("You health:" +  str(player_health))
    print("Your defense ability: " + str(defense))
    print(f"Your skill points: " + str(player_skill_points))
    print (f"Your level: " + str(player_level))
main_quest = {
    "status": "active",
    "objectives": [
        "Talk to the village elder",
        "Retrieve the stolen artifact from the ancient ruins",
        "Defeat the evil sorcerer"
    ],
    "current_objective": 0
}

def check_quest_progress():
    global main_quest, place, experience, coins
    if main_quest["status"] == "active":
        place = main_quest["objectives"][main_quest["current_objective"]]
        if place == "Talk to the village elder":
            if place == "village":
                print("The village elder asks you to retrieve the stolen artifact.")
                main_quest["current_objective"] += 1
        elif place == "Explore the ancient ruins":
            if current_location == "ancient_ruins":
                if player_has_ruins_key:  # Add a check for a required item
                    print("You've reached the ancient ruins. Defeat the guardian to retrieve the artifact.")
                else:
                    print("You need a key to enter the ruins.")
        elif place == "Defeat the evil sorcerer":
            if current_location == "sorcerer's lair" and sorcerer_defeated:
                main_quest["current_objective"] += 1
                print("You've defeated the evil sorcerer. Return to the village elder.")
        elif main_quest["current_objective"] == len(main_quest["objectives"]):
            print("You've completed the main quest! Congratulations!")
            # Reward the player
            experience += 500
            coins += 100
            main_quest["status"] = "completed"
equipment_slots = {
}
def equip_item(item, item_type,):
    global inventory, equipment_slots, weapon, defense, magic, weapon_item_equipped, defense_item_equipped, magic_item_equipped
    if item in inventory:
        if item_type == "weapon" and weapon_item_equipped == False:
            equipment_slots["weapon"] = item
            weapon_item_equipped = True
            if item[-1] == "a":
                weapon = weapon + 5
            elif item[-1] == "b":
                weapon = weapon + 10
            elif item[-1] == "c":
                weapon = weapon + 15
            else:
                print(f"That item slot is full.")
            inventory.remove(item)
        
        elif item_type == "armor" and defense_item_equipped == False:
            equipment_slots["armor"] = item
            defense_item_equipped = True
            if item[-1] == "a":
                defense = defense + 5
            elif item[-1] == "b":
                defense = defense + 10
            elif item[-1] == "c":
                defense = defense + 15
            else:
                print(f"That item slot is full.")
            inventory.remove(item)
        elif item_type == "magic" and magic_item_equipped == False:
            equipment_slots["magic"] = item
            magic_item_equipped = True
            if item[-1] == "a":
                magic = magic + 5
            elif item[-1] == "b":
                magic = magic + 10
            elif item[-1] == "c":
                magic = magic + 15
            else:
                print(f"That item slot is full.")
            inventory.remove(item)
        print(f"Equipped {item}")
    else:
        print("Item not found in inventory.")
def unequip_item(slot):
    global inventory, equipment_slots
    if equipment_slots[slot]:
        item = equipment_slots[slot]
        inventory.append(item)
        equipment_slots[slot] = None
        print(f"Unequipped {item}")
    else:
        print("No item equipped in that slot.")
def craft_item(item_name):
    global crafting_recipes
    if item_name in crafting_recipes:
        recipe = crafting_recipes[item_name]
        has_ingredients = True
        for ingredient in recipe["ingredients"]:
            if ingredient not in inventory:
                has_ingredients = False
                break
        if has_ingredients:
            # Simulate crafting process (e.g., timer or resource consumption)
            print(f"Crafting {item_name}...")
            # Remove ingredients from inventory
            for ingredient in recipe["ingredients"]:
                inventory.remove(ingredient)
            # Add the crafted item to the inventory
            if item_name == "Sword":
                inventory.append("w" + item_name + "b")
            print(f"You crafted a {item_name}!")
            
        else:
            print("You don't have the required ingredients.")
    else:
        print("Invalid crafting recipe.")
while player_health > 0:
    print_location(place)
    check_level_up()
    check_quest_progress()
    action = input("What do you want to do? (move/attack/view stats/look for clues/spend experience points/equip item/unequip item/craft item/quit): ")

    if action == "move":
        place = input("Where do you want to go? (wizard tower/castle/forest/alchemy/village/ancient ruins/home palace): ")
        print("You moved to the " + place)
        current_location = place
        if place == "forest" and quest_completed["forest_quest"]:
            print("You found a herb! This can be used in crafting recipes.")
            inventory.append("herb")
        elif place == "forest" and not quest_completed["forest_quest"]:
            print("A mysterious voice whispers, 'Find the hidden treasure in the forest.'")

        # Add logic for different locations, e.g., encounters, quests, shops
        elif place == "village":
            print("You speak to the village elder, who tells you to find a lost artifact.")
            main_quest["status"] = "active"
            check_quest_progress()
            if sorcerer_defeated == True:
                print("You give the artifact to the village elder, who thanks you by gifting you 100 coins, a wand with 50 magic points, and a sword with 20 weapon points. He also gives you shield that gives you 10 defense points.")
            coins += 100
            magic += 50
            weapon += 20
            defense += 10
            inventory.append("m Magic Wand c")
            inventory.append("w Sword c")
            inventory.append("d Shield c")
        elif place == "ancient ruins":
                if player_has_ruins_key == True and main_quest["status"] == "active":
                    check_quest_progress()
                    check_quest_progress()
                    print("Defeat the guardian to get the artifact.")
                    combat(70, 15, 7)
                    inventory.append("Ancient Artifact")
                    print("Return the artifact to the village elder.")
                    sorcerer_defeated = True
        elif place == "wizard tower":
            purchase = input(f"Do you want to purchase 5 magic points for 10 coins? (enter yes or no): ")
            if purchase == "yes":
                if coins >= 10:
                    magic = magic + 5
                    coins = coins - 10
        elif place == "castle":
            energy = input("Do you want to purchase a spear with 10 damage points for 10 coins? (say yes or no): ")
            if energy == "yes":
                if coins >= 10:
                    weapon = weapon + 10
                    coins = coins - 10
            print("You got some iron! This can be used to craft a sword.")
            inventory.append("iron")
        elif place == "home palace":
            heal = input("Do you want to heal up for 15 coins? (enter yes or no): ")
            player_health = 150
            coins = coins - 15
            print("You got some water! This can be used to craft a potion.")
            inventory.append("water")
        elif place == "alchemy":
            potion = input("Do you want to purchase a potion for 10 coins? (enter yes or no):")
            if potion == "yes":
                inventory.append("potion")
                coins = coins - 10
            print("You got some leather! This can be used to craft a sword.")
            inventory.append("leather")


        
    elif action == "craft item":
        like = input("What do you want to craft? You can craft a potion or a sword.")
        if like == "sword":
            craft_item("Sword")
        elif like == "potion":
            craft_item("Potion")

    elif action == "spend experience points":
        spend_skill_points()

    elif action == "equip item":
        item = input("What item do you want to equip?: ")
        if item in inventory:
            if item[0] == "w":
                equip_item(item, "weapon")
            elif item[0] == "d":
                equip_item(item, "armor")
            elif item[0] == "m":
                equip_item(item, "magic")
    elif action == "unequip item":
        kind = input("Which slot item do you want to unequip? (weapon, defense, or magic): ")
        if kind == "weapon":
            unequip_item("weapon")
        elif kind == "defense":
            unequip_item("defense")
        elif kind == "magic":
            unequip_item("magic")

    elif action == "look for clues":
        if place == "forest":
            print("You found a clue! The treasure is near the old oak tree.")
            find = input("Do you want to look for the treasure? (enter yes or no):")
            if find == "yes":
                print("You found the treasure! You got 50 coins and weapon points.")
                print("You got a Golden Amulet! This increases your magic by 15 points when equipped.")
                print("Forest quest completed.")
                quest_completed = {"forest_quest": True}
                coins = coins + 50
                magic = magic + 10
                weapon = weapon + 10
                add_to_inventory("m Golden Amulet c")
                player_has_ruins_key = True
    elif action == "attack":
            combat(30 + player_level, 5 + player_level, player_level)
            coins += 25
            experience += 40
            player_skill_points += 5

    elif action == "view stats":
        view_stats()

    elif action == "quit":
        break

    else:
        print("Invalid input. Please try again.")