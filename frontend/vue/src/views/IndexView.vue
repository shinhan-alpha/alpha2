<template>
    <div class="container">
      <div class="index">
        <img src="../../../images/index.png">
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name:"index",
      
  };
  </script>
  
  <style>
/* index */
.index {
            text-align: center;
            display: table;
        }
        .index img {
            max-width: 100%;
            max-height: 100%;
        }

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
  