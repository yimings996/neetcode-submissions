class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        pairs = []
        for i in range(len(position)):
             pairs.append((position[i], speed[i]))
        
        pairs.sort(key=lambda x: x[0])

        for i in range(len(pairs) - 1, -1, -1):
            pos, spee = pairs[i]
            time = ((target - pos)/spee)
            if not fleets:
                fleets.append(time)
            
            else:
                prev = fleets[-1]
                if time > prev:
                    fleets.append(time)
        

        return len(fleets)
