import pandas as pd
import pyperclip

# Store some static data as variables to make it easier to change later if need be
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
# sort data by timestamp
sorted_df = df.sort_values(by=["Timestamp"])
# export dataframe as .csv file
sorted_df.to_csv('csv/raidhelper.csv', index=False)

# read new csv file
f = pd.read_csv('csv/raidhelper.csv', usecols=['Name','Role','Spec'])

# iterate through csv and check each line for name, role, spec. Adds names and roles to URL generator.
for i in range(f['Name'].size):
    name = f['Name'][i]
    role = f['Role'][i]
    spec = f['Spec'][i]

    # Handle names and signup exceptions
    if role != 'Tentative' and role != 'Absence' and role != 'Late' and role != 'Bench':
        names = names + '(' + str(i + 1) + ') ' + name + ';'
    if role == 'Tentative':
        names = names + '(' + str(i + 1) + ') ' + name + ' (T);'
    if role == 'Late':
        names = names + '(' + str(i + 1) + ') ' + name + ' (L);'
    if role == 'Bench':
        names = names + '(' + str(i + 1) + ') ' + name + ' (B);'

    # Druids
    if spec == 'Balance':
        roles = roles + balanceDruidChar
    if spec == 'Feral' or spec == 'Guardian':
        roles = roles + feralDruidChar
    if spec == 'Restoration':
        roles = roles + restoDruidChar

    # Rogues
    if spec == 'Assassination':
        roles = roles + assassinationRogueChar
    if spec == 'Combat':
        roles = roles + combatRogueChar
    if spec == "Subtlety":
        roles = roles + subRogueChar

    # Hunters
    if spec == 'Beastmastery':
        roles = roles + beastMasterHunterChar
    if spec == 'Marksman':
        roles = roles + marksHunterChar
    if spec == 'Survival':
        roles = roles + survHunterChar

    # Shamans
    if spec == 'Elemental':
        roles = roles + eleShamanChar
    if spec == 'Enhancement':
        roles = roles + enhShamanChar
    if spec == 'Restoration1':
        roles = roles + restoShamanChar

    # Mages
    if spec == 'Arcane':
        roles = roles + arcaneMageChar
    if spec == 'Fire':
        roles = roles + fireMageChar
    if spec == 'Frost':
        roles = roles + frostMageChar

    # Warlocks
    if spec == 'Affliction':
        roles = roles + affWarlockChar
    if spec == 'Demonology':
        roles = roles + demonWarlockChar
    if spec == 'Destruction':
        roles = roles + destroWarlockChar
        
    # Paladins
    if spec == 'Holy1':
        roles = roles + holyPaladinChar
    if spec == 'Protection1':
        roles = roles + protPaladinChar
    if spec == 'Retribution':
        roles = roles + retPaladinChar
        
    # Warriors
    if spec == 'Arms':
        roles = roles + armsWarriorChar
    if spec == 'Fury':
        roles = roles + furyWarriorChar
    if spec == 'Protection':
        roles = roles + protWarriorChar
        
    # Priests
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
