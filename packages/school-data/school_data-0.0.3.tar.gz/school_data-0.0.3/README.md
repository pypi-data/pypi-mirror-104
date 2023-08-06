# SCHOOL📱

파이썬용 학생 학교 데이터 라이브러리 입니다.

- https://pypi.org/project/school_data
- https://github.com/cord0318/python_school_data

## 📥다운로드

윈도우나 리눅스의 터미널에서 다음과 같이 입력합니다.

```shell
pip install school_data
```

오류가 나는 경우, `python -m pip install --upgrade pip` 로 pip를 업데이트 해주세요.

## 🤖사용법

나이스 서버와 통신하는 기능이기 때문에, 비동기 처리를 추천드립니다.

```python
# 동기
import school
school.meal_data("B10", "7081423")

#school_meal_data("지역코드", "학교코드", "급식 코드", "날짜")
```

```python
# 비동기
import asyncio
import school
async def main():
    await school.asyncMealData("지역코드", "학교코드", "급식 코드", "날짜")
asyncio.get_event_loop().run_until_complete(main())
```

더 많은 기능이 있습니다!
- 학교 정보
- 학교 급식 정보
- 학원 정보 (추가 예정)

## ↩️리턴값

모든 리턴값은 Dict 로 반환됩니다.

```python
{"error":Boolen(True,False),"code":"처리코드(밑의 처리코드 종류 참조)","message":"해당 에러나, 성공 상황에 대한 설명",......}
```