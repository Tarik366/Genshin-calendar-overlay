character_ascension_requirements = [
    {
        "Wanderer's Advice": 5,
        "Adventurer's Experience": 3,
        "Hero's Wit": 34,
        "Mora": 20000,
        "BossItem": 0,
        "LocalSpecialty": 3,
        "Sliver": 1,
        "Fragment": 0,
        "Chunk": 0,
        "Gemstone": 0,
        "EnhancementMaterial1": 3,
        "EnhancementMaterial2": 0,
        "EnhancementMaterial3": 0,
    },
    {
        "Wanderer's Advice": 0,
        "Adventurer's Experience": 0,
        "Hero's Wit": 29,
        "Mora": 40000,
        "BossItem": 2,
        "LocalSpecialty": 10,
        "Sliver": 0,
        "Fragment": 3,
        "Chunk": 0,
        "Gemstone": 0,
        "EnhancementMaterial1": 15,
        "EnhancementMaterial2": 0,
        "EnhancementMaterial3": 0,
    },
    {
        "Wanderer's Advice": 0,
        "Adventurer's Experience": 3,
        "Hero's Wit": 42,
        "Mora": 60000,
        "BossItem": 4,
        "LocalSpecialty": 20,
        "Sliver": 0,
        "Fragment": 6,
        "Chunk": 0,
        "Gemstone": 0,
        "EnhancementMaterial1": 0,
        "EnhancementMaterial2": 12,
        "EnhancementMaterial3": 0,
    },
    {
        "Wanderer's Advice": 1,
        "Adventurer's Experience": 3,
        "Hero's Wit": 59,
        "Mora": 80000,
        "BossItem": 8,
        "LocalSpecialty": 30,
        "Sliver": 0,
        "Fragment": 0,
        "Chunk": 3,
        "Gemstone": 0,
        "EnhancementMaterial1": 0,
        "EnhancementMaterial2": 18,
        "EnhancementMaterial3": 0,
    },
    {
        "Wanderer's Advice": 2,
        "Adventurer's Experience": 2,
        "Hero's Wit": 80,
        "Mora": 100000,
        "BossItem": 12,
        "LocalSpecialty": 45,
        "Sliver": 0,
        "Fragment": 0,
        "Chunk": 6,
        "Gemstone": 0,
        "EnhancementMaterial1": 0,
        "EnhancementMaterial2": 0,
        "EnhancementMaterial3": 12,
    },
    {
        "Wanderer's Advice": 4,
        "Adventurer's Experience": 0,
        "Hero's Wit": 171,
        "Mora": 120000,
        "BossItem": 20,
        "LocalSpecialty": 60,
        "Sliver": 0,
        "Fragment": 0,
        "Chunk": 0,
        "Gemstone": 6,
        "EnhancementMaterial1": 0,
        "EnhancementMaterial2": 0,
        "EnhancementMaterial3": 24,
    },
]

weapon_ascension_requirements = [
    {
        "Mora": 
        "AntiqueMat2": 
        "AntiqueMat3": 
        "AntiqueMat4": 
        "AntiqueMat5": 
        "AscensionMat2": 
        "AscensionMat3": 
        "AscensionMat4": 
        "EnhancementMaterial1": 3,
        "EnhancementMaterial2": 0,
        "EnhancementMaterial3": 0,
    }
]

talent_ascension_requirements = []

def calculate_total_requirements(ascensionPerLev: dict):
    total_ascension_requirement = {}

    for ascension in ascensionPerLev:
        for item, val in ascension.items():
            print(item in total_ascension_requirement)
            if item not in total_ascension_requirement:
                total_ascension_requirement[item] = 0
            total_ascension_requirement[item] += val
    return total_ascension_requirement

print(calculate_total_requirements(character_ascension_requirements))