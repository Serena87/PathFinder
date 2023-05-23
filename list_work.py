from backend import get_arbetsuppgifter, get_egenskaper
import random

nyckelord_tasks = get_egenskaper()
nyckelord_attributes = get_arbetsuppgifter()

def list_mixer(list1, list2):
    list_mixed = []
    for x in range (len(list1)):
        list_mixed.append(list1[x])
    for y in range (len(list2)):
        list_mixed.append(list2[y])
    return list_mixed

nyckelord_mixed = list_mixer(nyckelord_tasks, nyckelord_attributes)
random.shuffle(nyckelord_mixed)


