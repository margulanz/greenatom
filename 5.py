class Version():
    def __init__(self,major = 0,minor = 0,patch = 0):
        self.major = major
        self.minor = minor
        self.patch = patch
    def __lt__(self,obj):
        if self.major>obj.major:
            return False
        else:
            if self.minor>obj.minor:
                return False
            else:
                if self.patch>obj.patch:
                    return False
                else:
                    return True
    def __gt__(self,obj):
        if self.major<obj.major:
            return False
        else:
            if self.minor<obj.minor:
                return False
            else:
                if self.patch<obj.patch:
                    return False
                else:
                    return True
    def __eq__(self,obj):
        return self.major == obj.major and self.minor == obj.minor and self.patch == obj.patch


def solution(A,B):
    a = Version(*A)
    b = Version(*B)
    if a == b:
        return 0
    elif a<b:
        return -1
    else:
        return 1

# Example
A = [1,2]
B = [1,2,3]
print(solution(A,B))
