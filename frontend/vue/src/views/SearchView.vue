<template>
  <div>
    <input type="text" v-model="query" @input="searchStocks" placeholder="Search stocks" />
    <ul>
      <li v-for="stock in stocks" :key="stock.stockCode" @click="curstock(stock)">{{ stock.stockName }} - {{ stock.stockCode }}</li>
    </ul>
  </div>
</template>
<!-- /*
        https://www.sedaily.com/Stock/Quote/JsonSearchData?text=LG전자
       
       JSON Data Format
       { "Items": 
        [ {"Market":"1","IndustryCode":"013","StockCode":"066570","StockName":"LG전자","CurrentPrice":"92,900","PreGap":"400","PreRate":"+0.43","Change":"2","Initial":"E","StockTime":"153004"},
          {"Market":"1","IndustryCode":"013","StockCode":"066575","StockName":"LG전자우","CurrentPrice":"45,100","PreGap":"250","PreRate":"-0.55","Change":"5","Initial":"E","StockTime":"153030"}
        ]
       }
       */ -->
<script>
import axios from 'axios';
import store from '../store'

export default {
  data() {
    return {
      query: '',
      stocks: [],
      searchRequest: null
    }
  },
  methods: {
    curstock(stock) {
      console.log(stock)
      this.$store.commit('curStock', stock)
      this.$router.push('/stockbuy');
    },
    searchStocks() {
      if (this.searchRequest) {
        this.searchRequest.cancel(); // cancel previous request
      }
      this.searchRequest = axios.CancelToken.source();
      axios.get('http://www.sedaily.com/Stock/Quote/JsonSearchData', {
        params: { text: this.query },
        cancelToken: this.searchRequest.token // use the cancel token
      })
      .then(response => {
        const items = response.data.Items;
        const formattedData = items.map(item => {
          return {
            stockName: item.StockName,
            stockCode: item.StockCode,
            currentPrice: item.CurrentPrice,
            preGap: item.PreGap,
            preRate: item.PreRate,
          };
        });
        this.stocks = formattedData;
      })
      .catch(error => {
        if (axios.isCancel(error)) {
          console.log('Request cancelled', error.message);
        } else {
          console.log(error);
        }
      });
    }
  }
}
</script>
