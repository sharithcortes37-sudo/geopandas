import geopandas as gpd
from cargar_archivo import cargar_archivo
from mostrar_info import mostrar_info
from mostrar_mapa import mostrar_mapa
my_gdf = cargar_archivo('barriolegalizado.json')

mostrar_info(my_gdf)
mostrar_mapa(my_gdf)
