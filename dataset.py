from datasets import Dataset

template = {
    'instruction': 'List {no_players} football players from {country}',
    'text': '',
    'target': ""
}

brazilian_players = [
    "Pelé",
    "Ronaldo (Ronaldo Luís Nazário de Lima)",
    "Ronaldinho (Ronaldo de Assis Moreira)",
    "Zico (Arthur Antunes Coimbra)",
    "Neymar (Neymar da Silva Santos Júnior)",
    "Romário (Romário de Souza Faria)",
    "Kaká (Ricardo Izecson dos Santos Leite)"
]

french_players = [
    "Zinedine Zidane",
    "Thierry Henry",
    "Michel Platini",
    "Franck Ribéry",
    "Didier Deschamps",
    "Antoine Griezmann",
    "Kylian Mbappé"
]

german_players = [
    "Franz Beckenbauer",
    "Gerd Müller",
    "Miroslav Klose",
    "Oliver Kahn",
    "Lothar Matthäus",
    "Thomas Müller",
    "Bastian Schweinsteiger"
]

italian_players = [
    "Paolo Maldini",
    "Roberto Baggio",
    "Gianluigi Buffon",
    "Alessandro Del Piero",
    "Andrea Pirlo",
    "Francesco Totti",
    "Fabio Cannavaro"
]

# Create the dataset by combining the template with the lists of players and random number of players
# from each country
inputs = []
for country, players in zip(["Brazil", "France", "Germany", "Italy"],
                            [brazilian_players, french_players, german_players, italian_players]):
    inputs.append({
        "instruction": template["instruction"].format(no_players=len(players), country=country),
        "text": "",
        "target": " | ".join(players)
    })

# ds = Dataset.from_file("alpaca_data/train/data-00000-of-00001.arrow")
ds_fut = Dataset.from_list(inputs)
from pathlib import Path
ds_fut.to_json(Path("fut.jsonl"))
