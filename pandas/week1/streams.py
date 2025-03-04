current_streams = int(input())
stream_flow = []

for i in range(current_streams):
    flow = int(input())
    stream_flow.append(flow)

done = False
while not done:
    command = int(input())

    #End of splits and joins for the streams
    if command == 77:
        done = True

    #Split of streams 
    elif command == 99:
        pos_split = int(input())
        split_flow = int(input())
        inital_flow = stream_flow[pos_split - 1]
        stream_flow[pos_split - 1] = inital_flow * split_flow // 100
        stream_flow.insert(pos_split, inital_flow * (100 - split_flow) // 100)
    
    #Joining of streams
    elif command == 88:
        pos_join = int(input())
        join_flow = stream_flow[pos_join - 1] + stream_flow[pos_join]
        stream_flow[pos_join - 1] = join_flow
        stream_flow.pop(pos_join)

#Unpacking and print of streams
print(*stream_flow)
