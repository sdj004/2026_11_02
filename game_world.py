#world = [] #1차원 리스트

world = [ [], [] ] # world를 2차원 리스트로 만들기 / 0번 1번 레이어를 가지는 리스트

# 게임 월드에 객체 추가, layer를  지정해야 한다.
def add_object(o, depth = 0):
    world[depth].append(o)

# 게임 월드에서 객체 제거
def remove_object(o):
    for layer in world:
        if o in layer : 
            layer.remove(o)
            break # 더 이상 찾을 필요가 없기 때문에 종료, 최적화

# game logic
def update():
    for layer in world:
        for o in layer[:]:
            o.update()

#game rendering
def render():
    index = 0
    for layer in world:
        for o in layer:
            if index == 2 : o.draw(0, 20)
            else : o.draw(0, 0)
            index += 1