class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x:x[1])
        units = 0
        boxesUsed = 0
        for box in boxTypes:
            if boxesUsed == truckSize: return units
            if boxesUsed + box[0] <= truckSize:
                units += box[1] * box[0]
                boxesUsed += box[0]
            elif boxesUsed + box[0] > truckSize:
                units += box[1] * (truckSize - boxesUsed)
                boxesUsed += truckSize - boxesUsed
        return units
