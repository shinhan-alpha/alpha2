<template>
    <div>
        <div>        
            <div id="top-wrapper">
                <font-awesome-icon icon="fa-solid fa-chevron-left" onclick="window.href='/index"/>
                <a href="/search"><input v-model="stock.stockName" placeholder="종목검색"/></a> 
                <button id="cart">카트</button>
                <button id="order">현재가</button>
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
                        {{ buyPrice }}원
                        <button type="button" @click="incrementPrice(stock)">+</button>
                    </div>
                </div>
                <div>
                    <br>
                    <br>
                    <br>
                    <b>총 매수금액: {{ calculate }}</b>
                </div>
                <div class="cart-buy">
                    <button @click="openModal = true">카트 담기</button>
                    <button id="stock-buy">매수 주문</button>
                </div>
            </div>
            <!-- Modal -->
            <div id="modal-container" class="black-bg" v-if="openModal == true">
                <div class="white-bg al-left">
                    <div id="modal-title"><span>알파카트</span> 담기 내역확인</div>
                    <div>
                        <table id="modal-table">
                            <tr>
                                <td class="al-left">게좌번호</td>
                                <td class="al-right">110-1231-13432 김신한</td>
                            </tr>
                            <tr>
                                <td class="al-left">주문종목</td>
                                <td class="al-right">{{ stock.stockName }}</td>
                            </tr>
                            <tr>
                                <td class="al-left">주문수량</td>
                                <td class="al-right">
                                    <div class="plus-minus">
                                        <button type="button" @click="decrementQuantity(stock)">-</button>
                                        {{ quantity }}주
                                        <button type="button" @click="incrementQuantity(stock)">+</button>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td class="al-left">주문단가</td>
                                <td class="al-right">
                                    <div>
                                        <div class="plus-minus">
                                            <button type="button" @click="decrementPrice(stock)">-</button>
                                            {{ buyPrice }}원
                                            <button type="button" @click="incrementPrice(stock)">+</button>
                                        </div>
                                    </div>
                                    
                                </td>
                            </tr>
                            <tr>
                                <td class="al-left">주문금액</td>
                                <td class="al-right">{{ calculate }}</td>
                            </tr>
                        </table>
                    </div>
                    <div class="al-center">
                        <div class="al-flex">
                            <button @click="openModal = false" class="close">취소</button>
                            <button @click="updateCart()" class="check">확인</button>                    
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import store from '../store'
export default {
  data() {
    return {
      stock: this.$store.state.stock,
      quantity: 1,
      buyPrice: this.$store.state.stock.currentPrice,
      totalPrice: '',
      openModal: false,
      pk: 1,
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
      const priceWithoutComma = this.buyPrice.replace(',', '');
      const newPrice = Number(priceWithoutComma) + 100;
      this.buyPrice = newPrice.toLocaleString(); // adds comma back as thousands separator
      console.log(this.buyPrice);
    },
    decrementPrice(stock) {
      const priceWithoutComma = this.buyPrice.replace(',', '');
      if (Number(priceWithoutComma) > 100) {
        const newPrice = Number(priceWithoutComma) - 100;
        this.buyPrice = newPrice.toLocaleString(); // adds comma back as thousands separator
      }
    },
    updateCart() {
        this.pk += 1
        const data = {
            buy_price: this.buyPrice,
            buy_quantity: this.quantity,
            stock_code: this.stock.stockCode,
            stock_name: this.stock.stockName,
        };
        const headers = { 'Authorization': `JWT ${localStorage.getItem('access_token')}` };
        axios
            .post("http://127.0.0.1:8000/api/stock/cart", data, { headers })
            .then(() => {
                console.log('장바구니 데이터 반영');
            })
            .catch((error) => {
                let errorMsg = "";
            });
    }
  },
  computed: {
    calculate() {
        const priceWithoutComma = this.buyPrice.replace(',', '');
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
    margin-left: 15px;
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
    margin-top: 5px;
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
.ml-0 {
    margin: 0;
}

.plus-minus {
    display: inline-flex;
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
    width: 320px;
    height: 260px;
    left: 0px;
    bottom:43px;
    border-radius: 8px;
    background-color: white;
    border-top: 0.5px solid gray;
}
.white-bg {
    width: 320px; 
    height: 260px;
    background-color: white;
    border-radius: 8px;
}

#modal-title {
    font-weight: bold;
    margin: 10px;
    padding-top: 10px;
}

#modal-title span {
    color: #4868E1;
}

#modal-table {
    width: 300px;
    margin: 10px;
}

.al-left {
    text-align: left;
}

.al-right {
    text-align: right;
}

.al-center {
    text-align: center;
}

.al-flex {
    display: inline-flex;
}

.al-flex button {
    margin: 5px;
    width: 100px;
    height: 30px;
}

.cartcheck img{
    width: 110%;
    display: block;            
    object-fit: cover;
}
.close{
    background: #CCCCCC;
    color: #fff;
    border: none;
    border-radius: 5px;
    transition: 0.25s;
}
.check{
    background: #4868E1;
    color: #fff;
    border: none;
    border-radius: 5px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    transition: 0.25s;
}

.top_nav a{
    align-content: stretch;
}

/* popup */
/* #popup {
    position: absolute;
} */


</style>