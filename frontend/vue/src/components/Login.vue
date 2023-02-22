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
    <div class="text-right">
      <button type="button" class="btn btn-primary" @click="login">로그인</button>
    </div>
    <div v-if="token" id="token">{{ token }}</div>
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
        this.token = response.data.access;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
/* Insert your CSS styles here */
</style>
