'''
n unopened boxes with k figurines in each box. The boxes cannot be opened and hence, the order of the figurines 
in the boxes cannot be changed. A box cannot be rotated (because the figuribnes will be poitinting the wrong way)

Each figurine has a specific height ex: in a given box, the height of the figurines from left to right can be something
like 4 -> 5 -> 7. Note that the number of figurines in each box may vary, assume that no box will be empty.

What to to do: organize all the toy boxes such that they are arranged in non increasing order {or equal height) of
figurine heights from left to right. Note that this might not be possible depending on the type of input given. Write a
program that can determine if it is possible to arrange the boxe3s or not.

Input specification:
first line n = number of toy boxes
each one of the next lines: for each box, integer k = the number of figurines, followed by k integers giving the height
of each figurine seperated by a space from left to right
(all variables >= 1)
'''



n_boxes = int(input())
box_height_list = []
for i in range(n_boxes):
    box_height_list.append([int(element)for element in input().split()[1:]])

header_list = []

for box in box_height_list:
    if box == box.sort():
        print("We cannot sort the boxes 1")
        exit()
    header_list.append([box[0], box[-1]])

attempt_sorted = [header_list.pop(0)]

for box in header_list:
    if box[1] <= attempt_sorted[0][0]:
        attempt_sorted = box + attempt_sorted
    else:
        i = 0
        while True:
            if i + 1 == len(attempt_sorted):
                if box[0] >= attempt_sorted[-1][1]:
                    attempt_sorted.append(box)
                    break
                print("We cannot sort the boxes 2")
                exit()

            if box[0] >= attempt_sorted[i][1] and box[1] <= attempt_sorted[i+1][0]:
                attempt_sorted = attempt_sorted[:i] + box + attempt_sorted[i:]
                break
            i += 1

print("The boxes are sortable!")