import os

def cmd(path, terraform_data):
    os.system("terraform -chdir={path} init".format(path=path))
    os.system("terraform -chdir={path} apply -var-file=vars.tfvars -auto-approve -state-out={path}/terraform_state.json".format(path = path))

    json_data = j2p_l('{path}/terraform_state.json'.format(path=path))

    if(json_data["output"] == None):
        os.system("[{now}]vm create done. [result : Failed, vm_name : {vmname}, error_msg : exception error for terraform] >> {result}/result.log".format(now=datetime.datetime.now(), vmname=terraform_data["vmname"], result=terraform_data["result_log_path"]))
    else:
        os.system("[{now}]vm create done. [result : SUCCESS, vm_name : {vmname}, vm_ip : {vmIp}] >> {result}/result.log".format(now=datetime.datetime.now(), vmname=terraform_data["vmname"], vm_Ip=json_data["output"]["instance_state"]["value"], result=terraform_data["result_log_path"]))
