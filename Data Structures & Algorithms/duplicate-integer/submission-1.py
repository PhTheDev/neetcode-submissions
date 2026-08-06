class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listaOrdenada = sorted(nums)
        for i in range(len(listaOrdenada) - 1):
            if listaOrdenada[i] == listaOrdenada[i+1]:
                return True
            
        return False