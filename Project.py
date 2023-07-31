def Sort(arr,d):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        Sort(L,d)
 
        # Sorting the second half
        Sort(R,d)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i][d] <= R[j][d]:
                arr[k]= L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
class PointDatabase :
    def __init__(self,p,d=0):
        n=len(p)
        if(n%2==0):
            m=n//2 -1
        else:
            m=n//2
        self.left=None
        self.right=None
        p.sort(key=lambda x:x[d])
        self.val=p[m]
        d=(d+1)%2
        if m>0:
            self.left=PointDatabase(p[:m],d)
        if n-(m+1)>0:
            self.right=PointDatabase(p[m+1:],d)
        
    def preorder(self):
        root=self
        def printPreorder(root):
            if root:
                print(root.val)
                printPreorder(root.left)
                printPreorder(root.right)
        printPreorder(root)
    
    
    
    def searchNearby(self, q, d):
        root=self
        x1=q[0]-d
        x2=q[0]+d
        y1=q[1]-d
        y2=q[1]+d
        list=[(x1,x2),(y1,y2)]
        finallist=[]
        d=0
        def search(root,d):
            l=(d+1)%2
            if root is None:
                return
            if (root.val[d]>=list[d][0]) and (root.val[d]<=list[d][1]):
                # print(root.val,"kkkk")
                if(root.val[l]>=list[l][0] and root.val[l]<=list[l][1]):
                    temp=root.val
                    # print(temp,"jjjjjj")
                    finallist.append(temp)
                search(root.left,l)
                search(root.right,l)
            elif(root.val[d]<=list[d][0]):
                if(root.val[l]>=list[l][0] and root.val[l]<=list[l][1] and root.val[d]==list[d][0]):
                    temp=root.val
                    # print(temp,"jjjjjj")
                    finallist.append(temp)
                search(root.right,l)
            elif(root.val[d]>=list[d][1]):
                if(root.val[l]>=list[l][0] and root.val[l]<=list[l][1] and root.val[d]==list[d][1]):
                    temp=root.val
                    # print(temp,"jjjjjj")
                    finallist.append(temp)
                search(root.left,l)
        search(root,d)
        return finallist
        
        
pointDbObject = PointDatabase([(1,6), (2,4), (3,7), (4,9), (5,1), (6,3), (7,8), (8,10),(9,2), (10,5)])
l=pointDbObject.searchNearby((4,8), 2)
print(l)



