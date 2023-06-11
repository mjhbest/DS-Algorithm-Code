class LinearProbing: 
    def __init__(self, size): # 생성자
        self.M = size
        self.a = [None for x in range(size+1)]  # 해시테이블
        self.d = [None for x in range(size+1)]  # key관련 데이터 저장

    def hash(self, key):
        return key % self.M  # 나눗셈 함수
    
    def put(self, key, data): # 삽입 연산
        ## [미션] ##
        initial_position = self.hash(key) # 초기 위치 
        i = initial_position
        j = 0
        while True:  
            if self.a[i] == None : # 삽입 위치 발견
                self.a[i] = key   # key를 해시테이블에 저장
                self.d[i] = data  # key관련 데이터 저장 
                return     
            if self.a[i] == key:  # 이미 key 존재하면
                self.d[i] = data  # 데이터만 갱신
                return
            j += 1                      
            i = (initial_position + j) % self.M # i의 다음 위치
            ## [미션] ##
            if i == initial_position:
                break         
           
    def get(self, key): # 탐색 연산
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None: # a[i]가 empty가 아니면
            if self.a[i] == key:
                return self.d[i] # 탐색 성공
            i = (initial_position + j) % self.M  # i의 다음 위치
            j += 1
            if i == initial_position: # i가 초기위치와 같으면 루프 종료
                return None # 탐색 실패                 
        return None # 탐색 실패


    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()
        
        
t = LinearProbing(13)

t.put(25, 'grape') 
t.put(37, 'apple')    
t.put(18, 'banana')
t.put(55, 'cherry')
t.put(22, 'mango')    
t.put(35, 'lime')       
t.put(50, 'orange')
t.put(63, 'watermelon')

print('탐색 결과:')
print('50의 data = ', t.get(50))
print('63의 data = ', t.get(63))

print('해시테이블:')
t.print_table() 

print('63의 data = ', t.get(63))
print("berry's hashed value : ",t.hash(9))
t.put(9, 'berry')
t.print_table()
