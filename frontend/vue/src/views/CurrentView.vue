<template>
    <div>
    <div class="top_nav">
              <a href="#"><img src="../../../images/arrow.png" style="float:left"></a>
              <!-- <select id="stockList" v-model="selected">
                  <option v-for="option in options" :value="option.price">{{ option.stock }}</option>
              </select> -->
              <a href="./search"><input v-model="stock.stockName"/></a> 
              <a @click="openModal = true"><img src="../../../images/cart.png"></a>
              <a href="#"><img src="../../../images/order.png"></a>
              <a href="#"><img src="../../../images/more.png"></a>
          </div>
          <!-- Modal -->
          <div id="modal-container" class="black-bg" v-if="openModal == true">
              <div class="white-bg">
                  <div>
                    계좌번호   124-124-124124<br>
                    주문종목   LG전자(066570)<br><br>
                </div>
                <div>
                    주문수량
                    <button type="button" @click="decrementQuantity(stock)">-</button>
                        {{ quantity }}
                    <button type="button" @click="incrementQuantity(stock)">+</button>
                </div>
                <br>
                <div>
                  <button @click="openModal = false" class="close">취소</button>
                  <button @click="check($event)" class="check">확인</button>
                </div>
              </div>
          </div>
          <div>
            <div style="text-align: left;">
                {{stock.currentPrice}}<br>
                {{stock.preGap}}  {{stock.preRate}}%
            </div>
            <div>
                <div class="tabs">
                    <div class="tab" @click="selectedTab = 'first'" :class="{ 'active': selectedTab === 'first' }">호가</div>
                    <div class="tab" @click="selectedTab = 'sec'" :class="{ 'active': selectedTab === 'sec' }">차트</div>
                    <div class="tab" @click="selectedTab = 'third'" :class="{ 'active': selectedTab === 'third' }">체결</div>
                    <div class="tab" @click="selectedTab = 'fourth'" :class="{ 'active': selectedTab === 'fourth' }">일별/수급</div>
                    <div class="tab" @click="selectedTab = 'fifth'" :class="{ 'active': selectedTab === 'fifth' }">거래원</div>
                </div>
                <div v-if="selectedTab == 'first'">
                  <div class="container">
                    <div class="box" v-for="(item, index) in items" :key="index">
                      {{ item }}
                    </div>
                  </div>
                </div>
                <div v-if="selectedTab == 'sec'">
                    <div ref="chart"></div>
                </div>
                <div v-if="selectedTab == 'third'">
                  third
                </div>
                <div v-if="selectedTab == 'fourth'"></div>
                <div v-if="selectedTab == 'fifth'"></div>
            </div>
          </div>
  
    </div>
  </template>
  
  <script>
  import { createChart, CrosshairMode } from 'lightweight-charts'
  import store from '../store'
  export default {
      data() {
      return {
        stock: this.$store.state.stock,
        chart: null,
        selectedTab: "first",
        quantity: 1,
        openModal:false,
        items: [],
      } 
    
    },
    watch: {
      stock: function(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.generateItems(newVal)
      }
    }
    },
    methods:{
      generateItems() {
        for (let i = 1; i <= 5; i++) {
        const price = Math.round(Number(this.stock.currentPrice) * (1 + (i / 100)));
        console(price)
        const percentChange = i;
        this.items.push(price);
      } 
    },
      incrementQuantity(stock) {
      this.quantity += 1;
    },
    decrementQuantity(stock) {
      if (this.quantity > 1){
        this.quantity -= 1;
      }
    },
      createCharts() {
      if (this.selectedTab !== 'sec') {
        return
      }

      this.chart = createChart(this.$refs.chart, {
        width: 400,
        height: 300,
        layout: {
          backgroundColor: '#000000',
          textColor: 'rgba(255, 255, 255, 0.9)',
        },
        grid: {
          vertLines: {
            color: 'rgba(197, 203, 206, 0.5)',
          },
          horzLines: {
            color: 'rgba(197, 203, 206, 0.5)',
          },
        },
        crosshair: {
          mode: CrosshairMode.Normal,
        },
        rightPriceScale: {
          borderColor: 'rgba(197, 203, 206, 0.8)',
        },
        timeScale: {
          borderColor: 'rgba(197, 203, 206, 0.8)',
        },
      })

      const candleSeries = this.chart.addCandlestickSeries({
        upColor: 'red',
        downColor: 'blue',
        borderDownColor: 'blue',
        borderUpColor: 'red',
        wickDownColor: 'blue',
        wickUpColor: 'red',
      })
      candleSeries.setData([
        { time: '2018-10-19', open: 180.34, high: 180.99, low: 178.57, close: 179.85 },
        { time: '2018-10-22', open: 180.82, high: 181.40, low: 177.56, close: 178.75 },
        { time: '2018-10-23', open: 175.77, high: 179.49, low: 175.44, close: 178.53 },
        { time: '2018-10-24', open: 178.58, high: 182.37, low: 176.31, close: 176.97 },
        { time: '2018-10-25', open: 177.52, high: 180.50, low: 176.83, close: 179.07 },
      ])
    },
    
  }}
  
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 33.33%;
    margin: auto;
  }
  
  .box {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 10px;
    border: 1px solid black;
    margin: 0;
  }
  .tabs {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ccc;
  }
  
  .tab {
    padding: 10px;
    cursor: pointer;
    font-size: small;
  }
  
  .tab.active {
    background-color: #ccc;
  }
  
  .tab-content {
    margin-top: 10px;
  }
  body {
              margin:0;
          }
          /* menubar */
          #menu-wrapper {
              overflow-x: auto;  
              position: fixed;
              left: 0;
              bottom: 0;
              border-collapse: collapse;
              height: 50px;
          }
          #stockList {
              width: 150px;
              height: 30px;
          }
          table {
              border-collapse: collapse;
              width: 200%;
              height: 50px;
          }
          th, td {
              text-align: center;
          }
          th {
              background-color: #333;
              color: #fff;
              text-transform: uppercase;
              letter-spacing: 2px;
              font-weight: bold;
          }
          tr:nth-child(even) {
              background-color: #f2f2f2;
          }
          a {
              color: white;
              text-decoration: none;
              font-weight: bold;
          }
          .black-bg {
              position: absolute;
              width: 321.99px;
              height: 284px;
              left: 0px;
              top: 244px;
              right: 0px;
              }
          .white-bg {
              width: 320px; background: white;
              border-radius: 8px;
  
              }
          .cartcheck img{
              width: 100%;
              display: block;            
              object-fit: cover;
          }
          .close{
              background: #c0bebe;
              color: #fff;
              position:relative;
              right:10px;
              display: inline-block;
              border-radius: 15px;
              box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
              transition: 0.25s;
          }
          .check{
              background: blue;
              color: #fff;
              position: relative;
              left: 20px;
              display: inline-block;
              border-radius: 15px;
              box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
              transition: 0.25s;
          }
          .top_nav a{
              align-content: stretch;
          }
  </style>