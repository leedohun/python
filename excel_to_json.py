import os
import json
import pandas

def e2j(xlsx_path, sheet): #excel_path, excel_sheet
    try:
        edf = pandas.read_excel(xlsx_path, sheet_name=sheet)
        ret = edf.to_json(orient='records') #ret : saved excel data
        f = open("excel_data.json".format(udf = userprofile, sheet = sheet), mode='wt', encoding='utf-8') #open json file
        f.write(ret) #write json file
        f.close()
        return
    except:
        raise Exception("error")
        
def j2p_l(path): #json_file_path
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)
        data = json.loads(json.dumps(json_data))
        return data #json_data
    except:
        raise Exception("error")

