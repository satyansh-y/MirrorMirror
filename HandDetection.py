import cv2 as cv, numpy as np

vid = cv.VideoCapture(1)

while True:
    ret, hand = vid.read()
    # hand = cv.imread("HandImage.jpeg")
    # handedited = cv.imread("HandImageEdited.jpg")
    convimg = cv.cvtColor(hand, cv.COLOR_BGR2HSV)
    low = np.array([0, 48, 80], dtype = "uint8")
    up = np.array([100, 255, 255], dtype = "uint8")
    skin_range = cv.inRange(convimg, low, up)
    appl_blur = cv.blur(skin_range, (2, 2))
    contour, hierarchy = cv.findContours(appl_blur, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(type(contour), type(hierarchy))
    appl_cont = max(contour, key = lambda x : cv.contourArea(x))
    cv.drawContours(hand, [appl_cont], -1, (0, 0, 255), 3)
    inter_hulls = cv.convexHull(appl_cont)
    cv.drawContours(hand, [inter_hulls], -1, (0, 255, 0), 3)
    inter_hulls = cv.convexHull(appl_cont, returnPoints = False)
    defx = cv.convexityDefects(appl_cont, inter_hulls)

    cnt = 0

    for i in range(defx.shape[0]):
        s, e, f, d = defx[i][0]
        s, e, f= tuple(appl_cont[s][0]), tuple(appl_cont[e][0]), tuple(appl_cont[f][0])
        a, b, c= np.sqrt((e[0] - s[0]) ** 2 + (e[1] - s[1]) ** 2), np.sqrt((f[0] - s[0]) ** 2 + (f[1] - s[1]) ** 2), np.sqrt((e[0] - f[0]) ** 2 + (e[1] - f[1]) ** 2)
        ang = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) 
        if ang <= np.pi / 2:
            cnt += 1
            cv.circle(hand, f, 4, [255, 0, 0], -1)
    if cnt > 0:
        cnt = cnt + 1
    cv.putText(hand, str(cnt), (0, 150), cv.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 255), 4, cv.LINE_AA)
    cv.imshow('frame', hand)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break