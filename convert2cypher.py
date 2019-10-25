import os
import re
import csv

def create_node(nid,entity,attr,attr_val):
    sp = 'CREATE ('
    sp += str(nid)+':'+entity
    sp += ' {'
    if len(attr):
        for i in range(len(attr)):
            if attr[i] and attr_val[i]:
                sp += str(attr[i])+':'
                sp += '\''+str(attr_val[i])+'\''
                if i != len(attr)-1:
                    sp += ','
    sp = sp.strip(',')
    sp += '})\n'
    return sp

def create_relation(nid,relation,attr,attr_val,tid):
    sp = 'CREATE\n  ('
    sp += str(nid)+')-[:'
    sp += str(relation)
    if len(attr):
        if len(attr_val):
            sp += ' {'
            sp += str(attr)+':[\''+str(attr_val)+'\''
            sp += ']}'
    sp+=']->('
    sp += tid+')\n'
    return sp

def ref(a):
    a = re.sub(r'\\|@|#|\$|%|\^|&|\*|\+|\.|!|/|,|\[|\]', '', a)
    a = re.sub(r' |\(|\)|-|;|:|\'|\"', '_', a)
    return a
def sref(a):
    a = re.sub(r'\\||@|#|\$|%|\^|&|\*|\+','',a)
    a = re.sub(r' |\|\)|-|\'|\"','_',a)
    a = re.sub(r':|;|,|\.|/|\\',' ',a)
    return a