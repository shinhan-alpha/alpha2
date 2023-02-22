<template>
  <div id="login-page">
    <div class="top">
          <div class="logo">
              <img src="../../../images/shinhan_ci.jpg">
          </div>
      </div>
      <div class="main">
          <h2>로그인</h2>
          <form>
              <input class="info" type="text" v-model="username" placeholder="아이디"><br><br>
              <input class="info" type="password" v-model="password" placeholder="비밀번호"><br><br>
              <input id="login" type="button" value="로그인" @click="login">
          </form>
      </div>
      <div class="bottom">
          <div class="logo">
              <img src="../../../images/shinhan_ad.png">
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
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
        location.href='/'
      } catch (error) {
        alert('로그인 실패');
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
  /* top */
  .top {
      text-align: center;
      margin-top: 10vh;
      display: table;
  }
  .logo img {
      max-width: 100%;
      max-height: 100%;
  }

  /* main */
  .main {
      top: 30%;
      width: 100%;
      text-align: center;
      background-color: #E8F1FE;
      border-radius: 20px;
      padding-top: 1vh;
      padding-bottom: 1vh;
  }
  .main h2 {
      text-align: left;
      padding-left: 5vh;
      margin-bottom: 0;
      color: #478BE1;
  }
  .main form {
      border-radius: 20px;
      padding: 10vw;
  }
  .main form input {
      width: 100%;
      height: 25px;
      font: 20px;
      background-color: #E8F1FE;
  }
  .main .info {
      border-top: 0px;
      border-right: 0px;
      border-left: 0px;
      border-bottom-style: #D3D6D9;
  }
  #login {
      border: none;
      background-color: #478BE1;
      color: white;
      border-radius: 20px;
      height: 7vh;
  }

  /* bottom */
  .bottom {
      text-align: center;
      display: table;
      margin-top: 57px;
  }
</style>