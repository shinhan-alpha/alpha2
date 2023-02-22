<template>
    <div class="container">
      <div class="box" v-for="(item, index) in items" :key="index" :style="{ width: item + '%' }">{{ item }}</div>
    </div>
  </template>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 33.33%;
    margin: auto;
  }
  
  .box {
    height: 10px;
    border: 1px solid black;
    margin: 0;
  }
  </style>
  
  <script>
  export default {
    data() {
      return {
        price: 100, // 현재가
        items: [], // 1% 씩 커진 값이 들어갈 배열
      }
    },
    mounted() {
      // 1% 씩 커진 값들을 계산하여 items 배열에 추가합니다.
      for (let i = 1; i <= 100; i++) {
        this.items.push((this.price / 100) * i);
      }
    }
  }
  </script>
  