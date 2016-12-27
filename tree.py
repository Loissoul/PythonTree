#coding=utf-8

#mac版
#windows只需要把/ 换成//
import os
class dir(object):
    def __init__(self):
        self.SPACE = ""
        self.list = []
    def getCount(self, url):
        files = os.listdir(url)
        count = 0;
        for file in files:
            myfile = url + "/" + file
            if os.path.isfile(myfile):
                count = count + 1
            return count

    def getDirList(self, url):
        files = os.listdir(url)
        fileNum = self.getCount(url)
        tmpNum = 0
        for file in files:
            myfile = url + "/" + file
            # size = os.path.getsize(myfile)
            if os.path.isfile(myfile):
                tmpNum = tmpNum + 1
                if (tmpNum != fileNum):
                    self.list.append(str(self.SPACE) + "├─" + file + "\n")
                else:
                    self.list.append(str(self.SPACE) + "└─" + file + "\n")

            if os.path.isdir(myfile):
                self.list.append(str(self.SPACE) + "├─" + file + "\n")
                self.SPACE = self.SPACE + "| "
                self.getDirList(myfile)
                self.SPACE = self.SPACE[:-4]
        return self.list

    def writeList(self, url):
        # print(self.list)
        f = open(url, 'w')
        f.writelines(self.list)
        f.close()

if __name__ == '__main__':
    url1 = os.getcwd()
    print (url1)
    d = dir()
    d.getDirList(url1)
    d.writeList(url1 + "/1.text")
    # d.getDirList("F:\PythonIde")
    # d.writeList("F:/1.text")
