from collections import deque


def longestSubarray(nums, limit):
    maxDeque = deque()
    minDeque = deque()
    left = 0
    maxLength = 0

    for right in range(len(nums)):

        while maxDeque and nums[maxDeque[-1]] <= nums[right]:
            maxDeque.pop()
        maxDeque.append(right)

        # Maintain minDeque
        while minDeque and nums[minDeque[-1]] >= nums[right]:
            minDeque.pop()
        minDeque.append(right)

        # Check if the current window is valid
        while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
            left += 1
            # Remove indices that are out of the new window range
            if maxDeque[0] < left:
                maxDeque.popleft()
            if minDeque[0] < left:
                minDeque.popleft()

        # Update the maximum length of valid subarray
        maxLength = max(maxLength, right - left + 1)

    return maxLength


# Example usage:
nums = [8, 2, 4, 7]
limit = 4
print(longestSubarray(nums, limit))  # Output: 2
