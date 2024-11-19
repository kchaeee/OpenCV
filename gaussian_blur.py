import cv2

# 이미지 읽기
image = cv2.imread("cafe.jpg")

# 가우시안 블러 적용
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)  # (5, 5)는 커널 크기, 0은 표준 편차

# 원본 및 블러 처리된 이미지 표시
cv2.imshow("Original", image)
cv2.imshow("Blurred - Gaussian", gaussian_blur)
cv2.waitKey()
cv2.destroyAllWindows()