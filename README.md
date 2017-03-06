flask-socketio-test
===================

- flask-app : http://localhost:5000/
- socket-io-app http://localhost:5001/


#### 테스트 ####
- flask-app 에서 주문전송 버튼을 누르면 requests 로 socket-io-app 의 URL로 전송
- 해당 URL 에서 현재 연결되어 있는 클라이언트에서 emit 수행
