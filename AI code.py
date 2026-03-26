# 1. 라이브러리 불러오기
from sklearn.linear_model import LinearRegression

# 2. 학습 데이터 만들기 (공부 시간 -> 점수)
# X: 공부 시간 (입력)
# y: 시험 점수 (정답)
X = [[1], [2], [3], [4], [5]]   # 시간
y = [50, 60, 70, 80, 90]        # 점수

# 3. AI 모델 만들기
model = LinearRegression()

# 4. 학습시키기
model.fit(X, y)

# 5. 예측하기 (6시간 공부하면?)
prediction = model.predict([[6]])

# 6. 결과 출력
print("6시간 공부하면 예상 점수:", prediction[0])
