import pandas as pd
import pyperclip

urlPrefix = 'https://tbc.wowhead.com/raid-composition'
names = ';'
roles = '#0'

balanceDruidChar = "x"
feralDruidChar = 'v'
restoDruidChar = 'w'

assassinationRogueChar = 'k'
combatRogueChar = 'j'
subRogueChar = 'm'

beastMasterHunterChar = 'C'
marksHunterChar = 'F'
survHunterChar = 'D'

eleShamanChar = 'r'
enhShamanChar = 't'
restoShamanChar = 's'

arcaneMageChar = 'd'
fireMageChar = 'b'
frostMageChar = 'c'

affWarlockChar = 'z'
demonWarlockChar = 'B'
destroWarlockChar = 'y'

holyPaladinChar = 'H'
protPaladinChar = 'J'
retPaladinChar = 'G'

armsWarriorChar = 'f'
furyWarriorChar = 'h'
protWarriorChar = 'g'

discPriestChar = 'n'
holyPriestChar = 'p'
shadowPriestChar = 'q'

# read_clipboard attempts to read whatever is in your
# clipboard in as a .csv file. It uses read_csv() under
# the hood.
df = pd.read_clipboard(sep=',')
# sort data by bedrooms
sorted_df = df.sort_values(by=["Timestamp"])
# export dataframe as .csv file
sorted_df.to_csv('csv/raidhelper.csv', index=False)

f = pd.read_csv('csv/raidhelper.csv', usecols=['Name','Role','Spec'])

for i in range(f['Name'].size):
    name = f['Name'][i]
    role = f['Role'][i]
    spec = f['Spec'][i]

    if role != 'Tentative' and role != 'Absence' and role != 'Late':
        names = names + name + ';'
    if role == 'Tank':
        if spec == 'Guardian':
            roles = roles + feralDruidChar
        if spec == 'Protection':
            roles = roles + protWarriorChar
        if spec == 'Protection1':
            roles = roles + protPaladinChar
    if role == 'Druid':
        if spec == 'Balance':
            roles = roles + balanceDruidChar
        if spec == 'Feral':
            roles = roles + feralDruidChar
        if spec == 'Restoration':
            roles = roles + restoDruidChar
    if role == 'Rogue':
        if spec == 'Assassination':
            roles = roles + assassinationRogueChar
        if spec == 'Combat':
            roles = roles + combatRogueChar
        if spec == "Subtlety":
            roles = roles + subRogueChar
    if role == 'Hunter':
        if spec == 'Beastmastery':
            roles = roles + beastMasterHunterChar
        if spec == 'Marksman':
            roles = roles + marksHunterChar
        if spec == 'Survival':
            roles = roles + survHunterChar
    if role == 'Shaman':
        if spec == 'Elemental':
            roles = roles + eleShamanChar
        if spec == 'Enhancement':
            roles = roles + enhShamanChar
        if spec == 'Restoration1':
            roles = roles + restoShamanChar
    if role == 'Mage':
        if spec == 'Arcane':
            roles = roles + arcaneMageChar
        if spec == 'Fire':
            roles = roles + fireMageChar
        if spec == 'Frost':
            roles = roles + frostMageChar
    if role == 'Warlock':
        if spec == 'Affliction':
            roles = roles + affWarlockChar
        if spec == 'Demonology':
            roles = roles + demonWarlockChar
        if spec == 'Destruction':
            roles = roles + destroWarlockChar
    if role == 'Paladin':
        if spec == 'Holy1':
            roles = roles + holyPaladinChar
        if spec == 'Protection':
            roles = roles + protPaladinChar
        if spec == 'Retribution':
            roles = roles + retPaladinChar
    if role == 'Warrior':
        if spec == 'Arms':
            roles = roles + armsWarriorChar
        if spec == 'Fury':
            roles = roles + furyWarriorChar
        if spec == 'Protection':
            roles = roles + protWarriorChar
    if role == 'Priest':
        if spec == 'Discipline':
            roles = roles + discPriestChar
        if spec == 'Holy':
            roles = roles + holyPriestChar
        if spec == 'Shadow':
            roles = roles + shadowPriestChar

pyperclip.copy(urlPrefix + roles + names)
print('The URL is now copied to your clipboard. Paste it into a web browser.')
print(urlPrefix + roles + names)