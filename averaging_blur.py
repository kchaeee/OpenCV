import cv2

# 이미지 읽기
image = cv2.imread("cafe.jpg")

# 평균 블러 적용
blurred = cv2.blur(image, (5, 5))  # (5, 5)는 커널 크기

# 원본 및 블러 처리된 이미지 표시
cv2.imshow("Original", image)
cv2.imshow("Blurred - Averaging", blurred)
cv2.waitKey()
cv2.destroyAllWindows()