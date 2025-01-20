import time as t
import random as r

def strawberry_game(straw_player_object, friend_list, is_friend=False):
    ### is_friend=False => 실제 사용자
    ### is_friend=True => 컴퓨터 사용자
    straw_player = straw_player_object.name
    num=0
    
    print("\n========================================================\n")
    print('''
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠶⣦⣤⣀⡀⠀⢀⣴⠞⠻⣧⠀⠀⠀⠀⢀⣤⣶⣿⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠈⠙⠳⣾⡇⠀⠀⢹⡇⠀⣠⡴⠟⢉⣹⣿⡀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⡤⠖⠋⠙⢿⣆⠀⠉⠉⠒⢌⣳⡄⢀⠀⣷⣞⣥⠶⠛⠋⠉⠉⠀⠀⠀
        ⠀⠀⠀⠀⢀⡴⠋⠀⢀⠤⣦⠀⠙⠳⣤⣀⣀⣀⣙⣿⣼⣴⣿⠿⠗⠶⢶⣤⡀⠀⠀⠀⠀
        ⠀⠀⠀⣠⠏⠀⠀⠀⠸⠿⠋⠀⠀⣠⣾⠿⠋⠡⠼⠻⣿⣿⡿⢏⡉⠑⠢⡉⠻⢷⣤⣀⡀
        ⠀⠀⢠⠏⣠⠚⡷⠀⠀⠐⣤⣴⣾⠛⠁⠀⠀⢀⣤⡾⣿⡀⠉⢢⠙⢦⣤⣤⣤⣶⡿⠛⠁
        ⠀⢀⡏⠀⠛⠛⠁⠀⠀⣀⣀⠉⠛⠿⠿⠿⠿⠟⠋⠀⠸⣷⣤⡀⠣⠈⢿⣯⠁⠀⠀⠀⠀
        ⠀⣸⠁⠀⠀⠀⠀⠀⢰⣁⡼⠀⠀⠀⣀⣀⠀⠀⠀⠀⢀⡈⠻⠿⣶⣦⣼⣿⣇⠀⠀⠀⠀
        ⢀⡏⡴⢳⡄⠀⠀⠀⠈⠉⠀⠀⠀⣸⣅⣸⠆⠀⠀⢰⣇⣽⠀⠀⠀⠀⢠⠲⣿⡄⠀⠀⠀
        ⢸⠃⠿⠟⠀⠀⠀⠀⣴⠋⣧⠀⠀⠈⠉⠉⠀⠀⠀⠈⠛⠋⠀⠀⠀⠀⢸⣤⢿⡇⠀⠀⠀
        ⣾⠀⠀⠀⣠⣄⠀⠀⢻⡾⠃⠀⠀⠀⠀⢠⡤⣤⠀⠀⠀⠀⡴⠛⡦⠀⠈⠁⣾⠃⠀⠀⠀
        ⣿⠀⠀⢰⣧⣼⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿⣤⠞⠀⠀⠀⠀⢿⠾⠃⠀⢀⣼⠏⠀⠀⠀⠀
        ⣿⠀⠀⠀⠛⠁⠀⠀⠀⢠⠖⢲⠀⠀⠀⠉⠀⠀⠀⠀⢀⣀⡀⠀⢀⣴⠿⠁⠀⠀⠀⠀⠀
        ⣿⡄⢠⠤⡀⠀⠀⠀⠀⢺⣴⠟⠀⠀⣠⠖⢲⡄⠀⣰⣏⡸⢃⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀
        ⢻⣷⢸⣀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠶⠛⠀⠀⠈⣩⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⢿⣧⠉⠀⠀⡴⢳⠀⠀⢀⣴⢒⡆⠀⠀⠀⣠⣴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠈⠻⣷⣄⡀⠷⠛⠀⠀⠘⠿⣟⣡⣤⡶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠈⠛⠿⢷⣶⣶⣶⡾⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ''')
    t.sleep(1)
    print("{}님이 \"딸기게임\" 을 선택하셨습니다!🍓".format(straw_player))
    t.sleep(1)
    for friend in friend_list:
        t.sleep(0.5)
        print("{0}님 입장 하실게요~ 🍓".format(friend.name))
        num += 1
        
    ran_dead = r.randint(0,num-1)
    
    t.sleep(2)
    print("\n===================<🕹️  딸기게임의 규칙>==================\n")
    t.sleep(1)
    print("아이엠그라운드 박자 다들 아시죠?")
    t.sleep(1)
    print("딸기게임은 이 박자에 맞춰 \"딸기\"와 \"딸~기\"를 알맞게 말하는 게임인데요~")
    t.sleep(1)
    print("1박에는 짧게 '딸기', 2박에는 길게 '딸~기'를 외치면 됩니다!")
    t.sleep(1)
    print("🔄️ 8박(딸~기 딸~기)에 도달하면 reverse 딸기 게임으로(다시 7박으로~!) 돌아가요 🤠🔄️")
    t.sleep(1)
    print("박자에 맞춰 박수👏 와 딸기🍓 를 신나게 외쳐보아요~ 🎵")
    t.sleep(1)
    print("\n========================================================\n")
    t.sleep(2)

    if not is_friend:
        if num == 1:
            # 친구가 1명일 때
            t.sleep(1)
            print("👏👏👏 딸기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '👏👏 딸~기'):
                pass
            else:
                t.sleep(1)
                print("\n========================================================\n")
                print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏 딸기 딸~기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '딸~기 딸~기'):
                t.sleep(1)
                print("\n========================================================\n")
                t.sleep(1)
                print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
                t.sleep(1)
                print("\n========================================================\n")
            else:
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            answer = input('지금이에요!!🫵: ')
            if(answer == '👏 딸기 딸~기'):
                pass
            else: 
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏👏 딸~기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '👏👏👏 딸기'):
                pass
            else: 
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏👏 딸기 딸기..?")
            t.sleep(1)
            print("\n========================================================\n")
            print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(friend_list[ran_dead].name))
            t.sleep(1)
            print("🍓 딸기게임이 종료되었습니다.👏")
            t.sleep(1)
            return [friend_list[ran_dead]] # 성공 시 술마시기 pass!
        elif num == 2:
            # 친구가 2명일 때
            print("👏👏👏 딸기")
            t.sleep(1)
            print("👏👏 딸~기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '👏 딸기 딸~기'):
                pass
            else:
                t.sleep(1)
                print("\n========================================================\n")
                print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("딸~기 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏👏 딸기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '딸~기 딸~기 👏👏 딸~기'):
                pass
            else:
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("딸~기 딸~기 👏 딸기 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 딸~기 딸~기")
            t.sleep(1)
            print("\n========================================================\n")
            t.sleep(1)
            print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
            t.sleep(1)
            print("\n========================================================\n")
            t.sleep(1)
            print("딸~기 딸~기 👏 딸기 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏 딸~기")
            answer = input('지금이에요!!🫵: ')
            if(answer == '딸~기 딸~기 👏👏👏 딸기'):
                pass
            else: 
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("딸~기 딸~기")
            t.sleep(1)
            print("👏 딸기 딸~기")
            answer = input('지금이에요!!🫵: ')
            if(answer == '👏👏 딸~기'):
                pass
            else: 
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏👏 딸기 딸기..?")
            t.sleep(1)
            print("\n========================================================\n")
            print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(friend_list[ran_dead].name))
            t.sleep(1)
            print("🍓 딸기게임이 종료되었습니다.👏")
            t.sleep(1)
            return [friend_list[ran_dead]] # 성공 시 술마시기 pass!
        elif num == 3:
            # 친구가 3명일 때
            print("👏👏👏 딸기")
            t.sleep(1)
            print("👏👏 딸~기")
            t.sleep(1)
            print("👏 딸기 딸~기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '딸~기 딸~기'):
                pass
            else:
                t.sleep(1)
                print("\n========================================================\n")
                print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("딸~기 딸~기 👏👏👏 딸기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏 딸기 딸~기")
            t.sleep(1)
            answer = input('지금이에요!!🫵: ')
            if(answer == '딸~기 딸~기 딸~기 딸~기'):
                t.sleep(1)
                print("\n========================================================\n")
                t.sleep(1)
                print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
                t.sleep(1)
                print("\n========================================================\n")
            else:
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            answer = input('지금이에요!!🫵: ')
            if(answer == '딸~기 딸~기 👏 딸기 딸~기'):
                pass
            else: 
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("딸~기 딸~기 👏👏 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏👏 딸기")
            t.sleep(1)
            print("딸~기 딸~기")
            answer = input('지금이에요!!🫵: ')
            if(answer == '👏 딸기 딸~기'):
                pass
            else: 
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏👏 딸기 딸기..?")
            t.sleep(1)
            print("\n========================================================\n")
            print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(friend_list[ran_dead].name))
            t.sleep(1)
            print("🍓 딸기게임이 종료되었습니다.👏")
            t.sleep(1)
            return [friend_list[ran_dead]] # 성공 시 술마시기 pass!
    else:
        ### p != player(가상의 사용자)
        if num == 1:
            ran_choice_1 = r.randint(0,1)
            print("👏👏👏 딸기")
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_1==0):
                print('👏👏 딸~기🍓')
            else:
                print("👏 딸기 딸기..?")
                t.sleep(1)
                print("\n========================================================\n")
                print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            
            ran_choice_2 = r.randint(0,1)
            print("👏 딸기 딸~기")
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_2==0):
                print('딸~기 딸~기🍓')
                t.sleep(1)
                print("\n========================================================\n")
                t.sleep(1)
                print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
                t.sleep(1)
                print("\n========================================================\n")
            else:
                print("딸~기 👏👏👏 딸기!...")
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            
            ran_choice_3 = r.randint(0,1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_3==1):
                print('👏 딸기 딸~기🎵')
            else:
                print('딸~기 딸~기 .. 으갸갹...??!!??')
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("👏👏 딸기 딸기..?")
            t.sleep(1)
            print("\n========================================================\n")
            print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(friend_list[ran_dead].name))
            t.sleep(1)
            print("🍓 딸기게임이 종료되었습니다.👏")
            t.sleep(1)
            return [friend_list[ran_dead]] # 성공 시 술마시기 pass!
        elif num ==2:
            ran_choice_1 = r.randint(0,1)
            print("👏👏👏 딸기")
            t.sleep(1)
            print("👏👏 딸~기")
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_1==0):
                print('👏 딸기 딸~기🍓')
            else:
                print("👏👏 딸~기..?")
                t.sleep(1)
                print("\n========================================================\n")
                print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            
            ran_choice_2 = r.randint(0,1)
            print("딸~기 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏👏 딸기")
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_2==0):
                print('딸~기 딸~기 👏👏 딸~기!🍓')
            else:
                print("딸~기 딸~기 👏👏👏 딸기!...")
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print('딸~기 딸~기 👏 딸기 딸~기')
            t.sleep(1)
            print("딸~기 딸~기 딸~기 딸~기")
            t.sleep(1)
            print("\n========================================================\n")
            t.sleep(1)
            print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
            t.sleep(1)
            print("\n========================================================\n")
            t.sleep(1)
            print('딸~기 딸~기 👏 딸기 딸~기')
            t.sleep(1)
            print('딸~기 딸~기 👏👏 딸~기!')
            ran_choice_3 = r.randint(0,1)
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_3==1):
                print('딸~기 딸~기 👏👏👏 딸기')
            else:
                print('딸~기 딸~기 .. 으갸갹...??!!??')
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("딸~기 딸~기")
            t.sleep(1)
            print("👏 딸기 딸~기")
            t.sleep(1)
            ran_choice_4 = r.randint(0,1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_4==1):
                print('👏👏 딸~기!!')
            else:
                print("👏👏 딸기 딸기!!")
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏👏 딸기 딸기..?")
            t.sleep(1)
            print("\n========================================================\n")
            print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(friend_list[ran_dead].name))
            t.sleep(1)
            print("🍓 딸기게임이 종료되었습니다.👏")
            t.sleep(1)
            return [friend_list[ran_dead]] # 성공 시 술마시기 pass!
        elif num ==3:
            ran_choice_1 = r.randint(0,1)
            print("👏👏👏 딸기")
            t.sleep(1)
            print("👏👏 딸~기")
            t.sleep(1)
            print("👏 딸기 딸~기")
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_1==0):
                print('딸~기 딸~기🍓')
            else:
                print("👏👏 딸~기..?")
                t.sleep(1)
                print("\n========================================================\n")
                print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            
            ran_choice_2 = r.randint(0,1)
            print("딸~기 딸~기 👏👏👏 딸기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏 딸기 딸~기")
            t.sleep(1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_2==0):
                print('딸~기 딸~기 딸~기 딸~기!🍓')
                t.sleep(1)
                print("\n========================================================\n")
                t.sleep(1)
                print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
                t.sleep(1)
                print("\n========================================================\n")
            else:
                print("딸~기 딸~기 👏👏👏 딸기!...")
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            
            ran_choice_3 = r.randint(0,1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_3==1):
                print('딸~기 딸~기 👏 딸기 딸~기')
            else:
                print('딸~기 딸~기 .. 으갸갹...??!!??')
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            print("딸~기 딸~기 👏👏 딸~기")
            t.sleep(1)
            print("딸~기 딸~기 👏👏👏 딸기")
            t.sleep(1)
            print("딸~기 딸~기")
            
            ran_choice_4 = r.randint(0,1)
            print('지금이에요!!🫵: ')
            t.sleep(2)
            if(ran_choice_4==1):
                print('👏 딸기 딸~기')
            else:
                print("👏👏 딸기 딸기!!")
                t.sleep(1)
                print("\n========================================================\n")
                print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(straw_player))
                t.sleep(1)
                print("🍓 딸기게임이 종료되었습니다.👏")
                t.sleep(1)
                return [straw_player_object] # 실패 시 1잔
            t.sleep(1)
            print("👏👏 딸기 딸기..?")
            t.sleep(1)
            print("\n========================================================\n")
            print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(friend_list[ran_dead].name))
            t.sleep(1)
            print("🍓 딸기게임이 종료되었습니다.👏")
            t.sleep(1)
            return [friend_list[ran_dead]] # 성공 시 술마시기 pass!
            
