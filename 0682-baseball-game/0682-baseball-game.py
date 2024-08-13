class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for char in operations:
            if char == 'D':
                # Double the last score and add to the record
                record.append(2 * record[-1])
            elif char == 'C':
                # Remove the last score
                record.pop()
            elif char == '+':
                # Add the sum of the last two scores
                record.append(record[-1] + record[-2])
            else:
                # Add the score as an integer to the record
                record.append(int(char))
        
        # Return the sum of all scores
        return sum(record)
