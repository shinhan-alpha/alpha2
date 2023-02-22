<template>
  <div>
    <canvas ref="lineChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js';

export default {
  name: 'LineChart',
  data() {
        return {
          title: 'Chart Title',
          labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'],
          values: [10, 20, 30, 40, 50],
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }
      },
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  mounted() {
    this.drawLineChart();
  },
  methods: {
    drawLineChart() {
      const ctx = this.$refs.lineChart.getContext('2d');

      const lineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.data.labels,
          datasets: [{
            label: this.data.title,
            data: this.data.values,
            backgroundColor: this.data.backgroundColor,
            borderColor: this.data.borderColor,
            borderWidth: this.data.borderWidth
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
    }
  }
}
</script>
