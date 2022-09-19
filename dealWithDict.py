# 1. make dictionary
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72])) 
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})

# 2. if duplicated element?
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 3. 값에 접근
# lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# lux['health']
# lux['armor']

# 4. 할당
# lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
# lux['mana'] = 1184      # 키 'mana'의 값을 1184로 변경

# 5. in / not in
# 'health' in lux
# 'attack_speed' not in lux

# 6. pprint? => 딕셔너리를 읽기 쉽게 프린트해준다.
# from pprint import pprint as pp
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30,"dodo": [1,3,5,7], "mario": "pitch"}
# print(a)
# pp(a)
