import os
import stat

localConfig = [
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient",
        "projectPath" : "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\dy_PCClient.vcxproj",
        "outputPath" : "E:\\unused_cpp.txt",
        "type" : ".cpp"
    },
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML",
        "projectPath" : "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\QML\qml.qrc",
        "outputPath" : "E:\\unused_qml.txt",
        "type" : ".qml"
    },
    {
        "targetScanPath": "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\IMG",
        "projectPath" : "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient\IMG\img.qrc",
        "outputPath" : "E:\\unused_img.txt",
        "type" : ".png|.gif|.ico"
    },
]

def getFileNames(rootDir,typeItems):
    list_dirs = os.walk(rootDir)
    fileNames = {}
    for root, dirs, files in list_dirs:
        for f in files:
            os.chmod(os.path.join(root, f), stat.S_IWRITE)
            for type in typeItems.split("|") :
                if os.path.join(root, f).find(type) != -1:
                    fileNames[f] = os.path.join(root, f)
    return fileNames

def scanFile(filePath,outputPath,fileNames):
    if os.path.exists(filePath):
        with open(filePath, "r+", encoding="utf8") as file:
            fileLines = file.readlines()
            print(fileLines)
    unusedFiles = []
    for fileName in fileNames:
        isFound = False
        for line in fileLines:
            if(line.find(fileName) != -1):
                isFound = True
                break
        if isFound == False:
            unusedFiles.append("unUsed fileName path:            "+ fileNames[fileName]+"\n")
    with open(outputPath, "w+", encoding="utf8") as unUsedFile:
        unUsedFile.seek(0)
        unUsedFile.truncate()
        unUsedFile.writelines(unusedFiles)

if __name__ == "__main__":
    for item in localConfig:
        fileNames = getFileNames(item["targetScanPath"], item["type"]);
        scanFile(item["projectPath"], item["outputPath"], fileNames)