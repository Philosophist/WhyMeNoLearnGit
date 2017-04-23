from visual import *

wallWid = 24
wallDep = .2
wallHei = wallWid
ball1 = sphere(pos=vector(-5,4,0), radius=1, color=color.red, material = materials.bricks)
ball2 = sphere(pos=vector(-3,-4,0), radius=1, material = materials.BlueMarble)
ball3 = sphere(pos=vector(-3,3,-4), radius=1, color=color.green, material = materials.emissive)
ball4 = sphere(pos=vector(-1,0,5), radius=1, material = materials.silver)

op = .2

wallR = box(pos=vector(.5 * wallWid,0,0), size=vector(wallDep,wallWid,wallHei), axis = vector(-wallDep,0,0), color=color.white, opacity=op)
wallL = box(pos=vector(-.5 * wallWid,0,0), size=vector(wallDep,wallWid,wallHei), axis = vector(wallDep,0,0), color=color.white, opacity=op)
wallT = box(pos=vector(0,.5 * wallWid,0), size=vector(wallDep,wallWid,wallHei), axis = vector(0,-wallDep,0), color=color.white, opacity=op)
wallB = box(pos=vector(0,-.5 * wallWid,0), size=vector(wallDep,wallWid,wallHei), axis = vector(0,-wallDep,0), color=color.white, opacity=op)
wallBa = box(pos=vector(0,0,-.5 * wallHei), size=vector(wallDep,wallWid,wallWid), axis = vector(0,0,wallDep), color=color.white, opacity=op)
wallFr = box(pos=vector(0,0,.5 * wallHei), size=vector(wallDep,wallWid,wallWid), axis = vector(0,0,-wallDep), color=color.white, opacity=op)
    
dt = .05
ball1.velocity =  vector(2,3,1)
ball2.velocity =  vector(3,1,-2)
ball3.velocity =  vector(-3,-3,.5)
ball4.velocity =  vector(-2,-1,-3)

objArr = [ball1, ball2, ball3, ball4]
def sph2sph_collision(obj1,obj2):
    #print('sphere collision:',obj1.pos,obj2.pos)
    t = mag(obj1.pos-obj2.pos) / (2 * (mag(obj1.velocity - obj2.velocity) ))
    obj1.pos = obj1.pos - obj1.velocity * t
    obj2.pos = obj2.pos - obj2.velocity * t
    if mag(obj1.pos-obj2.pos) < obj1.radius + obj2.radius:
        obj1.pos = obj1.pos + obj1.velocity * t
        obj2.pos = obj2.pos + obj2.velocity * t
        t = (mag(obj1.pos-obj2.pos) + obj1.radius +obj2.radius) / (2 * (mag(obj1.velocity - obj2.velocity) ))
        obj1.pos = obj1.pos - obj1.velocity * t
        obj2.pos = obj2.pos - obj2.velocity * t
    v = obj1.velocity
    obj1.velocity = obj2.velocity
    obj2.velocity = v
    obj1.pos = obj1.pos + obj1.velocity * t
    obj2.pos = obj2.pos + obj2.velocity * t
    collision_check(objArr)

def sph2wall_collision_check(ball):
    if ball.pos.x > wallR.pos.x - wallDep - ball.radius:
        thresh = wallR.pos + .5 * wallR.axis
        t = mag(proj((thresh-ball.pos), norm(wallR.axis))) /  mag(proj(ball.velocity, norm(wallR.axis))) 
        ball.pos = ball.pos - ball.velocity * t
        ball.velocity.x = -ball.velocity.x
        ball.pos = ball.pos + ball.velocity * t
        collision_check(objArr)
    if ball.pos.x < wallL.pos.x + wallDep + ball.radius:
        thresh = wallL.pos + .5 * wallL.axis
        t = mag(proj((thresh-ball.pos), norm(wallL.axis))) /  mag(proj(ball.velocity, norm(wallL.axis))) 
        ball.pos = ball.pos - ball.velocity * t
        ball.velocity.x = -ball.velocity.x
        ball.pos = ball.pos + ball.velocity * t
        collision_check(objArr)
    if ball.pos.y > wallT.pos.y - wallDep - ball.radius:
        thresh = wallT.pos + .5 * wallT.axis
        t = mag(proj((thresh-ball.pos), norm(wallT.axis))) /  mag(proj(ball.velocity, norm(wallT.axis))) 
        ball.pos = ball.pos - ball.velocity * t
        ball.velocity.y = -ball.velocity.y
        ball.pos = ball.pos + ball.velocity * t
        collision_check(objArr)
    if ball.pos.y < wallB.pos.y + wallDep + ball.radius:
        thresh = wallB.pos + .5 * wallB.axis
        t = mag(proj((thresh-ball.pos), norm(wallB.axis))) /  mag(proj(ball.velocity, norm(wallB.axis))) 
        ball.pos = ball.pos - ball.velocity * t
        ball.velocity.y = -ball.velocity.y
        ball.pos = ball.pos + ball.velocity * t
        collision_check(objArr)
    if ball.pos.z < wallBa.pos.z + wallDep + ball.radius:
        thresh = wallBa.pos + .5 * wallBa.axis
        t = mag(proj((thresh-ball.pos), norm(wallBa.axis))) /  mag(proj(ball.velocity, norm(wallBa.axis))) 
        ball.pos = ball.pos - ball.velocity * t
        ball.velocity.z = -ball.velocity.z
        ball.pos = ball.pos + ball.velocity * t
        collision_check(objArr)
    if ball.pos.z > wallFr.pos.z - wallDep - ball.radius:
        thresh = wallFr.pos + .5 * wallFr.axis
        t = mag(proj((thresh-ball.pos), norm(wallFr.axis))) /  mag(proj(ball.velocity, norm(wallFr.axis))) 
        ball.pos = ball.pos - ball.velocity * t
        ball.velocity.z = -ball.velocity.z
        ball.pos = ball.pos + ball.velocity * t
        collision_check(objArr)
        
def collision_check(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1,len(arr)):
            if mag(arr[i].pos-arr[j].pos) < arr[i].radius + arr[j].radius:
                sph2sph_collision(arr[i],arr[j])
    for i in range(len(arr) ):
        sph2wall_collision_check(arr[i])

while 1:
    rate(200)
    ball1.pos = ball1.pos+ball1.velocity*dt
    ball2.pos = ball2.pos+ball2.velocity*dt
    ball3.pos = ball3.pos+ball3.velocity*dt
    ball4.pos = ball4.pos+ball4.velocity*dt
    collision_check(objArr)
