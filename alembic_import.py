

import hou
import os


def alemebicPath():
    a = input('Enter Your Aelembic Path :- ')
    while a:
        break
    else:
        print('Please Run Again or Past Your Aelembic Path !!! ')

    return a
        

p = alemebicPath()


# ********** Create Houdini Nodes *******************

print('Node Created SuccesFully')

geo = hou.node('/obj').createNode('geo','Alembic_Import')

alembic = geo.createNode('alembic','Import_alembic')
alembic.parm('fileName').set(path)

unpack = geo.createNode('unpack')
unpack.setNextInput(alembic)

print('unpack geo success....')
# Find Groups names

# A:/Houdini_Projects/Test\Python_hip/test_obj_2.abc

groupList=[]
ungroup = unpack.geometry()
for group in ungroup.primGroups():
    groupList.append(group.name())
# print(groupList)

for blast in groupList:
    node = geo.createNode('blast',blast)
    node.parm('group').set(blast)
    node.parm('negate').set(1)
    node.setNextInput(unpack)
    print(node)


null = geo.createNode('null','OUT_GEO')
null.setRenderFlag(1)
null.setDisplayFlag(1)

geo.layoutChildren()


