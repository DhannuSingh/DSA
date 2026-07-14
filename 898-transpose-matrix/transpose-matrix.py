class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # zip(*matrix) unpacks the rows and groups elements by column index
        return [list(col) for col in zip(*matrix)]