class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        avg_salary = sum(salary[1:-1]) / len(salary[1:-1])
        return avg_salary
