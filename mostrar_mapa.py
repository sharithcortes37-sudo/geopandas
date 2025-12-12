import matplotlib.pyplot as plt

def mostrar_mapa(gdf):
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.geometry.plot(ax=ax)
    ax.set_title("Mapa del GeoDataFrame")
    plt.show()