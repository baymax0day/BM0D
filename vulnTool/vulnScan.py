import os
import imp

file_path = os.path.split(os.path.realpath(__file__))[0] + "/"
def getModule():
    dirArr = []
    for dirname in os.listdir(os.path.realpath(file_path)):
        if not dirname.endswith(".py") and not dirname.endswith(".pyc"):
            dirArr.append(dirname)
    count = 0
    modSchema = {}
    for dirname in dirArr:
        dirMod = []
        for modName in os.listdir(os.path.realpath(file_path + dirname + '/')):
            if modName.endswith(".py") and not modName == '__init__.py':
                _module = imp.load_source("123",os.path.join(file_path + dirname + '/',modName))
                res = _module.get_plugin_info()
                if res:
                    res.update({"index":count})
                    count = count + 1
                    #tmp = {modName:res}
                    dirMod.append(res)
        #print(dirMod)
        modSchema.update({dirname:dirMod})

    # for i in modSchema["server"]:
    #     print(i["name"])

    return modSchema


def getModName():
    modNameList = []
    for dirname in os.listdir(os.path.realpath(file_path)):
        if not dirname.endswith(".py") and not dirname.endswith(".pyc"):
            for modName in os.listdir(os.path.realpath(file_path + dirname + '/')):
                if modName.endswith(".py") and  (modName not in ['__init__.py',"Config.py"]):
                    modNameList.append(os.path.realpath(file_path + dirname)  + '/' + modName)

    return modNameList