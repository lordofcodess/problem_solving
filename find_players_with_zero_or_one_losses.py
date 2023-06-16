class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    
        losses = {}  
    
        for match in matches:
            winner, loser = match
        
            if winner not in losses:
                losses[winner] = 0
        
            if loser not in losses:
                losses[loser] = 1
            else:
                losses[loser] += 1
    
        no_losses = [] 
        one_loss = []  
    
        for player, num_losses in losses.items():
            if num_losses == 0:
                no_losses.append(player)
            elif num_losses == 1:
                one_loss.append(player)
    
        no_losses.sort()
        one_loss.sort()
    
        answer = [no_losses, one_loss]
        return answer
