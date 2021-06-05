def Download_File(url, path):
    r = req_get(url, allow_redirects=True)
    open(path, 'wb').write(r.content)

def file_download(file_inf):
    #os.path.isfile('{path}\\{file_name}') //path에 file_name이 존재하는지 확인
    if os.path.isfile("{folder}\\{file_name}".format(folder = path_list[file_inf["path_num"]], file_name = file_inf["file_name"]))==False:
        try:
            
            Download_File(url_list[file_inf["url_name"]], "{folder}\\{file_name}".format(folder = path_list[file_inf["path_num"]], file_name = file_inf["file_name"]))
        except:
            raise Exception(file_inf["error_code"])
    return
