import fire
import json
from numpy import mean, median, bincount, argmax


class VaultAnalyzer(object):
    """Analyzes vault files."""

    def analyze(self, file_name):

        with open(file_name) as vault_file:
            data = json.load(vault_file)
            # pprint(data['dwellers'])
            dweller_strengths = []
            dweller_perceptions = []
            dweller_endurances = []
            dweller_charismas = []
            dweller_intelligences = []
            dweller_agilities = []
            dweller_lucks = []
            lvl50_dwellers = []
            for i in data['dwellers']['dwellers']:
                dweller_strengths.append(i['stats']['stats'][1]['value'])
                dweller_perceptions.append((i['stats']['stats'][2]['value']))
                dweller_endurances.append((i['stats']['stats'][3]['value']))
                dweller_charismas.append((i['stats']['stats'][4]['value']))
                dweller_intelligences.append((i['stats']['stats'][5]['value']))
                dweller_agilities.append((i['stats']['stats'][6]['value']))
                dweller_lucks.append((i['stats']['stats'][7]['value']))
                if i['health']['lastLevelUpdated'] is 50:
                    lvl50_dwellers.append(i)
            print("#################### DWELLER MEAN SPECIALS ####################")
            print(f"Mean dweller strength: {mean(dweller_strengths)}")
            print(f"Mean dweller perception: {mean(dweller_perceptions)}")
            print(f"Mean dweller endurance: {mean(dweller_endurances)}")
            print(f"Mean dweller charisma: {mean(dweller_charismas)}")
            print(f"Mean dweller intelligence: {mean(dweller_intelligences)}")
            print(f"Mean dweller agility: {mean(dweller_agilities)}")
            print(f"Mean dweller luck: {mean(dweller_lucks)}")
            # -----------------------------------------------------------------
            print("################### DWELLER MEDIAN SPECIALS ###################")
            print(f"Median dweller strength: {median(dweller_strengths)}")
            print(f"Median dweller perception: {median(dweller_perceptions)}")
            print(f"Median dweller endurance: {median(dweller_endurances)}")
            print(f"Median dweller charisma: {median(dweller_charismas)}")
            print(f"Median dweller intelligence: {median(dweller_intelligences)}")
            print(f"Median dweller agility: {median(dweller_agilities)}")
            print(f"Median dweller luck: {median(dweller_lucks)}")
            # -----------------------------------------------------------------
            # https://stackoverflow.com/questions/6252280/find-the-most-frequent-number-in-a-numpy-vector
            print("#################### DWELLER MODE SPECIALS ####################")
            print(f"Mode dweller strength: {bincount(dweller_strengths).argmax()}")
            print(f"Mode dweller perception: {bincount(dweller_perceptions).argmax()}")
            print(f"Mode dweller endurance: {bincount(dweller_endurances).argmax()}")
            print(f"Mode dweller charisma: {bincount(dweller_charismas).argmax()}")
            print(f"Mode dweller intelligence: {bincount(dweller_intelligences).argmax()}")
            print(f"Mode dweller agility: {bincount(dweller_agilities).argmax()}")
            print(f"Mode dweller luck: {bincount(dweller_lucks).argmax()}")
            # -----------------------------------------------------------------
            print("################## LEVEL 50 DWELLERS & HEALTH ##################")
            print("10E -> 472.5")
            print("13E -> 546")
            print("14E -> 570.5")
            print("15E -> 595")
            print("17E -> 644")
            for i in lvl50_dwellers:
                print(f"Dweller: {i['name']} {i['lastName']}\
                \n\tMaxHealth: {i['health']['maxHealth']}\
                \n\tStrength: {i['stats']['stats'][1]['value']}\
                \n\tPerception: {i['stats']['stats'][2]['value']}\
                \n\tEndurance: {i['stats']['stats'][3]['value']}\
                \n\tCharisma: {i['stats']['stats'][4]['value']}\
                \n\tIntelligence: {i['stats']['stats'][5]['value']}\
                \n\tAgility: {i['stats']['stats'][6]['value']}\
                \n\tLuck: {i['stats']['stats'][7]['value']}\
                ")

if __name__ == '__main__':
    fire.Fire(VaultAnalyzer)
