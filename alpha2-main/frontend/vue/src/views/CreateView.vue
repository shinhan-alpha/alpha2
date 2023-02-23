<template>
    <div class="container">
        <div id="top-wrapper">
            <font-awesome-icon icon="fa-solid fa-chevron-left" onclick=""/>
            <span>포트폴리오 생성</span>
        </div>
        <!-- 메인 -->
        <div>
            <div class="tabs">
                <div class="tab" @click="selectedTab = 'first'" :class="{ 'active': selectedTab === 'first' }">총자산 포트폴리오</div>
                <div class="tab" @click="selectedTab = 'sec'" :class="{ 'active': selectedTab === 'sec' }">배당 포트폴리오</div>
            </div>
            <div v-if="selectedTab == 'first'">
                <div id="main">
            <div class="main-top">
                <span>문민제</span>님의 목표 자산 포트폴리오
                <div class="pie-chart">
                    <Pie :data="chartData" :options="options" />
                </div>
                <hr>
            </div>
            <div class="main-bottom">      
                <div>
                    <div class="my-box">
                        <table>
                            <thead>
                                <colgroup>
                                    <col width="10%" />
                                    <col width="40%" />
                                    <col width="10%" />
                                    <col width="40%" />
                                </colgroup>
                            </thead>
                            <tbody>
                                <tr v-for="(asset, index) in assets" :key="index">
                                    <td>{{ asset.name }}</td>
                                    <td><input type="text" class="percent" v-model="asset.percent" placeholder="%" /></td>
                                </tr>                          
                            </tbody>
                        </table>
                    </div>
                </div>
                <div id="save" @click=updatePort()>
                    <span>설정 완료</span>
                </div>
            </div>
        </div>
            </div>
            <div v-if="selectedTab == 'sec'">
                <div id="main">
            <div class="main-top">
                <div class="my-box">
                     <span>월별 목표 배당금</span>
                     <Bar :data="divchartData" :options="options"/>
                </div>
            </div>
             
            <div class="main-bottom">      
                <div>
                    <table>
                    <thead>
                        <tr>
                        <th>월</th>
                        <th>금액</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in monthlyData" :key="index">
                            <td>{{ item.month }}</td>
                            <td>{{ item.amount }}</td>
                        </tr>
                    </tbody>
                    </table>
                </div>
                <div id="save" @click=updatePort()>
                    <span>설정 완료</span>
                </div>
            </div>
            </div>
        </div>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios';
import { Chart as ChartJS, ArcElement, Tooltip, Legend,Title,BarElement,CategoryScale,LinearScale } from 'chart.js'
import { Pie, Bar } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
    name: 'CreateView',
    components: {
        Pie, Bar
    },
    data() {
        return {
            assets: [
                { name: "주식", percent: 0 },
                { name: "채권", percent: 0 },
                { name: "실물자산", percent: 0},
                { name: "가상화폐", percent: 0 },
            ],
            selectedTab : 'first',
            monthlyData: [
                { month: '1월', amount: 100000 },
                { month: '2월', amount: 200000 },
                { month: '3월', amount: 300000 },
                { month: '4월', amount: 400000 },
                { month: '5월', amount: 500000 },
                { month: '6월', amount: 600000 },
                { month: '7월', amount: 700000 },
                { month: '8월', amount: 800000 },
                { month: '9월', amount: 900000 },
                { month: '10월', amount: 1000000 },
                { month: '11월', amount: 1100000 },
                { month: '12월', amount: 1200000 }
            ]
        }
    },
    computed:{
        chartData() {
            const assetNames = this.assets.map(asset => asset.name);
            const assetPrices = this.assets.map(asset => Number(asset.percent));
            return {
                labels: assetNames,
                datasets: [
                    {
                    backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                    data: assetPrices
                    }
                ],
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
        updatePort() {
            const data = {
                stock: Number(this.assets[0].percent),
                bond: Number(this.assets[1].percent),
                real_asset: Number(this.assets[2].percent),
                crypto: Number(this.assets[3].percent),
            };
            const headers = { 'Authorization': `JWT ${localStorage.getItem('access_token')}` };
            axios
                .post("http://127.0.0.1:8000/api/portfolio/", data, { headers })
                .then(() => {
                    alert('포트폴리오 반영');
                })
                .catch((error) => {
                    let errorMsg = "";
                });
        }
    }
    }
</script>

<style scoped>
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
  table {
          border-collapse: collapse;
          width: 100%;
          margin-bottom:100px;
      }

      td {
          text-align: center;
          padding: 8px;
      }

      th {
          background-color: #333;
          color: white;
      }
    tr:nth-child(odd) {
            background-color: #a5a5a5;
        }
    /* topbar */
    #top-wrapper {
        text-align: left;
        height: 30px;
        font-size: 15px;
        padding-left: 5px;
    }

    /* main */
    #main div {
        padding-top: 5px;
        font-size: 16px;
    }
    #main div span {
        font-weight: bold;
    }
    .main-top {
        text-align: center;
        height: 200px;
    }
    .pie-chart {
        display: inline-block;
        height: 150px;
        margin: 0;
    }
    .main-bottom {
        width: 100%;
    }
    #port-select  {
        text-align: center;
    }
    #port-select button {
        float: left;
        border-radius: 8px;
        background-color: transparent;
        font-size: 12px;
        width: 100px;
        height: 30px;
        margin-right: 10px;
    }
    .my-box table {
        width: 100%;
    }
    .my-box table th {
        text-align: left;
        padding-top: 10px;
    }

    .question {
        padding-right: 10px;
    }
    .percent {
        width: 100px;
        height: 25px;
    }
    #save {
        position: fixed;
        width: 100%;
        bottom: 43px;
        left: 0px;
        text-align: center;
        padding-bottom: 8px;
        background-color: #4868E1;
        margin-top: 15px;
        color: white;
    }
</style>