class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        num_of_prereqs = [0]*numCourses
        prereq_to_course = [[] for _ in range(numCourses)]
        for cp in prerequisites:
            course = cp[0]
            prereq = cp[1]
            num_of_prereqs[course]+=1
            prereq_to_course[prereq].append(course)
        q = deque()
        for i in range(numCourses):
            if num_of_prereqs[i]==0:
                q.append(i)
        course_order = []
        while q:
            course_taken = q.popleft()
            course_order.append(course_taken)
            for course in prereq_to_course[course_taken]:
                num_of_prereqs[course]-=1
                if num_of_prereqs[course]==0:
                    q.append(course)
        if len(course_order)==numCourses:
            return course_order
        else:
            return []


        