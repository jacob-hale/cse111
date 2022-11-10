import math

def main():
    # Sample = ["sample name", Radius (centimeters), Height (centimeters), Cost per Can (U.S. dollars)]
    Picnic = ["Picnic",6.83,10.16,0.28]
    Tall = ["Tall",7.78,11.91,0.43]
    two = ["2",8.73,11.59,0.45]
    twoplusalf = ["2.5",10.32,11.91,0.61]
    Cylinder = ["Cylinder",10.79,17.78,0.86]
    five = ["5",13.02,14.29,0.83]
    sixZ = ["6Z",5.40,8.89,0.22]
    eightZ_Short =["8Z short",6.83,7.62,0.26]
    ten = ["10",15.72,17.78,1.53]
    twoeleven = ['211',6.83,12.38,0.34]
    threedred = ['300',7.62,11.27,0.38]
    threezerothree = ["303",8.10,11.11,0.42]
    gigalist = [Picnic,Tall,two,twoplusalf,Cylinder,five,sixZ,eightZ_Short,ten,twoeleven,threedred,threezerothree]
    
    for i in gigalist:
        volume = compute_volume(i[1], i[2])
        surface_area = compute_surface_area(i[1], i[2])
        storage_efficiency = volume / surface_area
        print(f'{i[0]}: {storage_efficiency:.2f}')
    pass

def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main()