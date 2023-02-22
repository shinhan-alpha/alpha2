<template>
    <div id="menu-wrapper">
            <table>
                <tr>
                    <th id="menu-tab"><a href="/menu"><font-awesome-icon icon="fa-solid fa-bars" /></a></th>
                    <th><router-link to="/">홈</router-link></th>
                    <th><router-link to="/">관심<br>종목</router-link></th>
                    <th><router-link to="/current">현재가</router-link></th>
                    <th><router-link to="/stockbuy">주식<br>주문</router-link></th>
                    <th><router-link to="/balance">주식<br>잔고</router-link></th>
                    <th><router-link to="/chart">종합<br>차트</router-link></th>
                    <th><router-link to="/indicators">지수환율<br>시장지표</router-link></th>
                    <th><router-link to="/trends">매매<br>동향</router-link></th>
                    <th><router-link to="/toss">즉시<br>이체</router-link></th>
                    <th><router-link to="/total">총자산<br>현황</router-link></th>
                </tr>
            </table>
    </div>
</template>

<script>
export default {
}
</script>


<style scoped>
    /* menubar */
    #menu-wrapper {
        overflow-x: auto;  
        position: fixed;
        left: 0;
        bottom: 0;
        border-collapse: collapse;
        height: 43px;
    }
    #menu-tab {
        background-color: #393D46;
    }
    #menu-tab i {
        font-size: 20px;
    }
    table {
        background-color: #333;
        border-collapse: collapse;
        width: 200%;
        height: 43px;
    }
    th, td {
        text-align: center;
    }
    th {
        background-color: #333;
        color: #fff;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: auto;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    a {
        color: white;
        text-decoration: none;
        font-weight: bold;
        font-size: 13px;
    }
</style>