class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        stack = []
        fleet = 0

        cars = sorted(zip(pos, speed))

        for pos, speed in reversed(cars):
            time = (target - pos) / speed
            if not stack:
                fleet += 1
                stack.append(time)
            else:
                if stack[-1] >= time:
                    continue
                else:
                    fleet += 1
                    stack.append(time)

        return fleet