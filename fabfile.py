from fabric.api import run,env
import yaml

yaml_host_file="example.yml"

def get_data(yaml_host_file,expand=False):
    stream=open(yaml_host_file,'r')
    data=yaml.load(stream)
    stream.close()
    if expand is True:
        return data

    result={}
    for x in data:
        host=[]
        for j in data[x]:
            host.append(j)
        result[x]=host
    return result


env.roledefs=get_data(yaml_host_file)
env.hostData=get_data(yaml_host_file,True)

def _get_current_role():
    for role in env.roledefs.keys():
        if env.host_string in env.roledefs[role]:
            return role
    return None

def set_env():
    host=env.host_string
    role=_get_current_role()
    env.user=env.hostData[role][host]['user']
    env.password=env.hostData[role][host]['pass']

def deploy():
    set_env()
    run('ls -la /tmp/ | tail ')

