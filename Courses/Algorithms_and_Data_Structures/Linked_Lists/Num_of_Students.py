class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hash = {}
        res = len(students)
        for n in students:
            if n not in hash:
                hash[n] = 0
            hash[n] += 1
        for n in sandwiches:
            if n in hash and hash[n] > 0:
                hash[n] -= 1
                res -= 1
            else:
                return res        
        return res


