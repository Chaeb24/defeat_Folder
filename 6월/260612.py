def solution(numbers, target):
    def dfs(depth, total):
        if depth == len(numbers):
            return 1 if total == target else 0

        return (
            dfs(depth + 1, total + numbers[depth]) +
            dfs(depth + 1, total - numbers[depth])
        )

    return dfs(0, 0)