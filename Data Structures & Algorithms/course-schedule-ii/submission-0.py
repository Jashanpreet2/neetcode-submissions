class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrereq = dict()
        prereqToCourse = dict()
        for p in prerequisites:
            course, prereq = p
            if course not in courseToPrereq:
                courseToPrereq[course] = set()
            if prereq not in prereqToCourse:
                prereqToCourse[prereq] = set()
            courseToPrereq[course].add(prereq)
            prereqToCourse[prereq].add(course)
        order = []
        take = [i for i in range(numCourses) if i not in courseToPrereq]
        while len(take) > 0:
            prereq = take.pop()
            order.append(prereq)
            if prereq not in prereqToCourse:
                continue
            for course in prereqToCourse[prereq]:
                courseToPrereq[course].remove(prereq)
                if len(courseToPrereq[course]) == 0:
                    courseToPrereq.pop(course)
                    take.append(course)
            prereqToCourse.pop(prereq)
        return order if len(order) == numCourses else []

