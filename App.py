import streamlit as st
import pandas as pd
st.title("Deli-Sano")
st.title("Alimentacion Saludable En Chihuahua")
st.write ("En Chihuahua tenemos alimentos de primera calidad")
st.image("https://www.morelandobgyn.com/hubfs/Imported_Blog_Media/GettyImages-854725402-1.jpg")
boton = st.button("Informacion Adicional")
if boton:
  st.write("El estado de Chihuahua ocupa actualmente el primer lugar mundial en obesidad y sobrepeso infantil, juvenil y adulto. De acuerdo a la Secretaría de Salud federal, el 60 por ciento de la población en la entidad registra un peso corporal encima de lo debido, mientras que el 11.4. por ciento de los niños y el 31 por ciento de los adolescentes padecen sobrepeso y algún nivel de obesidad, según información del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado (ISSSTE).'")
options = st.multiselect(
  '¿Que se te antoja hoy?',
     ['Postres', 'Ensaladas', 'Sopas', 'Sandwich', "Jugos", "Licuados"])
st.write('Seleccionaste:', options)
df = pd.read_csv("Libro1.csv")
lista_df = df["nombre2"].tolist()
st.write(lista_df)
st.sidebar.write("Chihuahua tiene una exquisita variedad de platillos y comida regionales, elaborada en base de carne de res la mayoría de ellos, pues aquí se cría ganado bovino de calidad, como el famoso cara blanca (Hereford) Brangus, Angus y Charolais; entre otros. Los cortes más finos deliciosos se sirven en los restaurantes acompañados de papa al horno y cebolla asada. Debido a los climas extremos de la región los primeros pobladores se vieron en la necesidad de aprovechar los cortos períodos de cosecha para preservar y almacenar alimentos. Y es por ello que dentro de los usos y costumbres gastronómicos chihuahuenses está el deshidratar, a secar los granos, los vegetales, las frutas e incluso las carnes.")
st.sidebar.image("https://chihuahua.gob.mx/sites/default/files/pictures/gastronomia_1.jpg")
boton = st.button("Recetario")
if boton:
  st.write ("https://issuu.com/pamfloresg/docs/saboresregionales"),("https://gravepa.com/granaino/RECETAS/el-gran-libro-de-la-cocina-mexicana-dangeli.pdf")
