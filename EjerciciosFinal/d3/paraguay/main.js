// Cargar el archivo GeoJSON de límites departamentales de Paraguay
d3.json('map.geojson').then((geojson) => {
    // Configuración del tamaño del contenedor del mapa
    const width = 800;
    const height = 600;

    // Crear la proyección y el camino
    const projection = d3.geoMercator().fitSize([width, height], geojson);
    const path = d3.geoPath().projection(projection);

    // Crear el lienzo SVG
    const svg = d3.select('#map-container')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // Agregar los límites departamentales
    svg.selectAll('path')
        .data(geojson.features)
        .enter().append('path')
        .attr('d', path)
        .attr('class', 'department-border');
});
