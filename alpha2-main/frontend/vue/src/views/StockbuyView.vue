<template>
    <div>
        <div>        
            <div id="top-wrapper">
            <font-awesome-icon icon="fa-solid fa-chevron-left" onclick="window.href='/index"/>
            <a href="/search"><input v-model="stock.stockName" placeholder="종목검색"/></a> 
            <button id="cart">카트</button>
            <button id="order">주문</button>
        </div>

        <div>
            <div class="middle-info">
                <div class="info-top">
                    <h3>{{stock.stockName}}</h3>
                    <b>{{stock.currentPrice}}</b><br>
                    <span>{{stock.preGap}}</span>
                    <span>{{stock.preRate}}%</span> 
                </div>
                <div class="info-bottom">
                    <span>110-1231-13432 김신한</span>
                    <span>매수가능: 0원</span>
                </div>
                <br><br>
                
            </div>
        </div>

        <div class="middle-menu">
            <table>
                <tr>
                    <th id="mesu">매수</th>
                    <th>매도</th>
                    <th>정정/취소</th>
                    <th>체결내역</th>
                </tr>
            </table>
        </div>
        <div>
            <img id="stock" src="../../../images/stocks.png" style="left:0; position:absolute">    
        </div>
        <div class="user-input">
            <div class="ml-3">
                <button class="button-group active">현금</button>
                <button class="button-group">신용</button>
            </div>
            <div class="ml-3">
                <button class="button-group">지정가</button>
                <button class="button-group active">시장가</button>
            </div>
            <div class="ml">
                <div class="plus-minus">
                    <button type="button" @click="decrementQuantity(stock)">-</button>
                    {{ quantity }}주
                    <button type="button" @click="incrementQuantity(stock)">+</button>
                </div>
            </div>
            <div class="ml">
                <div class="plus-minus">
                    <button type="button" @click="decrementPrice(stock)">-</button>
                    {{ stock.currentPrice }}원
                    <button type="button" @click="incrementPrice(stock)">+</button>
            </div>
            </div>
            <div>
                <br>
                <br>
                <br>
            </div>
                <b>총 매수금액: {{ calculate }}</b>
            <div class="cart-buy">
                <button @click="openModal = true">카트 담기</button>
                <button id="stock-buy">매수 주문</button>
            </div>
        </div>
        <!-- Modal -->
        <div id="modal-container" class="black-bg" v-if="openModal == true">
            <div class="white-bg">
                <div class="cartcheck"><img src="../../../images/cartcheck.png"></div>
                <div class="al-center">
                    <button @click="openModal = false" class="close">취소</button>
                    <button @click="check($event)" class="check">확인</button>                    
                </div>
            </div>
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
      quantity: 1,
      totalPrice: '',
      openModal: false,
    }
  },
  methods: {
    incrementQuantity(stock) {
      this.quantity += 1;
    },
    decrementQuantity(stock) {
      if (this.quantity > 1) {
        this.quantity -= 1;
      }
    },
    incrementPrice(stock) {
      const priceWithoutComma = this.stock.currentPrice.replace(',', '');
      const newPrice = Number(priceWithoutComma) + 100;
      this.stock.currentPrice = newPrice.toLocaleString(); // adds comma back as thousands separator
      console.log(this.stock.currentPrice);
    },
    decrementPrice(stock) {
      const priceWithoutComma = this.stock.currentPrice.replace(',', '');
      if (Number(priceWithoutComma) > 1) {
        const newPrice = Number(priceWithoutComma) - 100;
        this.stock.currentPrice = newPrice.toLocaleString(); // adds comma back as thousands separator
      }
    }
  },
  computed: {
    calculate() {
      const priceWithoutComma = this.stock.currentPrice.replace(',', '');
      const totalPrice = Number(priceWithoutComma) * this.quantity;
      return totalPrice.toLocaleString();
    },
  }
}
</script>

<style scoped>
body {
    margin:0;
}

/* topbar */
#top-wrapper {
    display: table-cell;
    vertical-align: top;
    text-align: left;
    height: 30px;
    font-size: 15px;
    padding-left: 5px;
}
#top-wrapper a input {
    margin-left: 20px;
    width: 150px;
    height: 25px;
}
#top-wrapper button {
    margin-left: 10px;
}
#cart {
    background-color: white;
    color: black;
    border-radius: 5px;
    font-weight: bold;
}
#order {
    background-color: black;
    color: white;
    border-radius: 5px;
    font-weight: bold;
}

/* middle-info */
.middle-info {
    text-align: left;
    width: 320px;
    height: 110px;
    margin-top: 10px;
    width: 300px;
}

.info-top h3 {
    margin: 0;
}

.info-top {
    font-size: 20px;
}

.info-top span {
    font-size: 13px;
    margin-right: 5px;
    color: green;
}

.info-bottom {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    font-size: 13px;
}


.middle-menu {
    position: relative;
    left: 0;
    width: 320px;
}
.middle-menu table {
    width: 320px;
    margin-bottom: 5px;
    height: 35px;
}
.middle-menu tr {
    width: 300px;
    border: #CCCCCC;
}
.middle-menu th {
    text-align: center;
    background-color: white;
    border: #CCCCCC;
    color: #8D8D8D;
    padding-left: 10px;
    font-weight: 500;
    font-size: 13px;
}
#mesu {
    color: #D82E25;
    border-bottom: 3px solid #D82E25;
    font-weight: bold;
}

#stock {
    display: relative;
    top: 240px;
}

/* user-input */
.user-input {
    position: absolute;
    right: 0;
    top: 250px;
    width: 200px;
    text-align: center;
    margin: 10px;
}
.button-group {
    width: 70px;
    margin-bottom: 10px;
    border-radius: 5px;
    background-color: white;
    font-weight: 200;
    border-color: #CCCCCC;
}

.active {
    background-color: #CCCCCC;
    border-color: #CCCCCC;
    color: white;
}

.ml {
    margin-left: 25px;
}
.ml-3 {
    margin-left: 13px;
}

.plus-minus {
    display: flex;
    justify-content: space-between;
    width: 150px;
    border: 1px solid black;
    border-radius: 5px;
    margin: 5px;
}

.plus-minus button {
    background-color: transparent   ;
    border: none;
}

.cart-buy {
    width: 200;
    margin-top: 10px;
    margin-left: 10px;
}

.cart-buy button {
    border-color: red;
    border-radius: 5px;
    background: white;
    color: red;
    margin-right: 5px;
    font-size: 13px;
    width: 80px;
    height: 35px;
}

#stock-buy {
    background-color: red;
    color: white;
}

/* modal */
.black-bg {
    position: absolute;
    width: 100%;
    height: 284px;
    left: 0px;
    bottom:0px;
}
.white-bg {
    width: 320px; background: white;
    border-radius: 8px;
}

.al-center {
    display: flex;
    text-align: center;
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