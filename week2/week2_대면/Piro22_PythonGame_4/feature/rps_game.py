def rps_game(current_player,available_names, is_friend=False):
    import time as t
    import random as r
    print("""
⡿⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⣗
⣿⣳⣟⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⢞⠝⢜⢟⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⣾⡽⡾⡧
⣳⣟⣾⣳⣟⣷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢝⠜⢔⢍⢪⣯⢷⣟⣷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⣷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⣻⢷⠫⢁⠙⣷⣟⡷⣟⣷⣟⡷⣟⡷⣟⡷⣟⡷⣟⣿⢽
⣞⣷⣻⣞⣷⣻⢾⣻⡽⣯⣟⣯⣟⣯⢿⡽⡑⡅⢇⢣⣪⢿⢝⢍⢆⠕⢽⣯⣟⣯⣟⣯⣟⡯⡟⡯⣣⢢⠍⢿⠽⣯⣟⣯⣟⣯⣟⣯⣟⣯⣟⣯⢟⣯⣟⣯⢿⠃⢂⠐⡀⣿⡞⠏⢁⠸⣞⣿⢽⣻⣽⣻⣽⣻⣽⢾⣏
⣽⣗⣿⣺⣗⣿⢽⡯⣟⣷⣻⢾⣽⢾⢻⢘⢌⢪⢊⣞⢎⢕⢢⠱⡘⣬⡿⣞⣷⣻⣞⡗⡕⢅⢇⠕⡜⢌⢧⡣⡣⠪⡷⣟⣾⣳⣟⣾⣳⣟⣾⡣⠐⢀⠹⡾⡏⡈⠄⠠⢸⠗⡁⠌⠠⢸⣻⣞⣿⢽⣞⣷⣻⢾⣽⣻⢮
⣾⣳⣟⣾⣳⡯⣿⢽⣻⢾⢹⠩⡪⡙⡜⣜⢔⢕⢯⠢⡱⡨⡢⣣⣿⢽⣽⣻⣞⡷⡏⢆⢣⢱⡘⡌⡎⣜⢴⠣⡪⣱⢱⢑⢿⣺⣗⣿⣺⣗⣿⡢⠈⠠⠀⢿⠅⡀⢂⢁⢏⠐⡀⠂⡂⡿⡚⢑⢻⣽⣻⢾⣽⣻⢾⡽⣗
⣾⣳⣟⣾⣳⢿⣽⣻⡽⡑⡌⢎⢢⢱⢘⠔⡇⢎⢢⠣⡱⡼⢾⣻⣞⣯⡷⣟⡾⣯⠣⡣⡱⡑⡌⡯⢮⢎⢣⠣⡱⡪⢢⢣⢫⢻⣞⣷⣻⣞⣷⡃⠨⠀⠅⢸⢀⠂⣐⠬⠀⡂⠐⣐⠎⠡⠐⢀⢽⣗⣿⢽⡾⣽⢯⣟⣗
⣾⣳⣟⣾⢽⣻⣞⣷⢣⢱⠸⡘⡌⢗⢵⠹⡑⢕⢅⢗⢍⢪⠢⣻⣞⡷⣟⣯⢿⣽⢜⢔⢱⢨⠢⡣⢻⢜⠴⡕⡝⢌⢮⢪⠢⣽⣗⣿⣺⣗⣿⡊⠠⠁⠌⢸⠀⡐⢀⠁⠣⢄⠕⠁⠄⠡⠈⣴⢟⢷⣻⣽⢯⡿⣽⣽⢮
⣺⣗⣿⣺⢿⡽⣾⣽⢸⢐⢕⠱⡸⡘⡜⡜⡸⡐⢵⡱⣘⢔⡝⡳⣯⡿⣽⣽⣻⣞⣧⠪⡢⡑⡕⢜⠔⡇⢇⢫⠪⡫⣪⢢⢽⣗⣿⣺⣗⣿⣺⠀⡁⠂⡁⡈⠦⠐⡀⠌⠠⠁⢣⠁⠌⡠⡝⠅⢂⣸⣟⡾⣯⣟⣷⣻⡽
⢷⣻⢾⡽⣯⣟⣷⣻⡎⡢⢣⢑⢕⢸⢸⢨⠢⡣⡱⡸⡱⢱⢘⡼⣯⣟⣷⣻⢾⡽⣎⢧⡪⡘⡌⡆⡣⡇⡣⡱⢡⠣⡊⣮⣟⣷⣻⣞⡷⣯⡇⠐⡀⠡⠀⠄⠸⡐⢀⠂⡁⠌⠀⠕⡜⢈⠀⡂⣖⣟⡾⣯⢷⣟⣾⣳⡯
⣻⣽⢯⣟⣷⣻⣞⣷⣝⢜⡌⡆⡣⡪⡣⡑⡕⡌⢆⢇⢧⣧⡷⣟⣷⣻⢾⡽⣯⣟⣿⣲⣍⠮⢆⡇⡎⡜⡌⢎⢜⣜⣾⣳⣟⣾⣳⢯⣟⡷⣧⢁⠐⡈⠄⠡⢘⠔⢀⠂⠄⢂⠁⡂⡐⣠⣲⣻⣽⡽⣯⢿⣽⣳⣟⣾⢽
⣾⡽⣯⡷⣟⣾⣳⣟⣾⢧⣇⢏⢎⡎⡜⡌⡆⢇⣣⣵⣻⣞⣯⣟⣷⣻⣽⢯⡷⣟⣾⣳⢿⣽⢶⣵⡽⣾⣺⣽⢯⡷⣟⣾⣳⣟⣾⣻⢷⣻⡋⠱⢄⡂⠌⠄⠅⠌⠠⢂⠡⠐⡐⣀⡾⣾⢽⣗⣯⡿⣽⣻⣞⣷⣻⡾⣏
⣷⣟⣯⡿⣽⢷⣯⡷⣟⣯⣟⣷⢷⣝⣾⢾⡾⣯⡷⣟⣾⣽⢾⣽⢾⣻⣞⣿⣻⣽⢷⣻⣟⣾⣻⣗⡿⣯⡷⣟⣯⡿⣯⡷⣟⣷⢯⣟⣯⣟⣷⣥⡂⡘⠸⢄⡑⠨⠨⡀⡂⣅⣶⣳⣟⣯⣿⡽⣾⣻⣽⢷⣯⢷⡿⣽⡗
⡿⣞⣷⣟⣿⣻⣞⡿⣯⡷⣿⡽⣯⢿⣞⣿⡽⣷⣟⣿⣳⣟⣯⡿⣯⢿⣞⡿⣾⡽⣿⡽⣾⢯⣷⣟⣯⣷⢿⣻⢷⣟⣯⡿⣯⢿⣽⢯⣷⣟⣷⢷⣿⣺⣬⡐⡩⣺⢶⡾⣽⣻⣾⣽⢾⣻⣞⣯⣿⣳⣟⡿⣞⣿⣽⢷⡯
⣿⣻⢷⣻⢷⣯⣷⢿⣯⢿⣳⣿⣻⣯⢿⣞⣿⣳⣟⣷⣻⣽⢷⣟⡿⣯⡿⣽⡷⣿⢷⣟⡿⣯⡷⣟⣷⣟⣿⡽⣿⣽⢾⣻⣽⢿⣽⣻⣗⣿⢾⣻⣾⣻⣞⣿⣽⡾⣟⡿⣯⡷⣿⣞⣿⢯⣯⡷⣿⣞⣯⡿⣯⡷⣟⣯⣗
          """)
    print("가위바위보 하나 빼기 1을 선택했군요")
    print("규칙을 설명해줄게요!")
    t.sleep(1)
    print("\n===================<🕹️  가위바위보 하나빼기 1 규칙>==================\n")
    
    print("가위바위보 하나빼기 1은 양손으로 가위, 바위, 보 중에 하나를 내고 전략적으로 한 손을 빼는 가위바위보 게임이에요!")
    print("먼저 대결할 한 명을 골라주세요~🤗")
    print("그 다음에 '가위바위보!'를 외치고 동시에 모두 양손으로 가위, 바위, 보 중 하나를 내요~! ✋✊🖐")
    print("이제, 하나빼기 1을 외치며 동시에 본인이 빼고 싶은 모양을 하나 선택해서 외칩니다!")
    print("게임 결과는 빼고 남은 손모양으로 결정돼요!")
    
    print("   예:")
    print("     - A: 가위, 바위 (보를 뺀다고 선언)")
    print("     - B: 바위, 보 (가위를 뺀다고 선언)")
    print("     → 남은 모양은 A(가위) vs B(보), 결과는 A 승리! 🎉")
    print("\n---\n")
    
    print("🎮 **승패 결정하기!**")
    print("- 가위, 바위, 보의 기본 규칙대로 승부를 결정합니다:")
    print("  - 가위 > 보")
    print("  - 바위 > 가위")
    print("  - 보 > 바위")
    print("- 만약 남은 모양이 서로 같으면 무승부! 다음 판으로 넘어갑니다~ 😊")
    print("\n---\n")
    
    print("🎮 **주의할 점!**")
    print("- 두 손의 모양이 같을 필요는 없어요! 예를 들어, 한 손은 가위, 다른 손은 보를 낼 수도 있답니다.")
    print("- 상대방이 어떤 모양을 빼고 싶어 할지 예측하는 게 승리의 포인트! 🕵️‍♀️")
    print("\n---\n")

    print("이제 다들 준비되셨죠?")
    print("**자, 가위바위보 하나빼기 1 시작해볼까요?! 🙌**")

    rps_list = ["가위", "바위", "보"]
    rps_players_name=[]
    for i in available_names:
        name=i.name
        rps_players_name.append(name)
    
    current_player_name=current_player.name

    if not is_friend:
        print("대결상대 후보를 알려줄게요-!")
        print(", ".join(rps_players_name))
        while True:     
            try:
                rps_enemy_name=input("후보 안에서 대결상대를 골라주세요!")
                if rps_enemy_name not in rps_players_name:
                    raise ValueError
                rps_enemy = next((player for player in available_names if player.name == rps_enemy_name), None)
                break  
            except ValueError:
                print("자리에 없는 사람이에요!! 다시 골라주세요")
            
        print("===================<🎮게임 시작!>===================")
        t.sleep(1)
     
        while True:
            try:
                rps_left, rps_right = input("가위바위보! 'ex) 가위 바위' 형식으로 입력해주세요: ").split()
                if rps_left not in ["가위", "바위", "보"] or rps_right not in ["가위", "바위", "보"]:
                    raise ValueError
                break
            except ValueError:
                print("입력 형식이 올바르지 않아요! '가위 바위'처럼 두 개의 값을 띄어쓰기로 구분해서 입력해주세요.😊")

        rps_enemy_left, rps_enemy_right=r.sample(rps_list,2)
        print(f"{rps_enemy_name}는 {rps_enemy_left} {rps_enemy_right}를 냈네요!!")

        while True:
            try:
                rps_final=input("하나빼기 1! 님길 손을 선택해주세요 ex)왼손: ")
                if rps_final not in ["왼손","오른손"]:
                    raise ValueError
                break  
            except ValueError:
                print("입력 형식이 올바르지 않아요! '왼손' 혹은 '오른손'을 입력해주세요😊")

        t.sleep(1)
        print("누가 뭘 냈을까요? 두구두구두구두구구")
        if rps_final=="왼손":
            rps_final=rps_left
        if rps_final=="오른손":
            rps_final=rps_right

        print(f"{current_player_name}는 {rps_final}를 냈어요.")
        rps_enemy_final=r.choice([rps_enemy_left, rps_enemy_right])
        print(f"{rps_enemy_name}는 {rps_enemy_final}를 냈어요.")

        rps_player_win=[("가위","보"),("보","바위"),("바위","가위")]
        rps_enemy_win=[("보","가위"),("바위","보"),("가위","바위")]

        t.sleep(1)
        if rps_final==rps_enemy_final:
            print("무승부입니다! 둘다 한한잔씩 마시세요.🍺")  
            return [ current_player ,rps_enemy]
        elif (rps_final,rps_enemy_final) in rps_player_win:
            print(f"{current_player_name} wins~")
            print(f"{rps_enemy_name}한잔하세요~")
            return[rps_enemy]
        elif (rps_final,rps_enemy_final) in rps_enemy_win:
            print(f"{rps_enemy_name} wins~")
            print(f"{current_player_name}한잔하세요~")
            return 1
        

    elif is_friend:
        rps_enemy_name=r.choice( rps_players_name)
        rps_enemy=next((player for player in available_names if player.name == rps_enemy_name), None)
        print( f"당신의 상대는 {rps_enemy_name}😱 ")

        t.sleep(1)
        print("===================<🎮게임 시작!>===================")

        t.sleep(1)
        print("가위바위보!")
        rps_left, rps_right=r.sample(rps_list,2)
        print(f"당신은 {rps_left} {rps_right}를 냈네요!!")

        rps_enemy_left, rps_enemy_right=r.sample(rps_list,2)
        print(f"{rps_enemy_name}는 {rps_enemy_left} {rps_enemy_right}를 냈네요!!")

        t.sleep(1)
  
        rps_final=r.choice([rps_left, rps_right])

        t.sleep(2)
        print("누가 뭘 냈을까요? 두구두구두구두구구")


        t.sleep(1)
        print(f"{current_player_name}는 {rps_final}를 냈어요.")
        rps_enemy_final=r.choice([rps_enemy_left, rps_enemy_right])
        print(f"{rps_enemy_name}는 {rps_enemy_final}를 냈어요.")

        rps_player_win=[("가위","보"),("보","바위"),("바위","가위")]
        rps_enemy_win=[("보","가위"),("바위","보"),("가위","바위")]

        t.sleep(1)
        if rps_final==rps_enemy_final:
            print("무승부입니다! 둘다 한잔씩 마시세요.🍺")  
            return [current_player ,rps_enemy]

        elif (rps_final,rps_enemy_final) in rps_player_win:
            print(f"{current_player_name} wins~")
            print(f"{rps_enemy_name}한잔하세요~")
            return [rps_enemy]
        elif (rps_final,rps_enemy_final) in rps_enemy_win:
            print(f"{rps_enemy_name} wins~")
            print(f"{current_player_name}한잔하세요~")
            return 1
        