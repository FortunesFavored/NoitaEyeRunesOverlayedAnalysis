from itertools import product
import eyeFolder.eyeGroups as eyeGroups

eyegroup = eyeGroups.eyeGroups

currentChar = 65
eyeGroupLetters = {
    '{0, 2, 3}': "S",
    '{0, 1}': "H",
    '{0, 1, 3}': "C",
}
eyeGroupingRandomLetters = {
    "east1":[],
    "west1":[],
    "east2":[],
    "west2":[],
    "east3":[],
    "west3":[],
    "east4":[],
    "west4":[],
    "east5":[],
}

avaricePoints = product(range(5), repeat=3)

avariceMem = {}
AVARICE = {}
avariceLetters = {}

x = list(avaricePoints)
for i in x:
    avariceMem[f"{i}"] = 0

trigramCount = 0

for location in eyegroup:
    # print(location)
    for eye in range(int(len(eyegroup[location])/3)):
        trigramCount += 1
        eyePos = eye*3
        # print(eyegroup[location][eyePos:eyePos+3])
        try:
            avariceMem[f'{set(eyegroup[location][eyePos:eyePos+3])}'] += 1
        except:
            avariceMem[f'{set(eyegroup[location][eyePos:eyePos+3])}'] = 1


characterCount = 0

for comboInfo in avariceMem.keys():
    if avariceMem[comboInfo] != 0:
        characterCount += avariceMem[comboInfo]
        AVARICE[comboInfo] = avariceMem[comboInfo]

print(sorted(AVARICE.items(), key=lambda x:x[1]))
print(characterCount)

# Change me to evaluate different eye message locations
location = 'east1'
for trigram in range(0, len(eyegroup[location]), 3):
    if str(set(eyegroup[location][trigram:trigram+3])) in list(eyeGroupLetters.keys()):
        eyeGroupingRandomLetters[location] += eyeGroupLetters[ f'{set(eyegroup[location][trigram:trigram+3])}' ]
    else:
        eyeGroupingRandomLetters[location] += eyegroup[location][trigram:trigram+3]

print("Raw Eye Trigrams")
print(eyegroup[location])
print("Eye Trigrams with assumed letters interweaved")
print(eyeGroupingRandomLetters[location])