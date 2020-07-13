# Covid19_KST-Macro
 [KR] 한국 교육청 주관 코로나19 자가진단 매크로  
 대구광역시 교육청 사이트 기준으로 제작되어 타 시도 교육청 학생의 경우 제대로 동작하지 않을 수 있습니다.  
 버그는 본 레포지토리에 이슈를 남겨주시면 확인 후 처리합니다.

## 요구사항
 * [Chrome](https://www.google.com/chrome/)
 * [Chrome Web Driver](https://chromedriver.chromium.org/downloads)
   * 웹드라이버는 PATH에 추가하거나, 레포지토리 폴더에 같이 넣어야합니다.
   * 자신의 크롬 버전은 [chrome://version](chrome://version)으로 접속하면 볼 수 있습니다.
 * [Python3](https://python.org)
   * [Selenium](https://pypi.org/project/selenium/)

## 설정법
 1. 해당 레포지토리를 로컬로 다운로드 혹은 클론합니다.
 1. `config.inc.json` 파일을 복사하여 `config.json`을 만듭니다.
 1. [교육청 자가진단 홈페이지](https://eduro.dge.go.kr/hcheck/index.jsp)에 접속하여 자가진단 키를 취득합니다.
    - 본인 인증 후에 자가진단 문항이 있는 페이지의 url에서 `?k=` 뒤에 있는 것이 키값입니다.
    - `%2d`와 같은 문자가 있다면 디코딩해서 넣어야합니다.
    - 디코딩하는 가장 간단한 방법은 [구글 검색 url](https://www.google.com/search?q=)에 넣는 것입니다.
    - ?q= 뒤에 키값을 붙여넣으면 검색란에 디코딩된 키가 나옵니다.
 1. `config.json`의 `key` 항목의 값에 디코딩된 키를 작성합니다.
 1. `time` 항목의 값을 매크로를 실행할 시간으로 설정합니다.
    - 기본값은 `7`이며, 이는 매일 7시에 실행함을 의미합니다.
    - 시간은 24시간을 단위로 하나, 0시와 24시는 테스트가 되지 않았습니다.

## 실행법
 1. 파이썬으로 `loop.py` 파일을 실행합니다.
    - 일반적인 경우 레포지토리 폴더에서 다음 명령어를 입력하면 됩니다.
    - `python loop.py`
 1. 기다리면 설정한 시간이 될 때마다 매크로를 실행합니다.
    - 남은 시간이 1.5초 이상일 경우 남은 시간만큼 프로그램을 일시적으로 중단하며, 이는 버그가 아닙니다.

 - 한번만 실행하고 싶다면 키값을 설정한 후, `macro.py`을 실행하면 됩니다.
