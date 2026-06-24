class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereqs = dict()
        prereqToCourses = dict()
        for course, prereq in prerequisites:
            if course not in courseToPrereqs:
                courseToPrereqs[course] = set()
            if prereq not in prereqToCourses:
                prereqToCourses[prereq] = set()
            courseToPrereqs[course].add(prereq)
            prereqToCourses[prereq].add(course)
        availableCourses = []
        for c in range(numCourses):
            if c not in courseToPrereqs:
                availableCourses.append(c)
        taken = 0
        while len(availableCourses)>0:
            course = availableCourses.pop()
            taken += 1
            if course not in prereqToCourses:
                continue
            for nextCourse in prereqToCourses[course]:
                courseToPrereqs[nextCourse].remove(course)
                if len(courseToPrereqs[nextCourse]) == 0:
                    availableCourses.append(nextCourse)
        return taken == numCourses
        
        
        