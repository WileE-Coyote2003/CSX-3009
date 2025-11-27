#Name:Thwin Htoo Aung
#ID:6612109
#Section:541
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
        
    H = int(data[0])
    L = int(data[1])
    
    # Cans not shot by Harry = Total cans - Cans shot by Harry
    # Total cans N = H + L - 1
    # Cans not shot by Harry = (H + L - 1) - H = L - 1
    
    cans_not_shot_by_harry = L - 1
    
    # Cans not shot by Larry = Total cans - Cans shot by Larry
    # Cans not shot by Larry = (H + L - 1) - L = H - 1
    
    cans_not_shot_by_larry = H - 1
    
    print(f"{cans_not_shot_by_harry} {cans_not_shot_by_larry}")

solve()

