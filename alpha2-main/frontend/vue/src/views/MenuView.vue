<template>
  <div class="container">
    <div class="back">
      <img src="../../../images/menu_tab.png">
    </div>
    <div id="menus">
      <span id="portfolio">포트폴리오</span>
      <button class="btn" id="create" onclick="location.href='./create';">포트폴리오 생성</button>
      <button class="btn" id="recommend" onclick="location.href='#';">포트폴리오 추천</button>
      <button class="btn" id="current" onclick="location.href='#';">포트폴리오 현황</button>
      <button class="btn" id="master" onclick="location.href='#';">고수의 포트폴리오</button>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios';

  export default {
    name:"menu",
    data() {
      return {
        username: '',
        password: '',
        token: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/token', {
            username: this.username,
            password: this.password,
          });
          localStorage.setItem("access_token", response.data.access)
          // this.token = response.data.access;
        } catch (error) {
          console.log(error);
        }
      },
    },
  };
</script>
  
<style>
  .back {
    position: absolute;
    left: 0px;
  }
  #menus {
      position: relative;
  }
  #portfolio {
      position: absolute;
      left: 118px;
      top: 103px;

      font-family: 'Inter';
      font-style: normal;
      font-weight: 700;
      font-size: 12px;
      line-height: 15px;
      display: flex;
      align-items: center;
      color: #000000;
  }
  #create {
      position: absolute;
      left: 112px;
      top: 136px;
  }
  #recommend {
      position: absolute;
      left: 112px;
      top: 167px;
  }
  #current {
      position: absolute;
      left: 112px;
      top: 198px;
  }
  #master {
      position: absolute;
      left: 112px;
      top: 229px;
  }
  .btn {
      border: none;
      background-color: white;
    
  }
</style>
  