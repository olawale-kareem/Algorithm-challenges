# smiley face counter
def count_smileys(arr):
    # initiate a count variable
    # create the list of smiley faces possible
    # compare the list of smiley faces to the one given
    # return 1 for every valid combination found
    
    count = 0
    valid_smiley_faces = [":)",":-)",":~)",";)",";-)",";~)",":D",":-D",":~D",";D",";-D",";~D"]
    
    for smiley_faces in arr:
        if smiley_faces in valid_smiley_faces:
            count += 1
            
    return count