import random
import time

def number_game(current_player, flag, is_real_player=False,):
    """
    1~10 사이의 숫자를 맞추는 게임
    Args:
        current_player (Player): 현재 플레이어
        is_real_player (bool): 실제 플레이어인지 여부
    Returns:
        list: 술을 마셔야 하는 플레이어 리스트
    """
    
    if flag==0:
        print('''
    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗███████║██╔████╔██║█████╗  
    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        ''')
        time.sleep(0.5)
        print("\n===================<🕹️  숫자 맞추기 게임>===================")
        print("1부터 10 사이의 숫자를 맞춰보세요!")
        print("기회는 5번 있습니다.")
        print("기회를 모두 사용하면 1잔을 마셔야 합니다!")
        print("========================================================")

    target = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    previous_guesses = []
    
    while attempts < max_attempts:
        if not is_real_player:  # AI 플레이어
            time.sleep(1)
            if not previous_guesses:
                guess = random.randint(1, 10)
            else:
                min_val = max([g for g, r in previous_guesses if r == "Up"] + [1])
                max_val = min([g for g, r in previous_guesses if r == "Down"] + [10])
                guess = random.randint(min_val, max_val)
            print(f"\n{attempts + 1}번째 시도 - ", end="")
            time.sleep(0.5)
            print(f"{guess}!")
        else:  # 실제 플레이어
            try:
                guess = int(input(f"\n{attempts + 1}번째 시도 - 숫자를 입력하세요: "))
                if not 1 <= guess <= 10:
                    print("1부터 10 사이의 숫자를 입력해주세요!")
                    continue
            except ValueError:
                print("올바른 숫자를 입력해주세요!")
                continue
        
        attempts += 1
        
        if guess == target:
            print(f"\n🎉 정답입니다! {attempts}번 만에 맞추셨네요!")
            print(f"🎊 {current_player.name}님이 성공적으로 게임을 완료했습니다!")
            return []  # 성공: 아무도 마시지 않음
        
        elif guess < target:
            result = "Up"
            print("⬆️ Up! 더 큰 숫자입니다.")
        else:
            result = "Down"
            print("⬇️ Down! 더 작은 숫자입니다.")
            
        if not is_real_player:
            previous_guesses.append((guess, result))
            
        if attempts == max_attempts:
            print(f"\n❌ 기회를 모두 소진했습니다. 정답은 {target}였습니다!")
            print(f"🍺 벌칙: {current_player.name}(이)가 술 1잔을 마셔야 합니다!")
            return [current_player]  # 실패: 현재 플레이어만 마심
    
    return []  # 예외 상황 처리
