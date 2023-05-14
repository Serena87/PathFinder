from backend import get_arbetsuppgifter, get_egenskaper
import random

nyckelord_tasks = get_egenskaper()
nyckelord_attributes = get_arbetsuppgifter()

#print('Nyckelord arbetsuppgifter: ' + str(len(nyckelord_tasks)) + ' ord')
#print(nyckelord_tasks )
#print()
#print('Nyckelord egenskaper: ' + str(len(nyckelord_attributes)) + ' ord')
#print(nyckelord_attributes)

def list_mixer(list1, list2):
    list_mixed = []
    for x in range (len(list1)):
        list_mixed.append(list1[x])
    for y in range (len(list2)):
        list_mixed.append(list2[y])
    return list_mixed

#print()
nyckelord_mixed = list_mixer(nyckelord_tasks, nyckelord_attributes)
random.shuffle(nyckelord_mixed)
#print('Nyckelord blandat: ' + str(len(nyckelord_mixed)) + ' ord')
#print( nyckelord_mixed)

