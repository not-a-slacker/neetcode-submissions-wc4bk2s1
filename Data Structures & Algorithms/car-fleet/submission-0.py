class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i],speed[i]))
        pos_speed.sort(key = lambda x : x[0])
        pos_speed = pos_speed[::-1]
        pos_speed_time = []
        pos_speed_time.append((pos_speed[0][0],pos_speed[0][1],(target - pos_speed[0][0])/pos_speed[0][1]))
        for i in range(1,len(position)):
            time = (target - pos_speed[i][0])/pos_speed[i][1]
            if time <= pos_speed_time[-1][2]:
                a = pos_speed_time.pop()
                pos_speed_time.append((pos_speed[i][0],pos_speed[i][1],a[2]))
            else:
                pos_speed_time.append((pos_speed[i][0],pos_speed[i][1],time))
        return len(pos_speed_time)