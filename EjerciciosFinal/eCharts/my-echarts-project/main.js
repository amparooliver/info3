// Importar los estilos y la biblioteca ECharts
import './style.css';
import * as echarts from 'echarts';

// Función para crear y configurar el gráfico de ECharts
function setupChart(containerId) {
  // Datos de ejemplo para el gráfico
  const chartData = {
    dimensions: ['year', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
    source: [
      { year: 2020, Enero: 1825, Febrero: 869, Marzo: 891, Abril: 1572, Mayo: 963, Junio: 552, Julio: 1486 },
      { year: 2021, Enero: 1173, Febrero: 1124, Marzo: 1362, Abril: 1104, Mayo: 1014, Junio: 698, Julio: 1142 },
      { year: 2022, Enero: 1289, Febrero: 1353, Marzo: 1883, Abril: 563, Mayo: 1871, Junio: 705, Julio: 1499 },
    ],
  };

  // Obtener el contenedor del gráfico
  const chartContainer = document.getElementById(containerId);

  chartContainer.style.height = '300px'; // Puedes ajustar el valor según sea necesario

  // Inicializar ECharts
  const myChart = echarts.init(chartContainer);

  // Configuración del gráfico ECharts
  const option = {
    title: {
      text: 'Gráfico por Año',
      top: '5%',
    },
    legend: {
      data: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio']
    },
    tooltip: {
      trigger: 'axis'
    },
    dataset: chartData,
    xAxis: {
      type: 'category'
    },
    yAxis: {},
    series: [
      { type: 'bar', name: 'Enero' },
      { type: 'bar', name: 'Febrero' },
      { type: 'bar', name: 'Marzo' },
      { type: 'bar', name: 'Abril' },
      { type: 'bar', name: 'Mayo' },
      { type: 'bar', name: 'Junio' },
      { type: 'bar', name: 'Julio' },
    ],
    color: ['#7071E8', '#C683D7', '#ED9ED6', '#FFC7C7', '#392467', '#5D3587', '#A367B1'],
  };

  // Establecer la opción de ECharts
  myChart.setOption(option);
}

// Función para crear y configurar el segundo gráfico de ECharts
function setupChart2(containerId) {
  // Obtener el contenedor del gráfico
  const chartContainer = document.getElementById(containerId);

  // Inicializar ECharts
  const myChart = echarts.init(chartContainer);

  // Configuración del segundo gráfico ECharts
  const option = {
    title: {
      text: 'Series por Mes'
    },
    tooltip: {},
    legend: {
      data: ['meses']
    },
    xAxis: {
      data: ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio']
    },
    yAxis: {},
    series: [
      {
        name: '2020',
        type: 'bar',
        data: [1860, 923, 1613, 1761, 1573, 902, 534]
      },
      {
        name: '2021',
        type: 'bar',
        data: [1848, 1106, 1392, 1704, 1051, 1816, 872]
      },
      {
        name: '2022',
        type: 'bar',
        data: [1678, 986, 1988, 1479, 846, 1503, 981]
      }
    ]
  };

  // Establecer la opción de ECharts
  myChart.setOption(option);
}

// Configurar el contenido de la aplicación
document.getElementById('app').innerHTML = `
  <div>
    <h1>Examen Final - Amparo Oliver</h1>
    <div id="chartContainer" style="height: 300px;"></div>
    <div id="secondChartContainer" style="height: 300px;"></div>
    <p class="read-the-docs">
    Informatica 3
    </p>
  </div>
`;

// Configurar el primer gráfico de ECharts
setupChart('chartContainer');

// Configurar el segundo gráfico de ECharts
setupChart2('secondChartContainer');
