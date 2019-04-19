import os
import stat
targetScanPath = "E:\DouyuPC\ReleaseTemp\dy_pcclient\dy_PCClient"
class AddData:
    def __init__(self, str, lineNum):
        self.str = str
        self.lineNum = lineNum
    def getStr(self):
        return self.str
    def getLineNum(self):
        return self.lineNum
def scanFile(fileName):
    ColorButtonList = []
    with open(fileName, "r",encoding="utf8") as file:
        for lineNum,line in enumerate(file):
            result1 = line.find(":ColorButton")
            if result1 != -1:
                line = line.strip("\t\n ")
                # print(line)
                indexSpace = line.find(" ");
                ButtonDef = line[indexSpace+1:-13];
                # print(ButtonDef)
                addData = AddData(ButtonDef, lineNum)
                ColorButtonList.append(addData);
    with open(fileName, "r+", encoding="utf8") as file2:
        for lineNum,line in enumerate(file2):
             for addData in ColorButtonList:
                if line.find(addData.getStr())!= -1 and line.find("TOUCH_TAP")!= -1:
                    # print(addData.getStr())
                    line = line.replace("TOUCH_TAP", "TOUCH_RELEASE_OUTSIDE");
                    file2.writelines("\n" + line + "\n");
    if fileName.find("Panel") == -1:
        return
    fileNameStr = fileName.replace("Panel","Mediator");
    if not os.path.exists(fileNameStr):
        fileNameStr = fileName.replace(".ts","Mediator.ts");
    hasExist = False
    if os.path.exists(fileNameStr) :
        with open(fileNameStr, "r+",encoding="utf8") as file2:
             fileLines = file2.readlines()
             count = 0;
             for line in fileLines:
                 count += 1
                 for addData in ColorButtonList:
                     print(fileName)
                     if line.find(addData.getStr()) != -1 and line.find("TOUCH_TAP") != -1:
                        print(addData.getStr())
                        line = line.replace("TOUCH_TAP", "TOUCH_RELEASE_OUTSIDE");
                        fileLines.insert(count,line)
                        hasExist = True
             if hasExist:
                 file2.seek(0)
                 file2.truncate()
                 file2.writelines(fileLines)
def scanDir(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
                os.chmod(os.path.join(root, f), stat.S_IWRITE)
                scanFile(os.path.join(root, f))

if __name__ == "__main__":
    scanDir(targetScanPath);
