<template>
  <div>
  <div>
    {{stock.stockName}}
  </div>
  <div class="top_nav">
            <a href="#"><img src="../../../images/arrow.png"></a>
            <!-- <select id="stockList" v-model="selected">
                <option v-for="option in options" :value="option.price">{{ option.stock }}</option>
            </select> -->
            <a href="./search"><img src="../../../images/search.png"></a>    
            <a @click="openModal = true"><img src="../../../images/cart.png"></a>
            <a href="#"><img src="../../../images/order.png"></a>
            <a href="#"><img src="../../../images/more.png"></a>
        </div>
        <!-- Modal -->
        <div id="modal-container" class="black-bg" v-if="openModal == true">
            <div class="white-bg">
                <div class="cartcheck"><img src="../../../images/cartcheck.png"></div>
                <button @click="close($event)" class="close">취소</button>
                <button @click="check($event)" class="check">확인</button>
            </div>
        </div>
        <div>
            <img src="../../../images/stockn.png">
        </div>

  </div>
</template>

<script>
import store from '../store'
export default {
    data() {
    return {
      stock: this.$store.state.stock,
    }
  },
  
}
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