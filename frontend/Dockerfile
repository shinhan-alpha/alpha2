FROM node:18

WORKDIR /usr/src/app
COPY vue /usr/src/app

RUN npm install
RUN npm run build

# run은 도커의 이미지를 만듬
# cmd는 이미지를 실행시킴

CMD ["cp", "-r", "dist", "/usr/src/app/output"]