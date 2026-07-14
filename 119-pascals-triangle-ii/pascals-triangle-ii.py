class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        current_val = 1

        for i in range(1, rowIndex + 1):
            # Calculate next combination element using long integer precision natively
            current_val = current_val * (rowIndex - i + 1) // i
            row.append(current_val)

        return row