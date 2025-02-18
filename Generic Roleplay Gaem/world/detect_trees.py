import cv2 as cv
import numpy as np

def non_max_suppression(boxes, overlap_thresh):
    if len(boxes) == 0:
        return []

    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    pick = []
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[:last]]

        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlap_thresh)[0])))

    return boxes[pick].astype("int")

# Read images
game_img = cv.imread('game_screenshot2.png')
tree_img = cv.imread('yellow_tree.png')

# Split the images into their color channels
game_img_b, game_img_g, game_img_r = cv.split(game_img)
tree_img_b, tree_img_g, tree_img_r = cv.split(tree_img)

# Perform template matching on each color channel
result_b = cv.matchTemplate(game_img_b, tree_img_b, cv.TM_CCOEFF_NORMED)
result_g = cv.matchTemplate(game_img_g, tree_img_g, cv.TM_CCOEFF_NORMED)
result_r = cv.matchTemplate(game_img_r, tree_img_r, cv.TM_CCOEFF_NORMED)

# Combine the results by taking the average
result = (result_b + result_g + result_r) / 3

# Visualize the result to determine a good threshold
cv.imshow('Matching Result', result)
cv.waitKey(0)
cv.destroyAllWindows()

# Define a threshold to consider a location as a match
threshold = 0.5  # Adjusted threshold
loc = np.where(result >= threshold)

# Create bounding boxes for all matches
boxes = []
for pt in zip(*loc[::-1]):
    boxes.append((pt[0], pt[1], pt[0] + tree_img.shape[1], pt[1] + tree_img.shape[0]))

boxes = np.array(boxes)
filtered_boxes = non_max_suppression(boxes, 0.3)

# Draw rectangles around the filtered matches
for (x1, y1, x2, y2) in filtered_boxes:
    cv.rectangle(game_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the final result
cv.imshow('Detected Trees', game_img)
cv.waitKey(0)
cv.destroyAllWindows()
