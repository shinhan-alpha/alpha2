<template>
  <div id="app">
      <h2>알파카트(일괄매수)</h2>
      <p>1001020-23203-2332 김신한</p>
      <p>가능금액: {{ amount }}원</p>
      <table>
          <thead>
          <tr>
              <th>선택</th>
              <th>종목</th>
              <th>현재가</th>
              <th>수량</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(stock, index) in stocks" :key="index">
              <td><input type="checkbox" v-model="stock.checked" @click="stockClick(stock)"></td>
              <td>{{ stock.name }}</td>
              <td>{{ stock.price }}</td>
              <td>
                <button type="button" @click="incrementQuantity(stock)">+</button>
                {{ stock.quantity }}
                <button type="button" @click="decrementQuantity(stock)">-</button>
              </td>
          </tr>
          </tbody>
      </table>

      <h2>주문금액(합계) <span id="myValue">{{checkedStockPricesSum}}</span></h2>
      <button type="button" @click="modal">
        <img id="buy" src="../../images/buy.png" alt="매수버튼"/>
      </button>
      <h2>주식 포트폴리오</h2>
      <Pie :data="chartData" :options="options" />
    
      <div style="margin:50px;"></div>
  </div>

</template>

<script>

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  name: 'App',
  components: {
    Pie
  },
  data() {
    return {
      stocks: [
      { name: "LG전자", price: "113,000", quantity: 1, checked: false },
      { name: "현대차", price: "179,200", quantity: 1, checked: false },
      { name: "삼성전자", price: "62,600", quantity: 1, checked: false },
      { name: "대우중공업", price: "100,000", quantity: 1, checked: false },
      ],
    }
  },
  computed:{
      checkedStocks() {
        if(this.stocks){
          return this.stocks.filter(stock => stock.checked);
        }
        return [];
    
  },
  chartData() {
    const checkedStocks = this.checkedStocks;
    const checkedStockNames = checkedStocks.map(stock => stock.name);
    const checkedStockPrices = checkedStocks.map(stock => Number(stock.price.replace(',', ''))*stock.quantity);
    const sum = checkedStockPrices.reduce((acc, val) => acc + val, 0);
    this.checkedStockPricesSum = sum;
    return {
      labels: checkedStockNames,
      datasets: [
        {
          backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
          data: checkedStockPrices
        }
      ],
      checkedStockPricesSum: 0,
    };
  }
  },
  methods: {
    stockClick(stock) {
      stock.checked = true;
    },
    incrementQuantity(stock) {
      stock.quantity += 1;
    },
    decrementQuantity(stock) {
      if (stock.quantity > 1){
        stock.quantity -= 1;
      }
    }
  }
}
</script>
<style scoped>
      table {
          border-collapse: collapse;
          width: 100%;
      }

      td {
          text-align: left;
          padding: 8px;
      }

      th {
          background-color: #333;
          color: white;
      }
      tr:nth-child(odd) {
          background-color: #a5a5a5;
      }
      tr:nth-child(even) {
          background-color: #f2f2f2;
      }

      input[type=checkbox] {
          cursor: pointer;
      }
      #buy{
        position: relative;
        max-width: 200px;
      }
</style>