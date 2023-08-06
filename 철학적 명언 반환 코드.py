from flask import Flask, jsonify
import sys
import random
application = Flask(__name__)


@application.route("/random", methods=["POST"])
def random_function():
    rand = random.randint(1, 12)
    if rand == 1:
        message = "네 의지의 준칙이 언제나 동시에 보편적 입법의 원리가 될 수 있도록 행위하라 - 칸트"
    elif rand == 2:
        message = "내일 지구가 멸망하더라도 오늘 한 그루 사과나무를 심겠다 - 스피노자"
    elif rand == 3:
        message = "너 자신을 알라 - 소크라테스"
    elif rand == 4:
        message = "이 인생을 기뻐하라. 즐겁게 살아가라 - 니체"
    elif rand == 5:
        message = "실존은 본질에 앞선다 - 사르트르"
    elif rand == 6:
        message = "언어는 존재의 집이다 - 하이데거"
    elif rand == 7:
        message = "하나의 유령이 유럽을 떠돌고 있다, 공산주의라는 유령이 - 마르크스"
    elif rand == 8:
        message = "미네르바의 부엉이는 황혼이 질 때만 날개를 편다 - 헤겔"
    elif rand == 9:
        message = "군자는 의(義)를 밝히고 소인은 이(利)를 밝힌다 - 공자"
    elif rand == 10:
        message = "도를 도라고 하면 이미 도가 아니다 - 노자"
    elif rand == 11:
        message = "말할 수 있는 것에 대해 분명히 말하고 말할 수 없는 것에 대해 침묵하라 - 비트겐슈타인"
    elif rand == 12:
        message = "아는 것에 의해서가 아니라 아는 것을 실천할 때 비로소 지혜로운 사람이 될 수 있다 - 아리스토텔레스"
    else:
        message = "오늘은 추천해드릴 명언이 떠오르지 않네요"
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str(message)
                    }
                }
            ]
        }
    }
    return jsonify(response)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)