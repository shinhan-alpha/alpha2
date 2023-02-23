<template>
    <div class="container">
      <div class="form-group mb-3">
        <label for="username">아이디</label>
        <input type="text" class="form-control" v-model="username" />
      </div>
      <div class="form-group mb-3">
        <label for="password">비밀번호</label>
        <input type="password" class="form-control" v-model="password" />
      </div>
      <div class="form-group mb-3">
        <label for="password_check">비밀번호 확인</label>
        <input type="password" class="form-control" v-model="password_check" />
      </div>
      <div class="form-group mb-3">
        <label for="tel">전화번호</label>
        <input type="text" class="form-control" v-model="tel" />
      </div>
      <div class="text-right">
        <button type="button" class="btn btn-primary" @click="login">확인</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

    export default {
      name: "SignupView",
      data() {
        return {
          username: "",
          password: "",
          password_check: "",
          tel: "",
        };
      },
      methods: {
        login() {
          if (this.password !== this.password_check) {
            alert("비밀번호 확인 오류");
            return;
          }
  
          const data = {
            username: this.username,
            password: this.password,
            password_check: this.password_check,
            tel: this.tel,
          };
  
          axios
            .post("http://34.64.108.15/api/member", data)
            .then(() => {
              alert("회원가입 완료!");
            })
            .catch((error) => {
              let errorMsg = "";
  
              if (error.response.data.password) {
                errorMsg += "비밀번호 오류";
              }
              if (error.response.data.username) {
                errorMsg += "\n아이디 오류";
              }
              if (errorMsg) {
                alert(errorMsg);
              }
            });
        },
      },
    };
  </script>
  