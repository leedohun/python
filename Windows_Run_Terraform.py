import os

def cmd(item, result, path): #item : terraform data, result : result_log_path, path : terraform_data_path
    with open("{path}\\run.cmd".format(path = path),'w') as f:
        f.write("@echo off\n")
        f.write("{udf}\\Zconverter_TF\\terraform.exe -chdir={path} init\n".format(udf = userprofile, path = path))
        f.write("{udf}\\Zconverter_TF\\terraform.exe -chdir={path} apply -var-file=vars.tfvars -auto-approve -state-out={path}\\terraform.txt\n".format(udf = userprofile, path = path))
        f.write("type {path}\\terraform.txt |findstr \"instance_state\" >> {path}\\terraform_Check.txt\n".format(path = path))
        f.write("for /f ""tokens=1 delims= ""  %%i in ({path}\\terraform_Check.txt) do (\n".format(path = path))
        f.write("       type {path}\\terraform.txt |findstr \"value\" >> {path}\\terraform_Check_1.txt\n".format(path = path))
        f.write("       for /f ""tokens=2 delims"" %%j in ({path}\\terraform_Check_1.txt) do (\n".format(path = path))
        f.write("       	echo [%date% %time%]vm create done. (result : SUCCESS, vm_name : {vm_name}, vm_ip : %%j) >> {result}\n".format(result = result, vm_name = item["vmname"]))
        f.write("           exit\n")
        f.write("       )\n")
        f.write(")\n")
        f.write("echo [%date% %time%]vm create done. (result : FAILED, vm_name : {vm_name}, error_msg : exception error for terraform) >> {result}\n".format(result = result, vm_name = item["vmname"]))
    f.close()
    with open("{path}\\run.vbs".format(path = path),'w') as bf:
        bf.write("Set objShell = CreateObject(\"Shell.Application\")\nobjShell.ShellExecute \"{path}\\run.cmd\", \"/c lodctr.exe /r\" , \"\", \"runas\", 0".format(path = path))
    bf.close()
    os.system("start /b {path}\\run.vbs".format(path = path)) #terraform background 실행
