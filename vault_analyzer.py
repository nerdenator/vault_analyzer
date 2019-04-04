from __future__ import print_function
import fire
import json
from numpy import mean, median, bincount, argmax

# for d e c r y p t i o n
# https://github.com/BlackthornYugen/FSCrypt/blob/master/FSCrypt.py
# ^ used with permission

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from base64 import decodestring, encodestring
from sys import stdin, stdout


class VaultAnalyzer(object):
    """Analyzes vault files."""

    @staticmethod
    def decrypt(file_name):
        # decryption
        INITIALIZATION_VECTOR = b'tu89geji340t89u2'
        PASSWORD = b'UGxheWVy'

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
            lvl50_15e_dwellers = []
            lvl50_lowh_dwellers = []
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
                    if i['health']['maxHealth'] >= 595:
                        lvl50_15e_dwellers.append(i)
                    if i['health']['maxHealth'] < 472.5:
                        lvl50_lowh_dwellers.append(i)

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
            self.print_dweller_stats(list_obj=lvl50_dwellers)
            self.print_dweller_stats(title="Over 15E Health:", list_obj=lvl50_15e_dwellers)
            self.print_dweller_stats(title='HP below 472.5:', list_obj=lvl50_lowh_dwellers)

    @staticmethod
    def print_dweller_stats(list_obj, title=None):
        if title:
            print(title)

        print(f"Total dwellers: {len(list_obj)}")
        for i in list_obj:
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
