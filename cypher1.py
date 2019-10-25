from convert2cypher import *

#entity and node
vulnerability_entity = 'vulnerability'
cve_entity = 'cve'
dev_entity = 'device'
inf_entity = 'infection'


vul_name_node = 'vul_name_node'
link_node = 'link_node'
cvss_node = 'cvss_node'
dev_name_node = 'dev_name_node'
vendor_node = 'vendor_node'
version_node = 'version_node'

#relation
vul_has_name = 'vul_has_name'
vul_has_cve = 'vul_has_cve'
vul_from_link = 'source_file'
cve_has_cvss = 'cve_has_cvss'
vul_has_inf = 'vul_has_inf'
infected_device = 'infected_device'
infected_version = 'infected_version'
has_vendor = 'has_vendor'
has_infection = 'has_infection'

path = '/Users/huangyida/Desktop/大四上/row data/'
v = open(path+'newvul.csv','r')
vulf = csv.reader(v)
i = open(path+'newinf.csv','r')
inff = csv.reader(i)
f = open(path+'result.txt','w')

cve_dup = []
link_dup = []
for line in vulf:
    vul_id = 'vul_'+str(line[0])
    vul_name = str(line[1])
    cve_name = str(line[2])
    cvss = str(line[3])
    link = str(line[4])
    #vul entity
    f.writelines(create_node(vul_id,vulnerability_entity,['vul_node'],[vul_id]))
    #link node
    if link not in link_dup:
        f.writelines(create_node(ref(link),link_node,['source_file'],[sref(link)]))
    f.writelines(create_relation(vul_id,vul_from_link,[],[],ref(link)))
    #cve_entity
    if cve_name:
        f.writelines(create_node(ref(cve_name),cve_entity,['cve_node'],[cve_name]))
        # vul has_cve cve
        f.writelines(create_relation(vul_id, vul_has_cve, [], [], ref(cve_name)))
        #cvss node
        if cvss:
            f.writelines(create_node('cvss'+ref(cvss),cvss_node,['cvss_node'],['cvss'+cvss]))
            f.writelines(create_relation(ref(cve_name),cve_has_cvss,[],[],'cvss'+ref(cvss)))
    #vul_name_node
    f.writelines(create_node(ref('vul_'+vul_name),vul_name_node,['name'],[sref(vul_name)]))

    #vul has_vul_name
    f.writelines(create_relation(vul_id,vul_has_name,[],[],ref('vul_'+vul_name)))
    link_dup.append(link)
dev_dup = []
vendor_dup = []
for line in inff:
    inf_id = str(line[0])
    dev_name = str(line[1])
    vendor = str(line[2])
    version = str(line[3])
    vul_id = 'vul_'+str(line[4])

    #inf_entity
    f.writelines(create_node(inf_id,inf_entity,['ind_node'],[inf_id]))
    #vul has_infection
    if vul_id:
        if version:
            f.writelines(create_relation(vul_id, has_infection, 'infected_version', sref(version), inf_id))
        else:
            f.writelines(create_relation(vul_id,has_infection,[],[],inf_id))

    #infected_version
    # if version:
        # f.writelines(create_node(ref(version),version_node,['version_node'],[version]))
        # f.writelines(create_relation(inf_id,infected_version,[],[],ref(version)))

    #device_entity
    if dev_name:
        if dev_name not in dev_dup:
            f.writelines(create_node(ref('dev_'+dev_name),dev_entity,['dev_node'],[sref('dev_'+dev_name)]))
        f.writelines(create_relation(inf_id,infected_device,[],[],ref('dev_'+dev_name)))
        #vendor node
        if vendor:
            if vendor not in vendor_dup:
                f.writelines(create_node(ref('ved_'+vendor),vendor_node,['vendor_node'],[sref('ved_'+vendor)]))
            f.writelines(create_relation(ref('dev_'+dev_name),has_vendor,[],[],ref('ved_'+vendor)))
    dev_dup.append(dev_name)
    vendor_dup.append(vendor)
f.close()
v.close()

"""清空neo4j数据
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r
"""
