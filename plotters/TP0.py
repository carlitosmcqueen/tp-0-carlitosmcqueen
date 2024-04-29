import seaborn.objects as so
from gapminder import gapminder


def plot():
    datos_mundo = gapminder[gapminder['continent'] == 'Americas']
    datos_mundo_filtro_pop = datos_mundo[datos_mundo['pop'] >= 30000000]
    datos_mundo_filtro_ano= datos_mundo_filtro_pop[datos_mundo_filtro_pop["year"]>= 1990]
    
    figura = (
        so.Plot(data=datos_mundo_filtro_ano, x='year', y='pop')
        .add(so.Line(), color="country")
        .label(x="años",
               y="Aunmento de poblacion",
               title="Paises que superaron los 30 millones")
        )
    return dict(
        descripcion="Paises en America que superaron los 30 millones de habitantes desde 1990",
        autor="Carlos Quispe Estrada",
        figura=figura,
    )
