

#                    ** author **
#                ** Parth Lathiya **
#    ** https://www.cse.iitb.ac.in/~parthiitb/ **

 
from numpy import genfromtxt
from itertools import chain,combinations

def powerset(s):
	s=list(s)
	return set(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

#Decodes integer to their corresponding objects/attributes
def decode(Encoded, Original):
    Decoded = []
    for i in Encoded:
        Decoded.append(Original[int(i-1)])
    if Decoded==[]:
        return 'PHI'
    try:
        Decoded=[int(x) for x in Decoded]
    except ValueError:
        pass
    return set(Decoded)

#Finds maximal possible subset for a given key
def GreatestLowerBound(key,DictForAttributeSubset):
    MaximalSubset = []
    for i in list(DictForAttributeSubset):
        if i==key :
            continue
        if set(DictForAttributeSubset[i])<set(DictForAttributeSubset[key]):
            MaximalSubset.append(i)
    temp = []
    for i in MaximalSubset:
        for j in MaximalSubset:
            if i!=j and set(DictForAttributeSubset[i])>set(DictForAttributeSubset[j]) and (i in MaximalSubset):
                temp.append(j)
    for i in temp:
        if i in MaximalSubset:
            MaximalSubset.remove(i)
    return MaximalSubset

#Objects satisfying the provided attribute
def ObjectsSatisfyingGivenAttributeSubset(InputData,SubsetOfAttributesList,TempObjects):
    Objects=[]
    for i in range(len(TempObjects)):
        flag=1
        for j in range(len(SubsetOfAttributesList)):
            if InputData[int(TempObjects[i])][int(SubsetOfAttributesList[j])]!=1:
                flag=0
        if flag==1:
            Objects.append(TempObjects[i])
    return Objects

#Read Access Matrix from in.txt
InputData = genfromtxt('in.txt', delimiter=' ')

f = open('in.txt', "r")
lines = f.read().split()

AttributesOriginal = list(lines[1:len(InputData[0])])

ObjectsOriginal = []
with open('in.txt','r') as f:
    for line in f:
        ObjectsOriginal.append(line.split()[0])
ObjectsOriginal.remove(ObjectsOriginal[0])

TempObjects = []
for i in range(len(InputData)-1):
    TempObjects.append(i+1)

#Encode objects as integers
DictOfObjects = {}
count = 1
for i in ObjectsOriginal:
    DictOfObjects[count] = i
    count += 1

TempAttributes = []
for i in range(len(InputData[0]) - 1):
    TempAttributes.append(i + 1)

#Encode attribute as integers
DictOfAttributes = {}
count = 1
for i in AttributesOriginal:
    DictOfAttributes[count] = i
    count += 1

SubsetOfAttributes = {}

SubsetOfAttributes = powerset(set(TempAttributes))

SubsetOfAttributesList = list(SubsetOfAttributes)

DictForAttributeSubset = {}
DictForObjectSubset = {}

for i in range(len(SubsetOfAttributesList)):
    DictForAttributeSubset[i] = SubsetOfAttributesList[i]
    DictForObjectSubset[i] = ObjectsSatisfyingGivenAttributeSubset(InputData, SubsetOfAttributesList[i], TempObjects)
    
for i in list(DictForAttributeSubset):
    if DictForObjectSubset[i] == [] and len(DictForAttributeSubset[i]) != len(TempAttributes):
        del DictForAttributeSubset[i]
        del DictForObjectSubset[i]

#Removed sets which are not Maximal
for k in sorted(DictForAttributeSubset, key = lambda k: len(DictForAttributeSubset[k]), reverse = True):
    for i in list(DictForAttributeSubset):
        if k in DictForAttributeSubset and DictForObjectSubset[k] == DictForObjectSubset[i] and set(DictForAttributeSubset[k]) > set(DictForAttributeSubset[i]):
            del DictForAttributeSubset[i]
            del DictForObjectSubset[i]

SortedAttributeSubsets = []
for k in sorted(DictForAttributeSubset, key = lambda k: len(DictForAttributeSubset[k])):
    SortedAttributeSubsets.append(k)

#Creating a dot file
print("digraph G { ranksep=\"1.2 equally\" nodesep=0.70 rankdir=\"BT\"; node [style=rounded]")

#Final nodes in the diagram
for i in SortedAttributeSubsets:
    print(str(i) + " [shape = box, color = lightseagreen, label = \""+str(decode(DictForObjectSubset[i], ObjectsOriginal)) + "\n" + str(decode(DictForAttributeSubset[i], AttributesOriginal)) + "\"];")    

#Connections in the diagram
for i in range(len(SortedAttributeSubsets)):
    GLB = GreatestLowerBound(SortedAttributeSubsets[i], DictForAttributeSubset)
    if GLB != []:
        for j in GLB:
            print(str(SortedAttributeSubsets[i] ) + " -> " + str(j) + " [style=bold, arrowhead=none, color=yellowgreen];")
            
print("}")
