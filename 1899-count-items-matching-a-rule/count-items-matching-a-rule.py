class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            rule_index = 0
        elif ruleKey == "color":
            rule_index = 1
        else:
            rule_index = 2

        return sum(1 for item in items if item[rule_index] == ruleValue)