from statistics import median_low

class FileParser:
  dataList=[]
  dateList=[]
  minPoint=()
  midPoint=()
  maxPoint=()

  def __init__(self,path):
    try:
      f = open(path,"r")
      if f.mode == 'r':
        fl = f.readlines() 
        for x in fl:
          self.parseData(x) 
        self.findStats()   
    except(FileNotFoundError):
      print('File Not Found')
    except(FileExistsError):
      print('File Does Not Exist')

  def parseData(self,line):
    try:
      old = float(self.findNumber(line,'Old=','(MBps)'))
      new = float(self.findNumber(line,'New=','(MBps)'))
      avg = (old+new)/2
      self.dataList.append(avg)
      self.parseDate(line)
    except(ValueError):
      pass

  def findNumber(self,string,numStart,numEnd):
    startIndex = string.index(numStart)+len(numStart)
    endIndex = string.index(numEnd,startIndex)
    return(string[startIndex:endIndex])

  def parseDate(self,line):
    date = self.findNumber(line,'',' LVL')
    self.dateList.append(date)
  
  def findStats(self):
    maxIndex = self.dataList.index(max(self.dataList))
    self.maxPoint = (self.dateList[maxIndex],self.dataList[maxIndex])
    minIndex = self.dataList.index(min(self.dataList))
    self.minPoint = (self.dateList[minIndex],self.dataList[minIndex])
    midIndex = self.dataList.index(median_low(self.dataList))
    self.midPoint = (self.dateList[midIndex],self.dataList[midIndex])
    
def main():  
  parsedFile = FileParser(r'parser\sample_log.txt')

  timeIndex = 0
  dataIndex = 1
  print('Max Avg Output stream: %s' %str(parsedFile.maxPoint[dataIndex]), " at %s" %str(parsedFile.maxPoint[timeIndex]))
  print('Min Avg Output stream: %s' %str(parsedFile.minPoint[dataIndex]), " at %s" %str(parsedFile.minPoint[timeIndex]))
  print('Mid Avg Output stream: %s' %str(parsedFile.midPoint[dataIndex]), " at %s" %str(parsedFile.midPoint[timeIndex]))
   
if __name__ == "__main__":
  main()
