class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        total_energy = req_energy = req_exp = 0

        for i in energy:
            total_energy += i

        if initialEnergy <= total_energy:
            req_energy = (total_energy - initialEnergy) + 1

        totalExperience = initialExperience

        for i in experience:

            if totalExperience > i:
                totalExperience += i
            else:

                totalExperience -= req_exp
                # req_exp += (i - totalExperience) + 1
                req_exp = (i - totalExperience) + 1

                totalExperience += req_exp + i

        hours_required = req_energy + req_exp

        return hours_required