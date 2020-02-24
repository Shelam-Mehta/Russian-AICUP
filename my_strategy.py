import model
import math


class MyStrategy:
    def __init__(self):
        pass

    def get_action(self, unit, game, debug):
        # Replace this code with your own
        def distance_sqr(a, b):
            return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
        def help(approach):
            if(approach is not None and (unit.health>80 or nearest_health is None))and unit.weapon is not None:
            #debug.draw(model.CustomData.Log("Nearest bullet velocity: {}".format(nearest_bullet.velocity)))
            #debug.draw(model.CustomData.Log("Nearest bullet position: {}".format(nearest_bullet.position)))
            #debug.draw(model.CustomData.Log("Nearest bullet distance: {}".format(distance_sqr(nearest_bullet.position,unit.position))))
            
                if(distance_sqr(approach.position,unit.position)<25):
                    '''
                    ind=0
                    yind=0
                    #target_pos.x=unit.position.x+2*nearest_bullet.position.x//abs(nearest_bullet.position.x)
                    for i in range(nearest_bullet.position.x,50*(nearest_bullet.velocity.x),nearest_bullet.velocity.x//abs(nearest_bullet.velocity.x)):
                        ind=i
                        yind=nearest_bullet.y/nearest_bullet.x()
                        if(game.level.tiles[int(i)][int((nearest_enemy.position.y-unit.position.y)*(i-unit.position.x)/(nearest_enemy.position.x-unit.position.x)+unit.position.y)]==model.Tile.WALL):

                    '''
                    if(approach.velocity.x>0):
                        left=approach.velocity.y/approach.velocity.x*(unit.position.x-.9-approach.position.x)+approach.position.y
                        if(left-(unit.position.y+1.8)>0):
                            jump=False
                            
                        else:
                            #target_pos.y=32
                            '''
                            if(game.level.tiles[int(unit.position.x)][int(unit.position.y-3.8)] == model.Tile.EMPTY):
                                jump=False
                            else:
                            '''
                            jump=True
                        
                    else:
                        right=approach.velocity.y/approach.velocity.x*(unit.position.x+.9-approach.position.x)+approach.position.y
                        if(right-(unit.position.y+1.8)>0):
                            jump=False
                        else:
                            #target_pos.y=32
                            '''
                            if(game.level.tiles[int(unit.position.x )][int(unit.position.y-3.8)] == model.Tile.EMPTY):
                                jump=False
                            else:
                            '''
                            jump=True
                    if(approach.velocity.y<0):
                        up=((unit.position.y+1.8-approach.position.y)/(approach.velocity.y/approach.velocity.x)+approach.position.x)
                        if(abs(up-(unit.position.x-.9))>abs(up-(unit.position.x+.9))):
                            velocity=-50
                        else:
                            velocity=50
                    else:
                        down=((unit.position.y-approach.position.y)/(approach.velocity.y/approach.velocity.x)+approach.position.x)
                        if(abs(down-(unit.position.x-.9))>abs(down-(unit.position.x+.9))):
                            velocity=-50
                        else:
                            velocity=50
                    return jump,velocity
        nearest_enemy = min(
            filter(lambda u: u.player_id != unit.player_id, game.units),key=lambda u: distance_sqr(u.position, unit.position),default=None)
        
        nearest_weapon = min(filter(lambda box: isinstance(box.item, model.Item.Weapon), game.loot_boxes),key=lambda box: distance_sqr(box.position, unit.position),default=None)
        nearest_health = min(
            filter(lambda box: isinstance(box.item, model.Item.HealthPack), game.loot_boxes),key=lambda box: distance_sqr(box.position, unit.position),default=None)
        f = sorted(filter(lambda box: isinstance(box.item, model.Item.Weapon), game.loot_boxes),key=lambda box: distance_sqr(box.position, nearest_enemy.position),reverse=True)
        farthest_weapon=nearest_enemy
        for i in f:
            if(distance_sqr(unit.position,i.position)<=distance_sqr(i.position,nearest_enemy.position)):
                farthest_weapon=i
                break

        nearest_bullet=min(
            filter(lambda u: u.player_id != unit.player_id, game.bullets),key=lambda u: distance_sqr(u.position, unit.position),default=None)

        def approachingbullet():
            nearest=sorted(game.bullets,key=lambda u: distance_sqr(u.position, unit.position))
            for bull in nearest:
                vec2=model.Vec2Double(0, 0)
                vec2.x=unit.position.x-bull.position.x
                vec2.y=unit.position.y-bull.position.y
                if vec2.x*bull.velocity.x+vec2.y*bull.velocity.y>0:
                    return bull
            return None



        target_pos =model.Vec2Double(0, 0)
        target_pos.x=unit.position.x
        target_pos.y=unit.position.y 
        if unit.weapon is None and nearest_weapon is not None:
            target_pos = nearest_weapon.position
        
        #debug.draw(model.CustomData.Log("unit pos: {}".format(unit.position)))
        #debug.draw(model.CustomData.Log("approaching bullet: {}".format(approachingbullet())))
        aim = model.Vec2Double(0, 0)
        reloadweapon=False
        shoot=True
        #jump=False
        swap=False
       
        plant=False
        
        
                
                
        trick=1
        #print('Walked_right=',unit.walked_right)
        #print('shoot=',unit.shoot)
        '''
        if(len(game.bullets)!=0):
            print(game.bullets[0].player_id)
        '''
        
        if unit.weapon is not None  and (nearest_health is None ):
            if(str(unit.weapon.typ)!='WeaponType.ROCKET_LAUNCHER' ):
                target_pos=farthest_weapon.position
                jump=True
            else:
                target_pos=nearest_enemy.position


        #print(unit.size)
        #gap=1
        
        if nearest_health is not None and unit.weapon is not None and  nearest_enemy.position.x-nearest_health.position.x!=0 and unit.health>=90:
            #print('bhai')
            target_pos=nearest_health.position
            trick=(nearest_enemy.position.x-nearest_health.position.x)//abs((nearest_enemy.position.x-nearest_health.position.x))
            if(unit.position.y!=target_pos.y):
                trick*=-1
            target_pos.x+=trick
        if(unit.health<90 and nearest_health is not None and unit.weapon is not None):
            #velocity=(target_pos.x - unit.position.x)
            target_pos=nearest_health.position
            #debug.draw(model.CustomData.Log("Health: {}".format(nearest_health.position)))            
        
        
        
            #print(nearest_weapon.item.weapon_type)
        
        if nearest_weapon is not None and unit.weapon is not None and (unit.health>80 or nearest_health is None):
            if (str(nearest_weapon.item.weapon_type)=='WeaponType.ROCKET_LAUNCHER' and str(unit.weapon.typ)!='WeaponType.ROCKET_LAUNCHER' ):
                target_pos=nearest_weapon.position
                swap=True
            elif(str(nearest_weapon.item.weapon_type)!='WeaponType.PISTOL' and str(unit.weapon.typ)=='WeaponType.PISTOL' ):
                target_pos=nearest_weapon.position
                swap=True

        if(unit.weapon is not None):
            if str(unit.weapon.typ)=='WeaponType.ROCKET_LAUNCHER'  and unit.health==100:
                target_pos=nearest_enemy.position

        flag=0
        
        mini=min(int(unit.position.x),int(nearest_enemy.position.x))
        maxi=max(int(unit.position.x),int(nearest_enemy.position.x))
        for i in range(mini+1,maxi):
            if(game.level.tiles[int(i)][int((nearest_enemy.position.y-unit.position.y)*(i-unit.position.x)/(nearest_enemy.position.x-unit.position.x)+unit.position.y)]==model.Tile.WALL):
                #print('wall')
                flag=1
                break
        if(flag==1):
            shoot=False
            reloadweapon=True
        #l=[i.player_id for i in game.units]
        #print(l)
        for i in game.units:
            if(i.player_id==unit.player_id and (unit.position.x!=i.position.x or unit.position.y!=i.position.y) and nearest_enemy.position.x!=unit.position.x):
                if(((nearest_enemy.position.y-unit.position.y)*(i.position.x-unit.position.x)/(nearest_enemy.position.x-unit.position.x)+unit.position.y)>=i.position.y and ((nearest_enemy.position.y-unit.position.y)*(i.position.x-unit.position.x)/(nearest_enemy.position.x-unit.position.x)+unit.position.y)<=i.position.y+2):
                    if(distance_sqr(unit.position,i.position)<distance_sqr(unit.position,nearest_enemy.position)):
                        shoot=False
                        debug.draw(model.CustomData.Log("Health{}".format(shoot)))
                        reloadweapon=True
            elif(i.player_id==unit.player_id and (unit.position.y!=i.position.y) and i.position.x==unit.position.x and nearest_enemy.position.x==unit.position.x):
                if(distance_sqr(unit.position,i.position)<distance_sqr(unit.position,nearest_enemy.position)):
                        shoot=False
                        debug.draw(model.CustomData.Log("Health{}".format(shoot)))
                        reloadweapon=True

        
        
        #print(target_pos)
        
        '''
        if nearest_enemy.weapon is not None and unit.weapon is not None:
            if str(nearest_enemy.weapon.typ)=='WeaponType.ROCKET_LAUNCHER' or str(unit.weapon.typ)=='WeaponType.ROCKET_LAUNCHER':
                if distance_sqr(nearest_enemy,unit)<5:
                    target_pos=(nearest_enemy.position+unit.position)%25  

        '''
        #print(game.level.tiles)
        jump = (target_pos.y != unit.position.y)
        velocity=(target_pos.x - unit.position.x)
        
        
        if target_pos.x > unit.position.x and game.level.tiles[int(unit.position.x + 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        elif target_pos.x < unit.position.x and game.level.tiles[int(unit.position.x - 1)][int(unit.position.y)] == model.Tile.WALL:
            jump = True
        elif(abs(velocity)<5):
            velocity=(velocity)*5
        if(abs(target_pos.x-unit.position.x)<=2 and target_pos.y+1<unit.position.y):
            jump=False
        
        if(velocity>0 ):
            for i in game.units:
                if((unit.position.x<i.position.x and unit.position.x+2>i.position.x )and ( abs(unit.position.y-i.position.y)<=3)):
                    if(game.level.tiles[int(i.position.x )][int(i.position.y-3.8)] == model.Tile.EMPTY):
                        debug.draw(model.CustomData.Log("jump"))
                        jump=True
                    
                    else:

                        jump=False
        else:
            for i in game.units:
                if((unit.position.x>i.position.x and unit.position.x-1.5<i.position.x )and abs(unit.position.y-i.position.y)<=3):
                    if(game.level.tiles[int(i.position.x )][int(i.position.y-3.8)] == model.Tile.EMPTY):
                        debug.draw(model.CustomData.Log("jump"))
                        jump=True
                
                    else:
                        jump=False

        #print(len(game.units))
        approach=approachingbullet()
        if approach is not None:
            if(help(approach) is not None):
                jump,velocity=help(approach)
                debug.draw(model.CustomData.Log("approach"))
        elif(nearest_bullet is not None):
            if(help(nearest_bullet) is not None):
                jump,velocity=help(nearest_bullet)
                debug.draw(model.CustomData.Log("NearestBullet"))
        

        debug.draw(model.CustomData.Log("Velocity: {}".format(velocity)))  
            
        
        
        
            
    

        #debug.draw(model.CustomData.Log("Target: {}".format(target_pos)))
        if nearest_enemy is not None:
            #if(nearest_enemy.walked_right==True):
            if velocity!=0:
                aim = model.Vec2Double(nearest_enemy.position.x- unit.position.x,nearest_enemy.position.y - unit.position.y)
                
            else:
                aim = model.Vec2Double(nearest_enemy.position.x- unit.position.x,nearest_enemy.position.y - unit.position.y)
        return model.UnitAction(
            velocity=velocity,
            jump=jump,
            jump_down=not jump,
            aim=aim,
            shoot=shoot,
            reload=reloadweapon,
            swap_weapon=swap,
            plant_mine=plant) 
