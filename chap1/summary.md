# Downloading Web Pages

<br>

- Web Browser: URL로 특정 되는 데이터를 보여주는 프로그램
- Web Browser Engineering의 첫 단계는 URL을 통해 서버로부터 데이터를 가져오는 것이다.

<br>

## Connecting to a server

<br>

### 브라우저가 서버와 연결되는 과정(TCP 과정은 생략)
- OS에 서버와의 통신을 요청
- OS는 DNS 서버에 호스트에 해당하는 IP 주소를 요청
- OS는 통신을 위해 어떤 하드웨어가 적절할지 결정(예를 들어 유선 or 무선)
  - `routing table` 사용
- `device driver`들에 의해 신호 전송
- 이렇게 전송된 신호는 여러 라우터들을 지나 목적지 IP로 이동
- 위와 같이 url을 통해 서버와 통신할 수 있도록 하는 프로그램으로 `telnet` `netcat` 등이 있다.

<br>

### 서버 통신 예시
- mac OS에서는 기본적으로 netcat 지원
- `nc -v` 커맨드로 사용
- `nc -v google.com 80` 커맨드로 google.com에 tcp 연결을 한 예시
  <img width="391" alt="스크린샷 2022-03-30 오후 9 27 45" src="https://user-images.githubusercontent.com/57767891/160834272-5da5e1a9-ae08-4147-824b-14be46054184.png">
  - 이 상태에서 http 요청 가능

<br>

## Requesting information

<br>

- 서버와 연결에 성공하면 브라우저는 데이터를 요청한다.
- 브라우저는 method와 path, HTTP 버전, header 등을 명시
  - path는 리소스의 위치를 의미
  - 필요시 body도 포함
- 서버는 Response Code 및 Response Description과 함께 응답한다.
  - 100s - informational messages
    - 서버가 요청을 받음
    - 클라이언트는 작업을 계속 진행
  - 200s - success
    - 요청에 대한 작업을 성공적으로 완료함
  - 300s
    - request에 대한 다음 액션을 유도(주로 redirect)
  - 400s - bad request
    - browser의 요청에 문제가 있음을 의미
  - 500s - server error
    - server에서 요청에 대한 처리가 정상적으로 이루어지지 않음을 의미
  - 서버의 응답도 header와 body를 포함
    - body의 형태는 Content-Type에 의해 결정됨  

<br>