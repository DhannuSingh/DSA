class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        initial_satisfied = 0
        max_extra_satisfied = 0
        current_extra_satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                initial_satisfied += customers[i]
            else:
                current_extra_satisfied += customers[i]
                
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_extra_satisfied -= customers[i - minutes]
                    
            max_extra_satisfied = max(max_extra_satisfied, current_extra_satisfied)
            
        return initial_satisfied + max_extra_satisfied