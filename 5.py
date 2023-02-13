class Version():
  def __init__(self,s):
    self.version = self.convert(s if s[-1] == '.' else s+'.')
  def convert(self,s):
    tmp = ''
    ls = []
    for i in range(len(s)):
      if s[i] == '.':
        ls.append(int(tmp))
        tmp = ''
        continue
      tmp+=s[i]
    return ls
  def __eq__(self, obj):
    return self.version == obj.version
  def __le__(self,obj):
    l = min(len(self.version),len(obj.version))
    for i in range(l):
      if self.version[i]>obj.version[i]:
        return False
      
    return True
  def __ge__(self,obj):
    l = min(len(self.version),len(obj.version))
    for i in range(l):
      if self.version[i]<obj.version[i]:
        return False
      
    return True
  def __lt__(self,obj):
    l = min(len(self.version),len(obj.version))
    for i in range(l):
      if self.version[i]>obj.version[i]:
        return False
    if obj == self:
      return False
    return True
  def __gt__(self,obj):
    l = min(len(self.version),len(obj.version))
    for i in range(l):
      if self.version[i]<obj.version[i]:
        return False
    if self == obj:
      return False
    return True
    
'''
10.1 A
10.1.21 B

'''
A = Version('11.1.1')
B = Version('11.2')
print(A < B)
