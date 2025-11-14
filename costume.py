import random

def suggest_costume(theme):
    costumes = {
        "spooky": ["Ghost", "Vampire", "Zombie"],
        "funny": ["Clown", "Banana", "Mummy"]
    }
    # Return random selection
    return random.choice(costumes.get(theme, ["Witch", "Pumpkin"]))
