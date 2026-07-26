class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        fleet = []

        for position, speed in sorted(cars, key=lambda x: x[0], reverse=True):
            time = (target - position) / speed
            if not fleet or (fleet and fleet[-1] < time):
                fleet.append(time)

        return len(fleet)
