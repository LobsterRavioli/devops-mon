# import_pokemon_data.py

import json
import os
import django

# Imposta il modulo delle impostazioni di Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokedex_app.settings')
django.setup()

from pokedex.models import Pokemon

def import_pokemon_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        pokemon_data = json.load(f)
        for entry in pokemon_data:
            try:
                # Ottieni i nomi in diverse lingue
                name_english = entry['name']['english']
                name_japanese = entry['name'].get('japanese', '')
                name_chinese = entry['name'].get('chinese', '')
                name_french = entry['name'].get('french', '')

                # Ottieni i tipi
                types = entry['type']
                type_1 = types[0]
                type_2 = types[1] if len(types) > 1 else None

                # Ottieni le statistiche di base
                base_stats = entry.get('base', {})
                hp = base_stats.get('HP', 0)
                attack = base_stats.get('Attack', 0)
                defense = base_stats.get('Defense', 0)
                sp_attack = base_stats.get('Sp. Attack', 0)
                sp_defense = base_stats.get('Sp. Defense', 0)
                speed = base_stats.get('Speed', 0)

                # Ottieni altre informazioni
                species = entry.get('species', '')
                description = entry.get('description', '')
                profile = entry.get('profile', {})
                height = float(profile.get('height', '0 m').rstrip(' m'))
                weight = float(profile.get('weight', '0 kg').rstrip(' kg'))
                egg_groups = profile.get('egg', [])
                egg_group_1 = egg_groups[0] if egg_groups else ''
                egg_group_2 = egg_groups[1] if len(egg_groups) > 1 else ''
                abilities = profile.get('ability', [])
                ability_1_name = abilities[0][0] if abilities else ''
                ability_1_hidden = abilities[0][1] == 'true' if abilities else False
                ability_2_name = abilities[1][0] if len(abilities) > 1 else ''
                ability_2_hidden = abilities[1][1] == 'true' if len(abilities) > 1 else False
                gender_ratio = profile.get('gender', '')

                # Ottieni le immagini
                images = entry.get('image', {})
                sprite = images.get('sprite', '')
                thumbnail = images.get('thumbnail', '')
                hires_image = images.get('hires', '')

                # Crea un nuovo oggetto Pokemon nel database
                pokemon = Pokemon(
                    name_english=name_english,
                    name_japanese=name_japanese,
                    name_chinese=name_chinese,
                    name_french=name_french,
                    type_1=type_1,
                    type_2=type_2,
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_attack=sp_attack,
                    sp_defense=sp_defense,
                    speed=speed,
                    species=species,
                    description=description,
                    height=height,
                    weight=weight,
                    egg_group_1=egg_group_1,
                    egg_group_2=egg_group_2,
                    ability_1_name=ability_1_name,
                    ability_1_hidden=ability_1_hidden,
                    ability_2_name=ability_2_name,
                    ability_2_hidden=ability_2_hidden,
                    gender_ratio=gender_ratio,
                    sprite=sprite,
                    thumbnail=thumbnail,
                    hires_image=hires_image
                )
                pokemon.save()
                print(f"Pokemon {name_english} importato con successo.")
            except KeyError as e:
                print(f"Errore durante l'importazione di un Pokemon: {str(e)}")

if __name__ == '__main__':
    json_file_path = 'pokedex.json'  # Inserisci il percorso del tuo file JSON
    import_pokemon_from_json(json_file_path)
