import os
import stat

localConfig = [
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\IMG",
        "projectPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML",
        "outputPath": "E:\\unusedrefer_img.txt",
        "type": ".png|.gif|.ico",
        "removeAppendix":False
    },
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML",
        "projectPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML",
        "outputPath": "E:\\unusedrefer_qml.txt",
        "type": ".qml",
        "removeAppendix":True
    },
]

def getFileNames(rootDir,typeItems,removeAppendix):
    list_dirs = os.walk(rootDir)
    fileNames = {}
    for root, dirs, files in list_dirs:
        for f in files:
            os.chmod(os.path.join(root, f), stat.S_IWRITE)
            for type in typeItems.split("|") :
                if os.path.join(root, f).find(type) != -1:
                    if removeAppendix and f.find(".") != -1:
                        fileWithoutAppendix = f[0:f.find(".")]
                        fileNames[fileWithoutAppendix] = os.path.join(root, f)
                    else :
                        fileNames[f] = os.path.join(root, f)
    return fileNames

def scanFile(projectDir,outputPath,fileNames):
    list_dirs = os.walk(projectDir)
    allFileContents = ""
    for root, dirs, files in list_dirs:
        for f in files:
            with open(os.path.join(root, f), "r+", encoding="utf8") as file:
                if f.find("qml.qrc") == -1 :
                    fileLines = file.readlines()
                    allFileContents += str(fileLines)
    unusedFiles = []
    for fileName in fileNames:
        if allFileContents.find(fileName) == -1:
            unusedFiles.append("unUsed fileName path:            "+ fileNames[fileName]+"\n")
    with open(outputPath, "w+", encoding="utf8") as unUsedFile:
        unUsedFile.seek(0)
        unUsedFile.truncate()
        unUsedFile.writelines(unusedFiles)

if __name__ == "__main__":
    for item in localConfig:
        fileNames = getFileNames(item["targetScanPath"], item["type"],item["removeAppendix"]);
        scanFile(item["projectPath"], item["outputPath"], fileNames)