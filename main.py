import pandas as pd
import pyperclip

# Store some static data as variables to make it easier to change later if need be
urlPrefix = 'https://tbc.wowhead.com/raid-composition'
names = ';'
roles = '#0'

# Druid
balanceDruidChar = "x"
feralDruidChar = 'v'
restoDruidChar = 'w'

# Rogue
assassinationRogueChar = 'k'
combatRogueChar = 'j'
subRogueChar = 'm'

# Hunter
beastMasterHunterChar = 'C'
marksHunterChar = 'F'
survHunterChar = 'D'

# Shaman
eleShamanChar = 'r'
enhShamanChar = 't'
restoShamanChar = 's'

# Mage
arcaneMageChar = 'd'
fireMageChar = 'b'
frostMageChar = 'c'

# Warlock
affWarlockChar = 'z'
demonWarlockChar = 'B'
destroWarlockChar = 'y'

# Paladin
holyPaladinChar = 'H'
protPaladinChar = 'J'
retPaladinChar = 'G'

# Warrior
armsWarriorChar = 'f'
furyWarriorChar = 'h'
protWarriorChar = 'g'

# Priest
discPriestChar = 'n'
holyPriestChar = 'p'
shadowPriestChar = 'q'

# read_clipboard attempts to read whatever is in your
# clipboard in as a .csv file. It uses read_csv() under
# the hood.
df = pd.read_clipboard(sep=',')
# sort data by timestamp
sorted_df = df.sort_values(by=["Timestamp"])
# export dataframe as .csv file
sorted_df.to_csv('csv/raidhelper.csv', index=False)

# read new csv file
f = pd.read_csv('csv/raidhelper.csv', usecols=['Name','Role','Spec'])

# iterate through csv and check each line for name, role, spec. Adds names and spec to URL generator. Each spec has a specific character used in
# wowheads raid composition tool
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
            
# Copy generated URL to clipboard
pyperclip.copy(urlPrefix + roles + names)

# Supplemental print to help the user understand what just happened
print('The URL is now copied to your clipboard. Paste it into a web browser.')
print(urlPrefix + roles + names)
