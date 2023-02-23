<template>
  <div>
  <div>
    {{stock.stockName}}
  </div>
  <div class="top_nav">
            <a href="#"><img src="../../images/arrow.png"></a>
            <!-- <select id="stockList" v-model="selected">
                <option v-for="option in options" :value="option.price">{{ option.stock }}</option>
            </select> -->
            <a href="./search"><input v-model="stock.stockName"/></a>    
            <a @click="openModal = true"><img src="../../images/cart.png"></a>
            <a href="#"><img src="../../images/order.png"></a>
            <a href="#"><img src="../../images/more.png"></a>
        </div>
        <div>
            <div style="text-align: left;"><br><br>
                <b>{{stock.currentPrice}}</b><br>
                {{stock.preGap}}  {{stock.preRate}}%<br><br>
                110-1231-13432 김신한<br>
                매수가능: 0원
            </div>
        </div>
        <!-- Modal -->
        <div id="modal-container" class="black-bg" v-if="openModal == true">
            <div class="white-bg">
                <div class="cartcheck"><img src="../../images/cartcheck.png"></div>
                <button @click="close($event)" class="close">취소</button>
                <button @click="check($event)" class="check">확인</button>
            </div>
        </div>
        <div>
            <img src="../../images/stocktab.png">
        </div>
        <div>
            <img src="../../images/stocks.png" style="left:0; position:absolute">
            <img src="../../images/misu.png" style="left:105px;width:220px; height:80px; position:absolute"/>
            <div style="top:110px; left:55px; position:relative">
                <button type="button" @click="decrementQuantity(stock)">-</button>
                    {{ quantity }}주
                <button type="button" @click="incrementQuantity(stock)">+</button>
            </div>
            <div style="top:140px; left:55px; position:relative">
                <button type="button" @click="decrementPrice(stock)">-</button>
                    {{ stock.currentPrice }}원
                <button type="button" @click="incrementPrice(stock)">+</button>
            </div>
            <b style="top:180px; left:45px; position:relative">총 매수금액: {{ quantity * currentPrice }}</b>
            <div>
                <img src="../../images/cartbut.png" style="top:200px;left:45px; position:relative">
                <img src="../../images/stockbuy.png" style="top:200px;left:55px; position:relative">
            </div>
        </div>

  </div>
</template>

<script>
import store from '../store'
export default {
    data() {
    return {
      stock: this.$store.state.stock,
      quantity:1,
    }
  },
  methods:{
    incrementQuantity(stock) {
      this.quantity += 1;
    },
    decrementQuantity(stock) {
      if (this.quantity > 1){
        this.quantity -= 1;
      }
    },
      incrementPrice(stock) {
        this.stock.currentPrice += 100;
        console.log(this.stock.currentPrice)
    },
    decrementPrice(stock) {
      if (this.stock.currentPrice > 1){
        this.stock.currentPrice -= 100;
      }
    },
    
  }}
</script>

<style scoped>
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
            left: 50px;
            display: inline-block;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            transition: 0.25s;
        }
        .check{
            background: blue;
            color: #fff;
            position: relative;
            left: 100px;
            display: inline-block;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            transition: 0.25s;
        }
        .top_nav a{
            align-content: stretch;
        }
</style>