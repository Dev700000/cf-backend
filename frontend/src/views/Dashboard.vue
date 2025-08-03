<template>
  <div>
    <Navbar />
    <section class="dashboard">
      <h2 class="title">Panel de Control (Proximamente)</h2>

      <div class="stats">
        <div class="stat-card">
          <h3>{{ totalSales }}</h3>
          <p>Ventas este mes</p>
        </div>
        <div class="stat-card">
          <h3>{{ totalPosts }}</h3>
          <p>Publicaciones este mes</p>
        </div>
        <div class="stat-card">
          <h3>{{ activeUsers }}</h3>
          <p>Usuarios activos</p>
        </div>
      </div>

      <div class="charts">
        <div class="chart-wrapper">
          <h3>Ventas Mensuales</h3>
          <canvas ref="lineChart"></canvas>
        </div>

        <div class="chart-wrapper">
          <h3>Publicaciones Mensuales</h3>
          <canvas ref="barChart"></canvas>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import { ref, onMounted } from 'vue';

export default {
  name: 'Dashboard',
  components: {
    Navbar
  },
  setup() {
    const lineChart = ref(null);
    const barChart = ref(null);

    const totalSales = 12000;
    const totalPosts = 35;
    const activeUsers = 8;

    let lineChartInstance = null;
    let barChartInstance = null;

    onMounted(() => {
      // Asegúrate que Chart está disponible globalmente (viene del CDN)

      lineChartInstance = new Chart(lineChart.value.getContext('2d'), {
        type: 'line',
        data: {
          labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
          datasets: [{
            label: 'Ventas',
            data: [5000, 7000, 8000, 10000, 9000, 11000, 12000],
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            fill: true,
            tension: 0.3,
            pointRadius: 4,
            pointHoverRadius: 6,
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: true },
            title: {
              display: true,
              text: 'Ventas Mensuales'
            }
          },
          scales: {
            y: { beginAtZero: true }
          }
        }
      });

      barChartInstance = new Chart(barChart.value.getContext('2d'), {
        type: 'bar',
        data: {
          labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
          datasets: [{
            label: 'Publicaciones',
            data: [3, 5, 2, 8, 7, 4, 6],
            backgroundColor: 'rgba(46, 204, 113, 1)'
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
            title: {
              display: true,
              text: 'Publicaciones Mensuales'
            }
          },
          scales: {
            y: { beginAtZero: true, stepSize: 1 }
          }
        }
      });
    });

    return {
      lineChart,
      barChart,
      totalSales,
      totalPosts,
      activeUsers
    };
  }
};
</script>

<style scoped>
.dashboard {
  max-width: 900px;
  margin: 2rem auto;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}
.title {
  text-align: center;
  margin-bottom: 1.5rem;
  font-weight: 700;
  font-size: 2rem;
  color: #2c3e50;
}

.stats {
  display: flex;
  justify-content: space-around;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.stat-card {
  background: #f7f9fc;
  box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
  border-radius: 8px;
  padding: 1rem 2rem;
  width: 28%;
  min-width: 180px;
  text-align: center;
  transition: transform 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgb(0 0 0 / 0.15);
}

.stat-card h3 {
  font-size: 2.5rem;
  margin-bottom: 0.25rem;
  color: #2980b9;
}

.stat-card p {
  font-size: 1.1rem;
  color: #555;
}

.charts {
  display: flex;
  justify-content: space-around;
  gap: 2rem;
  flex-wrap: wrap;
}

.chart-wrapper {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
  padding: 1rem 1.5rem 2rem;
  width: 44%;
  min-width: 300px;
}

.chart-wrapper h3 {
  text-align: center;
  margin-bottom: 1rem;
  color: #34495e;
}
</style>
