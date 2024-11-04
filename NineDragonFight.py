import random

class Tile:
    def __init__(self, number):
        self.number = number
        self.color = 'white' if number % 2 == 0 else 'black'

    def __str__(self):
        emoji = "⚪️" if self.color == 'white' else "⚫️"  # 이모지로 색상 표현
        return f"{emoji} {self.number}"

class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = [Tile(i) for i in range(1, 10)]  # 1 ~ 9 까지의 타일 
        self.round_points = 0  # 라운드 포인트 
        self.round_log = []  # 각 라운드마다의 기록

    def choose_tile(self):
        print(f"{self.name}, 손 패 : {[str(tile) for tile in self.tiles]}")
        choice = int(input(f"{self.name}, 패 선택 (1-9): "))
        chosen_tile = next(tile for tile in self.tiles if tile.number == choice)
        self.tiles.remove(chosen_tile)
        return chosen_tile

class AIPlayer(Player):
    def choose_tile(self):
        # 랜덤하게 고르는 AI
        random.seed(2024)
        chosen_tile = random.choice(self.tiles)
        self.tiles.remove(chosen_tile)
        return chosen_tile

def determine_winner(tile1, tile2):
    if tile1.number == tile2.number: # 무승부 
        return None  
    if tile1.number == 1 and tile2.number == 9: 
        return tile1
    elif tile1.number == 9 and tile2.number == 1:
        return tile2
    return tile1 if tile1.number > tile2.number else tile2

def play_game():
    player = Player("User")
    ai_player = AIPlayer("AI")
    current_player = random.choice([player, ai_player])
    match_log = [] 

    while player.tiles and ai_player.tiles:
        print(f"\n{current_player.name}'의 차례")
        
        tile1 = current_player.choose_tile()
        if current_player == ai_player: 
            if tile1.color == 'black':
                print("ai가 낸 색상 : ⚫️")
            else:
                print("ai가 낸 색상 : ⚪️")

        other_player = ai_player if current_player == player else player
        tile2 = other_player.choose_tile()
        if current_player == player: 
            if tile2.color == 'black':
                print("ai가 낸 색상 : ⚫️")
            else:
                print("ai가 낸 색상 : ⚪️")


        # 승자 결정 
        winner = determine_winner(tile1, tile2)
        if winner:
            current_player.round_points += 1  
            match_log.append(f"{current_player.name} : {tile1} , {other_player.name} : {tile2}.")
        else:
            print("무승부!")
            match_log.append(f"무승부 : {tile1} vs. {tile2}.")

        # Print round points for both players
        print(f"라운드 포인트 : {player.name}: {player.round_points}, {ai_player.name}: {ai_player.round_points}")
        print("====================================================================================")

        # Change current player for the next round
        current_player = other_player

    # 경기 결과 출력 
    print("\n게임 종료!")
    print(f"최종 라운드 포인트 : {player.name}: {player.round_points}, {ai_player.name}: {ai_player.round_points}")
    print("\n경기 기록: ")
    print("=" * 30)  
    for i, log in enumerate(match_log):
        print(f"Round {i + 1}:")
        print(f" - {log}")
        print("-" * 30)  
    print("=" * 30)  

if __name__ == "__main__":
    play_game()