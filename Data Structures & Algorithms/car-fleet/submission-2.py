class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        stack = []

        cars = sorted(zip(position, speed))

        for position, speed in reversed(cars):
            time = (target - position) / speed
            if not stack:
                stack.append(time)
                fleet += 1
            else:
                if time <= stack[-1]:
                    continue
                else:
                    fleet += 1
                    stack.append(time)
        
        return fleet