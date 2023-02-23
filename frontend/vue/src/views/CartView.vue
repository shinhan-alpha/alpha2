<template>
  <div id="app">
      <h2>알파카트(일괄매수)</h2>
      <div class="scrollable" ref="scrollable" v-on:scroll="handleScroll">
      <table>
          <thead>
          <tr>
              <th style="position: sticky; top: 0;">선택</th>
              <th style="position: sticky; top: 0;">종목</th>
              <th style="position: sticky; top: 0;">현재가</th>
              <th style="position: sticky; top: 0;">수량</th>
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
        <Bar :data="divs" :options="divs.options" ref="barChart"/>
      </div>
      <div v-else-if="selectedTab == 'third'">
        <div style="display:inline-block; width:150px">
          <b>보유 포트폴리오</b>
          <Pie :data="chartData" :options="options"/>
        </div>
        
        <div style="display:inline-block; width:150px">
          <b>목표 포트폴리오</b>
          <Pie :data="darts" :options="options"/>
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
import axios from 'axios';
import dividend from "@/assets/dividend_3.json"
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
      dividend: dividend,
      categoryList: ['주식포트폴리오'],
      stocks: [
      { name: "신한지주", code: "055550", price: "39,050", quantity: 1, checked: false },
      { name: "LG전자", code: "066570", price: "113,000", quantity: 1, checked: false },
      { name: "현대차", code: "005380", price: "179,200", quantity: 1, checked: false },
      { name: "삼성전자", code: "005930", price: "62,600", quantity: 1, checked: false },
      { name: "대우중공업", code: "042670", price: "8,920", quantity: 1, checked: false },
      { name: "SK", code: "034730", price: "183,600", quantity: 1, checked: false },
      { name: "KT", code: "030200", price: "32,100", quantity: 1, checked: false },
      { name: "네이버", code: "035420", price: "213,000", quantity: 1, checked: false },
      ],
      selectedTab: "first",
      divs:{
        labels: [ '01', '02', '03','04', '05', '06','07', '08', '09','10', '11', '12'],
        datasets: [
          {
            label:'배당금',
            backgroundColor: 'red',
            data: [400, 200, 1200, 390, 100, 4000, 390, 800, 3000, 200, 120, 11000],
          },
          {
            label:'추가',
            backgroundColor: '#f87979',
            data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          },
        ],
        options: {
          responsive: true,
            scales: {
              x: {
                stacked: true,
              },
              y: {
                stacked: true
              }
    }
    },},
      darts:{
        labels:['주식','채권','실물자산','가상화폐'],
        datasets:[
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
            data:[]
          }
        ]
      }
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
    function getKeyByValue(obj, value) {
      return Object.keys(obj).find(key => obj[key] === value);
    }
    function getValueByKey(obj, key) {
      return obj[key];
    }
    console.log(checkedStockPrices)
    const filteredData = checkedStocks.map(checkedStock => getKeyByValue(this.dividend.stock_code, checkedStock.code));
    console.log(filteredData)
    const rate = filteredData.map(data => getValueByKey(this.dividend.div_rate, data))
    console.log(rate)
    const count = filteredData.map(data => getValueByKey(this.dividend.div_count, data))
    console.log(count)
    const month = filteredData.map(data => getValueByKey(this.dividend.div_months, data))
    console.log(month)

    const divdata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for (let s=0; s<checkedStockPrices.length; s++){
      for (let i=0; i<month[s].map(str => Number(str)).length; i++){
        divdata[month[s][i]-1] += Number(checkedStockPrices[s])*(Number(rate[s])/(Number(count[s])*100))
      }
    }
    
    this.divs.datasets[1].data = divdata
      
    return {
      
      labels: checkedStockNames,
      datasets: [
        {
          backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
          data: checkedStockPrices,
        }
      ],
      checkedStockPricesSum: 0,
    };
    }
  },
  methods: {
    updateDiv() {
      this.checkedStocks
      },
    updatePort() {
            const headers = { 'Authorization': `JWT ${localStorage.getItem('access_token')}` };
            axios
                .get("http://34.64.108.15/api/portfolio/", { headers })
                  .then(res => {
                    this.darts.datasets[0].data = [res.data.results[0].stock,res.data.results[0].bond,res.data.results[0].real_asset,res.data.results[0].crypto];
                  })
                  .catch(error => {
                    console.log(error);
                  });
    },
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
  },
  mounted() {
    this.updateDiv()
    this.updatePort()
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
