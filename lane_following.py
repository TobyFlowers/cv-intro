from numpy import sign


directions = {
    -1 : "right",
    1: "left",
    0 : "forward"

}

def get_lane_center(lane):
    if len(lane) % 2 == 0: 
        center_lane = lane[int((len(lane))/2) -1]
    else:
        center_lane = lane[int((len(lane) + 1)/2) - 1]
    #print(center_lane)

    center = (center_lane[0][1] + center_lane[1][1])/2 
    slope = (center_lane[0][0] + center_lane[1][0])/2 
    return (center, slope)

def recommend_direction(center, slope):
    # check if midpoint is in the center of the screen if so go forward 
    return directions[sign(slope)]