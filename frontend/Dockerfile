FROM node:14

WORKDIR /usr/src/app
COPY ./usr/src/app

RUN npm install
RUN npm build

# run은 도커의 이미지를 만듬
# cmd는 이미지를 실행시킴

CMD ["cp", "-r", "dist", "/usr/src/app/output"]