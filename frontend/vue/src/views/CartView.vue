<template>
  <div id="app">
      <h2>알파카트(일괄매수)</h2>
      <div class="scrollable" ref="scrollable" v-on:scroll="handleScroll">
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
                <button type="button" @click="decrementQuantity(stock)">-</button>
                {{ stock.quantity }}
                <button type="button" @click="incrementQuantity(stock)">+</button>
              </td>
          </tr>
          </tbody>
      </table>
    </div>
      <div class="tabs">
        <div class="tab" @click="selectedTab = 'first'" :class="{ 'active': selectedTab === 'first' }">주식<br>포트폴리오</div>
        <div class="tab" @click="selectedTab = 'sec'" :class="{ 'active': selectedTab === 'sec' }">배당<br>포트폴리오</div>
        <div class="tab" @click="selectedTab = 'third'" :class="{ 'active': selectedTab === 'third' }">총자산<br>포트폴리오</div>
      </div>
      <div v-if="selectedTab == 'first'">
        <div style="display:inline-block; width:200px">
          <Pie :data="chartData" :options="options"/>
        </div>
        <div style="display:inline-block">
          기대수익률<br>
          {{ percent }}%<br><br>
          위험<br>
          {{ danger }}%<br><br>
        </div>
        <h2>주문금액(합계) <span id="myValue">{{checkedStockPricesSum}}</span></h2>
      </div>
      <div v-else-if="selectedTab == 'sec'">
        <Bar :data="divchartData" :options="options"/>
      </div>
      <div v-else-if="selectedTab == 'third'">
        <div style="display:inline-block; width:100px">
          <Pie :data="chartData" :options="options"/>
        </div>
        <div style="display:inline-block; width:100px">
          주식
        </div>
        <div style="display:inline-block; width:100px">
          <Pie :data="chartData" :options="options"/>
        </div>
      </div>
      <button type="button" @click="add" style="background-color:white">
        종목추가
      </button>
      <button type="button" @click="modal" style="background-color:skyblue">
        매수
      </button>
      <div style="margin:50px;"></div>
      
  </div>

</template>

<script>

import { Chart as ChartJS, ArcElement, Tooltip, Legend,Title,BarElement,CategoryScale,LinearScale } from 'chart.js'
import { Pie, Bar } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)
export default {
  name: 'App',
  components: {
    Pie, Bar
  },
  data() {
    return {
      categoryList: ['주식포트폴리오'],
      stocks: [
      { name: "LG전자", price: "113,000", quantity: 1, checked: false },
      { name: "현대차", price: "179,200", quantity: 1, checked: false },
      { name: "삼성전자", price: "62,600", quantity: 1, checked: false },
      { name: "대우중공업", price: "100,000", quantity: 1, checked: false },
      { name: "LG전자", price: "113,000", quantity: 1, checked: false },
      { name: "현대차", price: "179,200", quantity: 1, checked: false },
      { name: "삼성전자", price: "62,600", quantity: 1, checked: false },
      { name: "대우중공업", price: "100,000", quantity: 1, checked: false },
      ],
      selectedTab: "first",
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
  },
  divchartData() {
    // const checkedStocks = this.checkedStocks;
    // const checkedStockdiv = checkedStocks.map(stock => Number(dividend)*stock.quantity);
      return{
        labels: [ '01', '02', '03','04', '05', '06','07', '08', '09','10', '11', '12'],
        datasets: [
          {
            label:'Dividend',
            backgroundColor: '#f87979',
            data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11],
          }
        ]
      }
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
    },
    handleScroll() {
        const scrollable = this.$refs.scrollable;
        if (scrollable.scrollTop + scrollable.offsetHeight >= scrollable.scrollHeight) {
          console.log('맨 아래 도달');
        }
      }
  }
}
</script>
<style scoped>
.scrollable {
    height: 170px;
    overflow-y: scroll;
  }
 .tabs {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ccc;
  }
  
  .tab {
    padding: 10px;
    cursor: pointer;
  }
  
  .tab.active {
    background-color: #ccc;
  }
  
  .tab-content {
    margin-top: 10px;
  }
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
      button img{
        width: 100px;
        height: 30px;
        object-fit: cover;
      }
      #chart {
        display: inline-block;
      }
</style>
